#
# Conditional build:
%bcond_without gtk2		# build gtk1 client, not gtk2

Summary:	FREE CIVilization clone
Summary(es):	Clon del juego Civilization
Summary(pl):	Niekomercyjny klon CIVilization
Summary(pt_BR):	Clone do jogo Civilization
Name:		freeciv
Version:	1.14.1
Release:	5
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	ftp://ftp.freeciv.org/freeciv/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	d328f65e7fca5252f27161f5f9e97a03
Source1:	%{name}-client.desktop
Source2:	%{name}-server.desktop
Source3:	%{name}.png
Source4:	ftp://ftp.freeciv.org/freeciv/contrib/sounds/sets/stdsounds1.tar.gz
# Source4-md5:	28a54fbe3ddb67a9b8fe85b8332415e1
Source5:	ftp://ftp.freeciv.org/freeciv/contrib/sounds/sets/stdsounds.spec
# Source5-md5:	6e3e2bc551eb49ca87c4f0085991db15
Patch0:		%{name}-locale_names.patch
URL:		http://www.freeciv.org/
BuildRequires:	SDL_mixer-devel
BuildRequires:	automake
BuildRequires:	esound-devel
%{!?with_gtk2:BuildRequires:	gtk+-devel > 1.2.1}
%{?with_gtk2:BuildRequires:	gtk+2-devel}
%{!?with_gtk2:BuildRequires:	imlib-devel >= 1.9.2}
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
%setup -q -a 4
%patch0 -p1

mv -f po/{no,nb}.po

%build
cp -f %{_datadir}/automake/config.sub .
%configure2_13 \
%{!?with_gtk2:	--enable-client=gtk} \
%{?with_gtk2:	--enable-client=gtk2}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_datadir}/freeciv/Freeciv

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/freeciv/stdsounds.soundspec
cp -ar stdsounds $RPM_BUILD_ROOT%{_datadir}/freeciv

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog NEWS
%{_pixmapsdir}/*
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

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/civclient
%{_desktopdir}/%{name}-client.desktop
%{_datadir}/%{name}/freeciv.rc*
%{_datadir}/%{name}/isotrident
%{_datadir}/%{name}/misc
%{_datadir}/%{name}/stdsounds
%{_datadir}/%{name}/trident
%{_datadir}/%{name}/*.*spec
