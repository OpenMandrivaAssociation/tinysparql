%define url_ver %(echo %{version} | cut -d. -f1,2)
# evolution and nautilus plugin dropped by upstream. Build disabled. (penguin)
%define build_evo	0
%define build_doc	1
%ifarch %arm aarch64
%define build_nautilus  0
%else
%define build_nautilus  0
%endif

%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1
%define _disable_lto 1

#gw libtracker-common is in the main package and not provided
%define __noautoreq 'devel\\(libtracker-common\\|devel\\(libtracker-data'

%define api	2.0
%define major	0
%define libname	%mklibname %{name} %{api} %{major}
%define devname	%mklibname %{name} -d
%define girname	%mklibname %{name}-gir %{api}

Summary:	Desktop-neutral metadata-based search framework
Name:		tracker
Version:	2.1.4
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.tracker-project.org
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Source1:	30-tracker.conf
#Patch0:                tracker-linkage.patch
BuildRequires:	intltool
#BuildRequires:	firefox
#BuildRequires:	mozilla-thunderbird
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	tiff-devel
BuildRequires:	jpeg-devel
BuildRequires:	icu-devel
BuildRequires:	gnome-common
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
BuildRequires:	pkgconfig(libnm-glib) >= 0.8
BuildRequires:  pkgconfig(libnm-glib-vpn)
BuildRequires:	pkgconfig(libosinfo-1.0)
BuildRequires:	pkgconfig(libpng) >= 1.2
BuildRequires:	pkgconfig(libsecret-unstable) >= 0.5
#BuildRequires:	pkgconfig(libstreamanalyzer) >= 0.7.0
BuildRequires:	pkgconfig(libxine) >= 1.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.6
BuildRequires:	pkgconfig(pango) >= 1.0.0
BuildRequires:	pkgconfig(poppler-glib) >= 0.16.0
BuildRequires:	pkgconfig(rest-0.7) >= 0.6
BuildRequires:	pkgconfig(sqlite3) >= 3.7.14
BuildRequires:	pkgconfig(taglib_c) >= 1.6
BuildRequires:	pkgconfig(totem-plparser)
BuildRequires:	pkgconfig(upower-glib) >= 0.9.0
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(vorbisfile) >= 0.22
BuildRequires:	pkgconfig(libgrss)
BuildRequires:	pkgconfig(json-glib-1.0)
Obsoletes:	tracker-search-tool < 0.10
Obsoletes:	%{name}-common < 0.12.8-2
Obsoletes:	%{name}-preferences < 0.12.8-2
Obsoletes:	%{name}-applet < 0.12.8-2

%description
Tracker is a framework designed to extract information and metadata about your
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.

#package firefox-plugin
#Summary:	A simple bookmark exporter for Tracker
#Group:		Graphical desktop/GNOME
#Requires:	%{name} = %{version}-%{release}

#description firefox-plugin
#This Firefox addon exports your bookmarks to Tracker, so that you can search
#for them for example using tracker-needle.

#package thunderbird-plugin
#Summary:	Thunderbird extension to export mails to Tracker
#Group:		Graphical desktop/GNOME
#Requires:	%{name} = %{version}-%{release}

#description thunderbird-plugin
#A simple Thunderbird extension to export mails to Tracker.

%if %{build_evo}
%package -n evolution-%{name}
Group:		Networking/Mail
Summary:	Integrate Evolution with the Tracker desktop search
Requires:	evolution
Requires:	%{name} = %{version}-%{release}
BuildRequires:  pkgconfig(evolution-data-server-1.2) >= 2.32.0
BuildRequires:  pkgconfig(evolution-shell-3.0) >= 3.1

%description -n evolution-%{name}
Tracker is a tool designed to extract information and metadata about your
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.

This package contains an evolution plugin for Tracker integration.
%endif

%if %{build_nautilus}
%package -n nautilus-%{name}
Group:		Graphical desktop/GNOME
Summary:	Nautilus integration of tracker
Requires:	%{name} = %{version}-%{release}
BuildRequires:	pkgconfig(libnautilus-extension)

%description -n nautilus-%{name}
Tracker is a tool designed to extract information and metadata about your
personal data so that it can be searched easily and quickly. Tracker is
desktop-neutral, fast and resource efficient.

This package contains an nautilus plugin for Tracker integration.
%endif

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
%setup -q
%apply_patches

%build
%configure \
	--enable-libflac \
	--enable-libvorbis \
	--enable-libosinfo \
	--disable-functional-tests \
	--disable-libstemmer \
%if %{build_doc}
	--enable-gtk-doc \
%endif
%if !%{build_evo}
	--disable-miner-evolution \
%else
        --enable-miner-evolution \
%endif
	--with-firefox-plugin-dir=%{_libdir}/firefox/extensions \
	--with-thunderbird-plugin-dir=%{_libdir}/thunderbird/extensions LIBS='-ldl -lpthread'

%make

%install
%makeinstall_std

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/sysctl.d/30-%{name}.conf

%find_lang %{name}

rm -rf %{buildroot}%{_datadir}/tracker-tests

# do not start under KDE
desktop-file-install \
	--remove-only-show-in=KDE \
	--dir=%{buildroot}%{_sysconfdir}/xdg/autostart \
	%{buildroot}%{_sysconfdir}/xdg/autostart/*.desktop


%files -f %{name}.lang
%doc README NEWS AUTHORS ChangeLog
#config(noreplace) #_sysconfdir}/xdg/autostart/%{name}-extract.desktop
#config(noreplace) #_sysconfdir}/xdg/autostart/%{name}-miner-apps.desktop
#config(noreplace) #_sysconfdir}/xdg/autostart/%{name}-miner-fs.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-store.desktop
#config(noreplace) #_sysconfdir}/xdg/autostart/%{name}-miner-rss.desktop
#config(noreplace) #_sysconfdir}/xdg/autostart/%{name}-miner-user-guides.desktop
%{_datadir}/bash-completion/completions/%{name}
#{_bindir}/%{name}-needle
#{_bindir}/%{name}-preferences
%{_bindir}/%{name}
%{_datadir}/%{name}/
#dir #{_libdir}/%{name}-%{api}/extract-modules
#dir #{_libdir}/%{name}-%{api}/writeback-modules
#{_libdir}/%{name}-%{api}/extract-modules/*.so
#{_libdir}/%{name}-%{api}/writeback-modules/*.so
#_libexecdir}/%{name}-extract
#_libexecdir}/%{name}-miner-apps
#_libexecdir}/%{name}-miner-fs
#_libexecdir}/%{name}-miner-rss
#_libexecdir}/%{name}-miner-user-guides
%{_libexecdir}/%{name}-store
#_libexecdir}/%{name}-writeback
%{_prefix}/lib/sysctl.d/30-%{name}.conf
#_mandir}/man1/%{name}-extract.1*
%{_mandir}/man1/%{name}-info.1*
#_mandir}/man1/%{name}-miner-fs.1*
#_mandir}/man1/%{name}-miner-rss.1*
#_mandir}/man1/%{name}-needle.1.*
%{_mandir}/man1/%{name}-search.1*
%{_mandir}/man1/%{name}-sparql.1*
%{_mandir}/man1/%{name}-store.1*
%{_mandir}/man1/%{name}-tag.1*
#_mandir}/man1/%{name}-writeback.1*
#_mandir}/man1/%{name}-preferences.1*
%{_mandir}/man1/%{name}-daemon.1*
%{_mandir}/man1/%{name}-index.1*
%{_mandir}/man1/%{name}-reset.1*
%{_mandir}/man1/%{name}-sql.1*
%{_mandir}/man1/%{name}-status.1*
#_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner*
#_datadir}/dbus-1/services/org.freedesktop.Tracker1.Writeback.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.service
#_datadir}/appdata/*.xml
#_datadir}/applications/tracker-needle.desktop
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.*
#{_datadir}/applications/%{name}-preferences.desktop
#_iconsdir}/hicolor/*/apps/%{name}.*
%{_prefix}/lib/systemd/user/tracker-*.service

%files vala
%{_datadir}/vala/vapi/%{name}-control-%{api}.vapi
%{_datadir}/vala/vapi/%{name}-control-%{api}.deps
%{_datadir}/vala/vapi/%{name}-sparql-%{api}.vapi
%{_datadir}/vala/vapi/%{name}-sparql-%{api}.deps
%{_datadir}/vala/vapi/%{name}-miner-%{api}.vapi
%{_datadir}/vala/vapi/%{name}-miner-%{api}.deps

%files -n %{libname}
%{_libdir}/lib%{name}-control-%{api}.so.%{major}*
%{_libdir}/lib%{name}-miner-%{api}.so.%{major}*
%{_libdir}/lib%{name}-sparql-%{api}.so.%{major}*
%dir %{_libdir}/%{name}-%{api}/
%{_libdir}/%{name}-%{api}/libtracker-*.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Tracker-%{api}.typelib
%{_libdir}/girepository-1.0/TrackerControl-%{api}.typelib
%{_libdir}/girepository-1.0/TrackerMiner-%{api}.typelib

%files -n %{devname}
%{_libdir}/lib%{name}-control-%{api}.so
%{_libdir}/lib%{name}-miner-%{api}.so
%{_libdir}/lib%{name}-sparql-%{api}.so
%{_libdir}/%{name}-%{api}/libtracker-*.so
%{_includedir}/*
%{_libdir}/pkgconfig/%{name}-control-%{api}.pc
%{_libdir}/pkgconfig/%{name}-miner-%{api}.pc
%{_libdir}/pkgconfig/%{name}-sparql-%{api}.pc
%{_datadir}/gir-1.0/Tracker-%{api}.gir
%{_datadir}/gir-1.0/TrackerControl-%{api}.gir
%{_datadir}/gir-1.0/TrackerMiner-%{api}.gir

%if %{build_doc}
%files docs
%{_datadir}/gtk-doc/html/lib%{name}-control
%{_datadir}/gtk-doc/html/lib%{name}-miner
%{_datadir}/gtk-doc/html/lib%{name}-sparql
%{_datadir}/gtk-doc/html/ontology
%endif

%if %{build_evo}
%files -n evolution-%{name}
%{_libdir}/evolution/*/plugins/liborg-freedesktop-Tracker-evolution-plugin.so
%{_libdir}/evolution/*/plugins/org-freedesktop-Tracker-evolution-plugin.eplug
%endif

%if %{build_nautilus}
%files -n nautilus-%{name}
%{_libdir}/nautilus/extensions-3.0/libnautilus-tracker-tags.*
%endif

#files thunderbird-plugin
#{_datadir}/xul-ext/trackerbird/
#{_libdir}/thunderbird/extensions/trackerbird@bustany.org
#{_datadir}/applications/trackerbird-launcher.desktop

#files firefox-plugin
#{_datadir}/xul-ext/trackerfox/
#{_libdir}/firefox/extensions/trackerfox@bustany.org

