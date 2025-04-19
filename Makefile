.PHONY: all install build package clean

FRONTEND_DIR=frontend
DIST_DIR=$(FRONTEND_DIR)/dist
ARCHIVE_NAME=package.tar.gz
TEMP_DIR=dist_package
SERVER_DIR=server

# Get the latest Git tag (e.g., v0.1)
VERSION := $(shell git describe --tags --abbrev=0)
ARCHIVE_NAME=patlite-tower-lights-controller_$(VERSION).tar.gz

all: package

install:
	cd $(FRONTEND_DIR) && yarn install

build: install
	cd $(FRONTEND_DIR) && yarn build

prepare_www: build
	mkdir -p $(TEMP_DIR)/www
	cp -r $(DIST_DIR)/* $(TEMP_DIR)/www/

prepare_server:
	cp -r $(SERVER_DIR)/*.py $(TEMP_DIR)
	cp $(SERVER_DIR)/requirements.txt $(TEMP_DIR)

package: clean prepare_www prepare_server
	tar -czf $(ARCHIVE_NAME) -C $(TEMP_DIR) .
	rm -rf $(TEMP_DIR)

clean:
	rm -rf $(ARCHIVE_NAME) $(TEMP_DIR)
