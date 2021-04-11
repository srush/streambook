import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import in_place
from .gen import Generator

abs_path = None
generator = Generator()
        
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global abs_path
        with in_place.InPlace('tmp.py') as out:
            generator.generate(abs_path, out)
                        
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

