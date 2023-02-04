from utils.logging import logger


def p1():
    a = 1
    b = a + 1
    logger.info("Print from Module 1")
    try:
        a = 1/0
    except:
        logger.exception("An error has occurred", exc_info=1)
    return b