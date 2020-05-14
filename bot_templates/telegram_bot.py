from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def __set_logger(logger_name, log_file, verbose):
    import logging

    logger = logging.getLogger(logger_name)  

    # .hasHandlers() is not working 
    # print(logger.handlers)
    # print(logger.hasHandlers())
    # if logger exists don't add new handlers
    if(not logger.handlers):
        verbosity = {0:50,1:40,2:30,3:20}
        if(verbosity.get(verbose)):
            logger.setLevel(verbosity.get(verbose))
        else:
            logger.setLevel(20)
        
        # log formatter
        formatter = logging.Formatter("[%(levelname)s] %(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

        # file handler
        if(log_file):
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        # stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger




def error(update, context):
    """Log Errors caused by Updates."""
    logger.error('Update "%s" caused error "%s"', update, context.error)

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("""
    """)

    # log info
    logger.info("help used username:{0}".format(update.message.from_user.username))

def example_function(update, context):
    try:
        arg0 = context.args[0]
        update.message.reply_text(arg0)

        # log info
        logger.info("example_function used username:{0}".format(update.message.from_user.username))
    except (IndexError, ValueError): 
        update.message.reply_text("usage /example_function <arg>")

        # log info
        logger.warning("function example_function username:{0}".format(update.message.from_user.username), exc_info=True)




# set logger
logger = __set_logger(__name__, "log/telegram.log", 3)


from my_bot_key import botkey
updater = Updater(botkey, use_context=True)

# bot loop
dp = updater.dispatcher

# command handler
dp.add_handler(CommandHandler("example_function", example_function, pass_args=True))
dp.add_handler(CommandHandler("help", help))

# message handler 
dp.add_handler(MessageHandler(Filters.text, echo))

# error handler
dp.add_error_handler(error)

updater.start_polling()
updater.idle()





