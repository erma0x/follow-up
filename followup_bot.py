import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from oauth2client.service_account import ServiceAccountCredentials
import gspread

TOKEN = "tokenbotfather" # token botfather telegram
YOUTUBE_LINK = "YouTube 1"
QUESTION_1, QUESTION_2, QUESTION_3, QUESTION_4, QUESTION_5 = range(5)
YOUTUBE_LINK_2 = "YouTube 2"
WHATSAPP_LINK = "whatsapp"

# /start
def start(update, context):
    # Messaggio di benvenuto
    update.message.reply_text("Benvenuto ❤️ Ti farò 5 domande e salverò le tue risposte su Google Spreadsheet.")
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Nome del file di Google Spreadsheet").sheet1
    context.bot.send_video(chat_id=update.effective_chat.id, video=YOUTUBE_LINK)
    update.message.reply_text("Benvenuto! Risponderai a due domande a risposta aperta.")
    return QUESTION_1

STUPID_ANSWERS = ('acconsento'.upper(),'acconsento','Acconsento','aCCONSENTO','aconsento','ACONSENTO')
def question_0(update, context):
    messaggio ="""
    Ciao! Grazie per aver scelto il nostro bot. 
    Prima di iniziare, ti informiamo che raccoglieremo alcune informazioni su di te, 
    come nome, cognome, email e preferenze di prodotto, per fini di marketing.
      Queste informazioni ci aiuteranno a personalizzare le nostre offerte 
      e ad inviarti comunicazioni commerciali in linea con i tuoi interessi.

    Per continuare con l'utilizzo del bot, 
    ti chiediamo gentilmente di acconsentire alla raccolta di 
    queste informazioni. Se non acconsenti, potrai comunque 
    continuare ad utilizzare il bot ma non potremo offrirti promozioni personalizzate.

    Per acconsentire alla raccolta di informazioni,
    basta rispondere con un messaggio contenente la parola 'acconsento'. Grazie!
    """
    text = update.message.text
    update.message.reply_text("Grazie per la risposta! ❤️")
    if text in STUPID_ANSWERS:
        context.user_data['question_0'] = text
    else:
        show_video_2(update, context)
        

def question_1(update, context):
    update.message.reply_text("Qual è il tuo nome?")
    return QUESTION_2

def question_2(update, context):
    update.message.reply_text("Qual è il tuo cognome?")
    return QUESTION_3

def question_3(update, context):
    update.message.reply_text("Qual è la tua email?")
    return QUESTION_4

def question_4(update, context):
    update.message.reply_text("Qual è il tuo account Instagram?")
    return QUESTION_5

def question_5(update, context):
    update.message.reply_text("Qual è il tuo colore preferito?")
    sheet = context.user_data["sheet"]
    sheet.append_row([update.message.from_user.id, update.message.text])        
    return show_video_2(update, context)

def show_video_2(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=YOUTUBE_LINK_2)
    return send_final_link

def send_final_link(update, context): 
    context.bot.send_link(chat_id=update.effective_chat.id, link=WHATSAPP_LINK)
    return ConversationHandler.END

def answer(update, context):
    text = update.message.text
    update.message.reply_text("Grazie per la risposta! ❤️")
    
    if not context.user_data.get('question_1_answered'):
        context.user_data['question_1'] = text
        context.user_data['question_1_answered'] = True
    elif not context.user_data.get('question_2_answered'):
        context.user_data['question_2'] = text
        context.user_data['question_2_answered'] = True
    elif not context.user_data.get('question_3_answered'):
        context.user_data['question_3'] = text
        context.user_data['question_3_answered'] = True
    elif not context.user_data.get('question_4_answered'):
        context.user_data['question_4'] = text
        context.user_data['question_4_answered'] = True
    elif not context.user_data.get('question_5_answered'):
        context.user_data['question_5'] = text
        context.user_data['question_5_answered'] = True
    else:
        return context.bot.send_video(chat_id=update.effective_chat.id, video=YOUTUBE_LINK_2)


# Funzione per gestire il comando /cancel
def cancel(update, context):
    update.message.reply_text("Hai interrotto la conversazione. ")
    sheet = context.user_data["sheet"]
    sheet.append_row([update.message.from_user.id, update.message.text])   
    return ConversationHandler.END

def main():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            QUESTION_1: [MessageHandler(Filters.text, answer, pass_user_data=True)],
            QUESTION_2: [MessageHandler(Filters.text, answer, pass_user_data=True)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(conversation_handler)
    # start bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()