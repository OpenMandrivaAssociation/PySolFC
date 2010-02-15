%define name PySolFC
%define version 2.0
%define unmangled_version 2.0
%define release %mkrel 1

Summary: A Python solitaire game collection
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.bz2
License: GPLv3+
Group: Amusements/Games
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Skomoroh <skomoroh@gmail.com>
Url: http://pysolfc.sourceforge.net/

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
python setup.py install --root=%buildroot --record=INSTALLED_FILES

# Hack to put /usr/bin/pysol.py as /usr/games pysol
mkdir -p %{buildroot}/%{_gamesbindir}
%define pysol_bin_path %{_gamesbindir}/pysol
%define pysol_orig_path %{_bindir}/pysol.py
mv %{buildroot}/%{pysol_orig_path} %{buildroot}/%{pysol_bin_path}
perl -lpi -e 'BEGIN { $src = shift(@ARGV); $dest = shift(@ARGV); } $_=$dest if $_ eq $src' %{pysol_orig_path} %{pysol_bin_path} INSTALLED_FILES

%clean
rm -rf %buildroot

%files -f INSTALLED_FILES

%defattr(-,root,root)
%doc COPYING README


