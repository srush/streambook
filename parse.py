import jupytext
import textwrap
import os


#!/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with open("tmp.py", "w") as out:
            os.system("jupytext --to ipynb run.py")
            print("import streamlit as st", file=out)
            for i, cell in enumerate(jupytext.read("run.py")["cells"]):
                if cell["cell_type"] == "markdown":
                    print('st.markdown("""%s""")'%cell["source"], file=out)
                else:
                    wrapper = textwrap.TextWrapper(initial_indent='\t', subsequent_indent='\t')
                    if not cell["source"].strip():
                        continue
                    print("with st.echo():", file=out)
                    for l in cell["source"].splitlines():
                        print(wrapper.fill(l), file=out)

if __name__ == "__main__":


    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='/home/srush/Projects/streambook/run.py', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

