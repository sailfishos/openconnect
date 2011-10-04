Name:		openconnect
Version:	3.02
Release:	1
Summary:	Open client for Cisco AnyConnect VPN

Group:		Applications/Internet
License:	LGPLv2+
URL:		http://www.infradead.org/openconnect.html
Source0:	ftp://ftp.infradead.org/pub/openconnect/openconnect-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	openssl-devel libxml2-devel
BuildRequires:	libproxy-devel
Requires:	vpnc

%description
This package provides a client for Cisco's "AnyConnect" VPN, which uses
HTTPS and DTLS protocols.

%package devel
Provides: openconnect-devel-static = %{version}-%{release}
Summary: Development package for OpenConnect VPN authentication tools
Group: Applications/Internet

%description devel
This package provides the core HTTP and authentication support from
the OpenConnect VPN client, to be used by GUI authentication dialogs
for NetworkManager etc.

%prep
%setup -q

%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
make install-lib LIBDIR=%{_libdir} DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
install -m0644 openconnect.8 $RPM_BUILD_ROOT/%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/openconnect
%{_mandir}/man8/*
%doc TODO COPYING.LGPL openconnect.html

%files devel
%defattr(-,root,root,-)
%{_libdir}/libopenconnect.a
/usr/include/openconnect.h
%{_libdir}/pkgconfig/openconnect.pc
