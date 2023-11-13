.PHONY: build clean

build:
	python ./scripts/build.py

clean:
	rm -rf scripts/__pycache__
	python ./scripts/clean.py
