# -*- coding: utf-8 -*-
import pytest  # type: ignore

import aikasilta.cli as cli


def test_main_nok_bad_arg(capsys):
    with pytest.raises(SystemExit, match='2'):
        cli.main(['non-existing-thing'], debug=False)
    out, err = capsys.readouterr()
    assert 'error' in out.lower()
    assert 'for now only existing paths accepted.' in out.lower()
    assert not err
