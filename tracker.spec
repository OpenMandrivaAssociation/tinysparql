%define svn 0
%define release %mkrel 3

%define name tracker
%define api 0.7
%define major		0
%define libname		%mklibname %{name} %api %{major}
%define develname	%mklibname %{name} -d

%define build_evo 0
%if %mdvver <= 201000
%define build_evo 1
%endif

Summary:	Desktop-neutral metadata-based search framework
Name:		%{name}
Version:	0.7.14
Release:	%{release}
%if %svn
Source0:	%{name}-%{svn}.tar.bz2
%else
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
%endif
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.tracker-project.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
#BuildRequires:	quill-devel
BuildRequires:	unac-devel
BuildRequires:	devicekit-power-devel
BuildRequires:	libxine-devel
BuildRequires:	id3lib-devel
BuildRequires:	sqlite3-devel >= 3.6.16
BuildRequires:	dbus-devel
BuildRequires:	gtk+2-devel >= 2.16
BuildRequires:	gnome-panel-devel
BuildRequires:	zlib-devel
BuildRequires:	libgstreamer-plugins-base-devel >= 0.10
BuildRequires:	libpoppler-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:	libvorbis-devel
BuildRequires:	png-devel
BuildRequires:	libexif-devel
BuildRequires:	libgsf-devel
BuildRequires:	gamin-devel
BuildRequires:	libgnome2-devel
BuildRequires:	gnomeui2-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtiff-devel
BuildRequires:	hal-devel
BuildRequires:	libpoppler-glib-devel
BuildRequires:	raptor-devel
BuildRequires:	enca-devel
BuildRequires:	libgee-devel
BuildRequires:	libiptcdata-devel
BuildRequires:	totem-plparser-devel
%if %mdvver < 201000
BuildRequires:  ext2fs-devel
%else
BuildRequires:  libuuid-devel
%endif
BuildRequires:	exempi-devel >= 2.1.0
BuildRequires:	deskbar-applet
BuildRequires:	imagemagick
BuildRequires:  graphviz
BuildRequires:	intltool
BuildRequires:  gtk-doc
BuildRequires:  docbook-dtd412-xml
#if %svn
BuildRequires:	gnome-common
#endif
Requires:	libxslt-proc
Requires:	w3m
Requires:	wv
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
Requires:	%{name} = %{version}
Requires:	%{name}-common = %{version}

%description search-tool
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains the
GNOME-based standalone graphical search tool for the tracker framework.

%package preferences
Summary:	Configuration tool for Tracker search framework
Group:		Graphical desktop/GNOME
Requires:	%{name} = %{version}
Requires:	%{name}-common = %{version}

%description preferences
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains the
GNOME-based configuration tool for the tracker framework.

%package deskbar-handler
Summary:	Deskbar plugin for Tracker search framework
Group:		Graphical desktop/GNOME
Requires:	%{name} = %{version}
Requires:	deskbar-applet

%description deskbar-handler
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains a
plugin that will allow the deskbar-applet panel search tool to search
using tracker.

%package applet
Summary:	Panel applet for Tracker search framework
Group:		Graphical desktop/GNOME
Requires:	%{name} = %{version}
Requires:	%{name}-common = %{version}

%description applet
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains a
panel applet for configuring and using Tracker.

%if %build_evo
%package -n evolution-tracker
Group:Networking/Mail
Summary: Integrate Evolution with the Tracker desktop search
Requires: evolution
Requires:	%{name} = %{version}
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
Requires:	%{name} = %{version}
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

%package -n %{develname}
Group:		Development/C
Summary:	Development library of Tracker
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname tracker 0 -d}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.

%prep
%if %svn
%setup -q -n %{name}
%else
%setup -q
%endif
#gw gtk-doc 1.13 issue
gnome-autogen.sh

%build
%if %svn
./autogen.sh
%endif
%define _disable_ld_no_undefined 1
#gw format string error in generated vala source in tracker 0.7.9
%define Werror_cflags %nil
%configure2_5x --enable-deskbar-applet=module --enable-gtk-doc \
--enable-libvorbis \
%if !%build_evo
--disable-evolution-miner
%endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%if %mdkversion < 200900
%post search-tool
%{update_icon_cache hicolor}
%{update_menus}
%endif
%if %mdkversion < 200900
%postun search-tool
%{clean_icon_cache hicolor}
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
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
%_libexecdir/tracker-extract
%{_libexecdir}/%{name}-miner-fs
%{_libexecdir}/%{name}-store
%_libexecdir/tracker-writeback
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
%defattr(-,root,root)
%{_iconsdir}/hicolor/*/apps/%{name}.*

%files search-tool
%defattr(-,root,root)
%{_bindir}/tracker-search-tool
%{_datadir}/applications/tracker-search-tool.desktop
%{_mandir}/man1/tracker-search-tool.1*

%files preferences
%defattr(-,root,root)
%{_bindir}/tracker-preferences
%{_datadir}/applications/tracker-preferences.desktop
%{_mandir}/man1/tracker-preferences.1*

%files deskbar-handler
%defattr(-,root,root)
%{_libdir}/deskbar-applet/modules-2.20-compatible/tracker-module.py

%files applet
%defattr(-,root,root)
%_libdir/bonobo/servers/GNOME_Search_Bar_Applet.server
%_libexecdir/tracker-search-bar
%{_mandir}/man1/tracker-search-bar.1*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libtracker-client-%api.so.%{major}*
%{_libdir}/libtracker-gtk-%api.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib*.so
%attr(644,root,root) %{_libdir}/lib*a
%{_includedir}/*
%{_libdir}/pkgconfig/tracker-client-%{api}.pc
%{_libdir}/pkgconfig/tracker-miner-%{api}.pc
%{_libdir}/pkgconfig/tracker-gtk-%{api}.pc
%_datadir/gtk-doc/html/libtracker-client
%_datadir/gtk-doc/html/libtracker-common
%_datadir/gtk-doc/html/libtracker-miner
%_datadir/gtk-doc/html/ontology

%if %build_evo
%files -n evolution-tracker
%defattr(-,root,root)
%_libdir/evolution/*/plugins/liborg-freedesktop-Tracker-evolution-plugin.la
%_libdir/evolution/*/plugins/liborg-freedesktop-Tracker-evolution-plugin.so
%_libdir/evolution/*/plugins/org-freedesktop-Tracker-evolution-plugin.eplug
%endif

%files -n nautilus-tracker
%defattr(-,root,root)
%_libdir/nautilus/extensions-2.0/libnautilus-tracker-tags*
