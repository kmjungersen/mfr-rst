"""RST renderer module"""

from docutils.core import publish_parts

from mfr import RenderResult

def render_html(fp, *args, **kwargs):
    '''This function takes a file, reads it, and then passes
    the content to Docutils for rendering.  After rendering
    the html content, the function returns a RenderResult
    object.

    Note: In this case, we only render the html_body because
    this html will be nested in an existing webpage.
    '''
    file_content = fp.read()
    html_string = publish_parts(
        file_content, writer_name='html')['html_body']

    return RenderResult(html_string)