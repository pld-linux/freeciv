#
# Conditional build:
%bcond_without	gtk		# do not build gtk client
%bcond_without  ggz_client	# build without ggz client
%bcond_without  ggz_server	# build without ggz server
#
%define		_beta	beta1
Summary:	FREE CIVilization clone
Summary(es.UTF-8):	Clon del juego Civilization
Summary(pl.UTF-8):	Niekomercyjny klon CIVilization
Summary(pt_BR.UTF-8):	Clone do jogo Civilization
Name:		freeciv
Version:	2.3.0
Release:	0.%{_beta}.1
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	http://downloads.sourceforge.net/freeciv/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	3d12e271887798be324f7f4b696b3cad
# NOTE: current version of freeland tiles does not work with newest freeciv version
#Source1:	http://download.gna.org/freeciv/contrib/tilesets/freeland/freeland-normal-2.0.0.tar.gz
Patch0:		%{name}-link.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-ggz.patch
URL:		http://freeciv.wikia.com/
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
%{?with_ggz_client:BuildRequires:	ggz-gtk-client-devel}
%{?with_gtk:BuildRequires:	gtk+2-devel}
BuildRequires:	libggz-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
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
Summary:	Freeciv game client
Summary(pl.UTF-8):	Klient gry Freeciv
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}
Requires:	SDL_mixer
Suggests:	%{name}-server = %{version}-%{release}

%description client
This package contains Freeciv game client.

%description client -l pl.UTF-8
Ten pakiet zawiera klienta gry Freeciv.

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
%setup -q -n %{name}-%{version}-%{_beta}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-ggzd-confdir=%{_sysconfdir}/ggzd \
	%{?with_gtk:--enable-client=gtk} \
	%{!?with_ggz_client:--without-ggz-client} \
	%{!?with_ggz_server:--without-ggz-server}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a client/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}/%{name}-client.desktop
cp -a server/%{name}-server.desktop $RPM_BUILD_ROOT%{_desktopdir}
%{__rm} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

cp -a data/icons/32x32/*.png $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a data/stdsounds{,.soundspec} $RPM_BUILD_ROOT%{_datadir}/%{name}
#cp -a freeland.tilespec $RPM_BUILD_ROOT%{_datadir}/%{name}
#cp -a freeland $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/no
%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/ggz.modules

%{?with_gtk:cp -a data/gtk_menus.xml $RPM_BUILD_ROOT%{_datadir}/%{name}}

%if %{with ggz_server}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/ggzd/{games,rooms}
cp -a data/civserver.dsc $RPM_BUILD_ROOT%{_sysconfdir}/ggzd/games/civserver.dsc
cp -a data/civserver.room $RPM_BUILD_ROOT%{_sysconfdir}/ggzd/rooms/civserver.room
%endif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog NEWS
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/helpdata.txt

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/freeciv-server
%{_desktopdir}/%{name}-server.desktop
%{_datadir}/%{name}/civ1
%{_datadir}/%{name}/civ2
%{_datadir}/%{name}/default
%{_datadir}/%{name}/experimental
%{_datadir}/%{name}/multiplayer
%{_datadir}/%{name}/nation
%{_datadir}/%{name}/scenario
%{_datadir}/%{name}/*.serv
%{_mandir}/man6/freeciv-server.6*
%{_iconsdir}/hicolor/*/apps/freeciv-server.png
%{_pixmapsdir}/freeciv-server.png

%if %{with ggz_server}
%dir %{_sysconfdir}/ggzd
%dir %{_sysconfdir}/ggzd/games
%dir %{_sysconfdir}/ggzd/rooms
%{_sysconfdir}/ggzd/games/civserver.dsc
%{_sysconfdir}/ggzd/rooms/civserver.room
%endif

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/freeciv-gtk2
%attr(755,root,root) %{_bindir}/freeciv-manual
%attr(755,root,root) %{_bindir}/freeciv-modpack
%{_desktopdir}/%{name}-client.desktop
%{_datadir}/%{name}/*.*spec
%{_datadir}/%{name}/amplio2
%{_datadir}/%{name}/buildings
%{_datadir}/%{name}/flags
%{_datadir}/%{name}/freeciv.rc*
#%%{_datadir}/%{name}/freeland
%{?with_gtk:%{_datadir}/%{name}/gtk_menus.xml}
%{_datadir}/%{name}/hex2t
%{_datadir}/%{name}/isophex
%{_datadir}/%{name}/isotrident
%{_datadir}/%{name}/misc
%{_datadir}/%{name}/stdsounds
%{_datadir}/%{name}/themes
%{_datadir}/%{name}/trident
%{_datadir}/%{name}/wonders
%{_mandir}/man6/freeciv-client.6*
%{_mandir}/man6/freeciv-ftwl.6*
%{_mandir}/man6/freeciv-gtk2.6*
%{_mandir}/man6/freeciv-sdl.6*
%{_mandir}/man6/freeciv-win32.6*
%{_mandir}/man6/freeciv-xaw.6*
%{_iconsdir}/hicolor/*/apps/freeciv-client.png
%{_pixmapsdir}/freeciv-client.png
