%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major	0
%define api	0.14
%define libname	%mklibname %{name} %{api} %{major}
%define girname	%mklibname %{name}-gir %{api}
%define devname	%mklibname %{name} -d

%define build_evo 0
%define build_doc 0
%define gstapi	1.0

#gw libtracker-common is in the main package and not provided
%define __noautoreq 'devel\\(libtracker-common\\|devel\\(libtracker-data'

Summary:	Desktop-neutral metadata-based search framework
Name:		tracker
Version:	0.14.5
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.tracker-project.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		tracker-0.12.8-linkage.patch

BuildRequires:	desktop-file-utils
BuildRequires:	glib2.0-common
BuildRequires:	firefox
BuildRequires:	intltool
BuildRequires:	mozilla-thunderbird
BuildRequires:	giflib-devel
BuildRequires:	tiff-devel
BuildRequires:	jpeg-devel
BuildRequires:	libunistring-devel
BuildRequires:	pkgconfig(camel-1.2)
BuildRequires:	pkgconfig(evolution-data-server-1.2) >= 3.3
BuildRequires:	pkgconfig(evolution-plugin-3.0)
BuildRequires:	pkgconfig(evolution-shell-3.0) >= 3.1
BuildRequires:	pkgconfig(exempi-2.0) >= 2.1.0
BuildRequires:	pkgconfig(flac) >= 1.2.1
BuildRequires:	pkgconfig(gdk-pixbuf-2.0) >= 2.12.0
BuildRequires:	pkgconfig(gee-1.0) >= 0.3
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.28.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.28.0
BuildRequires:	pkgconfig(gnome-keyring-1) >= 2.26
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires:	pkgconfig(gstreamer-%{gstapi}) >= 0.10.31
BuildRequires:	pkgconfig(gstreamer-pbutils-%{gstapi}) >= 0.10.31
BuildRequires:	pkgconfig(gstreamer-tag-%{gstapi}) >= 0.10.31
BuildRequires:	pkgconfig(gthread-2.0) >= 2.28.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(libcue)
BuildRequires:	pkgconfig(libexif) >= 0.6
BuildRequires:	pkgconfig(libebackend-1.2)
BuildRequires:	pkgconfig(libgsf-1) >= 1.13
BuildRequires:	pkgconfig(libiptcdata)
BuildRequires:	pkgconfig(libnm-glib) >= 0.8
BuildRequires:	pkgconfig(libpanelapplet-4.0)
BuildRequires:	pkgconfig(libpng) >= 1.2
BuildRequires:	pkgconfig(libstreamanalyzer) >= 0.7.0
BuildRequires:	pkgconfig(libxine) >= 1.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.6
BuildRequires:	pkgconfig(pango) >= 1.0.0
BuildRequires:	pkgconfig(poppler-glib) >= 0.16.0
BuildRequires:	pkgconfig(rest-0.7) >= 0.6
BuildRequires:	pkgconfig(sqlite3) >= 3.7.0
BuildRequires:	pkgconfig(taglib_c) >= 1.6
BuildRequires:	pkgconfig(totem-plparser)
BuildRequires:	pkgconfig(upower-glib) >= 0.9.0
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(vorbisfile) >= 0.22

Requires:	odt2txt

%description
Tracker is a framework designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.

%package common
Summary:	Graphical search tool for Tracker search framework
Group:		Graphical desktop/GNOME
Requires:	%{name} = %{version}

%description common
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains common
files for the tracker framework.

%package preferences
Summary:	Configuration tool for Tracker search framework
Group:		Graphical desktop/GNOME
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}

%description preferences
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains the
GNOME-based configuration tool for the tracker framework.

%package applet
Summary:	Panel applet for Tracker search framework
Group:		Graphical desktop/GNOME
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}

%description applet
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains a
panel applet for configuring and using Tracker.

%if %{build_evo}
%package -n evolution-tracker
Group:Networking/Mail
Summary: Integrate Evolution with the Tracker desktop search
Requires: evolution
Requires:	%{name} = %{version}-%{release}
BuildRequires:	pkgconfig(evolution-plugin-3.0)

%description -n evolution-tracker
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains an
evolution plugin for Tracker integration.
%endif

%package -n nautilus-tracker
Group: Graphical desktop/GNOME
Summary: Nautilus integration of tracker
Requires:	%{name} = %{version}-%{release}
BuildRequires: nautilus-devel

%description -n nautilus-tracker
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains an
nautilus plugin for Tracker integration.

%package firefox-plugin
Summary:        A simple bookmark exporter for Tracker
Group:		Graphical desktop/GNOME
Requires:       %{name} = %{version}-%{release}

%description firefox-plugin
This Firefox addon exports your bookmarks to Tracker, so that you can search
for them for example using tracker-needle.

%package thunderbird-plugin
Summary:        Thunderbird extension to export mails to Tracker
Group:		Graphical desktop/GNOME
Requires:       %{name} = %{version}-%{release}

%description thunderbird-plugin
A simple Thunderbird extension to export mails to Tracker.

%package -n %{libname}
Group:		System/Libraries
Summary:	Shared library of Tracker

%description -n %{libname}
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	Development library of Tracker
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname tracker 0 -d}

%description -n %{devname}
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-libflac \
	--disable-functional-tests \
%if %{build_doc}
	--enable-gtk-doc \
%endif
	--enable-libvorbis \
%if !%{build_evo}
	--disable-miner-evolution \
%else
	--enable-miner-evolution \
%endif
	--with-firefox-plugin-dir=%{_libdir}/firefox/extensions         \
	--with-thunderbird-plugin-dir=%{_libdir}/thunderbird/extensions 

%make  LIBS='-lgmodule-2.0'

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
rm -rf %{buildroot}%{_datadir}/tracker-tests

%find_lang %{name}

# do not start under KDE
desktop-file-install \
	--dir=%{buildroot}/%{_sysconfdir}/xdg/autostart \
	--remove-only-show-in=KDE \
	%{buildroot}/%{_sysconfdir}/xdg/autostart/*.desktop

%files -f %{name}.lang
%doc README NEWS AUTHORS ChangeLog
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-miner-flickr.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-miner-fs.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-store.desktop
%{_bindir}/%{name}-control
%{_bindir}/%{name}-explorer
%{_bindir}/%{name}-import
%{_bindir}/%{name}-info
%{_bindir}/%{name}-needle
%{_bindir}/%{name}-search
%{_bindir}/%{name}-sparql
%{_bindir}/%{name}-stats
%{_bindir}/%{name}-tag
%{_datadir}/%{name}
%dir %{_libdir}/%{name}-%{api}/extract-modules
%dir %{_libdir}/%{name}-%{api}/writeback-modules
%{_libdir}/%{name}-%{api}/extract-modules/*.so
%{_libdir}/%{name}-%{api}/writeback-modules/*.so
%{_libexecdir}/%{name}-extract
%{_libexecdir}/%{name}-miner-flickr
%{_libexecdir}/%{name}-miner-fs
%{_libexecdir}/%{name}-store
%{_libexecdir}/tracker-writeback
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Extract.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner*
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Writeback.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.SearchBarFactory.service
%{_datadir}/gnome-panel/4.0/applets/org.gnome.panel.SearchBar.panel-applet
%{_datadir}/applications/tracker-needle.desktop
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.*
%{_mandir}/man1/tracker-*.1*
%exclude %{_mandir}/man1/tracker-preferences.1*
%exclude %{_mandir}/man1/tracker-search-bar.1*

%files common
%{_iconsdir}/hicolor/*/apps/%{name}.*

%files preferences
%{_bindir}/tracker-preferences
%{_datadir}/applications/tracker-preferences.desktop
%{_mandir}/man1/tracker-preferences.1*

%files applet
%{_libexecdir}/tracker-search-bar
%{_mandir}/man1/tracker-search-bar.1*

%files -n %{libname}
%{_libdir}/libtracker-extract-%{api}.so.%{major}*
%{_libdir}/libtracker-miner-%{api}.so.%{major}*
%{_libdir}/libtracker-sparql-%{api}.so.%{major}*
%{_libdir}/%{name}-%{api}/libtracker-*.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Tracker-%{api}.typelib
%{_libdir}/girepository-1.0/TrackerExtract-%{api}.typelib
%{_libdir}/girepository-1.0/TrackerMiner-%{api}.typelib

%files thunderbird-plugin
%{_datadir}/xul-ext/trackerbird/
%{_libdir}/thunderbird/extensions/trackerbird@bustany.org
%{_datadir}/applications/trackerbird-launcher.desktop

%files firefox-plugin
%{_datadir}/xul-ext/trackerfox/
%{_libdir}/firefox/extensions/trackerfox@bustany.org

%files -n %{devname}
%{_libdir}/lib*.so
%{_libdir}/%{name}-%{api}/libtracker-*.so
%{_includedir}/%{name}-%{api}/*
%{_libdir}/pkgconfig/tracker-extract-%{api}.pc
%{_libdir}/pkgconfig/tracker-miner-%{api}.pc
%{_libdir}/pkgconfig/tracker-sparql-%{api}.pc
%{_datadir}/gtk-doc/html/libtracker-extract
%{_datadir}/gtk-doc/html/libtracker-miner
%{_datadir}/gtk-doc/html/libtracker-sparql
%{_datadir}/vala/vapi/tracker-miner-%{api}.vapi
%{_datadir}/vala/vapi/tracker-miner-%{api}.deps
%{_datadir}/vala/vapi/tracker-sparql-%{api}.vapi
%{_datadir}/vala/vapi/tracker-sparql-%{api}.deps
%{_datadir}/gir-1.0/Tracker-%{api}.gir
%{_datadir}/gir-1.0/TrackerExtract-%{api}.gir
%{_datadir}/gir-1.0/TrackerMiner-%{api}.gir

%if %{build_evo}
%files -n evolution-tracker
%{_libdir}/evolution/*/plugins/liborg-freedesktop-Tracker-evolution-plugin.so
%{_libdir}/evolution/*/plugins/org-freedesktop-Tracker-evolution-plugin.eplug
%endif

%files -n nautilus-tracker
%{_libdir}/nautilus/extensions-3.0/libnautilus-tracker-tags*

