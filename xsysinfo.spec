Summary: An X Window System kernel parameter monitoring tool.
Name: xsysinfo
Version: 1.6
Release: 5
Copyright: MIT
Group: Applications/System
Source: ftp://sunsite.unc.edu/pub/Linux/system/status/xstatus/xsysinfo-1.6.tar.gz
BuildRoot: /var/tmp/xsysinfo-root

%description
Xsysinfo is a graphic kernel monitoring tool for the X Window System.
Xsysinfo displays vertical bars for certain kernel parameters:  CPU load
average, CPU load, memory and swap sizes.

Install the xsysinfo package if you'd like to use a graphical kernel
monitoring tool.

%prep
%setup -q
make clean

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xsysinfo <<EOF
xsysinfo name "xsysinfo"
xsysinfo description "System Information"
xsysinfo group Administration
xsysinfo exec "xsysinfo &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/X11R6/bin/xsysinfo
%config /usr/X11R6/lib/X11/app-defaults/XSysinfo
%config /usr/X11R6/lib/X11/app-defaults/XSysinfo-color
%config /etc/X11/wmconfig/xsysinfo
