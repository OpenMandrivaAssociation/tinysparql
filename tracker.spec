%define svn 0
%if %svn
%define release %mkrel 1
%else
%define release %mkrel 1
%endif
%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Desktop-neutral metadata-based search framework
Name:		tracker
Version:	0.6.93
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
BuildRequires:	sqlite3-devel
BuildRequires:	dbus-devel
BuildRequires:	glib2-devel
BuildRequires:	zlib-devel
BuildRequires:	libgmime-devel
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
BuildRequires:	libglade2.0-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtiff-devel
BuildRequires:	hal-devel
BuildRequires:	libpoppler-glib-devel
BuildRequires:	raptor-devel
BuildRequires:	libstemmer-devel
BuildRequires:	exempi-devel
BuildRequires:	deskbar-applet
BuildRequires:	imagemagick
BuildRequires:	intltool
%if %svn
BuildRequires:	gnome-common
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
#%patch -p1

%build
%if %svn
./autogen.sh
%endif
%define _disable_ld_no_undefined 1
%configure2_5x --enable-deskbar-applet=module
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%if %_lib != lib
mv %buildroot%_prefix/lib/deskbar* %buildroot%_libdir
%endif

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
%{_bindir}/%{name}-files
%{_bindir}/%{name}-info
%{_bindir}/%{name}-meta-folder
%{_bindir}/%{name}-processes
%{_bindir}/%{name}-query
%{_bindir}/%{name}-search
%{_bindir}/%{name}-services
%{_bindir}/%{name}-stats
%{_bindir}/%{name}-status
%{_bindir}/%{name}-tag
%{_bindir}/%{name}-unique
%{_datadir}/%{name}
%{_libdir}/%{name}
%_libexecdir/tracker-extract
%_libexecdir/tracker-indexer
%_libexecdir/trackerd
%{_mandir}/man1/trackerd.1*
%{_mandir}/man1/tracker-extract.1*
%{_mandir}/man1/tracker-files.1*
%{_mandir}/man1/tracker-info.1*
%{_mandir}/man1/tracker-meta-folder.1*
%{_mandir}/man1/tracker-query.1*
%{_mandir}/man1/tracker-search.1*
%{_mandir}/man1/tracker-services.1*
%{_mandir}/man1/tracker-stats.1*
%{_mandir}/man1/tracker-status.1*
%{_mandir}/man1/tracker-tag.1*
%{_mandir}/man1/tracker-thumbnailer.1*
%{_mandir}/man1/tracker-unique.1*
%{_mandir}/man5/tracker.cfg.5*
%_datadir/dbus-1/services/org.freedesktop.Tracker.Extract.service
%_datadir/dbus-1/services/org.freedesktop.Tracker.Indexer.service
%_datadir/dbus-1/services/org.freedesktop.Tracker.service

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
%{_libdir}/pkgconfig/tracker-module-1.0.pc
%{_libdir}/pkgconfig/libtracker-gtk.pc
%_datadir/gtk-doc/html/libtracker-common
%_datadir/gtk-doc/html/libtracker-module


%changelog
* Sat Apr 11 2009 Reinout van Schouwen <reinout@gmail.com> 0.6.93-1mdv2009.1
- new version 0.6.93

* Sun Mar 29 2009 Reinout van Schouwen <reinout@gmail.com> 0.6.92-1mdv2009.1
- update to new version 0.6.92 (bug 49249)
- new binary tracker-processes

* Fri Mar 13 2009 Götz Waschk <waschk@mandriva.org> 0.6.91-1mdv2009.1
+ Revision: 354731
- fix deskbar handler dir
- update to new version 0.6.91

* Wed Feb 11 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.90-1mdv2009.1
+ Revision: 339542
- Released version now also buildrequires intltool, not only svn version

  + Götz Waschk <waschk@mandriva.org>
    - new version
    - drop patch
    - fix build
    - update build deps
    - update file list
    - update source URL

* Thu Jan 01 2009 Götz Waschk <waschk@mandriva.org> 0.6.6-8mdv2009.1
+ Revision: 323218
- fix format strings

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sat Nov 08 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.6-7mdv2009.1
+ Revision: 300978
- rebuild (for xcb this time)

* Thu Nov 06 2008 Götz Waschk <waschk@mandriva.org> 0.6.6-6mdv2009.1
+ Revision: 300241
- rebuild for new gnome-desktop
- rebuild for new  gnome-desktop

* Wed Jul 23 2008 Götz Waschk <waschk@mandriva.org> 0.6.6-5mdv2009.0
+ Revision: 242252
- rebuild

  + Adam Williamson <awilliamson@mandriva.org>
    - really fix the gstreamer BR (tvignaud's version doesn't work on 2008)

* Mon Jun 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.6-4mdv2009.0
+ Revision: 230239
- fix gstreamer0.10-devel BR on x86_64
- rebuild for new libpoppler

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Adam Williamson <awilliamson@mandriva.org>
    - buildrequires libgstreamer0.10-devel not gstreamer0.10-devel (2008 doesn't have the latter provide)

* Mon Mar 03 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.6-1mdv2008.1
+ Revision: 177849
- add several buildrequires
- introduce package for the panel applet
- new release 0.6.6

* Thu Feb 28 2008 Frederik Himpe <fhimpe@mandriva.org> 0.6.5-1mdv2008.1
+ Revision: 176510
- Fix buildrequirements
- New upstream version

* Mon Jan 28 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.4-1mdv2008.1
+ Revision: 159409
- new release 0.6.4 (should fix #35497)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 11 2007 Adam Williamson <awilliamson@mandriva.org> 0.6.3-1mdv2008.1
+ Revision: 96960
- new release 0.6.3

* Thu Sep 06 2007 Adam Williamson <awilliamson@mandriva.org> 0.6.2-1mdv2008.0
+ Revision: 80588
- adjust build for new deskbar-applet module setup
- new release 0.6.2

* Wed Aug 15 2007 Adam Williamson <awilliamson@mandriva.org> 0.6.1-1mdv2008.0
+ Revision: 63746
- package tracker-preferences manpage
- correct license
- new release 0.6.1

* Wed Jul 25 2007 Adam Williamson <awilliamson@mandriva.org> 0.6.0-1mdv2008.0
+ Revision: 55100
- adjust buildrequires
- new release 0.6.0

* Wed Jun 20 2007 Adam Williamson <awilliamson@mandriva.org> 0.6.0-0.598.1mdv2008.0
+ Revision: 41671
- drop X-Mandriva menu category
- drop old icons
- unversioned -devel package
- new svn snapshot 598 (fixes a crasher bug)

* Thu May 17 2007 Adam Williamson <awilliamson@mandriva.org> 0.6.0-0.591.1mdv2008.0
+ Revision: 27570
- new snapshot 591, spec clean, don't BuildRequires libmagic (no longer used)


* Thu Mar 22 2007 Adam Williamson <awilliamson@mandriva.com> 0.6.0-0.544.1mdv2007.1
+ Revision: 147979
- BuildRequires ImageMagick
- 0.6.0svn: more stable than 0.5.4, ignores temp dirs

* Sun Mar 04 2007 Adam Williamson <awilliamson@mandriva.com> 0.5.4-2mdv2007.1
+ Revision: 132626
- really delete patch from SVN

* Fri Mar 02 2007 Adam Williamson <awilliamson@mandriva.com> 0.5.4-1mdv2007.1
+ Revision: 130958
- BuildRequires ImageMagick (needed for icon generation)
- BuildRequires desktop-file-utils (needed to modify .desktop file during %%install)
- Import tracker

