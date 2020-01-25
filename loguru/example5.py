from loguru import logger
import sys

logger.remove()

my_sink = logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")


logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")


logger.debug("Test debug")


logger.error("Test error")


logger.critical("Test critical")
