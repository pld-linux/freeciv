#
# Conditional build:
#  _with_gtk2		build gtk2 client, not gtk
#
Summary:	FREE CIVilization clone
Summary(es):	Clon del juego Civilization
Summary(pl):	Niekomercyjny klon CIVilization
Summary(pt_BR):	Clone do jogo Civilization
Name:		freeciv
Version:	1.14.0
Release:	1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	ftp://ftp.freeciv.org/freeciv/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	c506ec29b94ea516aaa02a107129cf10
Source1:	%{name}-client.desktop
Source2:	%{name}-server.desktop
Source3:	%{name}.png
Source4:	ftp://ftp.freeciv.org/freeciv/contrib/sounds/sets/stdsounds1.tar.gz
# Source4-md5:	28a54fbe3ddb67a9b8fe85b8332415e1
Source5:	ftp://ftp.freeciv.org/freeciv/contrib/sounds/sets/stdsounds.spec
# Source5-md5:	6e3e2bc551eb49ca87c4f0085991db15
URL:		http://www.freeciv.org/
BuildRequires:	esound-devel
%{!?_with_gtk2:BuildRequires:	gtk+-devel > 1.2.1}
%{?_with_gtk2:BuildRequires:	gtk+2-devel}
%{!?_with_gtk2:BuildRequires:	imlib-devel >= 1.9.2}
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRequires:	SDL_mixer-devel
Requires:	esound
Requires:	SDL_mixer
%{!?_with_gtk2:Requires:	gtk+ > 1.2.1}
%{?_with_gtk2:Requires:		gtk+2}
%{!?_with_gtk2:Requires:	imlib >= 1.9.2}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free clone of Sid Meiers Civilization. Free Civilization clone for
unix and X. This is multiplayer strategic game and you can also play
against computer-AI players.

%description -l es
Clon del juego Civilization.

%description -l pl
Freeciv jest to niekomercyjny (GPL) klon gry Civilization Sid'a
Meiers'a. Jest to gra strategiczna pod X Window. Mo¿esz graæ w ni± z
innymi osobami poprzez sieæ, a tak¿e przeciwko "graczom" zarz±dzanym
przez komputer.

%description -l pt_BR
O FreeCiv é uma implementação do Civilization II para o Sistema X
Window.

%prep
%setup -q -a 4

%build
%configure2_13 \
%{!?_with_gtk2:	--enable-client=gtk} \
%{?_with_gtk2:	--enable-client=gtk2}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults \
	$RPM_BUILD_ROOT{%{_applnkdir}/Games/Strategy,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_datadir}/freeciv/Freeciv

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games/Strategy
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/freeciv/stdsounds.soundspec
cp -ar stdsounds $RPM_BUILD_ROOT%{_datadir}/freeciv

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/freeciv
%{_applnkdir}/Games/Strategy/*
%{_pixmapsdir}/*
