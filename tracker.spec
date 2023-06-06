%define url_ver %(echo %{version} | cut -d. -f1,2)

%define build_doc	1

%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1
%define _disable_lto 1
%define _userunitdir /usr/lib/systemd/user/

#gw libtracker-common is in the main package and not provided
%define __noautoreq 'devel\\(libtracker-common\\|devel\\(libtracker-data'

%define api	3.0
%define major	0
%define libname	%mklibname %{name} %{api} %{major}
%define devname	%mklibname %{name} -d
%define girname	%mklibname %{name}-gir %{api}

Summary:	Desktop-neutral metadata-based search framework
Name:		tracker
Version:	3.5.3
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
Url:		https://wiki.gnome.org/Projects/Tracker
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Source1:	30-tracker.conf
#Patch0:		tracker-3.5.2-fix-broken-strftime-check.patch

BuildRequires:  a2x
BuildRequires:	asciidoc
BuildRequires:  bash-completion
BuildRequires:	dbus-daemon
BuildRequires:	intltool
BuildRequires:	meson
#BuildRequires:	mozilla-thunderbird
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	tiff-devel
BuildRequires:	jpeg-devel
BuildRequires:	icu-devel
BuildRequires:	gnome-common
BuildRequires:	libstemmer-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libseccomp)
BuildRequires:	pkgconfig(camel-1.2) >= 2.32.0
BuildRequires:	pkgconfig(exempi-2.0) >= 2.1.0
BuildRequires:	pkgconfig(flac) >= 1.2.1
BuildRequires:	pkgconfig(gdk-pixbuf-2.0) >= 2.12.0
BuildRequires:	pkgconfig(gee-0.8) >= 0.3
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.28.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.28.0
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gstreamer-1.0) >= 0.10.31
BuildRequires:	pkgconfig(gstreamer-pbutils-1.0) >= 0.10.31
BuildRequires:	pkgconfig(gstreamer-tag-1.0) >= 0.10.31
BuildRequires:	pkgconfig(gthread-2.0) >= 2.28.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(libcue)
BuildRequires:	pkgconfig(libexif) >= 0.6
BuildRequires:	pkgconfig(libgsf-1) >= 1.13
BuildRequires:	pkgconfig(libgxps)
BuildRequires:	pkgconfig(libiptcdata)
BuildRequires:	pkgconfig(libmediaart-2.0) >= 0.5.0
BuildRequires:	pkgconfig(libnm)
BuildRequires:	pkgconfig(libosinfo-1.0)
BuildRequires:	pkgconfig(libpng) >= 1.2
BuildRequires:	pkgconfig(libsecret-unstable) >= 0.5
BuildRequires:  pkgconfig(libsoup-3.0)
#BuildRequires:	pkgconfig(libstreamanalyzer) >= 0.7.0
#BuildRequires:	pkgconfig(libxine) >= 1.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.6
BuildRequires:	pkgconfig(pango) >= 1.0.0
BuildRequires:	pkgconfig(poppler-glib) >= 0.16.0
BuildRequires:	pkgconfig(rest-1.0)
BuildRequires:	pkgconfig(sqlite3) >= 3.7.14
BuildRequires:	pkgconfig(taglib_c) >= 1.6
BuildRequires:	pkgconfig(totem-plparser)
BuildRequires:	pkgconfig(upower-glib) >= 0.9.0
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(vorbisfile) >= 0.22
BuildRequires:	pkgconfig(libgrss)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:  python3dist(pygobject)
BuildRequires:	vala
BuildRequires:  systemd

Obsoletes:	tracker-search-tool < 0.10
Obsoletes:	%{name}-common < 0.12.8-2
Obsoletes:	%{name}-preferences < 0.12.8-2
Obsoletes:	%{name}-applet < 0.12.8-2

%description
Tracker is a framework designed to extract information and metadata about your
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.


%package -n %{libname}
Group:		System/Libraries
Summary:	Shared library of Tracker
Conflicts:	%{name}	< 0.12.8-2

%description -n %{libname}
Tracker is a tool designed to extract information and metadata about your
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.

%package -n %{devname}
Group:		Development/C
Summary:	Development library of Tracker
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	%{name} < 0.12.8-2

%description -n %{devname}
Tracker is a tool designed to extract information and metadata about your
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.

%package -n %{girname}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package vala
Summary:	Vala bindings for %{name}
Group:		Development/Other
BuildArch:	noarch
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala

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

%description docs
This package contains the documentation for tracker.
%endif

%prep
%autosetup -p1

%build
export LC_ALL=UTF-8 CPATH+=":/usr/include/libstemmer/"
%meson \
  -Ddocs=true \
  -Dunicode_support=icu
%meson_build

%install
%meson_install

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/sysctl.d/30-%{name}.conf

%find_lang %{name}3

rm -rf %{buildroot}%{_datadir}/tracker-tests

# do not start under KDE
#desktop-file-install \
#	--remove-only-show-in=KDE \
#	--dir=%{buildroot}%{_sysconfdir}/xdg/autostart \
#	#{buildroot}%{_sysconfdir}/xdg/autostart/*.desktop


%files -f %{name}3.lang
%doc README.md NEWS AUTHORS
%{_datadir}/bash-completion/completions/tracker3
%{_bindir}/%{name}3
%{_datadir}/%{name}3/
%{_libexecdir}/tracker-xdg-portal-3
%{_libexecdir}/tracker3/*
%{_prefix}/lib/sysctl.d/30-%{name}.conf
%{_mandir}/man1/tracker-xdg-portal-3.1.*
%{_mandir}/man1/tracker3-*
%{_datadir}/dbus-1/services/org.freedesktop.portal.Tracker.service
%{_libdir}/tracker-3.0/trackertestutils/*
%{_libdir}/tracker-3.0/libtracker-http-soup2.so
%{_libdir}/tracker-3.0/libtracker-http-soup3.so
%{_libdir}/tracker-3.0/libtracker-parser-libicu.so
%{_userunitdir}/tracker-xdg-portal-3.service

%files vala
%{_datadir}/vala/vapi/%{name}-sparql-%{api}.vapi
%{_datadir}/vala/vapi/%{name}-sparql-%{api}.deps

%files -n %{libname}
%{_libdir}/lib%{name}-sparql-%{api}.so.%{major}*
%dir %{_libdir}/%{name}-%{api}/

%files -n %{girname}
%{_libdir}/girepository-1.0/Tracker-%{api}.typelib

%files -n %{devname}
%{_libdir}/lib%{name}-sparql-%{api}.so
%{_includedir}/*
%{_libdir}/pkgconfig/%{name}-sparql-%{api}.pc
%{_datadir}/gir-1.0/Tracker-%{api}.gir
%{_libdir}/pkgconfig/tracker-testutils-3.0.pc

%if %{build_doc}
%files docs
%{_datadir}/doc/Tracker-3.0/
%endif

