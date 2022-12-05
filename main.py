import constant as keys
import speechReg
import textreply

from telegram.ext import *

print('bot initializes...')


def start_command(update, context):
    update.message.reply_text("Hi im Goosebot, trying typing anything to get started!")


def help_command(update, context):
    update.message.reply_text("Google it HONK!")


def stop(update, context):
    update.message.reply_text("Goosebot shuts down...")
    updater.stop()
    updater.is_idle = False

def send_document(update, context, path):
    chat_id = update.message.chat_id
    document = open(f'{path}', 'r')
    context.bot.send_document(chat_id, document)


def handle_message(update, context):
    # divide the message by text and voice
    if update.message.photo:
        photo = update.message.photo
        print(f'Photo received')

        text = "The ratio of the image is: \n"
        for p in photo:
            text += f"{p.height} by {p.width}"
            text += '\n'
        print(text)
        update.message.reply_text(text)

    elif update.message.text:
        f = update.message.text
        print(f'Received text: {f}')
        r = textreply.reply(f)
        print(f'Replied text: {r}')

        # if the reply is a csv path
        # print(f'{r[-3:]=}')
        if r[-3:] == 'csv':
            send_document(update=update, context=context, path=f'{r}')
            return

        # else just reply a text
        update.message.reply_text(r)

    elif update.message.voice:

        voice = update.message.voice
        update.message.reply_text("Voice message received...")

        with open('sound.ogg', 'wb') as data:
            context.bot.get_file(voice).download(out=data)

        return


    elif update.message.video:
        update.message.reply_text("I don't watch videos :(")



def error(update, context):
    print(f'update {update} caused error {context.error}')


def main():
    global updater
    updater = Updater(keys.apikey, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler('stop', stop))
    dispatcher.add_handler(MessageHandler(Filters.all, handle_message))

    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
