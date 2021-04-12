# Streambook

<img src="output.gif">

Python notebooks without compomises. 

* Write your code in any editor (emacs, vi, vscode)
* Exports to standard Jupyter format. 
* Use standard tools (git, black, lint, pytest)

## Quick start

Install:

```bash
git clone https://github.com/srush/streambook; cd streambook```
pip install -r requirements.txt; pip install .
```


Run:

```bash
python -m streambook example.py & 
streamlit run  --server.runOnSave true example.streambook.py
```

Edit your file. When you are done and ready to export to a notebook run.

```bash
jupytext --to notebook --execute example2.notebook.py
```

See the (notebook)[example.notebook.ipynb] for a demo.


## How does this work 
Major Gotcha -
Streambook is a simple script that hooks together Streamlit + Jupytext + Watchdog to make this work.

* [Streamlit](https://docs.streamlit.io/) - Live updating webview with an advanced caching system
* [Jupytext](jupytext.readthedocs.io) - Bidirectional bridge between plaintext and jupyter format
* Watchdog - file watching in python


## Caching

A benefit of using notebooks is being able to keep data in memory. 
Streambook instead reruns your notebook whenever the file is changed. 
In order for this not to be slow, the user needs to do their own caching. 

Streambook relies 

