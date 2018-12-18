%define keepstatic 1

Name:       openconnect
Summary:    Open client for Cisco AnyConnect VPN
Version:    7.08
Release:    1
Group:      Applications/Internet
License:    LGPLv2+
URL:        http://www.infradead.org/openconnect.html
Source0:    ftp://ftp.infradead.org/pub/openconnect/openconnect-%{version}.tar.gz
Requires:   vpnc
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  libproxy-devel
BuildRequires:  gettext

%description
This package provides a client for Cisco's "AnyConnect" VPN, which uses
HTTPS and DTLS protocols.

%package devel
Summary:    Development package for OpenConnect VPN authentication tools
Group:      Applications/Internet
Requires:   %{name} = %{version}-%{release}
Provides:   openconnect-devel-static = %{version}-%{release}

%description devel
This package provides the core HTTP and authentication support from
the OpenConnect VPN client, to be used by GUI authentication dialogs
for NetworkManager etc.

%package docs
Summary:    Documentation package for OpenConnect VPN authentication tools
Group:      Applications/Internet
Requires:   %{name} = %{version}-%{release}

%description docs
This package provides documentation for openconnect, such as man pages.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
./autogen.sh
%configure --with-vpnc-script=/etc/vpnc/vpnc-script
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}%{_datadir}/openconnect

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_libdir}/libopenconnect.so.*
%{_sbindir}/openconnect
%doc COPYING.LGPL

%files devel
%defattr(-,root,root,-)
%{_libdir}/libopenconnect.so
%{_includedir}/openconnect.h
%{_libdir}/pkgconfig/openconnect.pc

%files docs
%defattr(-,root,root,-)
%{_mandir}/man8/*

