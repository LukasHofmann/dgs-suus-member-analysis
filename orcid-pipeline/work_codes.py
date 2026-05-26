import requests
import time
import pandas as pd
from datetime import datetime
from auth import get_headers


def fetch_work_codes(df):
    """
    Takes the members DataFrame and fetches all publication put-codes
    from the ORCID API for each member with a valid ORCID ID.
    Returns a DataFrame with one row per publication.
    """

    headers = get_headers()
    results = []
    total = len(df)

    for index, row in df.iterrows():

        # Skip members without a valid ORCID ID (format: 0000-0000-0000-0000 = 19 chars)
        if len(str(row['orcid_id'])) != 19:
            continue

        orcid_id = row['orcid_id']
        url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Error for {row['last_name']}, {row['first_name']}: {response.status_code}")
            continue

        data = response.json()
        groups = data.get('group', [])

        for group in groups:

            # Prefer the entry with display-index "1" (preferred source)
            summaries = group.get('work-summary', [])
            work_summary = next(
                (s for s in summaries if s.get('display-index') == '1'),
                summaries[0]  # fallback to first if none has index "1"
            )

            # Convert Unix timestamp to readable date
            timestamp = work_summary['created-date']['value']
            input_date = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')

            results.append({
                'workCode': work_summary['put-code'],
                'orcid_id': orcid_id,
                'org_first_name': row['first_name'],
                'org_last_name': row['last_name'],
                'input_date': input_date
            })

        time.sleep(1)  # Be polite to the API
        # Progress indicator
        processed = index + 1
        if processed % 10 == 0:
            print(f"Progress: {processed}/{total} members")
    df_result = pd.DataFrame(results)

    # Always save output
    df_result.to_csv('../data/outputs/work_codes.csv',
                     index=False,
                     sep=';',
                     encoding='utf-8-sig')

    print(f"Saved {len(df_result)} work codes to data/outputs/work_codes.csv")
    return df_result

def filter_work_codes(criteria="all", start_date="", end_date="", df=None, df_existing=None):
    """
    Filters the work codes DataFrame before fetching details.
    Note: 'input_date' is the date the work was added to ORCID, not the publication date.

    criteria options:
        "all"       — no filtering, fetch everything
        "date"      — only works added to ORCID on or after start_date
                      optionally also on or before end_date
        "new_only"  — only works whose workCode is not in df_existing
                      df_existing should be a previously saved work_details CSV
    """

    if df is None:
        print("Error: No DataFrame provided.")
        return None

    filtered_df = df.copy()

    if 'input_date' in filtered_df.columns:
        filtered_df['input_date'] = pd.to_datetime(filtered_df['input_date'], errors='coerce')

    if criteria == "new_only":
        if df_existing is None:
            print("Error: No existing data found or provided. Returning original data.")
            return filtered_df
        existing_codes = df_existing['workCode'].unique()
        filtered_df = filtered_df[~filtered_df['workCode'].isin(existing_codes)]

    elif criteria == "date":
        try:
            filtered_df = filtered_df[filtered_df['input_date'] >= pd.to_datetime(start_date)]
        except Exception as e:
            print(f"Date Error: {e}. Use 'YYYY-MM-DD' format.")
        if end_date != "":
            try:
                filtered_df = filtered_df[filtered_df['input_date'] <= pd.to_datetime(end_date)]
            except Exception as e:
                print(f"Date Error: {e}. Use 'YYYY-MM-DD' format.")

    elif criteria == "all":
        pass

    else:
        print(f"Warning: Invalid criteria '{criteria}'. Options: 'all', 'date', 'new_only'.")

    return filtered_df