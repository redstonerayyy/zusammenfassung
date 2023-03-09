import subprocess
import os
import pathlib


def build():
    for root, dirs, files in os.walk(".", topdown=True):
        for file in files:
            if pathlib.Path(file).suffix == ".tex":
                subprocess.run(["latexmk", "-xelatex", os.path.join(root, file)])


if __name__ == "__main__":
    build()
