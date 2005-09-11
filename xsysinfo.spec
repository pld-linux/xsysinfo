Summary:	An X Window System kernel parameter monitoring tool
Summary(de):	prДsentiert Balkendiagramme der Systemauslastung
Summary(es):	EnseЯa la carga del sistema con grАfico de barras
Summary(fr):	affiche la charge systХme sous forme d'histogrammes
Summary(pl):	NarzЙdzie do monitorowania parametrСw systemu pod X Window
Summary(pt_BR):	Mostra a carga do sistema com grАfico de barras
Summary(ru):	Программа мониторинга системной загрузки
Summary(tr):	Sistem yЭkЭnЭ grafiksel olarak belirtir
Summary(uk):	Програма мон╕торингу системного завантаження
Name:		xsysinfo
Version:	1.7
Release:	6
License:	MIT
Group:		X11/Applications
#Source0:	ftp://sunsite.unc.edu/pub/Linux/system/status/xstatus/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	1a2dab686d087923d8e19b2c2ba8d183
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-leak.patch
Icon:		xsysinfo.xpm
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
	
%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults
%define		_xbindir	/usr/X11R6/bin

%description
Xsysinfo is a graphic kernel monitoring tool for the X Window System.
Xsysinfo displays vertical bars for certain kernel parameters: CPU
load average, CPU load, memory and swap sizes.

%description -l de
Viele Aspekte der Systemleistung kЖnnen mit xsysinfo Эberwacht werden,
u.a. Netzwerk- und CPU-Auslastung, Festplattenspeicher u. -nutzung,
usw. Stellt дnderungen der Systemleistung leicht erkennbar in einem
Fenster dar.

%description -l es
Varios aspectos del desempeЯo del sistema pueden ser monitorados con
xsysinfo, incluyendo trАfico de red, carga de la CPU, espacio en
disco, uso de disco, y mАs. EnseЯa tambiИn un histСrico del desempeЯo
en una ventana para que puedas ver los cambios fАcilmente.

%description -l fr
De nombreux aspects des performances du systХme peuvent Йtre observИs
avec xsysinfo, dont le trafic sur le rИseau, la charge CPU, l'espace
disque, l'utilisation des disques, et plus encore. Il affiche une
historique des performances dans une fenЙtre pour que vous puissiez
facilement suivre l'Иvolution.

%description -l pl
Xsysinfo jest graficznym narzЙdziem pod X Window sЁu©╠cym do
monitorowania rС©nych parametrСw pracy systemu jak: obci╠©enie i
╤rednie obci╠©enie procesora, zajЙto╤Ф pamiЙci i partycji swap.

%description -l pt_BR
VАrios aspectos da performance do sistema podem ser monitorados com o
xsysinfo, incluindo trАfego de rede, carga da CPU, espaГo em disco,
uso de disco, e mais. Mostra tambИm um histСrico da performance em uma
janela para que vocЙ possa ver as mudanГas facilmente.

%description -l ru
Используя xsysinfo можно мониторить многие аспекты производительности
системы, включая сетевой траффик, загрузку процессора, место на диске,
использование диска и многое другое. Показывает историю изменений в
окне, так что можно легко отследить изменения.

%description -l tr
Sistem performansЩnЩ gЖsteren bazЩ iЧaretler (CPU yЭkЭ, boЧ disk
alanЩ, kullanЩmЩ, aП trafiПi, vs) xsysinfo yardЩmЩyla gЖzlemlenebilir
ve bir pencere iГinde sistemin yЭkЭ zamana baПlЩ olarak izlenebilir.

%description -l uk
За допомогою xsysinfo можна в╕дсл╕дковувати багато параметр╕в
функц╕онування системи, включаючи мережевий траф╕к, завантаження
процесора, м╕сце на диску та ╕нше.

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
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_xbindir}/xsysinfo
%config %{_appdefsdir}/XSysinfo
%config %{_appdefsdir}/XSysinfo-color
%{_desktopdir}/xsysinfo.desktop
%{_pixmapsdir}/*
