# -*- coding: utf-8 -*-
import mock

import pytest
from docutils.core import publish_parts

# import mfr
# from mfr_docx import Handler as RstHandler
# from mfr_docx.render import render_html


@pytest.fixture
def fakefile():
    """A simple file-like object"""
    return mock.Mock(spec=file)

# def setup_function(func):
#     mfr.register_filehandler(RstHandler)
#     mfr.config['STATIC_URL'] = '/static'
#
# def teardown_function(func):
#     mfr.core.reset_config()
#
# def test_detect_docx_extension():
#     fakefile.name = 'file.rst'
#     handler = RstHandler()
#
#     assert handler.detect(fakefile) is True
#
# def test_dont_detect_RST_extension():
#     fakefile.name = 'file.txt'
#     handler = RstHandler()
#     assert handler.detect(fakefile) is False

def test_render_text(fakefile):
    test_string = 'Hello World'
    fakefile.return_value = test_string

    html_string = publish_parts(fakefile.return_value,
                                writer_name='html')['html_body']

    assert test_string in html_string



def test_for_html_tags(fakefile):
    test_string = 'What is reStructuredText?\n~~~~~~~~~~~~~~~~~~~~~~~~~'
    fakefile.return_value = test_string

    target_string = '<div class="document" id="what-is-restructuredtext">\n' \
                    '<h1 class="title">What is reStructuredText?</h1>\n' \
                    '</div>\n'

    html_string = publish_parts(fakefile.return_value,
                                writer_name='html')['html_body']

    assert html_string == target_string

def test_for_bold(fakefile):
    test_string = '**bold text**'
    fakefile.return_value = test_string

    target_string = '<div class="document">\n' \
                    '<p><strong>bold text</strong></p>\n' \
                    '</div>'

    html_string = publish_parts(fakefile.return_value,
                                writer_name='html')['html_body']

    assert target_string in html_string

def test_for_unicode_character(fakefile):
    test_string = u'\xfc'
    fakefile.return_value = test_string

    html_string = publish_parts(fakefile.return_value,
                                writer_name='html')['html_body']

    print html_string
    assert test_string in html_string




#TODO(kmjungersen): ATTN(sloria) - Is this test for unicode really necessary? it's been included
#TODO:             in previous renderers but I personally don't see the need.

# def test_for_unicode(fakefile):
#     test_string = 'Hello World'
#     fakefile.return_value = test_string
#     assert isinstance(fakefile.return_value, unicode)