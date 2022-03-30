#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Leightweight template library
Summary(pl.UTF-8):	Lekka biblioteka szablonów
Name:		python3-wheezy.template
Version:	3.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/wheezy.template/
Source0:	https://files.pythonhosted.org/packages/source/w/wheezy.template/wheezy.template-%{version}.tar.gz
# Source0-md5:	007efefc10233bc723475c90e6dccb40
URL:		https://pypi.org/project/wheezy.template/
BuildRequires:	python3-Cython
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wheezy.template is a Python package written in pure Python code. It is
a lightweight template library. The design goals achieved:
- Compact, Expressive, Clean: Minimizes the number of keystrokes
  required to build a template. Enables fast and well read coding.
- Intuitive, No time to Learn: Basic Python programming skills
  plus HTML markup.
- Do Not Repeat Yourself: Master layout templates for inheritance;
  include and import directives for maximum reuse.
- Blazingly Fast: Maximum rendering performance: ultimate speed and
  context preprocessor features.

%description -l pl.UTF-8
wheezy.template to pakiet Pythona napisany w czystym Pythonie, będący
lekką biblioteką szablonów. Osiągnięte cele projektu:
- zwięzłość, wyrazistość, czystość: do stworzenia szablonu wymagana
  jest minimalna liczba naciśnięć klawiszy. Pozwala to na szybkie i
  czytelne kodowanie.
- intuicyjność, minimalny czas nauki: podstawy programowania w
  Pythonie plus znaczniki HTML.
- brak powtarzania kodu: główne szablony wyglądu do dziedziczenia;
  dyrektywy włączające i importujące, pozwalające na maksymalne
  ponowne używanie.
- szybkość: duża wydajność renderowania.

%prep
%setup -q -n wheezy.template-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/wheezy.template{,-3}
ln -s wheezy-template-3 $RPM_BUILD_ROOT%{_bindir}/wheezy.template

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/wheezy.template
%attr(755,root,root) %{_bindir}/wheezy.template-3
%dir %{py3_sitedir}/wheezy
%dir %{py3_sitedir}/wheezy/template
%{py3_sitedir}/wheezy/template/*.py
%{py3_sitedir}/wheezy/template/py.typed
%{py3_sitedir}/wheezy/template/__pycache__
%attr(755,root,root) %{py3_sitedir}/wheezy/template/*.cpython-*.so
%dir %{py3_sitedir}/wheezy/template/ext
%{py3_sitedir}/wheezy/template/ext/*.py
%{py3_sitedir}/wheezy/template/ext/__pycache__
%attr(755,root,root) %{py3_sitedir}/wheezy/template/ext/*.cpython-*.so
%{py3_sitedir}/wheezy.template-%{version}-py*-nspkg.pth
%{py3_sitedir}/wheezy.template-%{version}-py*.egg-info
