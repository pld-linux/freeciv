Summary:	FREE CIVilization clone
Summary(pl):	Niekomercyjny klon CIVilization
Name:		freeciv
Version:	1.10.0
Release:	1
License:	GPL
Group:		X11/Games/Strategy
Group(pl):	X11/Gry/Strategiczne
Source0:	ftp://ftp.freeciv.org/pub/freeciv/stable_version/%{name}-%{version}.tar.bz2
Source1:	freeciv-client.desktop
Source2:	freeciv-server.desktop
URL:		http://www.freeciv.org/
Icon:		freeciv.gif
BuildRequires:	gtk+-devel > 1.2.1
BuildRequires:	imlib-devel >= 1.9.2
BuildRequires:	XFree86-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-gtk
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults \
	$RPM_BUILD_ROOT{%{_applnkdir}/Games/Strategy,%{_datadir}/pixmaps}

make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_datadir}/freeciv/Freeciv

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applnk/Games/Strategy
install $RPM_SOURCE_DIR/%{icon} $RPM_BUILD_ROOT%{_datadir}/pixmaps

gzip -9nf AUTHORS README freeciv_hackers_guide.txt HOWTOPLAY NEWS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/freeciv
%{_datadir}/applnk/Games/Strategy/*
%{_datadir}/pixmaps/*
