import logging

logging.basicConfig(level=logging.DEBUG)
# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("file.log")
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(pathname)s- %(message)s - in line %(lineno)d "
    # "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(stack_info)s"
)
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# logger.warning("This is a warning")
# logger.error("This is an error")
