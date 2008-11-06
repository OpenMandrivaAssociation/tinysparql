%define svn 0
%if %svn
%define release %mkrel 0.%svn.2
%else
%define release %mkrel 5
%endif
%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Desktop-neutral metadata-based search framework
Name:		tracker
Version:	0.6.6
Release:	%{release}
%if %svn
Source0:	%{name}-%{svn}.tar.bz2
%else
Source0:	http://www.gnome.org/~jamiemcc/tracker/%{name}-%{version}.tar.bz2
%endif
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.tracker-project.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	sqlite3-devel
BuildRequires:	dbus-devel
BuildRequires:	glib2-devel
BuildRequires:	zlib-devel
BuildRequires:	libgmime-devel
BuildRequires:	libgstreamer-devel >= 0.10
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
BuildRequires:	libglade2.0-devel
BuildRequires:	libnotify-devel
BuildRequires:	hal-devel
BuildRequires:	libpoppler-glib-devel
BuildRequires:	exempi-devel
BuildRequires:	deskbar-applet
BuildRequires:	ImageMagick
%if %svn
BuildRequires:	gnome-common
BuildRequires:	intltool
%endif
Requires:	libxslt-proc
Requires:	w3m
Requires:	wv

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

%build
%if %svn
./autogen.sh
%endif
%configure --enable-deskbar-applet=module
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
%config(noreplace) %{_sysconfdir}/xdg/autostart/trackerd.desktop
%{_bindir}/o3totxt
%{_bindir}/%{name}d
%{_bindir}/%{name}-extract
%{_bindir}/%{name}-files
%{_bindir}/%{name}-meta-folder
%{_bindir}/%{name}-query
%{_bindir}/%{name}-search
%{_bindir}/%{name}-stats
%{_bindir}/%{name}-status
%{_bindir}/%{name}-tag
%{_bindir}/%{name}-thumbnailer
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/trackerd.1*
%{_mandir}/man1/tracker-extract.1*
%{_mandir}/man1/tracker-files.1*
%{_mandir}/man1/tracker-meta-folder.1*
%{_mandir}/man1/tracker-query.1*
%{_mandir}/man1/tracker-search.1*
%{_mandir}/man1/tracker-stats.1*
%{_mandir}/man1/tracker-status.1*
%{_mandir}/man1/tracker-tag.1*
%{_mandir}/man1/tracker-thumbnailer.1*
%{_mandir}/man5/tracker.cfg.5*
%{_mandir}/man7/tracker-services.7*
%{_datadir}/dbus-1/services/tracker.service

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
%{_bindir}/tracker-applet
%{_mandir}/man1/tracker-applet.1*
%{_sysconfdir}/xdg/autostart/tracker-applet.desktop

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib*.so
%attr(644,root,root) %{_libdir}/lib*a
%{_includedir}/*
%{_libdir}/pkgconfig/tracker.pc
%{_libdir}/pkgconfig/libtracker-gtk.pc
