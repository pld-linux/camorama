Summary:	GNOME webcam program
Summary(pl):	Program do kamer internetowych dla GNOME
Name:		camorama
Version:	0.16
Release:	1
License:	GPL
Group:		Applications
Source0:	http://camorama.fixedgear.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	8d685cdb872e890f047177e9aa6985f2
URL:		http://camorama.fixedgear.org/
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	pango-devel >= 1.0.3
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.1
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libbonoboui-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	bonobo-activation-devel >= 1.0.0
BuildRequires:	libpng-devel >= 1.2.2
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Camorama is a program for controlling webcams. It is pretty simple at
the moment, and I hope to make it much more complete. I also plan to
make it more generic, as I initially wrote it with only my own
Creative Webcam 3 in mind. Hopefully it will work with other cameras.

%description -l pl
Camorama to program do kontrolowania kamer internetowych. Na razie
jest prosty, ale autor ma nadziejê uczyniæ go bardziej kompletnym;
planuje tak¿e uczyniæ go bardziej ogólnym, bo na razie program by³
pisany tylko z my¶l± o Creative Webcam 3. W przysz³o¶ci ma dzia³aæ z
innymi kamerami.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post 
%gconf_schema_install

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/camorama
%{_datadir}/applications/camorama.desktop
%{_pixmapsdir}/camorama.png
%{_datadir}/camorama/camorama.glade
%{_sysconfdir}/gconf/schemas/camorama.schemas
