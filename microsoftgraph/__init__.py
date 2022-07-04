from microsoftgraph.client import Client
client = Client('CLIENT_ID', 'CLIENT_SECRET', account_type='common')
response = client.exchange_code(redirect_uri, code)