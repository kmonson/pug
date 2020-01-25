from loguru import logger

logger.add("output.log", backtrace=True, diagnose=True)

def my_function(x, y, z):
    # An error? It's caught anyway!
    try:
        return 1 / (x + y + z)
    except ZeroDivisionError:
        logger.exception("What?")

my_function(1,2,-3)