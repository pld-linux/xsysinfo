Summary: 	An X Window System kernel parameter monitoring tool
Summary(pl):	Narzêdzie monitoruj±ce parametry systemu dla X Window System
Name: 		xsysinfo
Version: 	1.6
Release: 	6
Copyright: 	MIT
Group: 		X11/Utilities
Group(pl):	X11/Narzêdzia
Source0: 	ftp://sunsite.unc.edu/pub/Linux/system/status/xstatus/%{name}-%{version}.tar.gz
Source1:	xsysinfo.desktop
BuildRequires:	XFree86-devel
BuildRoot: 	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description
Xsysinfo is a graphic kernel monitoring tool for the X Window System.
Xsysinfo displays vertical bars for certain kernel parameters:  CPU load
average, CPU load, memory and swap sizes.

%description -l pl
Xsysinfo jest graficznym narzêdziem dla X Window System, monitoruj±cym
parametry systemu: obci±¿enie i ¶rednie obci±¿enie procesora, wielko¶æ
pamiêci i partycji swap, i wy¶wietlaj±cym je w postaci s³upków.

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
