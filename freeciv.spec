#
%define		beta	beta2

Summary:	FREE CIVilization clone
Summary(es):	Clon del juego Civilization
Summary(pl):	Niekomercyjny klon CIVilization
Summary(pt_BR):	Clone do jogo Civilization
Name:		freeciv
Version:	2.1.0
Release:	0.%{beta}.1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	ftp://ftp.freeciv.org/freeciv/beta/%{name}-%{version}-%{beta}.tar.bz2
# Source0-md5:	8f8d7f9840d89ea850f907a54fa32f14
Source1:	%{name}-client.desktop
Source2:	%{name}-server.desktop
Source3:	%{name}.png
Source4:	ftp://ftp.freeciv.org/freeciv/contrib/sounds/sets/stdsounds3.tar.gz
# Source4-md5:	77215914712f2f351092918f5e41e39e
Source5:	ftp://ftp.freeciv.org/pub/freeciv/contrib/tilesets/freeland2/freeland-normal-2.0.0.tar.gz
# Source5-md5:	c9f061fca82aa50a19fbbc89c06ff81d
Patch0:		%{name}-locale_names.patch
URL:		http://www.freeciv.org/
BuildRequires:	SDL_mixer-devel
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gtk+2-devel
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
%setup -q -a 4 -a 5 -n %{name}-%{version}-%{beta}

%build
cp -f %{_datadir}/automake/config.sub bootstrap
%configure2_13 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
cp -f freeland.tilespec $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rf freeland $RPM_BUILD_ROOT%{_datadir}/%{name}

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
%{_datadir}/%{name}/nation
%{_datadir}/%{name}/scenario
%{_datadir}/%{name}/*.serv
%{_mandir}/man6/civserver.6*

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/civclient
%attr(755,root,root) %{_bindir}/civmanual
%{_desktopdir}/%{name}-client.desktop
%{_datadir}/%{name}/amplio
%{_datadir}/%{name}/freeciv.rc*
%{_datadir}/%{name}/freeland
%{_datadir}/%{name}/isophex
%{_datadir}/%{name}/isotrident
%{_datadir}/%{name}/misc
%{_datadir}/%{name}/stdsounds
%{_datadir}/%{name}/trident
%{_datadir}/%{name}/flags
%{_datadir}/%{name}/*.*spec
%{_mandir}/man6/civclient.6*
