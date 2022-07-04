import msal
from msal import PublicClientApplication

APPLICATION_ID = '79fe01a8-2622-41e6-9b06-e2eab4d942d0'
CLIENT_SECRET = '9y88Q~5Ra9ricJKqvVPGrHpckbuy8ROIKfrWobgz'
authority_url = 'http://login.microsoftonline.com/consumers/'
base_url = 'https://graph.microsoft.com/v1.0/'

endpoint = base_url + 'me'
SCOPES = ['User.Read', 'User.Export.All']

client_instance = msal.ConfidentialClientApplication(
    client_id=APPLICATION_ID,
    client_credential=CLIENT_SECRET,
    authority=authority_url
)

authorization_request_url = client_instance.get_authorization_request_url
