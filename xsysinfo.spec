Summary:	An X Window System kernel parameter monitoring tool
Summary(de.UTF-8):	präsentiert Balkendiagramme der Systemauslastung
Summary(es.UTF-8):	Enseña la carga del sistema con gráfico de barras
Summary(fr.UTF-8):	affiche la charge système sous forme d'histogrammes
Summary(pl.UTF-8):	Narzędzie do monitorowania parametrów systemu pod X Window
Summary(pt_BR.UTF-8):	Mostra a carga do sistema com gráfico de barras
Summary(ru.UTF-8):	Программа мониторинга системной загрузки
Summary(tr.UTF-8):	Sistem yükünü grafiksel olarak belirtir
Summary(uk.UTF-8):	Програма моніторингу системного завантаження
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
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
Xsysinfo is a graphic kernel monitoring tool for the X Window System.
Xsysinfo displays vertical bars for certain kernel parameters: CPU
load average, CPU load, memory and swap sizes.

%description -l de.UTF-8
Viele Aspekte der Systemleistung können mit xsysinfo überwacht werden,
u.a. Netzwerk- und CPU-Auslastung, Festplattenspeicher u. -nutzung,
usw. Stellt Änderungen der Systemleistung leicht erkennbar in einem
Fenster dar.

%description -l es.UTF-8
Varios aspectos del desempeño del sistema pueden ser monitorados con
xsysinfo, incluyendo tráfico de red, carga de la CPU, espacio en
disco, uso de disco, y más. Enseña también un histórico del desempeño
en una ventana para que puedas ver los cambios fácilmente.

%description -l fr.UTF-8
De nombreux aspects des performances du système peuvent être observés
avec xsysinfo, dont le trafic sur le réseau, la charge CPU, l'espace
disque, l'utilisation des disques, et plus encore. Il affiche une
historique des performances dans une fenêtre pour que vous puissiez
facilement suivre l'évolution.

%description -l pl.UTF-8
Xsysinfo jest graficznym narzędziem pod X Window służącym do
monitorowania różnych parametrów pracy systemu jak: obciążenie i
średnie obciążenie procesora, zajętość pamięci i partycji swap.

%description -l pt_BR.UTF-8
Vários aspectos da performance do sistema podem ser monitorados com o
xsysinfo, incluindo tráfego de rede, carga da CPU, espaço em disco,
uso de disco, e mais. Mostra também um histórico da performance em uma
janela para que você possa ver as mudanças facilmente.

%description -l ru.UTF-8
Используя xsysinfo можно мониторить многие аспекты производительности
системы, включая сетевой траффик, загрузку процессора, место на диске,
использование диска и многое другое. Показывает историю изменений в
окне, так что можно легко отследить изменения.

%description -l tr.UTF-8
Sistem performansını gösteren bazı işaretler (CPU yükü, boş disk
alanı, kullanımı, ağ trafiği, vs) xsysinfo yardımıyla gözlemlenebilir
ve bir pencere içinde sistemin yükü zamana bağlı olarak izlenebilir.

%description -l uk.UTF-8
За допомогою xsysinfo можна відслідковувати багато параметрів
функціонування системи, включаючи мережевий трафік, завантаження
процесора, місце на диску та інше.

%prep
%setup -q
%patch0 -p1

%build
%{__make} clean

#xmkmf
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/xsysinfo
%{_appdefsdir}/XSysinfo
%{_appdefsdir}/XSysinfo-color
%{_desktopdir}/xsysinfo.desktop
%{_pixmapsdir}/*
