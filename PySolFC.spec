Summary:	A Python solitaire game collection
Name:		PySolFC
Version:	2.16.0
Release:	1
Source0:	https://sourceforge.net/projects/pysolfc/files/PySolFC/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:	PySolFC.rpmlintrc
License:	GPLv3+
Group:		Games/Cards
BuildArch:	noarch
Url:		http://pysolfc.sourceforge.net/
Obsoletes:	pysol
BuildRequires:	python-devel
BuildRequires:	python-setuptools
Requires:	tkinter
Requires:	python-imaging
Requires:	python-random2
Requires: python3dist(pycotap)
Requires: python3dist(pysol-cards)
Suggests:	PySolFC-cardsets
Suggests:	freecell-solver

%description
PySolFC is a collection of more than 1000 solitaire card games.
Its features include modern look and feel (uses Tile widget set), multiple
card-sets and tableau backgrounds, sound, unlimited undo, player statistics,
a hint system, demo games, a solitaire wizard, support for user written
plug-ins, an integrated HTML help browser, and lots of documentation.

%prep
%setup -n %{name}-%{version} -q

%build
python setup.py build

%install
python setup.py install --root=%buildroot

# Hack to put /usr/bin/pysol.py as /usr/games pysol
mkdir -p %{buildroot}/%{_gamesbindir}
%define pysol_bin_path %{_gamesbindir}/pysol
%define pysol_orig_path %{_bindir}/pysol.py
mv %{buildroot}/%{pysol_orig_path} %{buildroot}/%{pysol_bin_path}

sed -i -e 's#Exec=.*#Exec=%{_gamesbindir}/pysol#' %{buildroot}%_datadir/applications/pysol.desktop

%find_lang pysol

%files -f pysol.lang
%_gamesbindir/*
%py_puresitedir/*
%_datadir/%name
%_datadir/applications/pysol.desktop
%{_iconsdir}/hicolor/*x*/apps/pysol.png
