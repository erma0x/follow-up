# followup-bot
## Bot Telegram per la registrazione di risposte su Google Spreadsheets

Questo bot Telegram è stato sviluppato con Python 3 e permette di registrare le risposte dell'utente su un file di Google Spreadsheets.

## Prerequisiti

Prima di utilizzare questo bot, è necessario creare un account Google e accedere alla console di Google Cloud. Inoltre, è necessario creare un progetto, abilitare l'API di Google Drive e generare le credenziali OAuth 2.0 per il progetto.

Una volta generato il file di credenziali JSON, è necessario inserire il nome del file nella variabile creds del file main.py.

Infine, è necessario installare le seguenti librerie Python:
```
    python-telegram-bot
    gspread
    oauth2client
```

## Utilizzo

Per utilizzare questo bot Telegram, è necessario eseguire il file main.py. Una volta avviato il bot, è possibile interagire con esso tramite la chat di Telegram.

Il bot farà cinque domande all'utente: nome, cognome, email, account Instagram e colore preferito. Le risposte dell'utente verranno salvate su un file di Google Spreadsheets.

## Limitazioni

Questo bot è stato sviluppato a scopo dimostrativo e non è stato ottimizzato per la scalabilità e la sicurezza. In particolare, le credenziali OAuth 2.0 sono memorizzate in chiaro nel file di codice, il che rappresenta un potenziale rischio di sicurezza.

## Crediti

Questo bot Telegram è stato sviluppato da [nome dello sviluppatore]. Il codice è distribuito con licenza MIT.

# Processo
1. manda link video 1
2. scrivi 'acconsento' per lasciare le informazioni
3. manda le 5 domande
4. domande e salva su google docs
5. manda link video 2
6. manda link chat whatsapp

# Test
`python3 followup_bot.py`

# In processo su un VPS tipo linode.com
`nohup python3 followup_bot.py 1> bot.out & 2>bot.err`