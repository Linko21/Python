# this is main entry point for the package
# it setups logging and calls the main function
# no need to change this file
# all changes should be done in cards_handler.py and submodules

import logging
import sys

import cards_handler

log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    stream=sys.stdout
)


def main():
    log.info("start cards main")
    cards_handler.handle()
    log.info("finished cards main")


if __name__ == '__main__':
    main()
