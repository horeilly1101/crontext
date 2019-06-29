import logging

# Create a custom logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

# Create handler
c_handler = logging.StreamHandler()

# Create formatter and add it to handler
c_format = logging.Formatter('%(levelname)s - %(name)s - %(asctime)s - %(message)s')
c_handler.setFormatter(c_format)

# Add handler to the logger
LOGGER.addHandler(c_handler)
