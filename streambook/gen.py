import jupytext
import textwrap
import mistune
import re
import io


class Collect(mistune.Renderer):
    def __init__(self):
        super().__init__()
        self.headers = []

    def header(self, text, level, raw=None):
        self.headers.append((text, level - 1))
        return ""


class Generate:
    def __init__(self, out_stream, section_filter=None):
        self.out_stream = out_stream
        self.all_markdown = ""
        self.headers = []
        self.current_section = [None, None, None]
        self.section_filter = section_filter

    def gen(self, output):
        print(output, file=self.out_stream)

    def markdown(self, source):
        # Collect all the markdown headers
        c = Collect()

        markdown = mistune.Markdown(renderer=c)
        markdown(source)
        self.headers += c.headers
        head = ""
        for text, _ in c.headers:
            head += f"<span id='{text}'> </span>"
        for text, level in c.headers:
            self.current_section[level] = text
        self.all_markdown += source + "\n"
        if self.section_filter is not None and self.current_section[1] is not None:
            if not re.search(self.section_filter, self.current_section[1]):
                return
        if head:
            self.gen(
                '__st.markdown(r"""%s\n%s""", unsafe_allow_html=True)' % (head, source)
            )
        else:
            self.gen('__st.markdown(r"""%s""", unsafe_allow_html=True)' % (source))

    def code(self, source):
        if self.section_filter is not None and self.current_section[1] is not None:
            if not re.search(self.section_filter, self.current_section[1]):
                return
        wrapper = textwrap.TextWrapper(
            initial_indent="    ", subsequent_indent="    ", width=5000
        )
        if not source.strip():
            return
        self.gen("with __st.echo(), streambook.st_stdout('info'):")
        for line in source.splitlines():
            self.gen(wrapper.fill(line))


header = """
import streamlit as __st
import streambook
__toc = streambook.TOCSidebar()"""

footer = """
__toc.generate()"""


class Generator:
    def __init__(self, section_filter=None):
        self.section_filter = section_filter

    def generate(self, in_file, out_stream):
        out = io.StringIO()
        gen = Generate(out, section_filter=self.section_filter)

        print(header, file=out_stream)

        for i, cell in enumerate(jupytext.read(in_file)["cells"]):
            if cell["cell_type"] == "markdown":
                gen.markdown(cell["source"])
            else:
                gen.code(cell["source"])
        levels = ["streambook.H1", "streambook.H2", "streambook.H3"]
        print(
            "\n".join(
                [
                    "__toc._add(" + levels[level] + "('" + text + "'))"
                    for text, level in gen.headers
                ]
            ),
            file=out_stream,
        )
        print(footer, file=out_stream)
        print(out.getvalue(), file=out_stream)


if __name__ == "__main__":
    import argparse
    import os
    import sys

    parser = argparse.ArgumentParser(description="Stream book options.")
    parser.add_argument("file", help="file to run", type=os.path.abspath)
    args = parser.parse_args()
    Generator().generate(args.file, sys.stdout)
