Summary: 	An X Window System kernel parameter monitoring tool
Summary(de):	pr�sentiert Balkendiagramme der Systemauslastung 
Summary(fr):	affiche la charge syst�me sous forme d'histogrammes
Summary(pl):	Narz�dzie do monitorowania parametry systemu pod X Window
Summary(tr):	Sistem y�k�n� grafiksel olarak belirtir
Name: 		xsysinfo
Version: 	1.6
Release: 	6
Copyright: 	MIT
Group: 		X11/Utilities
Group(pl):	X11/Narz�dzia
Source0: 	ftp://sunsite.unc.edu/pub/Linux/system/status/xstatus/%{name}-%{version}.tar.gz
Source1:	xsysinfo.desktop
BuildRequires:	XFree86-devel
BuildRoot: 	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description
Xsysinfo is a graphic kernel monitoring tool for the X Window System.
Xsysinfo displays vertical bars for certain kernel parameters:  CPU load
average, CPU load, memory and swap sizes.

%description -l de
Viele Aspekte der Systemleistung k�nnen mit xsysinfo �berwacht werden, u.a.
Netzwerk- und CPU-Auslastung, Festplattenspeicher u. -nutzung, usw. Stellt
�nderungen der Systemleistung leicht erkennbar in einem Fenster dar.

%description -l fr
De nombreux aspects des performances du syst�me peuvent �tre observ�s avec
xsysinfo, dont le trafic sur le r�seau, la charge CPU, l'espace disque,
l'utilisation des disques, et plus encore. Il affiche une historique des
performances dans une fen�tre pour que vous puissiez facilement suivre
l'�volution.

%description -l pl
Xsysinfo jest graficznym narz�dziem pod X Window s�u��cym do monitorowania
r�nych parametr�w pracy systemu jak: obci��enie i �rednie obci��enie
procesora, zaj�to�� pami�ci i partycji swap

%description -l tr
Sistem performans�n� g�steren baz� i�aretler (CPU y�k�, bo� disk alan�,
kullan�m�, a� trafi�i, vs) xsysinfo yard�m�yla g�zlemlenebilir ve bir
pencere i�inde sistemin y�k� zamana ba�l� olarak izlenebilir.

%prep
%setup -q

%build
make clean

xmkmf
make CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Administration

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Administration

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES}.gz
%attr(755,root,root) %{_bindir}/xsysinfo
%config %{_libdir}/X11/app-defaults/XSysinfo
%config %{_libdir}/X11/app-defaults/XSysinfo-color

/usr/X11R6/share/applnk/Administration/xsysinfo.desktop
