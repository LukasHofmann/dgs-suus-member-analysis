import ast
import re
import os
import unicodedata
import pandas as pd
import html

def _normalize_str(s):
    """NFC Unicode + collapsed whitespace + stripped edges."""
    if not isinstance(s, str):
        return s
    return ' '.join(unicodedata.normalize('NFC', s).split())


# --- Load journal aliases from CSV ---
def load_journal_aliases():
    """Loads journal name aliases from data/journal_aliases.csv."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', 'data', 'journal_aliases.csv')
    df = pd.read_csv(file_path, sep=';', comment='#')
    raw = df['raw'].apply(_normalize_str)
    return dict(zip(raw, df['clean']))


# --- Type grouping ---
TYPE_GROUPS = {
    'book':                 'book(-chapter)',
    'book-chapter':         'book(-chapter)',
    'edited-book':          'book(-chapter)',
    'data-set':             'other',
    'report':               'other',
    'conference-output':    'conference',
    'conference-paper':     'conference',
    'conference-poster':    'conference',
    'conference-abstract':  'conference',
    'magazine-article':     'journal-article',
    'working-paper':        'preprint',
}


def normalize_journal_titles(df):
    """Replaces known malformed journal titles with their correct versions."""
    aliases = load_journal_aliases()
    # NFC Unicode + collapse internal whitespace (handles embedded newlines)
    df['journal_title'] = df['journal_title'].apply(_normalize_str)
    df['journal_title'] = df['journal_title'].replace(aliases)
    return df


def group_publication_types(df):
    """Maps specific publication types to broader grouped categories."""
    df['type_grouped'] = df['type'].replace(TYPE_GROUPS)
    df['type_grouped'] = df['type_grouped'].fillna(df['type'])  # keep original if not in map
    return df


def parse_contributors(value):
    """Safely parses a contributor list from string representation back to Python list."""
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        value = value.strip()
        if not value:
            return []
        try:
            parsed = ast.literal_eval(value)
            return parsed if isinstance(parsed, list) else []
        except (ValueError, SyntaxError):
            return []
    return []


def normalize_name(name):
    """Normalizes a name string: strips whitespace, converts 'Last, First' to 'First Last'."""
    if not isinstance(name, str):
        return name
    name = re.sub(r'\s+', ' ', name).strip()
    if ',' in name:
        last, first = name.split(',', 1)
        return f"{first.strip()} {last.strip()}"
    return name


def normalize_contributors(df):
    """Parses contributor lists and normalizes all names within them."""
    df['contributors'] = df['contributors'].apply(parse_contributors)
    df['contributors'] = df['contributors'].apply(
        lambda contribs: [
            {**c, 'name': normalize_name(c['name'])} if c.get('name') else c
            for c in contribs
        ]
    )
    return df


def add_primary_author(df):
    """
    Adds the primary author (from org_first_name / org_last_name) to the
    contributors list if their last name is not already present.
    """
    def _add(row):
        last_lower = str(row['org_last_name']).lower()
        names_lower = [c['name'].lower() for c in row['contributors'] if c.get('name')]
        if not any(last_lower in n for n in names_lower):
            row['contributors'].insert(0, {
                'name':     f"{row['org_first_name']} {row['org_last_name']}",
                'orcid':    None,
                'role':     'author',
                'sequence': 'first'
            })
        return row['contributors']

    df['contributors'] = df.apply(_add, axis=1)
    return df


def sort_contributors(df):
    """Creates a sorted copy of contributors for stable deduplication comparisons."""
    df['contributors_sorted'] = df['contributors'].apply(
        lambda contribs: sorted(
            [c['name'] for c in contribs if c.get('name')]
        )
    )
    return df


def decode_html_entities(df):
    """Decodes HTML entities in journal titles (e.g. &amp; → &)."""
    df['journal_title'] = df['journal_title'].apply(
        lambda x: html.unescape(x) if isinstance(x, str) else x
    )
    return df

def run_pipeline(df):
    """Runs all processing steps in order and saves the result."""
    df = normalize_journal_titles(df)
    df = group_publication_types(df)
    df = normalize_contributors(df)
    df = add_primary_author(df)
    df = sort_contributors(df)
    df = decode_html_entities(df)

    df.to_csv('../data/outputs/work_processed.csv',
              index=False,
              sep=';',
              encoding='utf-8-sig')

    print(f"Saved {len(df)} processed records to data/outputs/work_processed.csv")
    return df