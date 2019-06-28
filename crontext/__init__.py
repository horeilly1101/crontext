import logging

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create handler
c_handler = logging.StreamHandler()

# Create formatter and add it to handler
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)

# Add handler to the logger
logger.addHandler(c_handler)
