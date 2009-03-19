%define Werror_cflags %nil

%define	name	grisbi
%define	version	0.5.9
%define	release	%mkrel 4


Summary:	Personal finance manager
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Url:		http://www.grisbi.org/
Source0:	http://switch.dl.sourceforge.net/sourceforge/grisbi/%{name}-%{version}.tar.bz2
Source1:	grisbi-manuel-0.5.1.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
# (fc) 0.5.8-2mdk fix browser name
Patch0:		grisbi-0.5.8-browser.patch
# (fc) 0.5.8-2mdk fix doc build
Patch1:		grisbi-0.5.8-fixbuild.patch
# (fc) 0.5.9-2mdv fix build when as-needed is enabled
Patch2:		grisbi-0.5.9-asneeded.patch
# (fc) 0.5.9-2mdv fix help path
Patch3:		grisbi-0.5.9-helppath.patch

Group:		Office
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgnomeui2-devel libgdk_pixbuf2.0-devel libgnomeprint-devel
BuildRequires:	imagemagick gtk2-devel libofx-devel hevea
BuildRequires:	gettext-devel
Requires: tetex-latex
Requires: tetex-dvips

%description
Grisbi helps you to manage your personal finances with Linux.

%prep
%setup -q -a 1
%patch0 -p1 -b .browser
%patch1 -p1 -b .fixbuild
%patch2 -p1 -b .asneeded
%patch3 -p1 -b .helppath

# needed by patches 1, 2 & 3
cp -f %{_datadir}/gettext/config.rpath .
aclocal -I macros
automake --add-missing
autoconf

%build
%configure2_5x
%make

make -C grisbi-manuel-0.5.1/src html_img

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p  $RPM_BUILD_ROOT%{_datadir}/grisbi/help/fr/

cp -f -r grisbi-manuel-0.5.1/src/fr/* $RPM_BUILD_ROOT%{_datadir}/grisbi/help/fr/
cp -f -r grisbi-manuel-0.5.1/src/image $RPM_BUILD_ROOT%{_datadir}/grisbi/help/

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Grisbi
Comment=Personnal finances manager
Exec=%{name}
Icon=office_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Finances;Office;Finance;
EOF

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%endif


%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc AUTHORS NEWS README
%{_bindir}/*
%dir %{_datadir}/grisbi
%dir %{_datadir}/grisbi/help
%lang(fr) %{_datadir}/grisbi/help/fr
%{_datadir}/grisbi/help/image
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_mandir}/man1/*
%{_datadir}/mime-info/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
