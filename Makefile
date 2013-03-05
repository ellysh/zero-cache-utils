INSTALL_BIN_DIR = usr/bin
UTILS = zc-list zc-set

install:
	mkdir -p $(DESTDIR)/$(INSTALL_BIN_DIR)
	cp $(UTILS) $(DESTDIR)/$(INSTALL_BIN_DIR)

deb:
	mkdir -p deb
	rm -fR deb/*
	dpkg-buildpackage -rfakeroot -b -us -uc
	mv -f ../*.changes ../*.deb deb
