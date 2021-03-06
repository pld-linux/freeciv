#
# TODO:
#	- work on authentication and Freeciv database support (fcdb)
#	- patch all packaged desktop files
#	- modpack requires gtk2 or gtk3
#
# Conditional build:
%bcond_without  magickwand	# build without MagickWand map image toolkit support
%bcond_without  system_lua	# build with bundled lua
%bcond_without	gtk2		# build without gtk2 client
%bcond_without	gtk3		# build without gtk3 client
%bcond_without	sdl		# build without sdl client
%bcond_without	xaw		# build without xaw client
%bcond_with	qt		# build with qt client (broken)
%bcond_without	modpack		# build without modpack installer
#
Summary:	FREE CIVilization clone
Summary(es.UTF-8):	Clon del juego Civilization
Summary(pl.UTF-8):	Niekomercyjny klon CIVilization
Summary(pt_BR.UTF-8):	Clone do jogo Civilization
Name:		freeciv
Version:	2.6.3
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	http://downloads.sourceforge.net/freeciv/%{name}-%{version}.tar.bz2
# Source0-md5:	68f3eab21a20fcf7fe7de39d0915e23f
# NOTE: current version of freeland tiles does not work with newest freeciv version
#Source1:	http://download.gna.org/freeciv/contrib/tilesets/freeland/freeland-normal-2.0.0.tar.gz
Patch0:		%{name}-link.patch
Patch1:		%{name}-desktop.patch
Patch3:		imagemagick7.patch
URL:		http://freeciv.wikia.com/
%{?with_magickwand:BuildRequires:	ImageMagick-devel}
%{?with_sdl:BuildRequires:	SDL_image-devel}
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	curl-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
%{?with_gtk2:BuildRequires:	gtk+2-devel}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
BuildRequires:	libpng-devel
BuildRequires:	libtool
%{?with_system_lua:BuildRequires:	lua53-devel}
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
%{?with_xaw:BuildRequires:	xorg-lib-libXaw-devel}
BuildRequires:	zlib-devel
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

%package client
Summary:	GTK2 Freeciv game client
Summary(pl.UTF-8):	Klient gry Freeciv korzystający z GTK2
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-client-common = %{version}-%{release}
Suggests:	%{name}-server = %{version}-%{release}

%description client
This package contains GTK2-based Freeciv game client.

%description client -l pl.UTF-8
Ten pakiet zawiera klienta gry Freeciv korzystającego z GTK2.

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

%package client-gtk3
Summary:	GTK3 Freeciv game client
Summary(pl.UTF-8):	Klient gry Freeciv korzystający z GTK3
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}
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
%patch3 -p1

cp -f %{_aclocaldir}/glib-gettext.m4 m4/

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-client=stub,%{?with_gtk2:gtk2},%{?with_gtk3:gtk3},%{?with_qt:qt},%{?with_sdl:sdl},%{?with_xaw:xaw} \
	--enable-mapimg=%{?with_magickwand:magickwand}%{!?with_magickwand:no} \
	%{?with_sdl:--enable-sdl-mixer=sdl} \
	%{!?with_modpack:--enable-fcmp=no} \
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

# needed if building --without gtk2,gtk3,sdl
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/themes

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS doc/BUGS ChangeLog doc/FAQ doc/HOWTOPLAY NEWS NEWS-2.6
%doc doc/README.effects doc/README.fcdb doc/README.graphics doc/README.sound
%doc doc/README.rulesets doc/TODO
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/helpdata.txt

%files server
%defattr(644,root,root,755)
%{_sysconfdir}/freeciv
%attr(755,root,root) %{_bindir}/freeciv-server
#attr(755,root,root) %{_bindir}/freeciv-manual
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
#{_mandir}/man6/freeciv-manual.6*
%{_iconsdir}/hicolor/*/apps/freeciv-server.png
%{_pixmapsdir}/freeciv-server.png

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

%if %{with gtk2}
%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/freeciv-gtk2
%{_desktopdir}/org.freeciv.gtk2.desktop
%{_datadir}/appdata/freeciv-gtk2.appdata.xml
%{_datadir}/%{name}/freeciv.rc-2.0
%{_datadir}/%{name}/gtk2_menus.xml
%{_datadir}/%{name}/themes/gui-gtk-2.0
%{_mandir}/man6/freeciv-client.6*
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

