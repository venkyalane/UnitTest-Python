import logging


def get_the_logs():
    logger = logging.getLogger()
    filehandler = logging.FileHandler("python_page_logs.log")  # mode="w"
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)  # WARNING DEBUGE
    return logger

