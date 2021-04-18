import streambook
from io import StringIO

def test_gen():
    output = StringIO()
    gen = streambook.Generate(output)
    gen.markdown("test")
    assert output.getvalue() == '__st.markdown("""test""")\n'
