#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Cross the bridge back from the Nineties."""
import pathlib
import os
import sys

import aikasilta.bridge as tb

DEBUG_VAR = 'AIKASILTA_DEBUG'
DEBUG = bool(os.getenv(DEBUG_VAR, ''))

ABORT_VAR = 'AIKASILTA_ABORT'
ABORT = bool(os.getenv(ABORT_VAR))


# pylint: disable=expression-not-assigned
def main(argv=None, abort=None, debug=None):
    """Dispatch processing of the job.
    This is the strings only command line interface.
    For python API use interact with lint functions directly.
    """
    argv = sys.argv[1:] if argv is None else argv
    debug = debug if debug else DEBUG
    abort = abort if abort else ABORT
    unique_trees = {arg: None for arg in argv}
    for tree_or_leaf in unique_trees:
        if not pathlib.Path(tree_or_leaf).is_file() and not pathlib.Path(tree_or_leaf).is_dir():
            print('ERROR: For now only existing paths accepted.')
            sys.exit(2)

    code, _ = tb.main(unique_trees, abort=abort, debug=debug)
    return code
