Summary:	UCView - video capture and display program based on unicap libraries
Summary(pl.UTF-8):	UCView - program do przechwytywania i wyświetlania obrazu oparty na bibliotekach unicap
Name:		ucview
Version:	0.33
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
#Source0Download: http://unicap-imaging.org/download.htm
Source0:	http://unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	da609cf706e70254abea06cc1fb495e2
URL:		http://unicap-imaging.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	glib2-devel >= 1:2.8.0
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libunicapgtk-devel >= 0.2.23
BuildRequires:	libucil-devel >= 0.2.2
BuildRequires:	pkgconfig
Requires(post,preun):	GConf2
Requires:	glib2 >= 1:2.8.0
Requires:	gtk+2 >= 2:2.8.0
Requires:	libunicapgtk >= 0.2.23
Requires:	libucil >= 0.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UCView is a video capture and display program based on unicap
libraries. It features:
- High performance live video display utilizing XVideo hardware
  acceleration where possible.
- Support of a broad range of video capture devices via the unicap
  library.
- Audio/Video recording and encoding using the free Ogg Vorbis and
  Theora high performance codecs.
- Extensible via a plugins.

%description -l pl.UTF-8
UCView to program do przechwytywania i wyświetlania obrazu oparty na
bibliotekach unicap. Cechuje się:
- wydajnym odtwarzaniem obrazu dzięki wykorzystaniu akceleracji
  sprzętowej XVideo (o ile to możliwe)
- obsługą szerokiej gamy urządzeń przechwytujących obraz poprzez
  bibliotekę unicap
- nagrywaniem i kodowaniem dźwięku i obrazu przy użyciu
  wolnodostępnych, wydajnych kodeków Ogg Vorbis i Theora
- rozszerzalnością poprzez wtyczki.

%package devel
Summary:	Header files for UCView plugins development
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia wtyczek dla programu UCView
Group:		Development/Libraries
# doesn't require base

%description devel
Header files for UCView plugins development.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek dla programu UCView.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# for plugins from external packages
install -d $RPM_BUILD_ROOT%{_libdir}/ucview/plugins

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install ucview.schemas

%preun
%gconf_schema_uninstall ucview.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/ucview
%{_datadir}/ucview
%dir %{_libdir}/ucview
%dir %{_libdir}/ucview/plugins
%{_sysconfdir}/gconf/schemas/ucview.schemas
%{_desktopdir}/ucview.desktop
%{_iconsdir}/hicolor/*/apps/ucview.png
%{_mandir}/man1/ucview.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/ucview
%{_pkgconfigdir}/ucview.pc
