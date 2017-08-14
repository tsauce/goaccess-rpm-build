#!/bin/sh

whatami="$1"
whereami="$(dirname $0)"

/usr/bin/rpmdev-setuptree

cp -f ${whereami}/${whatami}.spec ~/rpmbuild/SPECS/
/usr/bin/spectool -C ~/rpmbuild/SOURCES/ -g ${whereami}/${whatami}.spec 

rpmbuild -bb ~/rpmbuild/SPECS/${whatami}.spec 
