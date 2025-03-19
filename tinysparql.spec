%define url_ver %(echo %{version} | cut -d. -f1,2)

%define build_doc	0

%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1
%define _disable_lto 1
%define _userunitdir /usr/lib/systemd/user/

#gw libtracker-common is in the main package and not provided
%define __noautoreq 'devel\\(libtracker-common\\|devel\\(libtracker-data'

%define api	3.0
%define major	0
%define libname	%mklibname %{name}
%define devname	%mklibname %{name} -d
%define girname	%mklibname %{name}-gir %{api}
#define beta rc

Summary:	Desktop-neutral metadata-based search framework
Name:		tinysparql
Version:	3.9.1
Release:	%{?beta:0.%{beta}.}1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
Url:		https://wiki.gnome.org/Projects/Tracker
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}%{?beta:.%{beta}}.tar.xz
Source1:	30-tracker.conf

BuildRequires:  a2x
BuildRequires:	asciidoc
BuildRequires:  bash-completion
BuildRequires:	dbus-daemon
BuildRequires:	intltool
BuildRequires:	meson
BuildRequires:	gettext-devel
BuildRequires:	icu-devel
BuildRequires:	libstemmer-devel
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.28.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.28.0
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(libcue)
BuildRequires:	pkgconfig(libnm)
BuildRequires:	pkgconfig(libosinfo-1.0)
BuildRequires:	pkgconfig(libpng) >= 1.2
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libxml-2.0) >= 2.6
BuildRequires:	pkgconfig(pango) >= 1.0.0
BuildRequires:	pkgconfig(poppler-glib) >= 0.16.0
BuildRequires:	pkgconfig(sqlite3) >= 3.7.14
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:  python3dist(pygobject)
BuildRequires:	vala
BuildRequires:  systemd
#BuildRequires:  gi-docgen

# Tracker was renamed to tinysparql with 3.8 version. So lets obsolete previous name:
Obsoletes:  tracker < 3.7.9
Provides:   tracker = %{version}-%{release}

%description
Tinysparql is a framework designed to extract information and metadata about your
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.


%package -n %{libname}
Group:		System/Libraries
Summary:	Shared library of Tracker
Conflicts:	%{name}	< 0.12.8-2
Obsoletes:  lib64tracker3.0_0 < 3.7.4

%description -n %{libname}
Tinysparql is a tool designed to extract information and metadata about your
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.

%package -n %{devname}
Group:		Development/C
Summary:	Development library of Tinysparql
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	%{name} < 0.12.8-2
Obsoletes:  lib64tracker-devel < 3.7.4

%description -n %{devname}
Tinysparql is a tool designed to extract information and metadata about your
personal data so that it can be searched easily and quickly. Tinysparql is
desktop-neutral, fast and resource efficient.

%package -n %{girname}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Obsoletes:  	lib64tracker-gir3.0 < 3.7.4

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package vala
Summary:	Vala bindings for %{name}
Group:		Development/Other
BuildArch:	noarch
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
Obsoletes:  tracker-vala < 3.7.4

%description vala
This package contains vala bindings for development %{name}.

%if %{build_doc}
%package docs
Summary:	Documentations for tracker
Group:		Development/Other
BuildArch:	noarch
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:	graphviz
Conflicts:	%{name} < 0.10.17
Obsoletes:  tracker-docs < 3.7.4

%description docs
This package contains the documentation for tinysparql.
%endif

%prep
%autosetup -p1 -n %{name}-%{version}%{?beta:.%{beta}}

%build
export LC_ALL=UTF-8 CPATH+=":/usr/include/libstemmer/"
%meson \
  -Ddocs=false \
  -Dunicode_support=icu
%meson_build

%install
%meson_install

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/sysctl.d/30-%{name}.conf

%find_lang %{name}3

rm -rf %{buildroot}%{_datadir}/tracker-tests

%files -f %{name}3.lang
%doc README.md NEWS AUTHORS
%{_bindir}/tinysparql
%{_prefix}/lib/sysctl.d/30-tinysparql.conf
%{_userunitdir}/tinysparql-xdg-portal-3.service
%{_libexecdir}/tinysparql-sql
%{_libexecdir}/tinysparql-xdg-portal-3
%{_datadir}/bash-completion/completions/tinysparql
%{_datadir}/dbus-1/services/org.freedesktop.portal.Tracker.service
%{_mandir}/man1/tinysparql*
%{_libdir}/tinysparql-3.0/libtracker-http-soup3.so
%{_libdir}/tinysparql-3.0/libtracker-parser-libicu.so

%files vala
%{_datadir}/vala/vapi/tinysparql-3.0.deps
%{_datadir}/vala/vapi/tinysparql-3.0.vapi
%{_datadir}/vala/vapi/tracker-sparql-3.0.deps
%{_datadir}/vala/vapi/tracker-sparql-3.0.vapi

%files -n %{libname}
%{_libdir}/libtinysparql-3.0.so.%{major}*
%{_libdir}/libtracker-sparql-3.0.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Tracker-3.0.typelib
%{_libdir}/girepository-1.0/Tsparql-3.0.typelib

%files -n %{devname}
%{_libdir}/libtinysparql-3.0.so
%{_libdir}/libtracker-sparql-3.0.so
%{_libdir}/pkgconfig/tinysparql-3.0.pc
%{_libdir}/pkgconfig/tracker-sparql-3.0.pc
%{_datadir}/gir-1.0/Tracker-3.0.gir
%{_datadir}/gir-1.0/Tsparql-3.0.gir
%{_includedir}/tinysparql-3.0/

%if %{build_doc}
%files docs
%{_datadir}/doc/Tsparql-3.0/
%endif
