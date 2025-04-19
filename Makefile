.PHONY: all install build prepare_www prepare_server package clean

FRONTEND_DIR=frontend
DIST_DIR=$(FRONTEND_DIR)/dist
SERVER_DIR=server

VERSION := $(shell git describe --tags --abbrev=0)
PACKAGE_DIR := patlite-tower-lights-controller_$(VERSION)
ARCHIVE_NAME := $(PACKAGE_DIR).tar.gz

all: package

install:
	cd $(FRONTEND_DIR) && yarn install

build: install
	cd $(FRONTEND_DIR) && yarn build

prepare_www: build
	mkdir -p $(PACKAGE_DIR)/www
	cp -r $(DIST_DIR)/* $(PACKAGE_DIR)/www/

prepare_server:
	cp -r $(SERVER_DIR)/requirements.txt $(PACKAGE_DIR)/
	cp -r $(SERVER_DIR)/requirements-rpi.txt $(PACKAGE_DIR)/
	cp -r $(SERVER_DIR)/*.py $(PACKAGE_DIR)/

package: clean prepare_www prepare_server
	tar -czf $(ARCHIVE_NAME) $(PACKAGE_DIR)
	rm -rf $(PACKAGE_DIR)
	@echo "Created archive: $(ARCHIVE_NAME)"

clean:
	rm -rf *.tar.gz patlite-tower-lights-controller_*
