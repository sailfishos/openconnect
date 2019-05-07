%define keepstatic 1

Name:       openconnect
Summary:    Open client for Cisco AnyConnect VPN
Version:    8.02
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

%package doc
Summary:    Documentation for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}
Obsoletes:  %{name}-docs

%description doc
Man page for %{name}.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
./autogen.sh
%configure --with-vpnc-script=/etc/vpnc/vpnc-script \
           --without-gnutls
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}%{_datadir}/openconnect
rm -f %{buildroot}%{_libexecdir}/openconnect/tncc-wrapper.py

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%license COPYING.LGPL
%{_libdir}/libopenconnect.so.*
%{_sbindir}/openconnect
%{_libexecdir}/openconnect/

%files devel
%defattr(-,root,root,-)
%{_libdir}/libopenconnect.so
%{_includedir}/openconnect.h
%{_libdir}/pkgconfig/openconnect.pc

%files doc
%defattr(-,root,root,-)
%{_mandir}/man8/%{name}.*
%{_docdir}/%{name}-%{version}
