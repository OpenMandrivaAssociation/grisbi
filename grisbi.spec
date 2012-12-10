%define	name	grisbi
%define	version	0.8.5
%define	release	1

Name:		%{name}
Summary:	Personal finance manager
Version:	%{version}
Release:	%{release}
License:	GPLv2
Url:		http://www.grisbi.org/
Source0:	http://switch.dl.sourceforge.net/sourceforge/grisbi/%{name}-%{version}.tar.bz2
Group:		Office
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libofx)
BuildRequires:	gettext-devel
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(openssl)
BuildRequires:	intltool

%description
Grisbi helps you to manage your personal finance with Linux.

%prep
%setup -qn %{name}-%{version}

%build
export LIBS="-lm"
%configure2_5x --with-plugins
%make

%install
%makeinstall_std

install -d -m 755 %{buildroot}%{_liconsdir}
install -d -m 755 %{buildroot}%{_iconsdir}
install -d -m 755 %{buildroot}%{_miconsdir}
install -m 644 pixmaps/grisbi.png %{buildroot}%{_liconsdir}/grisbi.png
convert pixmaps/grisbi.png -resize 32x32 %{buildroot}%{_iconsdir}/grisbi.png
convert pixmaps/grisbi.png -resize 16x16 %{buildroot}%{_miconsdir}/grisbi.png

%find_lang %{name}

sed -i 's/grisbi.png/grisbi/' \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README COPYING
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/grisbi
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_mandir}/man1/*
%{_datadir}/mime-info/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/*/*.png


%changelog
* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 0.8.5-1mdv2011.0
+ Revision: 662349
- byebye docs
- br intltool
- new version 0.8.5

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-2mdv2011.0
+ Revision: 610985
- rebuild

* Sat May 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-1mdv2010.1
+ Revision: 546580
- 0.6.0 final version
- drop patches 2 and 3, merged upstream

* Thu Apr 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-0.rc2.5mdv2010.1
+ Revision: 540861
- drop useless dependencies and sources (spotted by P. Biava <pierre.biava@nerim.net>)

* Tue Apr 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-0.rc2.4mdv2010.1
+ Revision: 539859
- fix plugins loading on x86_64  (spotted by P. Biava <pierre.biava@nerim.net>)

* Sun Apr 04 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-0.rc2.3mdv2010.1
+ Revision: 531471
- drop doc location patch, which actually breaks doc retrieval, and install all documentation into a single place

* Mon Mar 22 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-0.rc2.2mdv2010.1
+ Revision: 526670
- rediff and reapply asneeded patch, to fix plugins build

* Sun Jan 31 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.0-0.rc2.1mdv2010.1
+ Revision: 498771
- update to 0.6.0rc2

* Sat Jan 23 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.0-0.rc1.20091229.3mdv2010.1
+ Revision: 495302
- add missing BR
- one .desktop file is enough, wouldn't you say?

* Sat Jan 23 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.0-0.rc1.20091229.2mdv2010.1
+ Revision: 495183
- currently we don't need autoconf in spec

* Sat Jan 23 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.0-0.rc1.20091229.1mdv2010.1
+ Revision: 495176
- add back the grisbi-manuel-0.5.1, no replacement available
- drop tetex* requires as grispi-manuel isn't built (is 0.5.1 docs still useful)
- update to 0.6.0rc1 to fix bug with gtk >= 2.18
- drop patch 0, upstream now uses xdg-open
- clean spec, drop unndeed parts for distros < 2009

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Mar 19 2009 Jérôme Soyer <saispo@mandriva.org> 0.5.9-4mdv2009.1
+ Revision: 357682
- Rebuild for Mandriva 2009.1

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.5.9-3mdv2009.0
+ Revision: 266978
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon May 26 2008 Frederic Crozat <fcrozat@mandriva.com> 0.5.9-2mdv2009.0
+ Revision: 211409
- Patch2: fix build when as-needed is used
- Patch3: fix help path
- Fix buildrequires

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Mar 21 2007 Adam Williamson <awilliamson@mandriva.com> 0.5.9-2mdv2007.1
+ Revision: 147387
- rebuild for new libofx
- spellcheck summary and description

* Wed Nov 22 2006 Jérôme Soyer <saispo@mandriva.org> 0.5.9-1mdv2007.1
+ Revision: 86320
- Fix Specs
- Add BuildRequires Tetex
- New release 0.5.9
- Import grisbi

* Fri Apr 07 2006 Frederic Crozat <fcrozat@mandriva.com> 0.5.8-2mdk
- Patch0: fix web browser name
- Patch1: fix doc build
- package french manual
- Add requires on latex, needed for printing
- fix buildrequires

* Thu Jan 19 2006 Lenny Cartier <lenny@mandriva.com> 0.5.8-1mdk
- 0.5.8

* Thu Nov 24 2005 Lenny Cartier <lenny@mandriva.com> 0.5.7-3mdk
- rebuild

* Tue Aug 09 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.5.7-2mdk
- %%mkrel
- get rid of bizarre stuff
- don't bzip2 icons
- cleanups!

* Fri Jun 10 2005 Lenny Cartier <lenny@mandriva.com> 0.5.7-1mdk
- 0.5.7

* Thu Jan 13 2005 Jerome Soyer <saispo@mandrake.org> 0.5.5-1mdk
- 0.5.5

* Mon Dec 20 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.5.3-2mdk
- rebuild for new ofx

* Thu Dec 02 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5.3-1mdk
- 0.5.3

* Fri Oct 22 2004 Jerome Soyer <saispo@mandrake.org> 0.5.2-1mdk
- 0.5.2
- Update BuildRequires

* Mon Aug 30 2004 Jerome Soyer <saispo@mandrake.org> 0.5.1-3mdk
- fix buildrequires

* Sun Aug 22 2004 Jerome Soyer <saispo@mandrake.org> 0.5.1-2mdk
- fix menu entry

* Thu Aug 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5.1-1mdk
- 0.5.1

* Tue Jul 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5.0-1mdk
- from neoclust <n1c0l4s.l3@wanadoo.fr> : 
	- 0.5.0

* Sat Apr 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.4.5-1mdk
- 0.4.5
- merge with original grisbi spec

