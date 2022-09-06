from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import settings_fetchgmail as settings

SCOPES = ['https://mail.google.com/']

def main():
    print ("Iniciant flux OAUTH2 loopback. Aixo obrirà un navegador on hauràs de fer login amb l'usuari del qual vols que mailtoticket pugui accedir a la seva bustia")
    print ("Primer hauràs de crear l'aplicació i baixar-te el fitxer credentials.json de la consola de Google Cloud")
    print ("------")
    flow = InstalledAppFlow.from_client_secrets_file(settings.credentials_file, SCOPES)
    creds = flow.run_local_server(port=0)
    with open(settings.token_file, 'wb') as token:
        pickle.dump(creds, token)
    print ("------")
    print ("Fitxer %s creat" % settings.token_file)
    print ("Ja pots copiar-lo al lloc on hagis d'executar el fetchgmail")

if __name__ == '__main__':
  main()
