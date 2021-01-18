import logging


logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(asctime)s %(message)s",
                    handlers=[logging.FileHandler("example.log"), logging.StreamHandler()])


logging.debug('This message should go to the log file and to the console')
logging.info('So should this')
logging.warning('And this, too')


# custom log level
logging.addLevelName(25, "Result")
logging.log(25, "asd")



def __set_logger(logger_name, log_file=None, log_level=20):

    logger = logging.getLogger(logger_name)  

    # .hasHandlers() is not working 
    # print(logger.handlers)
    # print(logger.hasHandlers())
    # if logger exists don't add new handlers
    if(not logger.handlers):
        logger.setLevel(log_level)
        
        # log formatter
        formatter = logging.Formatter("[%(levelname)s] %(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

        # stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # file handler
        if(log_file):
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

       
    return logger


    