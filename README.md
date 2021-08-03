# Streambook

Python notebooks without compromises. 

<img src="https://github.com/srush/streambook/blob/main/output.gif">

* Write your code in any editor (emacs, vi, vscode)
* Use standard tools (git, black, lint, pytest)
* Export to standard Jupyter format for collaboration

## Quick start

Install:

```bash
pip install streambook
```

Run streambook on a Python file. For the example notebook included:

```bash
pip install matplotlib
streambook run example.py
```

The output should look like this [streambook](https://share.streamlit.io/srush/streambook-example/main/example.streambook.py).

Editing your file `example.py` should automatically update the viewer.

When you are done and ready to export to a notebook run:

```bash
streambook convert example.py
```

This produces a standard [notebook](https://nbviewer.jupyter.org/github/srush/streambook/blob/main/example.notebook.ipynb).


## How does this work?

Streambook is a simple library (< 50 lines!) that hooks together Streamlit + Jupytext + Watchdog.

* [Streamlit](https://docs.streamlit.io/) - Live updating webview with an advanced caching system
* [Jupytext](https://jupytext.readthedocs.io/) - Bidirectional bridge between plaintext and jupyter format
* [Watchdog](https://github.com/gorakhargosh/watchdog) - File watching in python


## Is this fast enough?

![image](https://user-images.githubusercontent.com/35882/114342503-f0273d80-9b29-11eb-96d2-3fdd7938a04c.png)


A "benefit" of using notebooks is being able to keep data cached in memory, 
at the cost of often forgetting how it was created and in what order. 

Streambook instead reruns your notebook from the top whenever the file is changed. 
Typically this is pretty fast for writing demos or quick notebooks.


However this can be very slow for long running ML applications, particularly for users used to standard notebooks.
In order to circumvent this issue there are two tricks.

1) You can divide your notebook us into sections. This allows you to edit individual parts of the notebook.

```
streambook run --section "Main" example.py
```

2) You can write functions and add caching.

Streamlit's caching API to makes it pretty easy in most use case. See 
https://docs.streamlit.io/en/stable/caching.html for docs. 

An example is given in the [notebook](https://nbviewer.jupyter.org/github/srush/streambook/blob/main/example.notebook.ipynb).
