import subprocess
import time
from pathlib import Path
import os

import in_place
import typer
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from streambook.gen import Generator

app = typer.Typer()


class MyHandler(FileSystemEventHandler):
    def __init__(
        self,
        abs_path: str,
        stream_file: str,
        notebook_file: str,
        jupytext_command: str,
        generator: Generator,
        quiet: bool,
    ):
        self.abs_path = abs_path
        self.stream_file = stream_file
        self.notebook_file = notebook_file
        self.jupytext_command = jupytext_command
        self.generator = generator
        self.quiet = quiet
        super().__init__()

    def on_modified(self, event):
        if event is None or event.src_path == self.abs_path:
            if not self.quiet:
                print(f"Regenerating from {self.abs_path}...")
            with in_place.InPlace(self.stream_file) as out:
                self.generator.generate(self.abs_path, out)
            with open(self.notebook_file, "w") as out:
                for line in open(self.abs_path, "r"):
                    if "__st" not in line:
                        out.write(line)
            if self.jupytext_command is not None:
                os.system(self.jupytext_command)


def file_paths(file: Path):
    abs_path = file.resolve()
    directory = str(abs_path.parent)
    abs_path = str(abs_path)

    ipynb_file = abs_path[:-3] + ".ipynb"
    stream_file = abs_path[:-3] + ".streambook.py"
    notebook_file = abs_path[:-3] + ".notebook.py"
    return abs_path, directory, stream_file, notebook_file, ipynb_file


def main(
    file: Path,
    watch: bool,
    streamlit: bool,
    quiet: bool,
    jupyter: bool = False,
    port: int = None,
    sections: str = None,
):
    abs_path, directory, stream_file, notebook_file, ipynb_file = file_paths(file)
    jupytext_command = (
        f"jupytext --to notebook --execute {notebook_file} -o {ipynb_file}"
    )
    event_handler = MyHandler(
        abs_path=abs_path,
        stream_file=stream_file,
        notebook_file=notebook_file,
        jupytext_command=jupytext_command if jupyter else None,
        generator=Generator(sections),
        quiet=quiet,
    )
    observer = Observer()
    open(stream_file, "w").close()

    view_command = ["streamlit", "run", "--server.runOnSave", "true"]
    if port is not None:
        view_command += ["--server.port", str(port)]
    view_command += [stream_file]

    if not quiet:
        if watch:
            print("Streambook Daemon\n")
            print("Watching directory for changes:")
            print(f"\n {directory}")
            print()

            print("View Command")
            print(" ".join(view_command))
            print()
        if jupyter:
            print("Jupyter Daemon\n")
            print(jupytext_command)

    event_handler.on_modified(None)

    if watch:
        observer.schedule(event_handler, path=directory, recursive=False)
        observer.start()

        if streamlit:
            print()
            print("Starting Streamlit")
            subprocess.run(
                view_command, capture_output=True,
            )

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()


@app.command()
def convert(file: Path = typer.Argument(..., help="file to convert")):
    abs_path, directory, stream_file, notebook_file, ipynb_file = file_paths(file)
    command = f"jupytext --to notebook --execute {notebook_file} -o {ipynb_file} "
    os.system(command)


@app.command()
def run(
    file: Path = typer.Argument(..., help="file to run"),
    streamlit: bool = typer.Option(True, help="Lauches streamlit"),
    jupyter: bool = typer.Option(False, help="Compiles ipynb file"),
    quiet: bool = typer.Option(False, help="Don't print anything"),
    port: int = typer.Option(None, help="Port to launch streamlit on."),
    sections: str = typer.Option(None, help="Regex to filter sections."),
):
    """
    Starts the watcher and streamlit services.
    """
    main(
        file,
        watch=True,
        streamlit=streamlit,
        jupyter=jupyter,
        quiet=quiet,
        port=port,
        sections=sections,
    )


@app.command()
def export(
    file: Path = typer.Argument(..., help="file to run"),
    quiet: bool = typer.Option(False, help="Don't print anything"),
):
    """
    Only creates the '*.streambook.py' file.
    """
    main(file, watch=False, streamlit=False, quiet=quiet)


if __name__ == "__main__":
    app()
