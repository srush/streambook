
import streamlit as __st
import streambook
__toc = streambook.TOCSidebar()
__st.markdown("""# Streambook example""")
__st.markdown("""Streambook is a setup for writing live-updating notebooks
in any editor that you might want to use (emacs, vi, notepad).""")
with __st.echo(), streambook.st_stdout('info'):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import time
__st.markdown("""## Main Code""")
__st.markdown("""Notebook cells are separated by spaces. Comment cells are rendered
as markdown.

See https://jupytext.readthedocs.io/en/latest/formats.html#the-light-format""")
with __st.echo(), streambook.st_stdout('info'):
    x = np.array([10, 20, 30])
__st.markdown("""Cells that end with an explicit variables are printed. 

See https://docs.streamlit.io/en/stable/api.html#magic-commands""")
with __st.echo(), streambook.st_stdout('info'):
    x
__st.markdown("""Dictionaries are pretty-printed using streamlit and can be collapsed""")
with __st.echo(), streambook.st_stdout('info'):
    data = [dict(key1 = i, key2=f"{i}", key3=100 -i) for i in range(100)]
__st.markdown("""Pandas dataframe also show up in tables. """)
with __st.echo(), streambook.st_stdout('info'):
    df = pd.DataFrame(data)
    df
with __st.echo(), streambook.st_stdout('info'):
    fig, axs = plt.subplots(figsize=(12, 4))
    df.plot(ax=axs)
    fig
with __st.echo(), streambook.st_stdout('info'):
    x = "hello"
    # Printing
    print("Printing", x)
    "Output", x
__st.markdown("""## Advanced Features""")
__st.markdown("""By default, the notebook is rerun on save to ensure
consistency.""")
with __st.echo(), streambook.st_stdout('info'):
    def simple_function(x):
        return x + 10
    y = simple_function(10)
    y
__st.markdown("""Slower functions such as functions are loading data
can be cached during development.""")
with __st.echo(), streambook.st_stdout('info'):
    @__st.cache()
    def slow_function():
        for i in range(10):
            time.sleep(0.1)
        return None
    slow_function()
__st.markdown("""This uses streamlit caching behind the scenes. It will
run if the arguments or the body of the function change.""")
__st.markdown("""See https://docs.streamlit.io/en/stable/caching.html""")
__st.markdown("""## Longer example""")
with __st.echo(), streambook.st_stdout('info'):
    def lorenz(x, y, z, s=10, r=28, b=2.667):
        """
        Given:
           x, y, z: a point of interest in three dimensional space
           s, r, b: parameters defining the lorenz attractor
        Returns:
           x_dot, y_dot, z_dot: values of the lorenz attractor's partial
               derivatives at the point x, y, z
        """
        x_dot = s*(y - x)
        y_dot = r*x - y - x*z
        z_dot = x*y - b*z
        return x_dot, y_dot, z_dot
with __st.echo(), streambook.st_stdout('info'):
    dt = 0.01
    num_steps = 20000
with __st.echo(), streambook.st_stdout('info'):
    def calc_curve(dt, num_steps):
        # Need one more for the initial values
        xs = np.empty(num_steps + 1)
        ys = np.empty(num_steps + 1)
        zs = np.empty(num_steps + 1)

        # Set initial values
        xs[0], ys[0], zs[0] = (0., 1., 1.05)

        # Step through "time", calculating the partial derivatives at the
        # current point and using them to estimate the next point
        for i in range(num_steps):
            x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
            xs[i + 1] = xs[i] + (x_dot * dt)
            ys[i + 1] = ys[i] + (y_dot * dt)
            zs[i + 1] = zs[i] + (z_dot * dt)
        return xs, ys, zs
    xs, ys, zs = calc_curve(dt, num_steps)
with __st.echo(), streambook.st_stdout('info'):
    # Plot file
    fig = plt.figure(figsize=(12, 4))
    ax = fig.add_subplot(projection='3d')
    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    fig
__st.markdown("""## Exporting to Jupyter""")
__st.markdown("""The whole notebook can also be exported as a
Jupyter notebook.""")
__st.markdown("""The command is:

`jupytext --to notebook --execute example.notebook.py`""")
__st.markdown("""Some commands are slightly different in streamlit that jupyter.
You can include both and all `__st` lines will be stripped out.""")
with __st.echo(), streambook.st_stdout('info'):
    # Jupyter command
    from IPython.display import HTML
    HTML('<img src="example.gif">')
    # Streamlit command
    __st.image("example.gif")
__toc.title('Streambook example')
__toc.header('Main Code')
__toc.header('Advanced Features')
__toc.header('Longer example')
__toc.header('Exporting to Jupyter')

__toc.generate()
