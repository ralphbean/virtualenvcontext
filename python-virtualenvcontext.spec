%global modname virtualenvcontext

Name:             python-virtualenvcontext
Version:          0.1.4
Release:          1%{?dist}
Summary:          Switch virtualenvs with a python context manager

Group:            Development/Languages
License:          GPLv2+
URL:              http://pypi.python.org/pypi/%{modname}
Source0:          http://pypi.python.org/packages/source/v/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:        noarch


BuildRequires:    python2-devel
BuildRequires:    python-setuptools

Requires:         python-virtualenvwrapper

%description
Switch virtualenvs with a python context manager:

>>> from virtualenvcontext import VirtualenvContext

>>> try:
>>>     import kitchen
>>> except ImportError as e:
>>>     print "kitchen is definitely not installed in system-python"

>>> with VirtaulenvContext("my-venv"):
>>>     import kitchen
>>>     print "But it *is* installed in my virtualenv"

>>> try:
>>>     import kitchen
>>> except ImportError as e:
>>>     print "But once I exit that block, I lose my powers again..."

%prep
%setup -q -n virtualenvcontext-%{version}

%build
%{__python} setup.py build 

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# Don't run the check section, since it requires a network connection.

%files
%doc README.rst LICENSE PKG-INFO

%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}-*.egg-info


%changelog
* Tue May 08 2012 Ralph Bean <rbean@redhat.com> - 0.1.4-1
- New upstream version to (again) resolve license inconsistency.
- Included PKG-INFO in files section.

* Mon May 07 2012 Ralph Bean <rbean@redhat.com> - 0.1.3-1
- New upstream version -- resolves licensing ambiguity.
- More explicit directory ownership in %%{python_sitelib}

* Wed Apr 25 2012 Ralph Bean <rbean@redhat.com> - 0.1.2-1
- initial package for Fedora
