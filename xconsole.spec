Name: xconsole
Version: 1.0.5
Release: %mkrel 4
Summary: Monitor system console messages with X
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
The xconsole program displays messages which are usually sent to /dev/console.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xconsole
%{_datadir}/X11/app-defaults/XConsole
%{_mandir}/man1/xconsole.*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2011.0
+ Revision: 671286
- mass rebuild

* Fri Sep 24 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 580824
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-5mdv2010.1
+ Revision: 524387
- rebuilt for 2010.1

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.3-4mdv2009.1
+ Revision: 366631
- no more autoconf needed

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-3mdv2009.0
+ Revision: 226023
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 155928
- Updated BuildRequires and resubmit package.
- Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2008.0
+ Revision: 68275
- new release
- standard summary
- do not hardcode man page extension


* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 20:53:38 (59462)
- rebuild to fix libXaw.so.8 dependency

* Thu Jun 01 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-06-01 20:13:15 (31864)
- fill in missing description & summaries

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

