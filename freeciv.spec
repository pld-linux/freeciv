Summary:	FREE CIVilization clone
Summary(pl):	Niekomercyjny klon CIVilization
Name:		freeciv
Version:	1.8.0
Release:	2
Copyright:	GPL
Group:		X11/Games/Strategy
Group(pl):	X11/Gry/Strategiczne
Source0:	ftp://freeciv.ultraviolet.org/pub/freeciv/%{name}-%{version}.tar.bz2
Source1:	freeciv-client.wmconfig
Source2:	freeciv-server.wmconfig
URL:		http://www.freeciv.org/
BuildPrereq:	Xaw3d-devel
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
Buildroot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
Free clone of Sid Meiers Civilization. Free Civilization clone for unix and
X. This is multiplayer strategic game and you can also play against
computer-AI players.

%description -l pl
Freeciv jest to niekomercyjny (GPL) klon gry Civilization Sid'a Meiers'a.
Jest to gra strategiczna pod X Window. Mo¿esz graæ w ni± z innymi osobami
poprzez sieæ, a tak¿e przeciwko "graczom" zarz±dzanym przez komputer.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-xaw3d
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/X11/wmconfig,%{_libdir}/X11/app-defaults}

make install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/freeciv/Freeciv \
$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/freeciv-client
install %{SOURCE2} $RPM_BUILD_ROOT/etc/X11/wmconfig/freeciv-server

gzip -9nf AUTHORS README freeciv_hackers_guide.txt HOWTOPLAY NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
/etc/X11/wmconfig/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/freeciv
%{_libdir}/X11/app-defaults/Freeciv
