Name: xconsole
Version: 1.0.3
Release: %mkrel 2
Summary: Monitor system console messages with X
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libxaw-devel	>= 1.0.4

%description
The xconsole program displays messages which are usually sent to /dev/console.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -ifs
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xconsole
%{_datadir}/X11/app-defaults/XConsole
%{_mandir}/man1/xconsole.*
