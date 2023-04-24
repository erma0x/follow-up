# followup-bot
## Telegram bot for logging responses to Google Spreadsheets

This Telegram bot was developed with Python 3 and allows user responses to be recorded on a Google Spreadsheets file.

## Prerequisites

Before using this bot, you need to create a Google account and sign in to the Google Cloud Console. Additionally, you need to create a project, enable the Google Drive API, and generate OAuth 2.0 skills for the project.

Once the JSON credential file has been generated, you need to put the file name in the creds variable of the main.py file.

Finally, you need to install the following Python libraries:
```
      python-telegram-bot
      gspread
      oauth2client
```

## Usage

To use this Telegram bot, you need to run the main.py file. Once the bot has started, you can interact with it via Telegram chat.

The bot will ask the user five questions: first name, last name, email, Instagram account and favorite color. User responses will be saved to a Google Spreadsheets file.

## Limitations

This bot was developed for demonstration purposes and has not been optimized for scalability and security. In particular, OAuth 2.0 credentials are stored in plain text in the code file, which is a potential security risk.

## Credits

This Telegram bot was developed by [developer name]. The code is distributed under the MIT license.

# Process
1. send video link 1
2. write 'I agree' to leave information
3. send the 5 questions
4. questions and save to google docs
5. send video links 2
6. send whatsapp chat link

# Tests
`python3 followup_bot.py`

# Running on a VPS like linode.com
`nohup python3 followup_bot.py 1> bot.out & 2>bot.err`

## ______________________________________

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
