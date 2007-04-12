%define	name	grisbi
%define	version	0.5.9
%define	release	%mkrel 2


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

Group:		Office
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgnomeui2-devel libgdk_pixbuf2.0-devel libgnomeprint-devel
BuildRequires:	ImageMagick gtk2-devel libofx-devel hevea
Requires: tetex-latex
Requires: tetex-dvips

%description
Grisbi helps you to manage your personal finances with Linux.

%prep
%setup -q -a 1
%patch0 -p1 -b .browser
%patch1 -p1 -b .fixbuild

%build
%configure2_5x
%make

make -C grisbi-manuel-0.5.1/src html_img

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

cp -f -r grisbi-manuel-0.5.1/src/fr/* $RPM_BUILD_ROOT%{_datadir}/doc/grisbi/help/fr/

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

install -d $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="%{name}"\
needs="x11" \
icon="%{name}.png"\
section="More Applications/Finances"\
title="Grisbi"\
icon="office_section.png"\
longtitle="Personnal Finances Manager" \
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Grisbi
Comment=Personnal finances manager
Exec=%{name}
Icon=office_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Finances;Office;Finance;
EOF

%find_lang %{name}

%post
%{update_menus}


%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc AUTHORS NEWS README
%{_bindir}/*
%{_datadir}/doc/grisbi/help/C/
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_mandir}/man1/*
#%_iconsdir/*.png
%{_datadir}/mime-info/*
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%lang(fr) %{_datadir}/doc/grisbi/help/fr
%lang(de) %{_datadir}/doc/grisbi/help/de


