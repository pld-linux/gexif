Summary:	Utility to show EXIF information hidden in JPEG files
Summary(pl):	Narzêdzie do wy¶wietlania danych EXIF ukrytych w plikach JPEG
Name:		gexif
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/libexif/%{name}-%{version}.tar.gz
URL:		http://libexif.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	libexif-devel
BuildRequires:	libexif-gtk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Graphical utility to show EXIF information hidden in JPEG files.

%description -l pl
Graficzne narzêdzie dzia³aj±ce z linii poleceñ, s³u¿±ce do
pokazywania informacji EXIF ukrytych w plikach JPEG.

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
