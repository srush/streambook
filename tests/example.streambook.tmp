
import streamlit as __st
import streambook
__toc = streambook.TOCSidebar()
__toc._add(streambook.H1('Streambook example'))
__toc._add(streambook.H2('Main Code'))
__toc._add(streambook.H2('Advanced Features'))
__toc._add(streambook.H2('Longer example'))
__toc._add(streambook.H2('Exporting to Jupyter'))

__toc.generate()
__st.markdown(r"""<span id='Streambook example'> </span>
# Streambook example""", unsafe_allow_html=True)
__st.markdown(r"""
Streambook is a setup for writing live-updating notebooks
in any editor that you might want to use (emacs, vi, notepad).""", unsafe_allow_html=True)
with __st.echo(), streambook.st_stdout('info'):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import time
__st.markdown(r"""<span id='Main Code'> </span>
## Main Code""", unsafe_allow_html=True)
__st.markdown(r"""
Notebook cells are separated by spaces. Comment cells are rendered
as markdown.

See https://jupytext.readthedocs.io/en/latest/formats.html#the-light-format""", unsafe_allow_html=True)
with __st.echo(), streambook.st_stdout('info'):
    x = np.array([10, 20, 30])
__st.markdown(r"""
Cells that end with an explicit variables are printed. 

See https://docs.streamlit.io/en/stable/api.html#magic-commands""", unsafe_allow_html=True)
with __st.echo(), streambook.st_stdout('info'):
    x
__st.markdown(r"""
Dictionaries are pretty-printed using streamlit and can be collapsed""", unsafe_allow_html=True)
with __st.echo(), streambook.st_stdout('info'):
    data = [dict(key1 = i, key2=f"{i}", key3=100 -i) for i in range(100)]
__st.markdown(r"""
Pandas dataframe also show up in tables. """, unsafe_allow_html=True)
with __st.echo(), streambook.st_stdout('info'):
    df = pd.DataFrame(data)
    df
with __st.echo(), streambook.st_stdout('info'):
    df.plot()
    __st.pyplot()
with __st.echo(), streambook.st_stdout('info'):
    x = "hello"
    # Printing
    print("Printing", x)
    print("Printing2", x)
    "Output", x

