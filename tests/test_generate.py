import streambook
from io import StringIO

def test_gen():
    output = StringIO()
    gen = streambook.Generate(output)
    print(gen.markdown("test"))
    assert(False)
