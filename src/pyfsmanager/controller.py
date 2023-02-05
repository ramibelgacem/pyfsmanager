import logging
import os
from pathlib import Path

TEMPLATES_PATH = (
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/templates/"
)
TEMPLATES_SUFFIX = "template"


def create_file(args, content=None):
    """Create a file based on a predefined template extension

    Parameters
    ----------
    args : Namespace
            The arguments that are passed through the command line
    content : str, optional
                The content of the new file to create (default is None)

    Raises
    ------
    FileExistsError
            If the name of the file to create already exists.
    """
    # create the directory of the file
    full_path = Path()
    if args.dir:
        full_path = full_path / args.dir
        if not full_path.exists():
            full_path.mkdir()

    # create the new file if it does not exist
    full_path = full_path / args.name
    try:
        full_path.touch(exist_ok=False)
        if content:
            full_path.write_text(content)
        logging.info(f"the path {full_path.name} created successfully")
        # if the app returns None, then the exit code is by default 0
    except FileExistsError:
        logging.error(f"the file {full_path.name} already exists")
        raise SystemExit(1)


def create_from_template(args):
    """Create a file based on a predefined template extension

    Parameters
    ----------
    args : Namespace
            The arguments that are passed through the command line
    """
    from_file = Path(TEMPLATES_PATH + TEMPLATES_SUFFIX + "." + args.tname)

    if from_file.exists():
        create_file(args, from_file.read_text())
    else:
        logging.error("The chosen template is not found")
