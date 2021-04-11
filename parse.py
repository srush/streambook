import jupytext
import textwrap
import os


#!/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import in_place

abs_path = None
        
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global abs_path

        with in_place.InPlace('tmp.py') as out:
            print(abs_path)
            os.system(f"jupytext --to ipynb  {abs_path}")
            print("import streamlit as st", file=out)
            print("import lib", file=out)
            print("toc = lib.TOC()", file=out)
            for i, cell in enumerate(jupytext.read(abs_path)["cells"]):
                if cell["cell_type"] == "markdown":
                    print('st.markdown("""%s""")'%cell["source"], file=out)
                else:
                    wrapper = textwrap.TextWrapper(initial_indent='\t',
                                                   subsequent_indent='\t',
                                                   width=5000)
                    if not cell["source"].strip():
                        continue
                    print("with st.echo():", file=out)
                    for l in cell["source"].splitlines():
                        print(wrapper.fill(l), file=out)
            print("toc.generate()", file=out)
                        
if __name__ == "__main__":
    import argparse, os
    parser = argparse.ArgumentParser(description='Stream book options.')
    parser.add_argument('file', 
                        help='file to run', type=os.path.abspath)

    args = parser.parse_args()
    abs_path = args.file
    event_handler = MyHandler()
    observer = Observer()
    print(abs_path)
    
    event_handler.on_modified(None)
    observer.schedule(event_handler, path=abs_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

