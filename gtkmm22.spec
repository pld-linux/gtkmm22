%include        /usr/lib/rpm/macros.perl
Summary:	A C++ interface for the GTK+ (a GUI library for X)
Summary(pl):	Wrapper C++ dla GTK+
Name:		gtkmm22
Version:	2.2.12
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.2/gtkmm-%{version}.tar.bz2
# Source0-md5:	d72986a00006aad01c9f5c2566a6f671
Patch0:		%{name}-link.patch
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	atk-devel >= 1.2.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	glib2-devel >= 2.2.1
BuildRequires:	gtk+2-devel >= 1:2.2.1
BuildRequires:	libsigc++12-devel >= 1.2.5
BuildRequires:	libstdc++-devel >= 5:3.3.1
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	pango-devel >= 1.2.1
BuildRequires:	perl-base >= 5.6
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	zlib-devel
Requires:	%{name}-atk = %{version}-%{release}
Requires:	%{name}-glib = %{version}-%{release}
Requires:	%{name}-pango = %{version}-%{release}
Requires:	cpp
Obsoletes:	Gtk--
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a C++ interface for GTK+ (the Gimp ToolKit) GUI
library. The interface provides a convenient interface for C++
programmers to create GUIs with GTK+'s flexible object-oriented
framework. Features include type safe callbacks, widgets that are
extensible using inheritance and over 110 classes that can be freely
combined to quickly create complex user interfaces.

%description -l pl
GTK-- jest wrapperem C++ dla Gimp ToolKit (GTK). GTK jest bibliotek�
s�u��c� do tworzenia graficznych interfejs�w. W pakiecie znajduje si�
tak�e biblioteka GDK-- - wrapper C++ dla GDK (General Drawing Kit).

%package devel
Summary:	GTK-- and GDK-- header files, development documentation
Summary(pl):	Pliki nag��wkowe GTK-- i GDK--, dokumentacja dla programist�w
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-atk-devel = %{version}-%{release}
Requires:	%{name}-pango-devel = %{version}-%{release}
Requires:	gtk+2-devel >= 1:2.2.1
Requires:	libsigc++12-devel >= 1.2.5	

%description devel
Header files and development documentation for GTK-- library.

%description devel -l pl
Pliki nag��wkowe i dokumentacja dla programist�w do biblioteki GTK--.

%package doc
Summary:	Reference documentation and examples for GTK-- and GDK--
Summary(pl):	Szczeg�owa dokumentacja i przyk�ady dla GTK-- i GDK--
Group:		Documentation
Requires:	devhelp

%description doc
Reference documentation and examples for GTK-- and GDK--.

%description doc -l pl
Szczeg�owa dokumentacja i przyk�ady dla GTK-- i GDK--.

%package static
Summary:	GTK-- and GDK-- static libraries
Summary(pl):	Biblioteki statyczne GTK-- i GDK--
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GTK-- and GDK-- static libraries.

%description static -l pl
Biblioteki statyczne GTK-- i GDK--.

%package atk
Summary:	A C++ interface for atk library
Summary(pl):	Interfejs C++ dla biblioteki atk
Group:		X11/Development/Libraries
Requires:	%{name}-glib = %{version}-%{release}

%description atk
A C++ interface for atk library.

%description atk -l pl
Interfejs C++ dla biblioteki atk.

%package atk-devel
Summary:	A C++ interface for atk library - header files
Summary(pl):	Interfejs C++ dla biblioteki atk - pliki nag��wkowe
Group:		X11/Development/Libraries
Requires:	%{name}-atk = %{version}-%{release}
Requires:	%{name}-glib-devel = %{version}-%{release}
Requires:	atk-devel >= 1.2.0

%description atk-devel
A C++ interface for atk library - header files.

%description atk-devel -l pl
Interfejs C++ dla biblioteki atk - pliki nag��wkowe.

%package atk-static
Summary:	A C++ interface for atk library - static version
Summary(pl):	Interfejs C++ dla biblioteki atk - wersja statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-atk-devel = %{version}-%{release}

%description atk-static
A C++ interface for atk library - static version.

%description atk-static -l pl
Interfejs C++ dla biblioteki atk - wersja statyczna.

%package glib
Summary:	A C++ interface for glib library
Summary(pl):	Interfejs C++ dla biblioteki glib
Group:		X11/Development/Libraries

%description glib
A C++ interface for glib library.

%description glib -l pl
Interfejs C++ dla biblioteki glib.

%package glib-devel
Summary:	A C++ interface for glib library - header files
Summary(pl):	Interfejs C++ dla biblioteki glib - pliki nag��wkowe
Group:		X11/Development/Libraries
Requires:	%{name}-glib = %{version}-%{release}
Requires:	glib2-devel >= 2.2.1
Requires:	libsigc++12-devel >= 1.2.1
Requires:	libstdc++-devel >= 5:3.3.1

%description glib-devel
A C++ interface for glib library - header files.

%description glib-devel -l pl
Interfejs C++ dla biblioteki glib - pliki nag��wkowe.

%package glib-static
Summary:	A C++ interface for glib library - static version
Summary(pl):	Interfejs C++ dla biblioteki glib - wersja statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}

%description glib-static
A C++ interface for glib library - static version.

%description glib-static -l pl
Interfejs C++ dla biblioteki glib - wersja statyczna.

%package pango
Summary:	A C++ interface for pango library
Summary(pl):	Interfejs C++ dla biblioteki pango
Group:		X11/Development/Libraries
Requires:	%{name}-glib = %{version}-%{release}

%description pango
A C++ interface for pango library.

%description pango -l pl
Interfejs C++ dla biblioteki pango.

%package pango-devel
Summary:	A C++ interface for pango library - header files
Summary(pl):	Interfejs C++ dla biblioteki pango - pliki nag��wkowe
Group:		X11/Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}
Requires:	%{name}-pango = %{version}-%{release}
Requires:	pango-devel >= 1.2.1

%description pango-devel
A C++ interface for pango library - header files.

%description pango-devel -l pl
Interfejs C++ dla biblioteki pango - pliki nag��wkowe.

%package pango-static
Summary:	A C++ interface for pango library - static version
Summary(pl):	Interfejs C++ dla biblioteki pango - wersja statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-pango-devel = %{version}-%{release}

%description pango-static
A C++ interface for pango library - static version.

%description pango-static -l pl
Interfejs C++ dla biblioteki pango - wersja statyczna.

%prep
%setup -qn gtkmm-%{version}
%patch0 -p1

# GLIBMM_PROG_CXX_SUN exists only in aclocal.m4
tail -n +6979 aclocal.m4 | head -n 15 > scripts/cxx-sun.m4

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__autoheader}
%{__automake}
# exceptions and rtti are used in this package --misiek
%configure \
	--enable-static=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

mv -f $RPM_BUILD_ROOT%{_docdir}/gtkmm-2.0/{examples,tests} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p 	/sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	atk -p /sbin/ldconfig
%postun	atk -p /sbin/ldconfig

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%post	pango -p /sbin/ldconfig
%postun	pango -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS
%attr(755,root,root) %{_libdir}/libg[dt]kmm*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libg[dt]kmm*.so
%{_libdir}/libg[dt]kmm*.la

%{_libdir}/gtkmm-*/include/g[dt]kmm*
%dir %{_libdir}/gtkmm-2.0/proc
%{_libdir}/gtkmm-*/proc/m4
%{_libdir}/gtkmm-*/proc/pm
%attr(755,root,root) %{_libdir}/gtkmm-*/proc/gtkmmproc
%attr(755,root,root) %{_libdir}/gtkmm-*/proc/*.pl

%{_includedir}/gtkmm-2.0/g[dt]kmm*
%{_pkgconfigdir}/g[dt]kmm*.pc

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/gtkmm-2.0
%{_examplesdir}/%{name}-%{version}
%doc %{_datadir}/devhelp/books/gtkmm-2.0

%files static
%defattr(644,root,root,755)
%{_libdir}/libg[dt]kmm*.a

%files atk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatkmm*.so.*.*

%files atk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatkmm*.so
%{_libdir}/libatkmm*.la
%{_pkgconfigdir}/atkmm*.pc
%{_includedir}/gtkmm-2.0/atkmm*

%files atk-static
%defattr(644,root,root,755)
%{_libdir}/libatkmm*.a

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglibmm*.so.*.*

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglibmm*.so
%{_libdir}/libglibmm*.la

%dir %{_libdir}/gtkmm-2.0
%dir %{_libdir}/gtkmm-2.0/include
%{_libdir}/gtkmm-*/include/glibmm*

%dir %{_includedir}/gtkmm-2.0
%{_includedir}/gtkmm-2.0/glibmm*
%{_pkgconfigdir}/glibmm*.pc

%files glib-static
%defattr(644,root,root,755)
%{_libdir}/libglibmm*.a

%files pango
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpangomm*.so.*.*

%files pango-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpangomm*.so
%{_libdir}/libpangomm*.la
%{_pkgconfigdir}/pangomm*.pc
%{_includedir}/gtkmm-2.0/pangomm*

%files pango-static
%defattr(644,root,root,755)
%{_libdir}/libpangomm*.a
