#
# TODO:
#	- more modpack variants beside gtk3?
#	- qt client and modpack? (Qt5Core, Qt5Gui, Qt5Widgets >= 5.2)
#	- sdl2 instead of sdl?
#	- gtk3.22 instead of gtk3?
#	- work on authentication and Freeciv database support (fcdb: mysql/postgres/sqlite3)
#	- patch all packaged desktop files
#
# Conditional build:
%bcond_without	magickwand	# MagickWand map image toolkit support
%bcond_without	system_lua	# system Lua
%bcond_without	gtk2		# GTK+ 2 client
%bcond_without	gtk3		# GTK+ 3 client
%bcond_without	sdl		# SDL client
%bcond_without	xaw		# Xaw client
%bcond_with	qt		# Qt client (used to be broken)
%bcond_without	modpack		# modpack installer
%bcond_without	ruledit		# (Qt based) rule editor
#
Summary:	FREE CIVilization clone
Summary(es.UTF-8):	Clon del juego Civilization
Summary(pl.UTF-8):	Niekomercyjny klon CIVilization
Summary(pt_BR.UTF-8):	Clone do jogo Civilization
Name:		freeciv
Version:	2.6.6
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	http://downloads.sourceforge.net/freeciv/%{name}-%{version}.tar.bz2
# Source0-md5:	2f40775f142b509c0bfc6db89a3a8171
# NOTE: current version of freeland tiles does not work with newest freeciv version
#Source1:	http://download.gna.org/freeciv/contrib/tilesets/freeland/freeland-normal-2.0.0.tar.gz
Patch0:		%{name}-link.patch
Patch1:		%{name}-desktop.patch
URL:		http://freeciv.wikia.com/
%{?with_magickwand:BuildRequires:	ImageMagick-devel}
%{?with_sdl:BuildRequires:	SDL_image-devel}
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.9
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel >= 7.12.1
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.8.0}
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
%{?with_system_lua:BuildRequires:	lua53-devel}
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
%{?with_xaw:BuildRequires:	xorg-lib-libXaw-devel}
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
%if %{with ruledit}
BuildRequires:	Qt5Core-devel >= 5.2
BuildRequires:	Qt5Gui-devel >= 5.2
BuildRequires:	Qt5Widgets-devel >= 5.2
BuildRequires:	qt5-build >= 5.2
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-O1

%description
Free clone of Sid Meier's Civilization. Free Civilization clone for
Unix and X. This is multiplayer strategic game and you can also play
against computer-AI players.

%description -l es.UTF-8
Clon del juego Civilization.

%description -l pl.UTF-8
Freeciv jest to niekomercyjny (GPL) klon gry Civilization Sida Meiera.
Jest to gra strategiczna dla systemu X Window. Można grać w nią z
innymi osobami poprzez sieć, a także przeciwko "graczom" zarządzanym
przez komputer.

%description -l pt_BR.UTF-8
O FreeCiv é uma implementação do Civilization II para o Sistema X
Window.

%package client-common
Summary:	Freeciv game client common files
Summary(pl.UTF-8):	Wspólne pliki klientów gry Freeciv
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}
Requires:	SDL_mixer
Suggests:	%{name}-server = %{version}-%{release}

%description client-common
This package contains common files for Freeciv game clients.

%description client-common -l pl.UTF-8
Ten pakiet zawiera wspólne pliki dla klientów gry Freeciv.

%package client
Summary:	GTK2 Freeciv game client
Summary(pl.UTF-8):	Klient gry Freeciv korzystający z GTK2
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-client-common = %{version}-%{release}
Requires:	gtk+2 >= 2:2.12.0
Suggests:	%{name}-server = %{version}-%{release}

%description client
This package contains GTK2-based Freeciv game client.

%description client -l pl.UTF-8
Ten pakiet zawiera klienta gry Freeciv korzystającego z GTK2.

%package client-gtk3
Summary:	GTK3 Freeciv game client
Summary(pl.UTF-8):	Klient gry Freeciv korzystający z GTK3
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3 >= 3.8.0
Suggests:	%{name}-server = %{version}-%{release}

%description client-gtk3
This package contains GTK3-based Freeciv game client.

%description client-gtk3 -l pl.UTF-8
Ten pakiet zawiera klienta gry Freeciv korzystającego z GTK3.

%package client-sdl
Summary:	SDL Freeciv game client
Summary(pl.UTF-8):	Klient gry Freeciv korzystający z SDL
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-client-common = %{version}-%{release}
Suggests:	%{name}-server = %{version}-%{release}

%description client-sdl
This package contains SDL-based Freeciv game client.

%description client-sdl -l pl.UTF-8
Ten pakiet zawiera klienta gry Freeciv korzystającego z SDL.

%package client-xaw
Summary:	XAW Freeciv game client
Summary(pl.UTF-8):	Klient gry Freeciv korzystający z XAW
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-client-common = %{version}-%{release}
Suggests:	%{name}-server = %{version}-%{release}

%description client-xaw
This package contains based Freeciv game client using XAW (X Athena
Widgets).

%description client-xaw -l pl.UTF-8
Ten pakiet zawiera klienta gry Freeciv korzystającego z biblioteki XAW
(X Athena Widgets)

%package modpack
Summary:	Custom content installer for the Freeciv game
Summary(pl.UTF-8):	Instalator dodatków do gry Freeciv
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-client-common = %{version}-%{release}
Requires:	gtk+3 >= 3.8.0
Suggests:	%{name}-server = %{version}-%{release}

%description modpack
Custom content installer for the Freeciv game.

This program allows users to select and download add-on content
("modpacks") for Freeciv from the Internet, either from a list
maintained by the Freeciv team, or by using a URL obtained by other
means. It takes care of installing the files in the correct place
under the user's home directory for this version of Freeciv; it does
not install anything for system-wide use.

%description modpack -l pl.UTF-8
Ten pakiet zawiera instalator dodatków do gry Freeciv dostępnych w
internecie.

%package ruledit
Summary:	Freeciv graphical ruleset editor
Summary(pl.UTF-8):	Graficzny edytor reguł gry Freeciv
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}

%description ruledit
Freeciv graphical ruleset editor.

%description ruledit -l pl.UTF-8
Graficzny edytor reguł gry Freeciv.

%package server
Summary:	Freeciv game server
Summary(pl.UTF-8):	Serwer gry Freeciv
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}

%description server
This package contans Freeciv game server.

%description server -l pl.UTF-8
Ten pakiet zawiera server gry Freeciv.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1

cp -f %{_aclocaldir}/glib-gettext.m4 m4/

%build
%{__libtoolize}
%{__aclocal} -I m4 -I dependencies/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-client=stub,%{?with_gtk2:gtk2},%{?with_gtk3:gtk3},%{?with_qt:qt},%{?with_sdl:sdl},%{?with_xaw:xaw} \
	--enable-fcmp=%{?with_modpack:gtk3}%{!?with_modpack:no} \
	--enable-mapimg=%{?with_magickwand:magickwand}%{!?with_magickwand:no} \
	%{!?with_ruledit:--disable-ruledit} \
	%{?with_sdl:--enable-sdl-mixer=sdl} \
	%{?with_system_lua:--enable-sys-lua}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#cp -a client/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}/%{name}-client.desktop
#cp -a server/%{name}-server.desktop $RPM_BUILD_ROOT%{_desktopdir}
#%{__rm} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

cp -a data/icons/32x32/*.png $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a data/stdsounds{,.soundspec} $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfreeciv{,-srv}.{a,la}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man6/freeciv-qt*

# from freeciv-manual man:
#      This tool is currently only really of use to the Freeciv maintainers,
#      as a starting point for  pages  on  the  main Freeciv wiki;
#      it's not very useful to end users.
%{__rm} $RPM_BUILD_ROOT%{_bindir}/freeciv-manual
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man6/freeciv-manual*

%{__rm} $RPM_BUILD_ROOT%{_bindir}/freeciv-stub

# unpackaged variants
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man6/freeciv-{gtk3.22,mp-cli,mp-gtk2,mp-qt,sdl2}.6*

# needed if building --without gtk2,gtk3,sdl
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/themes

%find_lang %{name}
%find_lang %{name}-nations -a %{name}.lang
%if %{with ruledit}
%find_lang %{name}-ruledit
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS NEWS-2.6 doc/{BUGS,FAQ,HOWTOPLAY,README.effects,README.fcdb,README.graphics,README.sound,README.rulesets,TODO}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/helpdata.txt

%files client-common
%defattr(644,root,root,755)
%{_datadir}/%{name}/*.*spec
%{_datadir}/%{name}/amplio2
%{_datadir}/%{name}/buildings
%{_datadir}/%{name}/cimpletoon
%{_datadir}/%{name}/flags
%{_datadir}/%{name}/hex2t
%{_datadir}/%{name}/isophex
%{_datadir}/%{name}/isotrident
%{_datadir}/%{name}/misc
%{_datadir}/%{name}/stdmusic
%{_datadir}/%{name}/stdsounds
%dir %{_datadir}/%{name}/themes
%{_datadir}/%{name}/trident
%{_datadir}/%{name}/wonders
%{_mandir}/man6/freeciv.6*
%{_mandir}/man6/freeciv-client.6*

%if %{with gtk2}
%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/freeciv-gtk2
%{_desktopdir}/org.freeciv.gtk2.desktop
%{_datadir}/appdata/freeciv-gtk2.appdata.xml
%{_datadir}/%{name}/freeciv.rc-2.0
%{_datadir}/%{name}/gtk2_menus.xml
%{_datadir}/%{name}/themes/gui-gtk-2.0
%{_mandir}/man6/freeciv-gtk2.6*
%{_iconsdir}/hicolor/*/apps/freeciv-client.png
%{_pixmapsdir}/freeciv-client.png
%endif

%if %{with gtk3}
%files client-gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/freeciv-gtk3
%{_desktopdir}/org.freeciv.gtk3.desktop
%{_datadir}/appdata/freeciv-gtk3.appdata.xml
%{_datadir}/%{name}/gtk3_menus.xml
%{_datadir}/%{name}/themes/gui-gtk-3.0
%{_mandir}/man6/freeciv-gtk3.6*
%endif

%if %{with sdl}
%files client-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/freeciv-sdl
%{_desktopdir}/org.freeciv.sdl.desktop
%{_datadir}/appdata/freeciv-sdl.appdata.xml
%{_datadir}/%{name}/themes/gui-sdl
%{_mandir}/man6/freeciv-sdl.6*
%endif

%if %{with xaw}
%files client-xaw
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/freeciv-xaw
%{_datadir}/%{name}/Freeciv
%{_mandir}/man6/freeciv-xaw.6*
%endif

%if %{with modpack}
%files modpack
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/freeciv-mp-gtk3
%{_desktopdir}/org.freeciv.mp.gtk3.desktop
%{_datadir}/appdata/freeciv-mp-gtk3.appdata.xml
%{_iconsdir}/hicolor/*/apps/freeciv-modpack.png
%{_pixmapsdir}/freeciv-modpack.png
%{_mandir}/man6/freeciv-modpack.6*
%{_mandir}/man6/freeciv-mp-gtk3.6*
%endif

%if %{with ruledit}
%files ruledit -f %{name}-ruledit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/freeciv-ruledit
%{_datadir}/appdata/freeciv-ruledit.appdata.xml
%{_desktopdir}/org.freeciv.ruledit.desktop
%{_mandir}/man6/freeciv-ruledit.6*
%endif

%files server
%defattr(644,root,root,755)
%{_sysconfdir}/freeciv
%attr(755,root,root) %{_bindir}/freeciv-server
%{_desktopdir}/org.freeciv.server.desktop
%{_datadir}/appdata/freeciv-server.appdata.xml
%{_datadir}/%{name}/civ1
%{_datadir}/%{name}/civ2
%{_datadir}/%{name}/civ2civ3
%{_datadir}/%{name}/classic
%{_datadir}/%{name}/default
%{_datadir}/%{name}/experimental
%{_datadir}/%{name}/hexemplio
%{_datadir}/%{name}/multiplayer
%{_datadir}/%{name}/nation
%{_datadir}/%{name}/override
%{_datadir}/%{name}/sandbox
%{_datadir}/%{name}/scenarios
%{_datadir}/%{name}/*.serv
%{_mandir}/man6/freeciv-server.6*
%{_iconsdir}/hicolor/*/apps/freeciv-server.png
%{_pixmapsdir}/freeciv-server.png
