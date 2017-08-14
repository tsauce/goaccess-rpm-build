Name:		goaccess
Version:	1.2
Release:	1
Summary:	Apache Log Analyzer	

Group:		Applications/Utilities

License:        GPLv2
URL:            http://goaccess.io 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source:  	https://github.com/tsauce/goaccess-rpm-build/blob/master/goaccess-%{version}.tar.gz

BuildRequires:	glib2-devel
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	geoip-devel
BuildRequires:	tokyocabinet-devel

%description
An open source real-time web log analyzer and interactive viewer that runs in a terminal in *nix systems. It provides fast and valuable HTTP statistics for system administrators that require a visual server report on the fly.

%prep
%setup -q

%build
%configure --enable-geoip
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc COPYING README AUTHORS TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_sysconfdir}/%{name}.conf
%{_datadir}/doc/%{name}/*

%changelog
* Mon Aug 14 2017 tsauce@gmail.com - added new build that includes HTTP 429 code - 1.2-1
* Mon Apr 24 2017 Chris Collins <collins.christopher@gmail.com> - 1.2
- Initial packaging
