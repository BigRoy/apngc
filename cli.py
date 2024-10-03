# INITIALIZE LOGGER
import logging

import apngc.__main__

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%m-%d-%Y %H:%M:%S",
)

# LOG INFO
logging.info("Starting APNGC...")

if __name__ == "__main__":
    apngc.__main__.main()
