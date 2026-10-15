Name:		python-crypt-r
Version:	3.13.1
Release:	1
Summary:	crypt module removed from Python 3.13, as crypt_r
License:	PSF-2.0
Group:		Development/Python
URL:		https://github.com/fedora-python/crypt_r
Source0:	https://files.pythonhosted.org/packages/source/c/crypt_r/crypt_r-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(libcrypt)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)

%description
A copy of the crypt module that Python 3.13 removed.
This package installs crypt_r only. python-legacycrypt already owns crypt.py.

%prep
%autosetup -n crypt_r-%{version} -p1
# Do not install crypt.py. python-legacycrypt owns that path.
sed -i 's/py-modules = \["crypt_r", "crypt"\]/py-modules = ["crypt_r"]/' pyproject.toml

%build
%py_build

%install
%py_install

%files
%license LICENSE
%{python3_sitearch}/crypt_r.py
%{python3_sitearch}/_crypt_r*.so
%{python3_sitearch}/__pycache__/crypt_r*
%{python3_sitearch}/crypt_r-%{version}.dist-info
