Summary:	An X Window System kernel parameter monitoring tool
Summary(de):	pr�sentiert Balkendiagramme der Systemauslastung
Summary(es):	Ense�a la carga del sistema con gr�fico de barras
Summary(fr):	affiche la charge syst�me sous forme d'histogrammes
Summary(pl):	Narz�dzie do monitorowania parametr�w systemu pod X Window
Summary(pt_BR):	Mostra a carga do sistema com gr�fico de barras
Summary(ru):	��������� ����������� ��������� ��������
Summary(tr):	Sistem y�k�n� grafiksel olarak belirtir
Summary(uk):	�������� ��Φ������� ���������� ������������
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
Viele Aspekte der Systemleistung k�nnen mit xsysinfo �berwacht werden,
u.a. Netzwerk- und CPU-Auslastung, Festplattenspeicher u. -nutzung,
usw. Stellt �nderungen der Systemleistung leicht erkennbar in einem
Fenster dar.

%description -l es
Varios aspectos del desempe�o del sistema pueden ser monitorados con
xsysinfo, incluyendo tr�fico de red, carga de la CPU, espacio en
disco, uso de disco, y m�s. Ense�a tambi�n un hist�rico del desempe�o
en una ventana para que puedas ver los cambios f�cilmente.

%description -l fr
De nombreux aspects des performances du syst�me peuvent �tre observ�s
avec xsysinfo, dont le trafic sur le r�seau, la charge CPU, l'espace
disque, l'utilisation des disques, et plus encore. Il affiche une
historique des performances dans une fen�tre pour que vous puissiez
facilement suivre l'�volution.

%description -l pl
Xsysinfo jest graficznym narz�dziem pod X Window s�u��cym do
monitorowania r�nych parametr�w pracy systemu jak: obci��enie i
�rednie obci��enie procesora, zaj�to�� pami�ci i partycji swap.

%description -l pt_BR
V�rios aspectos da performance do sistema podem ser monitorados com o
xsysinfo, incluindo tr�fego de rede, carga da CPU, espa�o em disco,
uso de disco, e mais. Mostra tamb�m um hist�rico da performance em uma
janela para que voc� possa ver as mudan�as facilmente.

%description -l ru
��������� xsysinfo ����� ���������� ������ ������� ������������������
�������, ������� ������� �������, �������� ����������, ����� �� �����,
������������� ����� � ������ ������. ���������� ������� ��������� �
����, ��� ��� ����� ����� ��������� ���������.

%description -l tr
Sistem performans�n� g�steren baz� i�aretler (CPU y�k�, bo� disk
alan�, kullan�m�, a� trafi�i, vs) xsysinfo yard�m�yla g�zlemlenebilir
ve bir pencere i�inde sistemin y�k� zamana ba�l� olarak izlenebilir.

%description -l uk
�� ��������� xsysinfo ����� צ��̦��������� ������ �������Ҧ�
����æ�������� �������, ��������� ��������� ���Ʀ�, ������������
���������, ͦ��� �� ����� �� ����.

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
