Name:		xcb-modules
Version:	0.0.1
Release:	3%{?dist}
Summary:	Modules for XCUBE
Group:		Applications/Internet
License:	GPLv2
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	gcc
BuildRequires:	gperftools-devel
BuildRequires:	xcb-devel
Requires:	gperftools-libs
Requires:	xcb

%description
Modules for XCUBE.

%prep
%setup -q

%build
%configure --disable-static CFLAGS="-march=corei7 -g -O2 -pipe -funroll-loops"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_libdir}/*.la
mkdir -p %{buildroot}%{_sharedstatedir}/xcb/
mv -f %{buildroot}%{_libdir}/app_*.so %{buildroot}%{_sharedstatedir}/xcb/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%config(noreplace) %{_sysconfdir}/xcb/*
%{_sharedstatedir}/xcb/*

%changelog

