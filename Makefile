.PHONY: build upload

EBEDKE_JSON=ebedke.json
BUILD_DIR=build

build: $(BUILD_DIR)/index.html $(BUILD_DIR)/res/bootstrap.min.css

$(BUILD_DIR)/index.html: $(EBEDKE_JSON) template/index.html.j2 ebedke_static/main.py
	poetry run generator $(EBEDKE_JSON)

$(BUILD_DIR)/res/bootstrap.min.css: resources/bootstrap.min.css
	cp resources/bootstrap.min.css $(BUILD_DIR)/res/bootstrap.min.css

upload: build
	echo 'TODO'