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
BuildPrereq:	Xaw3d-devel
BuildPrereq:	XFree86-devel
URL:		http://www.freeciv.org/
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
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=%{_prefix} \
	--with-xaw3d
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/X11/wmconfig,%{_libdir}/X11/app-defaults}

make install prefix=$RPM_BUILD_ROOT%{_prefix}

mv $RPM_BUILD_ROOT%{_datadir}/freeciv/Freeciv \
$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/freeciv-client
install %{SOURCE2} $RPM_BUILD_ROOT/etc/X11/wmconfig/freeciv-server

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS README freeciv_hackers_guide.txt
%doc HOWTOPLAY NEWS 
/etc/X11/wmconfig/*
%attr(755, root, root) %{_bindir}/*
%{_datadir}/freeciv
%{_libdir}/X11/app-defaults/Freeciv

%changelog
* Mon May 31 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.8.0-2]
- spec writed by PLD team (based on my old spec for freeciv).
