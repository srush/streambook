
# ## Streambook example

import sys
import numpy as np 
import altair as alt
import pandas as pd


# Here I am writing some comments on the code

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

df

# Here is a chart

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c',
    tooltip=['a', 'b', 'c'])

c

