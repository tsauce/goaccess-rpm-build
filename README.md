# goaccess
goaccess repo for rpm builds

GoAccess (http://goaccess.io/) is a great real-time web log analyzer with an interface that makes it easy to visualize web traffic from within your terminal.

Building

    git clone https://github.com/tsauce/goaccess-rpm-build.git
    yum groupinstall -y "Development Tools" && yum install rpm-build rpmdevtools automake glib2-devel ncurses-devel geoip-devel tokyocabinet-devel
    ./build.sh goaccess
    yum install ~/rpmbuild/RPMS/*/*.rpm
    DONE.
Note: this is based off of GitHub - clcollins/goaccess-rpm 
Use as needed and change whatever you need.
