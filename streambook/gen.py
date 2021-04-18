import jupytext
import textwrap
import mistune


class Render(mistune.Renderer):
    def __init__(self, gen):
        super().__init__()
        self.gen = gen

    def header(self, text, level, raw=None):
        if level == 1:
            self.gen.gen(f"__toc.title('{text}')")
        if level == 2:
            self.gen.gen(f"__toc.header('{text}')")
        if level == 3:
            self.gen.gen(f"__toc.subheader('{text}')")
        return ""


class Generate:
    def __init__(self, out_stream):
        self.out_stream = out_stream
        self.all_markdown = ""

    def gen(self, output):
        print(output, file=self.out_stream)

    def markdown(self, source):
        self.all_markdown += source + "\n"
        self.gen('__st.markdown("""%s""")' % source)

    def code(self, source):
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
    def __init__(self):
        pass

    def generate(self, in_file, out_stream):
        gen = Generate(out_stream)
        markdown = mistune.Markdown(renderer=Render(gen))
        gen.gen(header)
        for i, cell in enumerate(jupytext.read(in_file)["cells"]):
            if cell["cell_type"] == "markdown":
                gen.markdown(cell["source"])
            else:
                gen.code(cell["source"])
        markdown(gen.all_markdown)
        gen.gen(footer)


if __name__ == "__main__":
    import argparse
    import os
    import sys

    parser = argparse.ArgumentParser(description="Stream book options.")
    parser.add_argument("file", help="file to run", type=os.path.abspath)
    args = parser.parse_args()
    Generator().generate(args.file, sys.stdout)
