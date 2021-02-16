# # The Title of the notebook is


import sys
import matplotlib.pyplot as plt
import numpy as np 
import altair as alt
import pandas as pd

# This is a multiline
# Markdown cell

# Another Markdown cell right here is o


# This is a code cell
class A():
    def one():
        return 1

    def two():
        return 2



# Some more markdown


"hello goodbye hello"



[1, 2, 3]





df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
df


c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])


c
