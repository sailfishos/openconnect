%define keepstatic 1 # FIXME remove
%define libname libopenconnect5

Name:       openconnect
Summary:    Open client for Cisco AnyConnect VPN
Version:    9.12
Release:    0
License:    LGPL-2.1-or-later
URL:        https://github.ocm/sailfishos/openconnect
Source0:    openconnect-%{version}.tar.gz
Patch0:     0001-Make-scripts-more-compatible-with-other-shells.patch
Requires:   vpnc
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-lxml
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libproxy-1.0)
#FIXME check wich other dependencies should be added
# BuildRequires:  pkgconfig(krb5)
# BuildRequires:  pkgconfig(libpcsclite)
# BuildRequires:  pkgconfig(libpskc)
# BuildRequires:  pkgconfig(socket_wrapper)
# BuildRequires:  pkgconfig(stoken)
# BuildRequires:  pkgconfig(uid_wrapper)
BuildRequires:  gettext

%description
This package provides a multi-protocol client for a number of SSL
VPNs, such as:

* Cisco's "AnyConnect" VPN (HTTPS/DTLS) supported by the ASA5500 Series,
  by IOS 12.4(9)T or later on Cisco SR500, 870, 880, 1800, 2800, 3800,
  7200 Series and Cisco 7301 Routers, and probably others.
* Array Networks AG SSL VPN
* Juniper SSL VPN
* Pulse Connect Secure
* Palo Alto Networks GlobalProtect SSL VPN
* F5 Big-IP SSL VPN
* Fortinet Fortigate SSL VPN

%package -n %{libname}
Summary:        Libraries for %{name}

%description -n %{libname}
This package provides a multi-protocol client for a number of SSL
VPNs, including Cisco's "AnyConnect" VPN.

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


%lang_package

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
./autogen.sh
%configure --docdir=%{_docdir}/%{name} \
           --disable-silent-rules \
           --with-vpnc-script=%{_sysconfdir}/openconnect/vpnc-script \
           --without-gnutls \
           --with-openssl --without-openssl-version-check \
           --without-gnutls-version-check \
           --with-lz4 \
           --with-libproxy \
           # --with-stoken \ FIXME
           # --with-libpcsclite \
           # --with-libpskc \
           # --with-gssapi \
           %{nil}
%make_build

%install
%make_install
# do not install androit script
rm %{buildroot}%{_libexecdir}/%{name}/*android.sh

rm -rf %{buildroot}%{_datadir}/openconnect
rm -rf %{buildroot}%{_datadir}/bash-completion

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

#%check
#%make_build check

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%license COPYING.LGPL
%{_sbindir}/openconnect
%{_libexecdir}/%{name}/*.{py,sh}


%files -n %{libname}
%license COPYING.LGPL
%{_libdir}/libopenconnect.so.*
%files devel
%{_libdir}/libopenconnect.so
%{_includedir}/openconnect.h
%{_libdir}/pkgconfig/openconnect.pc

%files doc
%{_mandir}/man8/%{name}.*

%files locale -f %{name}.lang
