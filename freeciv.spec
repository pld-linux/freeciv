Summary:     FREE CIVilization clone
Summary(pl): Nie komercyjny klon CIVilization
Name:        freeciv
Version:     1.7.1
Release:     1
Copyright:   GPL
Source0:     ftp://freeciv.ultraviolet.org/pub/freeciv/%{name}-%{version}.tar.bz2
Source1:     freeciv-client.wmconfig
Source2:     freeciv-server.wmconfig
Patch0:      freeciv-cfg.patch
URL:         http://www.freeciv.org/
Icon:        %{name}.gif
Group:       X11/Games/Strategy
Buildroot:   /tmp/%{name}-%{version}-root
%description
Free clone of Sid Meiers Civilization. Free Civilization clone for unix and
X. This is multiplayer strategic game and you can also play against
computer-AI players.

%description -l pl
Freeciv jest to nie komercyjny (GPL) klon gry Civilization Sid'a Meiers'a.
Jest to gra strategiczna pod X Window. Mo¿esz graæ w ni± z innymi osobami
poprzez sieæ, a tak¿e przeciwko "graczom" zarz±dzanym przez komputer.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/lib/X11/app-defaults}

make install prefix=$RPM_BUILD_ROOT/usr/X11R6

strip $RPM_BUILD_ROOT/usr/X11R6/bin/*

mv $RPM_BUILD_ROOT/usr/X11R6/share/freeciv/Freeciv \
$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/freeciv-client
install %{SOURCE2} $RPM_BUILD_ROOT/etc/X11/wmconfig/freeciv-server

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog README CREDITS freeciv_hackers_guide.txt
%doc HOWTOPLAY
%config(missingok) /etc/X11/wmconfig/*
%attr(755, root, root) /usr/X11R6/bin/*
%dir /usr/X11R6/share/freeciv
/usr/X11R6/share/freeciv/*
/usr/X11R6/lib/X11/app-defaults/Freeciv

%changelog
* Sat Aug 22 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7.0-2]
- removed CHANGES from %doc,
- fixed some bugs in pl translation.

* Thu Aug  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7.0-1]
- added -q %setup parameter,
- added pl translation,
- updated URL and %description (now ypu can play against AI players).

* Sun Jun  7 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.6.2-1]
- adde AUTHORS, ChangeLog, freeciv_hackers_guide.txt, HOWTOPLAY, ChangeLog
  to %doc,
- added use %{SOURCE#} in %install,
- fixed typo in wmconfig file for freeciv srv console,
- wmconfig entries for freeciv, freeciv srv console moved to Games/Strategy,
- added all modification for building freeciv with using GNU autoconf.

* Mon May 11 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.4-2]
- changed Source url,
- now freeciv is builded from tar.bz2,
- added temporary hack (Source2 field) rpm 2.4.109 bug wihch can't include
  Icon file in src.rpm.

* Fri May  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.4-1]
- added title in xterm with FC server console in wmconfig registration file,
- %%{version} macro instead %%{PACKAGE_VERSION},
- added using %%{name} macro in Buildroot,
- added -q parametr for %setup.

* Sun Apr 26 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.3-1]
- added %clean section,
- added using %defattr macro (require rpm >= 2.4.99),
- updated URL,
- added wmconfig registration file for freeciv client and server console,
- all data moved to /usr/X11R6/share/freeciv,
- removed Packager field from spec (if you want recompile package and
  redistribute this package later put this in your private .rpmrc).
- changed %build procedure (using xmkmf),
- added CDEBUGFLAGS="$RPM_OPT_FLAGS" make option.

* Sun Sep 21 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0k-1]
- changed %attr on %doc to (-, root,root)

* Sat Aug  9 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0j-1]
- new version 1.0j,
- all rewritetd for using Buildroot,
- added:
  - URL,
  - %attr macros in %file (allow build package from non root account).
