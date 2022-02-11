# Created by pyp2rpm-3.3.1
%global pypi_name pynacl

Name:           python-%{pypi_name}
Version:	1.5.0
Release:	1
Summary:        Python binding to the Networking and Cryptography (NaCl) library
Group:          Development/Python
License:        ASL 2.0
URL:            https://github.com/pyca/pynacl/
Source0:	https://files.pythonhosted.org/packages/a7/22/27582568be639dfe22ddb3902225f91f2f17ceff88ce80e4db396c8986da/PyNaCl-1.5.0.tar.gz

BuildRequires:  python2-devel
#BuildConflicts: python2dist(pytest) = 3.3.0
BuildRequires:  python2dist(cffi) >= 1.4.1
#BuildRequires:  python2dist(hypothesis) >= 3.27.0
#BuildRequires:  python2dist(pytest) >= 3.2.1
BuildRequires:  python2dist(setuptools)
BuildRequires:  python2dist(six)
BuildRequires:  python2dist(enum34)
BuildRequires:  python2dist(funcsigs)

BuildRequires:  python3-devel
#BuildConflicts: python3dist(pytest) = 3.3.0
BuildRequires:  python3dist(cffi) >= 1.4.1
#BuildRequires:  python3dist(hypothesis) >= 3.27.0
#BuildRequires:  python3dist(pytest) >= 3.2.1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(funcsigs)
BuildRequires:  pkgconfig(libsodium)

%description
PyNaCl is a Python binding to libsodium, which is a fork of the Networking
and Cryptography library.

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
PyNaCl is a Python binding to libsodium, which is a fork of the Networking
and Cryptography library.

%prep
%autosetup -n PyNaCl-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
export SODIUM_INSTALL=system
%py2_build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitearch}/nacl/
%{python2_sitearch}/PyNaCl-%{version}-py?.?.egg-info/

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/nacl/
%{python3_sitearch}/PyNaCl-%{version}-py?.?.egg-info/
