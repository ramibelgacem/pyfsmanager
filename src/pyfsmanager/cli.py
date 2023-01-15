import argparse
import logging

from pyfsmanager.controller import create_file, create_from_template

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(message)s",
    level=logging.INFO,
    datefmt="%d/%m/%Y %H:%M:%S",
)

TEMPLATES_EXTENSION = ["json", "txt", "py"]


def main():
    """
    Example:
    > pyfsmanager blank notes.txt -d notes
    > pyfsmanager template txt notes.txt -d notes
    """
    global_parser = argparse.ArgumentParser(
        prog="pyfsmanager",
        description="Create new files based on builtin templates or empty content",
        epilog="Hope you like this program !",
        argument_default=argparse.SUPPRESS,
    )
    global_parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    subparsers = global_parser.add_subparsers(
        title="subcommands", help="file creation choices", required=True
    )
    blank_parser = subparsers.add_parser("blank", help="Create an empty file")
    blank_parser.set_defaults(func=create_file)

    template_parser = subparsers.add_parser(
        "template", help="Create a file from a template"
    )
    template_parser.add_argument(
        "tname", choices=TEMPLATES_EXTENSION, help="Name of the template"
    )
    template_parser.set_defaults(func=create_from_template)

    for parser in [blank_parser, template_parser]:
        parser.add_argument("name", help="Name of the new file")
        parser.add_argument("-d", "--dir", help="Name of the directory")

    args = global_parser.parse_args()
    args.func(args)
