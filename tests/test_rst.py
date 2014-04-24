import mock

import pytest
import mfr

from mfr_docx import Handler as RstHandler
from mfr_docx.render import render_html


@pytest.fixture()
def fakefile():
    """A simple file-like object"""
    return mock.Mock(spec=file)

def setup_function(func):
    mfr.register_filehandler(RstHandler)
    mfr.config['STATIC_URL'] = '/static'

def teardown_function(func):
    mfr.core.reset_config()

def test_detect_docx_extension(fakefile):
    fakefile.name = 'file.rst'
    handler = RstHandler()

    assert handler.detect(fakefile) is True

def test_dont_detect_docx_extension(fakefile):
    fakefile.name = 'file.txt'
    handler = RstHandler()
    assert handler.detect(fakefile) is False

def test_render_text(fakefile):
    #TODO(kmjungersen)
    pass

#TODO(kmjungersen): more tests:

# def test_for_unicode(content):
#     assert isinstance(content, unicode)
#
# def test_for_html_tags(content):
#     assert '<div' in content
#
# def test_for_bold(content):
#     assert '<strong>' in content
#
# def test_for_unicode_character(content):
#     assert u'\xfc' in content