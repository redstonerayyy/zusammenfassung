import subprocess
import os
import pathlib
import shutil

def build():
    invokedir = os.path.abspath(".")
    for root, dirs, files in os.walk(invokedir, topdown=True):
        for file in files:
            if pathlib.Path(file).suffix == ".tex":
                os.chdir(root)
                print(os.path.join(root, file))
                try:
                    subprocess.run(["latexmk", "-xelatex", os.path.join(root, file)], stdout=subprocess.DEVNULL, timeout=5)
                    outname = pathlib.Path(file).name.split(".")[0] + ".pdf"
                    shutil.copy(os.path.join(root, pathlib.Path(file).name), os.path.join(invokedir, "out", outname))
                except:
                    print("File build timed out!")


if __name__ == "__main__":
    build()
