import subprocess, os, pathlib, shutil
from clean import clean

filelist = [
    "./physik/induktion.tex"
]

def build():
    root = os.path.abspath(".")
    os.makedirs("./out", exist_ok=True)

    for filepath in filelist:
        directory = os.path.join(root, pathlib.Path(filepath).parent)
        filename = pathlib.Path(filepath).name
        pdfname = pathlib.Path(filename).with_suffix(".pdf")

        os.chdir(directory)
        subprocess.run(["latexmk", "-xelatex", filename], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        shutil.copy(pdfname, os.path.join(root, "./out", pdfname))


if __name__ == "__main__":
    build()
    clean()
