%global edataserver_version 3.33.2
%global libical_version 1.0-9
%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-calendar
Version:	45.1
Release:	1
Summary:	Simple and beautiful calendar application designed to fit GNOME 3

License:	GPLv3+
URL:		https://wiki.gnome.org/Apps/Calendar
Group:		Graphical desktop/GNOME

Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	gtk-doc
BuildRequires:	meson
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(libecal-2.0) >= %{edataserver_version}
BuildRequires:	pkgconfig(libdazzle-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(gweather4)
BuildRequires:	pkgconfig(libgeoclue-2.0)
BuildRequires:	pkgconfig(libedataserver-1.2) >= %{edataserver_version}
BuildRequires:	pkgconfig(libical) >= %{libical_version}
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	appstream-util
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(gsettings-desktop-schemas)

%description
Calendar is a simple and beautiful calendar application designed to fit
GNOME 3.
Features:
* Week, month and year views
* Basic editing of events
* Evolution Data Server integration
* Search support

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%{find_lang} %{name}

%files -f %{name}.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Calendar.desktop
%{_datadir}/dbus-1/services/org.gnome.Calendar.service
%{_datadir}/metainfo/org.gnome.*.xml
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.gschema.xml
# co-own these directories
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Calendar.search-provider.ini
%{_iconsdir}/hicolor/*/apps/org.gnome.Calendar*.*
