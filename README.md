# Streambook

Python notebooks without compomises. 

* Write your code in any editor (emacs, vi, vscode)
* Live updating visual output
* Exports to standard Jupyter format. 
* Use standard Python tools (black, lint, pytest)
* Plays nicely with Git 


## Quick start

Install:

> git clone https://github.com/srush/streambook; cd streambook
> pip install -r requirements.txt; pip install .


Run:

> python -m streambook example.py & 
> streamlit run  --server.runOnSave true example.streambook.py

Edit your file. When you are done and ready to export to a notebook run.

> jupytext --to notebook --execute example2.notebook.py

See the (notebook)[example.notebook.ipynb] for a demo.


## How does this work 

Streambook is a simple script that hooks together Streamlit + Jupytext + Watchdog to make this work.

* [Streamlit](https://docs.streamlit.io/) - Live updating webview with an advanced caching system
* [Jupytext](jupytext.readthedocs.io) - Bidirectional bridge between plaintext and jupyter format
* Watchdog - file watching in python


## Caching
