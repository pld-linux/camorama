Summary:	GNOME webcam program
Summary(pl.UTF-8):   Program do kamer internetowych dla GNOME
Name:		camorama
Version:	0.18
Release:	1
License:	GPL
Group:		Applications
Source0:	http://camorama.fixedgear.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	26ea7219405f2ec1677329190bed5e01
Patch0:		%{name}-schemas.patch
Patch1:		%{name}-desktop.patch
URL:		http://camorama.fixedgear.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-activation-devel >= 1.0.0
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 1:2.0.3
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libbonoboui-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.1
BuildRequires:	libpng-devel >= 1.2.2
BuildRequires:	pango-devel >= 1:1.0.3
Requires(post):	GConf2
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

%build
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
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/camorama
%{_datadir}/camorama
%{_desktopdir}/camorama.desktop
%{_pixmapsdir}/*.png
%{_sysconfdir}/gconf/schemas/camorama.schemas
