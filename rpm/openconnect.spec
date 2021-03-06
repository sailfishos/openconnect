%define keepstatic 1
%define __requires_exclude /system/bin/sh

Name:       openconnect
Summary:    Open client for Cisco AnyConnect VPN
Version:    8.10
Release:    1
License:    LGPLv2+
URL:        https://git.sailfishos.org/mer-core/openconnect/
Source0:    ftp://ftp.infradead.org/pub/openconnect/openconnect-%{version}.tar.gz
Patch0:     Make-scripts-more-compatible-with-other-shells.patch
Patch1:     0001-setup-default-port-443-in-openconnect_vpninfo_new.patch
Patch2:     0002-remove-port-setup-in-ssl-connect.patch
Patch3:     0003-check-that-port-is-in-valid-range.patch
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
Requires:   %{name} = %{version}-%{release}
Provides:   openconnect-devel-static = %{version}-%{release}

%description devel
This package provides the core HTTP and authentication support from
the OpenConnect VPN client, to be used by GUI authentication dialogs
for NetworkManager etc.

%package doc
Summary:    Documentation for %{name}
Requires:   %{name} = %{version}-%{release}

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
rm -rf %{buildroot}%{_datadir}/bash-completion

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
# Do not pull in Python3
%exclude %{_libexecdir}/openconnect/tncc-emulate.py
%exclude %{_libexecdir}/openconnect/tncc-wrapper.py
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
