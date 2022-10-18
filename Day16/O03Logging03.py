
import logging

# logger1 = logging.getLogger("admin")
#
# logger2 = logging.getLogger("parent.child")

print("-"  * 40)

logger = logging.getLogger("parent.child")

# level was not set
logger.info("this is info level")

parentLogger = logging.getLogger("parent")

# configuring the parent logger
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s"))
# threshold level
parentLogger.setLevel(logging.INFO)
parentLogger.addHandler(handler)

# child logger emits
logger.info("this is info level.....")

