import streambook
from io import StringIO


def test_markdown():
    output = StringIO()
    gen = streambook.Generate(output)
    gen.markdown("test")
    assert output.getvalue() == '__st.markdown(r"""test""")\n'


def test_gen():
    output = StringIO()
    gen = streambook.Generate(output)
    gen.code("x = 10\ny = 20\ny")
    print(output.getvalue())
    assert (
        output.getvalue()
        == """with __st.echo(), streambook.st_stdout('info'):
    x = 10
    y = 20
    y
"""
    )


def test_example():
    output = StringIO()
    streambook.Generator().generate("example.py", output)
    generated_output = output.getvalue()
    expected_output = open("tests/example.streambook.tmp", "r").read()
    assert generated_output == expected_output
