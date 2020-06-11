from telegram.ext import Updater, CommandHandler, MessageHandler,    Filters, InlineQueryHandler


def sayhi(bot, job):
    job.context.message.reply_text("hi")

def time(bot, updater,job_queue):
    job = job_queue.run_repeating(sayhi, 5, context=updater)

def main():
    updater = Updater("Your token")
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text , time,pass_job_queue=True))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
