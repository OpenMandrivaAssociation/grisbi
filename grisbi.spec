%define	name	grisbi
%define	version	0.8.5
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
BuildRequires:	gtk2-devel
BuildRequires:	libofx-devel
BuildRequires:	gettext-devel
BuildRequires:	imagemagick
BuildRequires:	openssl-devel
BuildRequires:	intltool
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Grisbi helps you to manage your personal finance with Linux.

%prep
%setup -qn %{name}-%{version} -a 1

%patch1 -p1 -b .fixbuild

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

%clean
rm -rf %{buildroot}

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
