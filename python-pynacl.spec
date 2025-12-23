%define module pynacl
%define oname PyNaCl

Name:		python-pynacl
Version:	1.6.1
Release:	1
Summary:	Python binding to the Networking and Cryptography (NaCl) library
Group:		Development/Python
License:	ASL 2.0
URL:		https://github.com/pyca/pynacl/
Source0:	https://github.com/pyca/pynacl/archive/%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(cffi)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pycparser)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)

%description
%{oname} is a Python binding to libsodium, which is a fork of the Networking
and Cryptography library.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info
rm -rf src/libsodium

%build
export SODIUM_INSTALL="system"
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE
%{python_sitearch}/nacl/
%{python_sitearch}/%{module}-%{version}.dist-info
