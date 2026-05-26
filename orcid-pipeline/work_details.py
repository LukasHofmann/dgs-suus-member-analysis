import requests
import time
import pandas as pd
from auth import get_headers


def fetch_work_details(df_codes):
    """
    Takes the work codes DataFrame, fetches full metadata for each
    put-code from the ORCID API, saves to CSV and returns the DataFrame.
    """

    headers = get_headers()
    results = []

    total = len(df_codes)

    for index, row in df_codes.iterrows():
        work_id = row['workCode']
        orcid_id = row['orcid_id']

        url = f"https://pub.orcid.org/v3.0/{orcid_id}/work/{work_id}"

        try:
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                print(f"Error {response.status_code} for work {work_id} — skipping")
                continue

            data = response.json()

        except Exception as e:
            print(f"Request failed for work {work_id}: {e} — skipping")
            continue

        # --- DOI ---
        doi = None
        if data.get('external-ids') and data['external-ids'].get('external-id'):
            for ext_id in data['external-ids']['external-id']:
                if ext_id['external-id-type'] == 'doi':
                    doi = ext_id['external-id-value']
                    break

        # --- Contributors ---
        contributors = []
        if data.get('contributors') and data['contributors'].get('contributor'):
            for c in data['contributors']['contributor']:
                name = None
                if c.get('credit-name'):
                    name = c['credit-name']['value']

                orcid = None
                if c.get('contributor-orcid'):
                    orcid = c['contributor-orcid'].get('path')

                role = None
                sequence = None
                if c.get('contributor-attributes'):
                    role = c['contributor-attributes'].get('contributor-role')
                    sequence = c['contributor-attributes'].get('contributor-sequence')

                contributors.append({
                    'name':     name,
                    'orcid':    orcid,
                    'role':     role,
                    'sequence': sequence
                })

        # --- Citation (BibTeX or other) ---
        raw_bib = None
        other_citation = None
        if data.get('citation'):
            if data['citation'].get('citation-type') == 'bibtex':
                raw_bib = data['citation'].get('citation-value')
            else:
                other_citation = data['citation'].get('citation-value')

        # --- Publication date ---
        year, month, day = '0000', '00', '00'
        if data.get('publication-date'):
            pub = data['publication-date']
            if pub.get('year'):
                year = pub['year']['value']
            if pub.get('month'):
                month = pub['month']['value']
            if pub.get('day'):
                day = pub['day']['value']

        results.append({
            'workCode':         work_id,
            'orcid_id':         orcid_id,
            'org_first_name':   row['org_first_name'],
            'org_last_name':    row['org_last_name'],
            'input_date':       row['input_date'],
            'title':            data['title']['title']['value'] if data.get('title') else None,
            'subtitle':         data['title']['subtitle']['value'] if data.get('title') and data['title'].get('subtitle') else None,
            'type':             data.get('type'),
            'journal_title':    data['journal-title']['value'] if data.get('journal-title') else None,
            'publication_year': year,
            'publication_date': f"{year}-{month}-{day}",
            'doi':              doi,
            'url':              data['url']['value'] if data.get('url') else None,
            'contributors':     contributors,
            'language_code':    data.get('language-code'),
            'country':          data.get('country'),
            'short_description':data.get('short-description'),
            'source':           data['source']['source-name']['value'] if data.get('source') and data['source'].get('source-name') else None,
            'raw_bib':          raw_bib,
            'other_citation':   other_citation
        })

        # Progress indicator
        if (index + 1) % 50 == 0:
            print(f"Progress: {index + 1}/{total}")

        time.sleep(0.5)

    df_result = pd.DataFrame(results)

    df_result.to_csv('../data/outputs/work_details.csv',
                     index=False,
                     sep=';',
                     encoding='utf-8-sig')

    print(f"Saved {len(df_result)} work details to data/outputs/work_details.csv")
    return df_result