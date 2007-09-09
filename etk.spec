Summary:	Toolkit based on the EFL
Summary(pl.UTF-8):	Toolkit oparty na EFL
Name:		etk
Version:	0.1.0.003
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	52e1adf8cc840d486e21bf439c68f041
URL:		http://enlightenment.org/p.php?p=about/libs/etk
BuildRequires:	autoconf
BuildRequires:	automake >= 1.4
# ecore-file ecore-x ecore-fb
BuildRequires:	ecore-devel >= 0.9.9
BuildRequires:	edje >= 0.5.0
BuildRequires:	edje-devel >= 0.5.0
BuildRequires:	evas-devel >= 0.9.9
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires:	fonts-TTF-bitstream-vera
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enlightenment Foundations Library based toolkit.

%description -l pl.UTF-8
Toolkit oparty na EFL (Enlightenment Foundations Library).

%package libs
Summary:	EFL toolkit library
Summary(pl.UTF-8):	Biblioteka toolkitu EFL.
Group:		Libraries
Requires:	ecore-fb >= 0.9.9
Requires:	ecore-file >= 0.9.9
Requires:	ecore-x >= 0.9.9
Requires:	edje-libs >= 0.5.0
Requires:	evas >= 0.9.9
Conflicts:	etk < 0.1.0.003

%description libs
Enlightenment Foundations Library based toolkit library.

%description libs -l pl.UTF-8
Biblioteka toolkitu opartego na EFL (Enlightenment Foundations
Library).

%package devel
Summary:	Header files for etk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki etk
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
# ecore-file ecore-x ecore-fb
Requires:	ecore-devel >= 0.9.9
Requires:	edje-devel >= 0.5.0
Requires:	evas-devel >= 0.9.9

%description devel
This is the package containing the header files for etk library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki etk.

%package static
Summary:	Static etk library
Summary(pl.UTF-8):	Statyczna biblioteka etk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static etk library.

%description static -l pl.UTF-8
Statyczna biblioteka etk.

%prep
%setup -q

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

rm -f $RPM_BUILD_ROOT%{_libdir}/etk/engines/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/etk_prefs
%attr(755,root,root) %{_bindir}/etk_test
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libetk.so.*.*.*
%dir %{_libdir}/etk
%dir %{_libdir}/etk/engines
%attr(755,root,root) %{_libdir}/etk/engines/ecore_*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/etk-config
%attr(755,root,root) %{_libdir}/libetk.so
%{_libdir}/libetk.la
%{_includedir}/etk
%{_includedir}/Etk_Engine_Ecore_*.h
%{_pkgconfigdir}/etk.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libetk.a
