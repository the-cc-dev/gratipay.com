from subprocess import Popen, PIPE

from markupsafe import Markup
import misaka as m  # http://misaka.61924.nl/


def render(markdown):
    return Markup(m.html(
        markdown,
        extensions=m.EXT_AUTOLINK | m.EXT_STRIKETHROUGH | m.EXT_NO_INTRA_EMPHASIS,
        render_flags=m.HTML_SKIP_HTML | m.HTML_TOC | m.HTML_SMARTYPANTS | m.HTML_SAFELINK
    ))


def marky(markdown):
    """Process markdown the same way npm does.
    """
    echo = Popen(("echo", markdown), stdout=PIPE)
    marky = Popen(("marky-markdown", "/dev/stdin"), stdin=echo.stdout, stdout=PIPE)
    return marky.communicate()[0]
