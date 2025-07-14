Summary:	Utility to show EXIF information hidden in JPEG files
Summary(pl.UTF-8):	Narzędzie do wyświetlania danych EXIF ukrytych w plikach JPEG
Name:		gexif
Version:	0.5
Release:	6
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/libexif/%{name}-%{version}.tar.bz2
# Source0-md5:	472c109ffdb3f8528eabc039e0ac495b
Source1:	%{name}-pl.po
Patch0:		%{name}-gtk24.patch
Patch1:		%{name}-codeset.patch
URL:		http://libexif.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libexif-gtk-devel >= 0.3.3
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libexif-gtk >= 0.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical utility to show EXIF information hidden in JPEG files.

%description -l pl.UTF-8
Graficzne narzędzie działające z linii poleceń, służące do
pokazywania informacji EXIF ukrytych w plikach JPEG.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

cp %{SOURCE1} po/pl.po
%{__perl} -pi -e 's/de es fr/de es fr pl/' configure.in

%build
%{__gettextize}
%{__libtoolize}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
