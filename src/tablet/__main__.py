"""
__main__.py
"""

import logging
import logging.config
import sys
import argparse
from tablet import version
from pathlib import Path

_logpath = Path("tablet.log")

def get_logger():
    """Initiate the logger"""
    log_conf_path = Path(__file__).parent / 'log.conf'  # Logging configuration is in this file
    logging.config.fileConfig(fname=log_conf_path, disable_existing_loggers=False)
    return logging.getLogger(__name__)  # Create a logger for this module

# Configure the expected parameters and actions for the argparse module
def parse(cl_input):
    """
    The command line interface is for diagnostic purposes

    :param cl_input:
    :return:
    """
    parser = argparse.ArgumentParser(description='Tabletx 2D draw interface to Cairo')
    parser.add_argument('-COLORS', '--colors', action='store_true',
                        help='Show the list of background color names')
    parser.add_argument('-D', '--debug', action='store_true',
                        help='Debug mode'),
    parser.add_argument('-V', '--version', action='store_true',
                        help='Print the current version')
    return parser.parse_args(cl_input)


def main():
    # Start logging
    logger = get_logger()
    logger.info(f'Tablet version: {version}')
    logger.info('-----------------\n')

    # Parse the command line args
    args = parse(sys.argv[1:])

    if args.version:
        # Just print the version and quit
        print(f'Scrall parser version: {version}')
        sys.exit(0)

    if args.colors:
        # Just print the database colors and quit
        # Config(rebuild_db=args.rebuild)  # Do any configuration tasks necessary before starting up the app
        # already_configured = True  # Don't run it again
        from tablet.styledb import StyleDB
        StyleDB.report_colors()

    logger.info("No problemo")  # We didn't die on an exception
    print("\nNo problemo")


if __name__ == "__main__":
    main()