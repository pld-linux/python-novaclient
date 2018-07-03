#
# Conditional build:
%bcond_with	doc	# do build doc (missing deps)
%bcond_with	tests	# do perform "make test" (missing deps)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Client library for OpenStack Compute API
Name:		python-novaclient
Version:	9.1.0
Release:	2
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/python-novaclient/%{name}-%{version}.tar.gz
# Source0-md5:	4be037d19ec5ab7967d51a445a0c29e3
URL:		https://pypi.python.org/pypi/python-novaclient
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%endif
Requires:	python-babel >= 2.3.4
Requires:	python-iso8601 >= 0.1.11
Requires:	python-keystoneauth1 >= 3.0.1
Requires:	python-oslo.i18n >= 2.1.0
Requires:	python-oslo.serialization >= 1.10.0
Requires:	python-oslo.utils >= 3.20.0
Requires:	python-pbr >= 2.0.0
Requires:	python-prettytable >= 0.7.1
Requires:	python-simplejson >= 2.2.0
Requires:	python-six >= 1.9.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a client for the OpenStack Compute API. It provides a Python
API (the novaclient module) which implements 100% of the OpenStack
Compute API.

%package -n python3-novaclient
Summary:	Client library for OpenStack Compute API
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-novaclient
This is a client for the OpenStack Compute API. It provides a Python
API (the novaclient module) which implements 100% of the OpenStack
Compute API.

%package -n novaclient
Summary:	Client library OpenStack Compute API
Group:		Applications
%if %{with python3}
Requires:	python3-novaclient = %{version}-%{release}
%else
Requires:	%{name} = %{version}-%{release}
%endif

%description -n novaclient
This is a client for the OpenStack Compute API. It provides a
command-line script (nova) which implements 100% of the OpenStack
Compute API.

%package apidocs
Summary:	API documentation for Python novaclient module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona novaclient
Group:		Documentation

%description apidocs
API documentation for Pythona novaclient module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona novaclient.

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/novaclient
%{py_sitescriptdir}/python_novaclient-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-novaclient
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/novaclient
%{py3_sitescriptdir}/python_novaclient-%{version}-py*.egg-info
%endif

%files -n novaclient
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%attr(755,root,root) %{_bindir}/nova

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
