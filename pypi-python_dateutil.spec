#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-python_dateutil
Version  : 2.8.2
Release  : 84
URL      : https://files.pythonhosted.org/packages/4c/c4/13b4776ea2d76c115c1d1b84579f3764ee6d57204f6be27119f13a61d0a9/python-dateutil-2.8.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/4c/c4/13b4776ea2d76c115c1d1b84579f3764ee6d57204f6be27119f13a61d0a9/python-dateutil-2.8.2.tar.gz
Summary  : Extensions to the standard Python datetime module
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: pypi-python_dateutil-license = %{version}-%{release}
Requires: pypi-python_dateutil-python = %{version}-%{release}
Requires: pypi-python_dateutil-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(freezegun)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(six)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pytest
BuildRequires : tzdata

%description
dateutil - powerful extensions to datetime
==========================================

%package license
Summary: license components for the pypi-python_dateutil package.
Group: Default

%description license
license components for the pypi-python_dateutil package.


%package python
Summary: python components for the pypi-python_dateutil package.
Group: Default
Requires: pypi-python_dateutil-python3 = %{version}-%{release}

%description python
python components for the pypi-python_dateutil package.


%package python3
Summary: python3 components for the pypi-python_dateutil package.
Group: Default
Requires: python3-core
Provides: pypi(python_dateutil)
Requires: pypi(six)

%description python3
python3 components for the pypi-python_dateutil package.


%prep
%setup -q -n python-dateutil-2.8.2
cd %{_builddir}/python-dateutil-2.8.2
pushd ..
cp -a python-dateutil-2.8.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656401625
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-python_dateutil
cp %{_builddir}/python-dateutil-2.8.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-python_dateutil/f3b34c666d9f93071f6dbeeea6f8daefc2258e90
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-python_dateutil/f3b34c666d9f93071f6dbeeea6f8daefc2258e90

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
