%define name tracker
%define version 0.6.2
%define svn 0
%if %svn
%define release %mkrel 0.%svn.1
%else
%define release %mkrel 1
%endif
%define major 0
%define libname %mklibname %name %major
%define develname %mklibname %name -d

Summary: Desktop-neutral metadata-based search framework
Name: %{name}
Version: %{version}
Release: %{release}
%if %svn
Source0: %{name}-%{svn}.tar.bz2
%else
Source0: http://www.gnome.org/~jamiemcc/tracker/%{name}-%{version}.tar.bz2
%endif
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/GNOME
Url: http://www.gnome.org/projects/tracker
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: sqlite3-devel
BuildRequires: dbus-devel
BuildRequires: glib2-devel
BuildRequires: zlib-devel
BuildRequires: libgmime-devel
BuildRequires: libgstreamer0.10-devel
BuildRequires: libpoppler-devel
BuildRequires: pygtk2.0-devel
BuildRequires: libvorbis-devel
BuildRequires: png-devel
BuildRequires: libexif-devel
BuildRequires: libgsf-devel
BuildRequires: gamin-devel
BuildRequires: libgnome2-devel
BuildRequires: gnomeui2-devel
BuildRequires: gnome-desktop-devel
BuildRequires: libglade2.0-devel
BuildRequires: deskbar-applet
BuildRequires: ImageMagick
%if %svn
BuildRequires: gnome-common
BuildRequires: intltool
%endif
Requires: libxslt-proc
Requires: w3m
Requires: wv

%description
Tracker is a framework designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.

%package common
Summary: Graphical search tool for tracker search framework
Group: Graphical desktop/GNOME
Requires: %name = %version

%description common
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains common
files for the tracker framework.

%package search-tool
Summary: Graphical search tool for tracker search framework
Group: Graphical desktop/GNOME
Requires: %name = %version
Requires: %name-common = %version

%description search-tool
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains the
GNOME-based standalone graphical search tool for the tracker framework.

%package preferences
Summary: Configuration tool for tracker search framework
Group: Graphical desktop/GNOME
Requires: %name = %version
Requires: %name-common = %version

%description preferences
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains the
GNOME-based configuration tool for the tracker framework.

%package deskbar-handler
Summary: Deskbar plugin for tracker search framework
Group: Graphical desktop/GNOME
Requires: %name = %version
Requires: deskbar-applet

%description deskbar-handler
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient. This package contains a
plugin that will allow the deskbar-applet panel search tool to search
using tracker.

%package -n %libname
Group: System/Libraries
Summary: Shared library of tracker

%description -n %libname
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.

%package -n %develname
Group: Development/C
Summary: Development library of tracker
Requires: %libname = %version
Obsoletes: %mklibname tracker 0 -d
Provides: %name-devel = %version-%release

%description -n %develname
Tracker is a tool designed to extract information and metadata about your 
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.

%prep
%if %svn
%setup -q -n %name
%else
%setup -q
%endif

%build
%if %svn
./autogen.sh
%endif
%configure --enable-deskbar-applet
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%post search-tool
%update_icon_cache hicolor
%update_menus
%postun search-tool
%clean_icon_cache hicolor
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README NEWS AUTHORS ChangeLog
%config(noreplace) %_sysconfdir/xdg/autostart/trackerd.desktop
%_bindir/o3totxt
%_bindir/%{name}d
%_bindir/%{name}-extract
%_bindir/%{name}-files
%_bindir/%{name}-meta-folder
%_bindir/%{name}-query
%_bindir/%{name}-search
%_bindir/%{name}-stats
%_bindir/%{name}-status
%_bindir/%{name}-tag
%_bindir/%{name}-thumbnailer
%_datadir/%name
%_libdir/%name
%_mandir/man1/trackerd.1*
%_mandir/man1/tracker-extract.1*
%_mandir/man1/tracker-files.1*
%_mandir/man1/tracker-meta-folder.1*
%_mandir/man1/tracker-query.1*
%_mandir/man1/tracker-search.1*
%_mandir/man1/tracker-stats.1*
%_mandir/man1/tracker-status.1*
%_mandir/man1/tracker-tag.1*
%_mandir/man1/tracker-thumbnailer.1*
%_mandir/man5/tracker.cfg.5*
%_mandir/man7/tracker-services.7*
%_datadir/dbus-1/services/tracker.service

%files common
%defattr(-,root,root)
%_iconsdir/hicolor/16x16/apps/%{name}.png
%_iconsdir/hicolor/22x22/apps/%{name}.png
%_iconsdir/hicolor/24x24/apps/%{name}.png
%_iconsdir/hicolor/32x32/apps/%{name}.png
%_iconsdir/hicolor/48x48/apps/%{name}.png
%_iconsdir/hicolor/scalable/apps/%{name}.svg

%files search-tool
%defattr(-,root,root)
%_bindir/tracker-search-tool
%_datadir/applications/tracker-search-tool.desktop
%_mandir/man1/tracker-search-tool.1*

%files preferences
%defattr(-,root,root)
%_bindir/tracker-preferences
%_datadir/applications/tracker-preferences.desktop
%_mandir/man1/tracker-preferences.1*

%files deskbar-handler
%defattr(-,root,root)
%_libdir/deskbar-applet/handlers/tracker-handler.py

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*a
%_includedir/*
%_libdir/pkgconfig/tracker.pc
%_libdir/pkgconfig/libtracker-gtk.pc
