from members import load_members
from work_codes import fetch_work_codes

# Load members
df_members = load_members()

# Test on just one person - Corinna Kleinert
test_member = df_members[df_members['last_name'] == 'Kleinert']
print(f"Testing with: {test_member['first_name'].values[0]} {test_member['last_name'].values[0]}")

# Fetch work codes
df_codes = fetch_work_codes(test_member)

print(f"\nFound {len(df_codes)} publications")
print(df_codes.head())