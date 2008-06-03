#
%define		ecore_ver	0.9.9.043
%define		edje_ver	0.9.9.043
%define		evas_ver	0.9.9.043

Summary:	Toolkit based on the EFL
Summary(pl.UTF-8):	Toolkit oparty na EFL
Name:		etk
Version:	0.1.0.042
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://download.enlightenment.org/snapshots/2008-01-25/%{name}-%{version}.tar.bz2
# Source0-md5:	6c1f4c204f2227476cb232127156113f
URL:		http://enlightenment.org/p.php?p=about/libs/etk
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
# ecore-file ecore-x ecore-fb
BuildRequires:	ecore-devel >= %{ecore_ver}
BuildRequires:	edje >= %{edje_ver}
BuildRequires:	edje-devel >= %{edje_ver}
BuildRequires:	evas-devel >= %{evas_ver}
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
Requires:	ecore-fb >= %{ecore_ver}
Requires:	ecore-file >= %{ecore_ver}
Requires:	ecore-x >= %{ecore_ver}
Requires:	edje-libs >= %{edje_ver}
Requires:	evas >= %{evas_ver}
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
Requires:	ecore-devel >= %{ecore_ver}
Requires:	edje-devel >= %{edje_ver}
Requires:	evas-devel >= %{evas_ver}

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
%doc AUTHORS COPYING README TODO
%attr(755,root,root) %{_bindir}/etk_prefs
%attr(755,root,root) %{_bindir}/etk_test
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libetk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libetk.so.1
%dir %{_libdir}/etk
%dir %{_libdir}/etk/engines
%attr(755,root,root) %{_libdir}/etk/engines/ecore_*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libetk.so
%{_libdir}/libetk.la
%{_includedir}/etk
%{_includedir}/Etk_Engine_Ecore_*.h
%{_pkgconfigdir}/etk.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libetk.a
