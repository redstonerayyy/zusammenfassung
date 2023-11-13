import os
import pathlib

blacklisted = [
    ".aux",
    ".fls",
    ".log",
    ".pdf",
    ".gz",
    ".fdb_latexmk",
    ".dvi",
    ".xdv",
]


def clean(dir = "."):
    for root, dirs, files in os.walk(dir, topdown=True):
        if root == "./out":
            continue
        for file in files:
            if pathlib.Path(file).suffix in blacklisted:
                os.remove(os.path.join(root, file))


if __name__ == "__main__":
    clean()
