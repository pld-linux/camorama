Summary:	GNOME webcam program
Summary(pl.UTF-8):	Program do kamer internetowych dla GNOME
Name:		camorama
Version:	0.19
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/camorama/0.19/%{name}-%{version}.tar.bz2
# Source0-md5:	75025ba37d1dd1c398d92ba2dbef43ee
Patch0:		%{name}-schemas.patch
Patch1:		%{name}-desktop.patch
URL:		http://camorama.fixedgear.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	intltool >= 0.36.2
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
Requires(post,preun):	GConf2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Camorama is a program for controlling webcams. It is pretty simple at
the moment, and I hope to make it much more complete. I also plan to
make it more generic, as I initially wrote it with only my own
Creative Webcam 3 in mind. Hopefully it will work with other cameras.

%description -l pl.UTF-8
Camorama to program do kontrolowania kamer internetowych. Na razie
jest prosty, ale autor ma nadzieję uczynić go bardziej kompletnym;
planuje także uczynić go bardziej ogólnym, bo na razie program był
pisany tylko z myślą o Creative Webcam 3. W przyszłości ma działać z
innymi kamerami.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

sed -i -e s#sr\@Latn#sr\@latin# configure.in
mv -f po/sr\@{Latn,latin}.po

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install camorama.schemas

%preun
%gconf_schema_uninstall camorama.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/camorama
%{_datadir}/camorama
%{_desktopdir}/camorama.desktop
%{_pixmapsdir}/*.png
%{_sysconfdir}/gconf/schemas/camorama.schemas
