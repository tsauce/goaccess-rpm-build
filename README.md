# goaccess
goaccess repo for rpm builds

GoAccess (http://goaccess.io/) is a great real-time web log analyzer with an interface that makes it easy to visualize web traffic from within your terminal.

Building

Note: This spec file is complete and works, but the build script and documentation in this repository is still being worked on.

    git clone https://github.com/tsauce/goaccess-rpm-build.git
    yum groupinstall -y "Development Tools" && yum install rpm-build rpmdevtools automake glib2-devel ncurses-devel geoip-devel tokyocabinet-devel
    ./build.sh goaccess
    yum install ~/rpmbuild/RPMS/*/*.rpm
    DONE.
