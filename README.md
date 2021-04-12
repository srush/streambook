# Streambook

Python notebooks without compomises. 

<img src="output.gif">

* Write your code in any editor (emacs, vi, vscode)
* Use standard tools (git, black, lint, pytest)
* Export to standard Jupyter format for collaboration

## Quick start

Install:

```bash
git clone https://github.com/srush/streambook; cd streambook
pip install -r requirements.txt; pip install .
```

Run:

```bash
python -m streambook example.py & 
streamlit run  --server.runOnSave true example.streambook.py
```

Edit your file. When you are done and ready to export to a notebook run.

```bash
jupytext --to notebook --execute example.notebook.py
```

See the [notebook](example.notebook.ipynb) for a demo.


## How does this work 

Streambook is a simple script that hooks together Streamlit + Jupytext + Watchdog.

* [Streamlit](https://docs.streamlit.io/) - Live updating webview with an advanced caching system
* [Jupytext](jupytext.readthedocs.io) - Bidirectional bridge between plaintext and jupyter format
* Watchdog - file watching in python


## Caching

![image](https://user-images.githubusercontent.com/35882/114342503-f0273d80-9b29-11eb-96d2-3fdd7938a04c.png)


A "benefit" of using notebooks is being able to keep data cached in memory, 
at the cost of often forgetting how it was created and in what order. 

Streambook instead reruns your notebook from the top whenever the file is changed. 
This can be very slow, particularly for users used to standard notebooks.

In order to circumvent this issue, the user needs to write functions and add caching. 
Luckily Streamlit's caching API to makes it pretty easy in most use case. See 
https://docs.streamlit.io/en/stable/caching.html for docs. 

An example is given in the [notebook](example.notebook.py).
