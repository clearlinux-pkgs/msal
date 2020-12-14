#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : msal
Version  : 1.2.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/fd/28/3035c32c12b9963c31bd7b12e93b0ff04542362644fea81104fe56dd9283/msal-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/fd/28/3035c32c12b9963c31bd7b12e93b0ff04542362644fea81104fe56dd9283/msal-1.2.0.tar.gz
Summary  : The Microsoft Authentication Library (MSAL) for Python library enables your app to access the Microsoft Cloud by supporting authentication of users with Microsoft Azure Active Directory accounts (AAD) and Microsoft Accounts (MSA) using industry standard OAuth2 and OpenID Connect.
Group    : Development/Tools
License  : MIT
Requires: msal-python = %{version}-%{release}
Requires: msal-python3 = %{version}-%{release}
Requires: requests
BuildRequires : buildreq-distutils3
BuildRequires : requests

%description
| `dev` branch | Reference Docs
        |---------------|---------------

%package python
Summary: python components for the msal package.
Group: Default
Requires: msal-python3 = %{version}-%{release}

%description python
python components for the msal package.


%package python3
Summary: python3 components for the msal package.
Group: Default
Requires: python3-core
Provides: pypi(msal)
Requires: pypi(pyjwt)
Requires: pypi(requests)

%description python3
python3 components for the msal package.


%prep
%setup -q -n msal-1.2.0
cd %{_builddir}/msal-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588881125
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
