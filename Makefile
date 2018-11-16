PYTHON = python

.PHONY: atlas theming apk run install
atlas:

run: atlas
	$ (PYTHON) -m main.py
build:
    $ (PYTHON) -m main.py
apk:
	buildozer android debug
apk_release:
	buildozer android release
