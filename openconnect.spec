# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros
%define keepstatic 1

Name:       openconnect
Summary:    Open client for Cisco AnyConnect VPN
Version:    3.15
Release:    1
Group:      Applications/Internet
License:    LGPLv2+
URL:        http://www.infradead.org/openconnect.html
Source0:    ftp://ftp.infradead.org/pub/openconnect/openconnect-%{version}.tar.gz
Source100:  openconnect.yaml
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
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
autoreconf -f -i
# << build pre

%configure 
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post
%find_lang %{name}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig








%files -f %{name}.lang
%defattr(-,root,root,-)
# >> files
%{_libdir}/libopenconnect.so.*
%{_sbindir}/openconnect
%doc COPYING.LGPL
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%doc TODO openconnect.html
%{_libdir}/libopenconnect.so
%{_libdir}/libopenconnect.a
%{_includedir}/openconnect.h
%{_libdir}/pkgconfig/openconnect.pc
# << files devel

%files docs
%defattr(-,root,root,-)
# >> files docs
%{_mandir}/man8/*
# << files docs
