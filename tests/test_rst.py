import mock

import pytest
from docutils.core import publish_parts

# import mfr
# from mfr_docx import Handler as RstHandler
# from mfr_docx.render import render_html
#

@pytest.fixture
def fakefile(return_string):
    """A simple file-like object"""
    return mock.Mock(spec=file, return_value=return_string)

# def setup_function(func):
#     mfr.register_filehandler(RstHandler)
#     mfr.config['STATIC_URL'] = '/static'
#
# def teardown_function(func):
#     mfr.core.reset_config()
#
# def test_detect_docx_extension():
#     fakefile().name = 'file.rst'
#     handler = RstHandler()
#
#     assert handler.detect(fakefile) is True
#
# def test_dont_detect_RST_extension():
#     fakefile().name = 'file.txt'
#     handler = RstHandler()
#     assert handler.detect(fakefile) is False

def test_render_text():
    test_string = 'Hello World'

    #fakefile().return_value = test_string
    html_string = publish_parts(fakefile(test_string).return_value,
                                writer_name='html')['html_body']

    assert test_string in html_string

def test_for_unicode():
    test_string = 'Hello World'
    assert isinstance(fakefile(test_string).return_value, unicode)

def test_for_html_tags():
    test_string = 'What is reStructuredText?\n~~~~~~~~~~~~~~~~~~~~~~~~~'

    target_string = '<div class="document" id="what-is-restructuredtext">\n' \
                    '<h1 class="title">What is reStructuredText?</h1>\n' \
                    '</div>\n'

    html_string = publish_parts(fakefile(test_string).return_value,
                                writer_name='html')['html_body']

    assert target_string == html_string






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