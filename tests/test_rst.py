import mock

import pytest
import mfr_rst


@pytest.fixture()
def fakefile(request):
    return mock.Mock(spec=file)


def test_detect(fakefile):
    assert False, 'finish me'


def test_render(fakefile):
    assert False, 'finish me'