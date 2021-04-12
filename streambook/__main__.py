import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import in_place
from .gen import Generator

abs_path = None
stream_file = None
notebook_file = None
generator = Generator()


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event is None or event.src_path == abs_path:
            print(f"Regenerating from {abs_path}...")
            with in_place.InPlace(stream_file) as out:
                generator.generate(abs_path, out)
            with open(notebook_file, "w") as out:
                for l in open(abs_path, "r"):
                    if "__st" not in l:
                        out.write(l)

if __name__ == "__main__":
    import argparse, os

    parser = argparse.ArgumentParser(description="Stream book options.")
    parser.add_argument("file", help="file to run", type=os.path.abspath)

    args = parser.parse_args()
    abs_path = args.file
    directory = os.path.dirname(abs_path)
    event_handler = MyHandler()
    observer = Observer()

    stream_file = abs_path[:-3] + ".streambook.py"
    notebook_file = abs_path[:-3] + ".notebook.py"

    open(stream_file, "w").close()
    print("Streambook Daemon\n")
    
    print("Watching directory for changes:")
    print(f"\n {directory}")
    print()
    print("View Command")
    print(f"streamlit run  --server.runOnSave true {stream_file}")
    print()
    print("Notebook Execution Command")
    print(f"jupytext --to notebook --execute {notebook_file}")
    event_handler.on_modified(None)
    observer.schedule(event_handler, path=directory, recursive=False)
    observer.start()


    print()
    print("Starting Streamlit")
    import sys
    from streamlit import cli as stcli
    sys.argv = ["streamlit", "run", "--server.runOnSave", "true", stream_file]
    stcli.main()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
