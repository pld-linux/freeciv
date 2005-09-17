#
# Conditional build:
%bcond_without	gtk2		# build gtk1 client, not gtk2
#
Summary:	FREE CIVilization clone
Summary(es):	Clon del juego Civilization
Summary(pl):	Niekomercyjny klon CIVilization
Summary(pt_BR):	Clone do jogo Civilization
Name:		freeciv
Version:	2.0.5
Release:	2
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://dl.sourceforge.net/freeciv/%{name}-%{version}.tar.bz2
# Source0-md5:	cc224a166f914b3404291c6fe997f90a
Source1:	ftp://ftp.freeciv.org/freeciv/contrib/sounds/sets/stdsounds3.tar.gz
# Source1-md5:	77215914712f2f351092918f5e41e39e
Source2:	%{name}-client.desktop
Source3:	%{name}-server.desktop
Source4:	%{name}.png
URL:		http://www.freeciv.org/
BuildRequires:	SDL_mixer-devel
BuildRequires:	automake
BuildRequires:	esound-devel
%{!?with_gtk2:BuildRequires:	gtk+-devel > 1.2.1}
%{?with_gtk2:BuildRequires:	gtk+2-devel}
%{!?with_gtk2:BuildRequires:	imlib-devel >= 1.9.2}
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free clone of Sid Meier's Civilization. Free Civilization clone for
unix and X. This is multiplayer strategic game and you can also play
against computer-AI players.

%description -l es
Clon del juego Civilization.

%description -l pl
Freeciv jest to niekomercyjny (GPL) klon gry Civilization Sida Meiera.
Jest to gra strategiczna dla systemu X Window. Mo¿na graæ w ni± z
innymi osobami poprzez sieæ, a tak¿e przeciwko "graczom" zarz±dzanym
przez komputer.

%description -l pt_BR
O FreeCiv é uma implementação do Civilization II para o Sistema X
Window.

%package client
Summary:	Freeciv game client
Summary(pl):	Klient gry Freeciv
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}
Requires:	SDL_mixer
Requires:	esound
%{!?with_gtk2:Requires:	gtk+ > 1.2.1}
%{!?with_gtk2:Requires:	imlib >= 1.9.2}

%description client
This package contains Freeciv game client.

%description client -l pl
Ten pakiet zawiera klienta gry Freeciv.

%package server
Summary:	Freeciv game server
Summary(pl):	Serwer gry Freeciv
Group:		X11/Applications/Games/Strategy
Requires:	%{name} = %{version}-%{release}

%description server
This package contans Freeciv game server.

%description server -l pl
Ten pakiet zawiera server gry Freeciv.

%prep
%setup -q -a1

%build
cp -f /usr/share/automake/config.sub bootstrap
%configure \
%{!?with_gtk2:	--enable-client=gtk} \
%{?with_gtk2:	--enable-client=gtk2}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

cp -rf data/stdsounds{,.soundspec} $RPM_BUILD_ROOT%{_datadir}/%{name}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/he{_IL,}
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog NEWS
%{_pixmapsdir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/helpdata.txt

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/civserver
%{_desktopdir}/%{name}-server.desktop
%{_datadir}/%{name}/civ1
%{_datadir}/%{name}/civ2
%{_datadir}/%{name}/default
%{_datadir}/%{name}/history
%{_datadir}/%{name}/nation
%{_datadir}/%{name}/scenario
%{_datadir}/%{name}/*.serv
%{_mandir}/man6/civserver.6*

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/civclient
%attr(755,root,root) %{_bindir}/civmanual
%{_desktopdir}/%{name}-client.desktop
%{_datadir}/%{name}/freeciv.rc*
%{_datadir}/%{name}/isotrident
%{_datadir}/%{name}/misc
%{_datadir}/%{name}/trident
%{_datadir}/%{name}/isophex
%{_datadir}/%{name}/flags
%{_datadir}/%{name}/*.*spec
%{_datadir}/%{name}/stdsounds
%{_mandir}/man6/civclient.6*
