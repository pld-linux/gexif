Summary:	Utility to show EXIF information hidden in JPEG files
Summary(pl):	Narzêdzie do wy¶wietlania danych EXIF ukrytych w plikach JPEG
Name:		gexif
Version:	0.5
Release:	5
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/libexif/%{name}-%{version}.tar.bz2
# Source0-md5:	472c109ffdb3f8528eabc039e0ac495b
Patch0:		%{name}-gtk24.patch
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

%description -l pl
Graficzne narzêdzie dzia³aj±ce z linii poleceñ, s³u¿±ce do
pokazywania informacji EXIF ukrytych w plikach JPEG.

%prep
%setup -q
%patch0 -p1

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
