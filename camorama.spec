Summary:	GNOME webcam program
Summary(pl.UTF-8):	Program do kamer internetowych dla GNOME
Name:		camorama
Version:	0.20.7
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
# up to 0.19
#Source0:	http://ftp.gnome.org/pub/GNOME/sources/camorama/0.19/%{name}-%{version}.tar.bz2
# forked 0.20
Source0:	https://linuxtv.org/downloads/camorama/%{name}-%{version}.tar.gz
# Source0-md5:	98c09616c3fd23821a2644f665620fda
Patch0:		%{name}-desktop.patch
URL:		http://camorama.fixedgear.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools >= 0.19.8
# also possible: gtk+2 >= 2:2.24, gtk+4 >= 3.92
BuildRequires:	gtk+3-devel >= 3.10
BuildRequires:	libv4l-devel
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Camorama is a simple webcam viewer, with the ability to apply some
video effects.

%description -l pl.UTF-8
Camorama to prosty program do podglądu z kamery, z możliwością
dodawania niektórych efektów graficznych.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr@Latn,sr@latin}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/camorama
%{_datadir}/camorama
%{_datadir}/glib-2.0/schemas/org.gnome.camorama.gschema.xml
%{_datadir}/metainfo/camorama.appdata.xml
%{_desktopdir}/camorama.desktop
%{_iconsdir}/hicolor/*x*/devices/camorama.png
%{_mandir}/man1/camorama.1*
