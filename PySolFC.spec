%define name PySolFC
%define version 2.0
%define unmangled_version 2.0
%define release %mkrel 7

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
