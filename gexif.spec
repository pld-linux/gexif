Summary:	Utility to show EXIF information hidden in JPEG files
Summary(pl):	Narz�dzie do wy�wietlania danych EXIF ukrytych w plikach JPEG
Name:		gexif
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/libexif/%{name}-%{version}.tar.bz2
URL:		http://libexif.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRequires:	libexif-devel
BuildRequires:	libexif-gtk-devel >= 0.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Graphical utility to show EXIF information hidden in JPEG files.

%description -l pl
Graficzne narz�dzie dzia�aj�ce z linii polece�, s�u��ce do
pokazywania informacji EXIF ukrytych w plikach JPEG.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*