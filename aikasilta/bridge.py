# -*- coding: utf-8 -*-
# pylint: disable=c-extension-no-member,expression-not-assigned,line-too-long,logging-fstring-interpolation
"""Build a bridge back from the Nineties."""
import configparser
import csv
import json
import logging
import pathlib
import sys
from typing import no_type_check

# from atlassian import Bitbucket, Confluence, Jira


ENCODING = 'utf-8'

APP = 'aikasilta'

LOG = logging.getLogger()  # Temporary refactoring: module level logger
LOG_FOLDER = pathlib.Path('logs')
LOG_FILE = f'{APP}.log'
LOG_PATH = pathlib.Path(LOG_FOLDER, LOG_FILE) if LOG_FOLDER.is_dir() else pathlib.Path(LOG_FILE)
LOG_LEVEL = logging.INFO

FAILURE_PATH_REASON = 'Failed validation for path %s with error: %s'


@no_type_check
def init_logger(name=None, level=None):
    """Initialize module level logger"""
    global LOG  # pylint: disable=global-statement

    log_format = {
        'format': '%(asctime)s.%(msecs)03d %(levelname)s [%(name)s]: %(message)s',
        'datefmt': '%Y-%m-%dT%H:%M:%S',
        # 'filename': LOG_PATH,
        'level': LOG_LEVEL if level is None else level,
    }
    logging.basicConfig(**log_format)
    LOG = logging.getLogger(APP if name is None else name)
    LOG.propagate = True


@no_type_check
def walk_tree_explicit(base_path):
    """Visit the files in the folders below base path."""
    if base_path.is_file():
        yield base_path
    else:
        for entry in base_path.iterdir():
            if entry.is_dir():
                for file_path in entry.iterdir():
                    yield file_path
            else:
                yield entry


@no_type_check
def visit(tree_or_file_path):
    """Visit tree and yield the leaves."""
    thing = pathlib.Path(tree_or_file_path)
    if thing.is_file():
        yield thing
    else:
        for path in thing.rglob('*'):
            yield path


@no_type_check
def slugify(error):
    """Replace newlines by space."""
    return str(error).replace('\n', '')


@no_type_check
def parse_csv(path):
    """Opinionated csv as config parser returning the COHDA protocol."""
    if not path.stat().st_size:
        return False, 'ERROR: Empty CSV file'

    with open(path, newline='') as handle:
        try:
            try:
                dialect = csv.Sniffer().sniff(handle.read(1024), ',\t; ')
                handle.seek(0)
            except csv.Error as err:
                if 'could not determine delimiter' in str(err).lower():
                    dialect = csv.Dialect()
                    dialect.delimiter = ','
                    dialect.quoting = csv.QUOTE_NONE
                    dialect.strict = True
                else:
                    return False, slugify(err)
            try:
                reader = csv.reader(handle, dialect)
                for _ in reader:
                    pass
                return True, ''
            except csv.Error as err:
                return False, slugify(err)
        except (Exception, csv.Error) as err:
            return False, slugify(err)


@no_type_check
def parse_ini(path):
    """Simple ini as config parser returning the COHDA protocol."""
    config = configparser.ConfigParser()
    try:
        config.read(path)
        return True, ''
    except (
        configparser.NoSectionError,
        configparser.DuplicateSectionError,
        configparser.DuplicateOptionError,
        configparser.NoOptionError,
        configparser.InterpolationDepthError,
        configparser.InterpolationMissingOptionError,
        configparser.InterpolationSyntaxError,
        configparser.InterpolationError,
        configparser.MissingSectionHeaderError,
        configparser.ParsingError,
    ) as err:
        return False, slugify(err)


@no_type_check
def parse_json(path):
    """Simple json as config parser returning the COHDA protocol."""
    return parse_generic(path, json.load)


@no_type_check
def load_xml(source):
    """Proxy until implemented."""
    return NotImplemented


@no_type_check
def parse_xml(path):
    """Simple xml as config parser returning the COHDA protocol."""
    if not path.stat().st_size:
        return False, 'ERROR: Empty XML file'

    xml_tree, message = load_xml(path)
    if xml_tree:
        return True, ''

    return False, slugify(message)


@no_type_check
def parse_generic(path, loader, loader_options=None):
    """Simple generic parser proxy."""
    if loader_options is None:
        loader_options = {}
    with open(path, 'rt', encoding='utf-8') as handle:
        try:
            _ = loader(handle, **loader_options)
            return True, ''
        except Exception as err:
            return False, slugify(err)


@no_type_check
def process(path, handler, success, failure):
    """Generic processing of path yields a,ended COHDA protocol."""
    valid, message = handler(path)
    if valid:
        return True, message, success + 1, failure

    return False, message, success, failure + 1


def main(argv: dict[str, None] | None = None, abort: bool | None = None, debug: bool | None = None) -> tuple[int, str]:
    """Drive across the bridge.
    This function acts as the command line interface backend.
    There is some duplication to support testability.
    """
    init_logger(level=logging.DEBUG if debug else None)
    forest = argv if argv else sys.argv[1:]
    if not forest:
        print('Usage: time-bridge paths-to-files')
        return 0, 'USAGE'
    num_trees = len(forest)
    LOG.debug('Guarded dispatch forest=%s, num_trees=%d', forest, num_trees)

    LOG.info(
        'Starting validation visiting a forest with %d tree%s',
        num_trees,
        '' if num_trees == 1 else 's',
    )
    for tree in forest:
        for path in visit(tree):
            LOG.debug(' - path=%s', path)
    failure = False
    print(f"{'OK' if not failure else 'FAIL'}")

    return 0, ''
