# dgs-suus-member-analysis

## Setup

### 1. Get your ORCID API token

Go to [orcid.org/developer-tools](https://orcid.org/developer-tools) and register an app to get your `CLIENT_ID` and `CLIENT_SECRET`.

Then run this once manually in your terminal to generate a token:

```python
import requests

response = requests.post("https://orcid.org/oauth/token", data={
    'client_id': 'YOUR_CLIENT_ID',
    'client_secret': 'YOUR_CLIENT_SECRET',
    'grant_type': 'client_credentials',
    'scope': '/read-public'
}, headers={'Accept': 'application/json'})

print(response.json()['access_token'])
```

Copy the printed token into your `.env` file:

ORCID_TOKEN=paste_your_token_here

### 2. Set up your environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r orcid-pipeline/requirements.txt
```

### 3. Configure your `.env`

Copy `.env.example` to `.env` and fill in your values:

