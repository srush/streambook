import streamlit as st
from contextlib import contextmanager
from io import StringIO
from streamlit.report_thread import REPORT_CONTEXT_ATTR_NAME
from threading import current_thread
import sys

st.set_option("deprecation.showPyplotGlobalUse", False)


@contextmanager
def st_redirect(src, dst):
    placeholder = st.empty()
    output_func = getattr(placeholder, dst)

    with StringIO() as buffer:
        old_write = src.write

        def new_write(b):
            if getattr(current_thread(), REPORT_CONTEXT_ATTR_NAME, None):
                buffer.write(b.replace("\n", "\n\n"))
                output_func(buffer.getvalue())
            else:
                old_write(b)

        try:
            src.write = new_write
            yield
        finally:
            src.write = old_write


@contextmanager
def st_stdout(dst):
    with st_redirect(sys.stdout, dst):
        yield


@contextmanager
def st_stderr(dst):
    with st_redirect(sys.stderr, dst):
        yield


class Header:
    tag: str = ""

    def __init__(self, text: str):
        self.text = text

    @property
    def id(self):
        """Create an identifcator from text."""
        return "-".join(self.text.split()).lower()

    @property
    def anchor(self):
        """Provide html text for anchored header. Example:
        <h1 id="abcdef">Abc Def</h1>
        """
        return f"<{self.tag} id='{self.id}'>{self.text}</{self.tag}>"

    def toc_item(self) -> str:
        """Make markdown item for TOC listing. Example:
        '  - <a href='#abc'>Abc</a>'
        """
        return f"{self.spaces}- <a href='#{self.text}'>{self.text}</a>"

    @property
    def spaces(self):
        return dict(h1="", h2=" " * 2, h3=" " * 4).get(self.tag)


class H1(Header):
    tag = "h1"


class H2(Header):
    tag = "h2"


class H3(Header):
    tag = "h3"


class TOC:
    """
    Original code, used with modifications:
    https://discuss.streamlit.io/t/table-of-contents-widget/3470/8?u=epogrebnyak
    """

    def __init__(self):
        self._headers = []
        self._placeholder = st.empty()

    def title(self, text):
        self._add(H1(text))

    def header(self, text):
        self._add(H2(text))

    def subheader(self, text):
        self._add(H3(text))

    def generate(self):
        text = "\n".join([h.toc_item() for h in self._headers])
        self._placeholder.markdown(text, unsafe_allow_html=True)

    def _add(self, header):
        self._headers.append(header)


class TOCSidebar(TOC):
    def __init__(self):
        self._headers = []
        self._placeholder = st.sidebar.empty()
