# -*- coding: utf-8 -*-
import pytest

format_header = {
    'default': "== %s ==",
    'markdown': "## %s",
}


@pytest.fixture(params=format_header)
def test_syntax(request):
    key = request.param
    return (key, format_header[key])

