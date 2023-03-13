.PHONY: build out clean

build:
	python build.py

clean:
	python clean.py

out:
	python build.py
	python clean.py