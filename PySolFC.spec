%define name PySolFC
%define version 2.0
%define unmangled_version 2.0
%define release %mkrel 9

Summary: A Python solitaire game collection
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.bz2
License: GPLv3+
Group: Games/Cards
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Url: http://pysolfc.sourceforge.net/
Obsoletes: pysol
BuildRequires: python-devel
BuildRequires: python-setuptools
Requires: tkinter
Requires: python-imaging
Suggests: PySolFC-cardsets
Suggests: freecell-solver

%description
PySolFC is a collection of more than 1000 solitaire card games.
Its features include modern look and feel (uses Tile widget set), multiple
card-sets and tableau backgrounds, sound, unlimited undo, player statistics,
a hint system, demo games, a solitaire wizard, support for user written
plug-ins, an integrated HTML help browser, and lots of documentation.

%prep
%setup -n %{name}-%{unmangled_version} -q

%build
python setup.py build

%install
rm -rf %buildroot
python setup.py install --root=%buildroot

# Hack to put /usr/bin/pysol.py as /usr/games pysol
mkdir -p %{buildroot}/%{_gamesbindir}
%define pysol_bin_path %{_gamesbindir}/pysol
%define pysol_orig_path %{_bindir}/pysol.py
mv %{buildroot}/%{pysol_orig_path} %{buildroot}/%{pysol_bin_path}

sed -i -e 's#Exec=.*#Exec=%{_gamesbindir}/pysol#' %{buildroot}%_datadir/applications/pysol.desktop

%find_lang pysol

%clean
rm -rf %buildroot

%files -f pysol.lang
%defattr(-,root,root)
%doc COPYING README
%_gamesbindir/*
%py_puresitedir/*
%_datadir/%name
%_datadir/applications/pysol.desktop
%_iconsdir/*.png
%_datadir/pixmaps/*


%changelog
* Sun Dec 19 2010 Shlomi Fish <shlomif@mandriva.org> 2.0-9mdv2011.0
+ Revision: 623151
- Now suggesting freecell-solver

* Mon Nov 01 2010 Shlomi Fish <shlomif@mandriva.org> 2.0-8mdv2011.0
+ Revision: 591520
- New release for new python and also suggesting the cardsets package

* Sun Sep 19 2010 Funda Wang <fwang@mandriva.org> 2.0-7mdv2011.0
+ Revision: 579772
- fix desktop file (mdv#57687)

* Fri Jul 09 2010 Shlomi Fish <shlomif@mandriva.org> 2.0-6mdv2011.0
+ Revision: 549896
- Add missing tkiner and python-imaging dependencies

* Wed May 05 2010 Funda Wang <fwang@mandriva.org> 2.0-5mdv2010.1
+ Revision: 542300
- update file list to reflect pyc removal

* Mon Feb 15 2010 Shlomi Fish <shlomif@mandriva.org> 2.0-4mdv2010.1
+ Revision: 506356
- Add BuildRequires on python-devel and python-setuptools
- Fixed the Vendor field and moved to the group Games/Cards
- Add an obsoletes field for the original (and no longer maintained) PySol
- import PySolFC


* Sat Dec 05 2009 Shlomi Fish <shlomif@iglu.org.il> 2.0-1mdv
+ Generated from python setup.py bdist_rpm .
+ Hack to put /usr/bin/pysol.py under /usr/games/pysol .
+ Fixed the rpmlint problems.

