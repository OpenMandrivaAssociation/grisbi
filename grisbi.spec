%define	name	grisbi
%define	version	0.6.0
%define	release	%mkrel 1

Name:		%{name}
Summary:	Personal finance manager
Version:	%{version}
Release:	%{release}
License:	GPLv2
Url:		http://www.grisbi.org/
Source0:	http://switch.dl.sourceforge.net/sourceforge/grisbi/%{name}-%{version}.tar.bz2
Source1:	grisbi-manuel-0.5.1.tar.bz2
# (fc) 0.5.8-2mdk fix doc build
Patch1:		grisbi-0.5.8-fixbuild.patch
Group:		Office
BuildRequires:	libgnomeui2-devel
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	libgnomeprint-devel
BuildRequires:	gtk2-devel
BuildRequires:	libofx-devel
BuildRequires:	gettext-devel
BuildRequires:	hevea
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Grisbi helps you to manage your personal finance with Linux.

%prep
%setup -q -n %{name}-%{version} -a 1

%patch1 -p1 -b .fixbuild

# needed by patches 1, 2 & 3
#export AUTOMAKE="automake --foreign"
#autoreconf -i -f -I macros
#cp -f %{_datadir}/gettext/config.rpath .
#aclocal -I macros --force
#automake --add-missing --foreign
#autoconf

%build
%configure2_5x --with-plugins
%make

make -C grisbi-manuel-0.5.1/src html_img

%install
rm -rf %{buildroot}
%makeinstall_std

install -d -m 755  %{buildroot}%{_docdir}/grisbi

cp -fr grisbi-manuel-0.5.1/src/fr %{buildroot}%{_docdir}/grisbi
cp -fr grisbi-manuel-0.5.1/src/image %{buildroot}%{_docdir}/grisbi

install -d -m 755 %{buildroot}%{_liconsdir}
install -d -m 755 %{buildroot}%{_iconsdir}
install -d -m 755 %{buildroot}%{_miconsdir}
install -m 644 pixmaps/grisbi.png %{buildroot}%{_liconsdir}/grisbi.png
convert pixmaps/grisbi.png -resize 32x32 %{buildroot}%{_iconsdir}/grisbi.png
convert pixmaps/grisbi.png -resize 16x16 %{buildroot}%{_miconsdir}/grisbi.png


%find_lang %{name}

sed -i 's/grisbi.png/grisbi/' \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install \
    --add-category=X-MandrivaLinux-MoreApplications-Finance \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README COPYING
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/grisbi
%{_datadir}/locale/*/LC_MESSAGES/*-tips.mo
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_mandir}/man1/*
%{_datadir}/mime-info/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/*/*.png
