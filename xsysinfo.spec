Summary:	An X Window System kernel parameter monitoring tool
Summary(de):	präsentiert Balkendiagramme der Systemauslastung
Summary(fr):	affiche la charge système sous forme d'histogrammes
Summary(pl):	Narzêdzie do monitorowania parametrów systemu pod X Window
Summary(tr):	Sistem yükünü grafiksel olarak belirtir
Name:		xsysinfo
Version:	1.7
Release:	4
License:	MIT
Group:		X11/Applications
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/status/xstatus/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-leak.patch
Icon:		xsysinfo.xpm
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Xsysinfo is a graphic kernel monitoring tool for the X Window System.
Xsysinfo displays vertical bars for certain kernel parameters: CPU
load average, CPU load, memory and swap sizes.

%description -l de
Viele Aspekte der Systemleistung können mit xsysinfo überwacht werden,
u.a. Netzwerk- und CPU-Auslastung, Festplattenspeicher u. -nutzung,
usw. Stellt Änderungen der Systemleistung leicht erkennbar in einem
Fenster dar.

%description -l fr
De nombreux aspects des performances du système peuvent être observés
avec xsysinfo, dont le trafic sur le réseau, la charge CPU, l'espace
disque, l'utilisation des disques, et plus encore. Il affiche une
historique des performances dans une fenêtre pour que vous puissiez
facilement suivre l'évolution.

%description -l pl
Xsysinfo jest graficznym narzêdziem pod X Window s³u¿±cym do
monitorowania ró¿nych parametrów pracy systemu jak: obci±¿enie i
¶rednie obci±¿enie procesora, zajêto¶æ pamiêci i partycji swap.

%description -l tr
Sistem performansýný gösteren bazý iþaretler (CPU yükü, boþ disk
alaný, kullanýmý, að trafiði, vs) xsysinfo yardýmýyla gözlemlenebilir
ve bir pencere içinde sistemin yükü zamana baðlý olarak izlenebilir.

%prep
%setup -q
%patch0 -p1

%build
%{__make} clean

#xmkmf
%{__make} CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/System,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/System
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/xsysinfo
%config %{_libdir}/X11/app-defaults/XSysinfo
%config %{_libdir}/X11/app-defaults/XSysinfo-color
%{_applnkdir}/System/xsysinfo.desktop
%{_pixmapsdir}/*
