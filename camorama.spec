
Summary:	GNOME webcam program
Name:		camorama
Version:	0.16
Release:	1
Source0:	http://camorama.fixedgear.org/downloads/%{name}-%{version}.tar.gz
URL:		http://camorama.fixedgear.org
License:	GPL
Group:		Applications
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Camorama is a program for controlling webcams. It is pretty simple at
the moment, and I hope to make it much more complete. I also plan to
make it more generic, as I initially wrote it with only my own
Creative Webcam 3 in mind. Hopefully it will work with other cameras.

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

%post 
%gconf_schema_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/camorama
%{_datadir}/applications/camorama.desktop
%{_datadir}/pixmaps/camorama.png
%{_datadir}/camorama/camorama.glade
%{_sysconfdir}/gconf/schemas/camorama.schemas
