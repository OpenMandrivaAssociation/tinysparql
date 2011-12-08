%define api			0.12
%define major		0
%define gir_major	0.12
%define libname		%mklibname %{name} %{api} %{major}
%define develname	%mklibname %{name} -d

%define build_evo 1
%define build_doc 0

#gw libtracker-common is in the main package and not provided
%define _requires_exceptions devel(libtracker-common\\|devel(libtracker-data

Summary:	Desktop-neutral metadata-based search framework
Name:		tracker
Version:	0.12.8
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.tracker-project.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz
Patch0:		tracker-0.12.8-linkage.patch
Patch1:		tracker-0.12.7-gthread.patch

BuildRequires:	intltool
BuildRequires:	giflib-devel
BuildRequires:	tiff-devel
BuildRequires:	jpeg-devel
BuildRequires:	libunistring-devel
BuildRequires: pkgconfig(camel-1.2) >= 2.32.0
BuildRequires: pkgconfig(evolution-data-server-1.2) >= 2.32.0
BuildRequires: pkgconfig(evolution-plugin-3.0)
BuildRequires: pkgconfig(evolution-shell-3.0) >= 3.1
BuildRequires: pkgconfig(exempi-2.0) >= 2.1.0
BuildRequires: pkgconfig(flac) >= 1.2.1
BuildRequires: pkgconfig(gdk-pixbuf-2.0) >= 2.12.0
BuildRequires: pkgconfig(gee-1.0) >= 0.3
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.28.0
BuildRequires: pkgconfig(glib-2.0) >= 2.28.0
BuildRequires: pkgconfig(gmodule-2.0) >= 2.28.0
BuildRequires: pkgconfig(gnome-keyring-1) >= 2.26
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires: pkgconfig(gstreamer-0.10) >= 0.10.31
BuildRequires: pkgconfig(gstreamer-pbutils-0.10) >= 0.10.31
BuildRequires: pkgconfig(gstreamer-tag-0.10) >= 0.10.31
BuildRequires: pkgconfig(gthread-2.0) >= 2.28.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires: pkgconfig(libcue)
BuildRequires: pkgconfig(libexif) >= 0.6
BuildRequires: pkgconfig(libgsf-1) >= 1.13
BuildRequires: pkgconfig(libiptcdata)
BuildRequires: pkgconfig(libnm-glib) >= 0.8
BuildRequires: pkgconfig(libpanelapplet-4.0)
BuildRequires: pkgconfig(libpng) >= 1.2
BuildRequires: pkgconfig(libstreamanalyzer) >= 0.7.0
BuildRequires: pkgconfig(libxine) >= 1.0
BuildRequires: pkgconfig(libxml-2.0) >= 2.6
BuildRequires: pkgconfig(pango) >= 1.0.0
BuildRequires: pkgconfig(poppler-glib) >= 0.16.0
BuildRequires: pkgconfig(rest-0.7) >= 0.6
BuildRequires: pkgconfig(sqlite3) >= 3.7.0
BuildRequires: pkgconfig(taglib_c) >= 1.6
BuildRequires: pkgconfig(totem-plparser)
BuildRequires: pkgconfig(upower-glib) >= 0.9.0
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(vorbisfile) >= 0.22

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

%package search-tool
Summary:	Graphical search tool for Tracker search framework
Group:		Graphical desktop/GNOME
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}

%description search-tool
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains the
GNOME-based standalone graphical search tool for the tracker framework.

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
BuildRequires:	evolution-devel
#gw libtool dep of evo:
BuildRequires: gnome-pilot-devel

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
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Group:		Development/C
Summary:	Development library of Tracker
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname tracker 0 -d}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
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
	--disable-miner-evolution
%else
	--enable-miner-evolution 
%endif

%make

%install
rm -rf %{buildroot}
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
%config(noreplace) %{_sysconfdir}/xdg/autostart/tracker-miner-fs.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/tracker-status-icon.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/tracker-store.desktop
%{_bindir}/%{name}-control
%{_bindir}/%{name}-explorer
%{_bindir}/%{name}-import
%{_bindir}/%{name}-info
%{_bindir}/%{name}-search
%{_bindir}/%{name}-sparql
%{_bindir}/%{name}-status-icon
%{_bindir}/%{name}-stats
%{_bindir}/%{name}-status
%{_bindir}/%{name}-tag
%{_datadir}/%{name}
%{_libdir}/%{name}-%{api}
%{_libexecdir}/tracker-extract
%{_libexecdir}/%{name}-miner-fs
%{_libexecdir}/%{name}-store
%{_libexecdir}/tracker-writeback
%{_mandir}/man1/tracker-control.1*
%{_mandir}/man1/tracker-extract.1*
%{_mandir}/man1/tracker-import.1*
%{_mandir}/man1/tracker-info.1*
%{_mandir}/man1/tracker-miner-fs.1*
%{_mandir}/man1/tracker-search.1*
%{_mandir}/man1/tracker-sparql.1*
%{_mandir}/man1/tracker-stats.1*
%{_mandir}/man1/tracker-status.1*
%{_mandir}/man1/tracker-status-icon.1*
%{_mandir}/man1/tracker-store.1*
%{_mandir}/man1/tracker-tag.1*
%{_mandir}/man5/tracker-extract.cfg.5*
%{_mandir}/man5/tracker-fts.cfg.5*
%{_mandir}/man5/tracker-miner-fs.cfg.5*
%{_mandir}/man5/tracker-store.cfg.5*
%_datadir/dbus-1/services/org.freedesktop.Tracker1.Extract.service
%_datadir/dbus-1/services/org.freedesktop.Tracker1.Miner*
%_datadir/dbus-1/services/org.freedesktop.Tracker1.service

%files common
%{_iconsdir}/hicolor/*/apps/%{name}.*

%files search-tool
%{_bindir}/tracker-search-tool
%{_datadir}/applications/tracker-search-tool.desktop
%{_mandir}/man1/tracker-search-tool.1*

%files preferences
%{_bindir}/tracker-preferences
%{_datadir}/applications/tracker-preferences.desktop
%{_mandir}/man1/tracker-preferences.1*

%files applet
%_libdir/bonobo/servers/GNOME_Search_Bar_Applet.server
%{_libexecdir}/tracker-search-bar
%{_mandir}/man1/tracker-search-bar.1*

%files -n %{libname}
%{_libdir}/libtracker-client-%{api}.so.%{major}*
%{_libdir}/libtracker-extract-%{api}.so.%{major}*
%{_libdir}/libtracker-miner-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Tracker-%{girmajor}.typelib
%{_libdir}/girepository-1.0/TrackerExtract-%{girmajor}.typelib
%{_libdir}/girepository-1.0/TrackerMiner-%{girmajor}.typelib

%files -n %{develname}
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/tracker-client-%{api}.pc
%{_libdir}/pkgconfig/tracker-extract-%{api}.pc
%{_libdir}/pkgconfig/tracker-miner-%{api}.pc
%_datadir/gtk-doc/html/libtracker-client
%_datadir/gtk-doc/html/libtracker-common
%_datadir/gtk-doc/html/libtracker-extract
%_datadir/gtk-doc/html/libtracker-miner
%_datadir/gtk-doc/html/ontology
%_datadir/vala/vapi/tracker-client-%{api}.vapi
%_datadir/vala/vapi/tracker-miner-%{api}.vapi
%_datadir/vala/vapi/tracker-miner-%{api}.deps
%{_datadir}/gir-1.0/Tracker-%{girmajor}.gir
%{_datadir}/gir-1.0/TrackerExtract-%{girmajor}.gir
%{_datadir}/gir-1.0/TrackerMiner-%{girmajor}.gir

%if %{build_evo}
%files -n evolution-tracker
%_libdir/evolution/*/plugins/liborg-freedesktop-Tracker-evolution-plugin.la
%_libdir/evolution/*/plugins/liborg-freedesktop-Tracker-evolution-plugin.so
%_libdir/evolution/*/plugins/org-freedesktop-Tracker-evolution-plugin.eplug
%endif

%files -n nautilus-tracker
%_libdir/nautilus/extensions-3.0/libnautilus-tracker-tags*
