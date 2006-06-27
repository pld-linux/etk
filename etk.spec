%define	_snap	20060625
Summary:	Toolkit based on the EFL
Summary(pl):	Toolkit oparty na EFL
Name:		etk
Version:	0.1
Release:	0.%{_snap}.1
License:	BSD
Group:		Libraries
Source0:	http://sparky.homelinux.org/snaps/enli/e17/proto/%{name}-%{_snap}.tar.bz2
# Source0-md5:	c105a19c8b523a573933d581b2fa79e3
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	edje-devel
BuildRequires:	libtool
Requires:	fonts-TTF-bitstream-vera
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enlightenment Foundations Library based toolkit.

%description -l pl
Toolkit oparty na EFL (Enlightenment Foundations Library).

%package devel
Summary:	Header files for etk library
Summary(pl):	Pliki nag³ówkowe biblioteki etk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for etk library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki etk.

%package static
Summary:	Static etk library
Summary(pl):	Statyczna biblioteka etk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static etk library.

%description static -l pl
Statyczna biblioteka etk.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts
VERA=$(ls Vera*.ttf)
for FONT in $VERA; do
	rm -f $FONT
	ln -s %{_fontsdir}/TTF/$FONT .
done
cd -

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
%attr(755,root,root) %{_bindir}/etk_test
%attr(755,root,root) %{_libdir}/libetk.so.*.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/etk-config
%attr(755,root,root) %{_libdir}/libetk.so
%{_libdir}/libetk.la
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libetk.a
