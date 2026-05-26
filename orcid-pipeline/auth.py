from config import ORCID_TOKEN

def get_headers():
    """Returns the headers required for every ORCID API request."""
    return {
        'Accept': 'application/json',
        'Authorization': f'Bearer {ORCID_TOKEN}'
    }