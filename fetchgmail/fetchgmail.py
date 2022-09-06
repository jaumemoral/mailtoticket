import imaplib
import settings_fetchgmail as settings
import os
import subprocess
import pickle
import base64
from google.auth.transport.requests import Request


MAIL_TMP="/tmp/mail"

def escriure_mail(mail):
    with open(MAIL_TMP, "wb") as f:
        f.write(mail)
        f.flush()

def llegir_token():
    with open(settings.token_file, 'rb') as token:
        creds = pickle.load(token)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(settings.token_file, 'wb') as token:
            pickle.dump(creds, token)
    return creds

def generate_oauth2_string(username, access_token, base64_encode=True):
  """Generates an IMAP OAuth2 authentication string.

  See https://developers.google.com/google-apps/gmail/oauth2_overview

  Args:
    username: the username (email address) of the account to authenticate
    access_token: An OAuth2 access token.
    base64_encode: Whether to base64-encode the output.

  Returns:
    The SASL argument for the OAuth2 mechanism.
  """
  auth_string = 'user=%s\1auth=Bearer %s\1\1' % (username, access_token)
  if base64_encode:
    auth_string = base64.b64encode(auth_string)
  return auth_string


if not os.path.exists(settings.token_file):
    print("No tinc el token.pickle creat. Executa el oauth2.sh")
    exit(0)

creds = llegir_token()
access_token=creds.token
auth_string=generate_oauth2_string(settings.user, access_token,base64_encode=False)
imap_conn = imaplib.IMAP4_SSL('imap.gmail.com')
imap_conn.authenticate('XOAUTH2', lambda x: auth_string)
imap_conn.select('INBOX')

resp, items = imap_conn.uid('SEARCH',None, '(UNSEEN)')
items = items[0].split() # getting the mails id

for emailid in items:
    resp, data = imap_conn.uid('FETCH',emailid, "(RFC822)")    
    escriure_mail(data[0][1])
    with open(MAIL_TMP, "rb") as f:
        r=subprocess.run(settings.mailtoticket,stdin=f) 
        if r.returncode>0:
            imap_conn.uid('STORE', emailid, '-FLAGS', '(\Seen)')
