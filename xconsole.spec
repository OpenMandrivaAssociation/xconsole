Name:		xconsole
Version:	1.0.8
Release:	2
Summary:	Monitor system console messages with X
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(xt)
BuildRequires:	xaw-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

%description
The xconsole program displays messages which are usually sent to /dev/console.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xconsole
%{_datadir}/X11/app-defaults/XConsole
%{_mandir}/man1/xconsole.*
