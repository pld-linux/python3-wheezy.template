#
# Conditional build:
%bcond_with	tests	# unit tests (not included in release package)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Leightweight template library
Summary(pl.UTF-8):	Lekka biblioteka szablonów
Name:		python-wheezy.template
Version:	0.1.195
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/wheezy.template/
Source0:	https://files.pythonhosted.org/packages/source/w/wheezy.template/wheezy.template-%{version}.tar.gz
# Source0-md5:	d6820542cebd340c34756cbb4485fbce
URL:		https://pypi.org/project/wheezy.template/
%if %{with python2}
BuildRequires:	python-Cython
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-Cython
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
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

%package -n python3-wheezy.template
Summary:	Leightweight template library
Summary(pl.UTF-8):	Lekka biblioteka szablonów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-wheezy.template
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

%description -n python3-wheezy.template -l pl.UTF-8
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
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/wheezy.template{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/wheezy.template{,-3}
ln -s wheezy-template-3 $RPM_BUILD_ROOT%{_bindir}/wheezy.template
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/wheezy.template-2
%dir %{py_sitedir}/wheezy
%dir %{py_sitedir}/wheezy/template
%{py_sitedir}/wheezy/template/*.py[co]
%attr(755,root,root) %{py_sitedir}/wheezy/template/*.so
%dir %{py_sitedir}/wheezy/template/ext
%{py_sitedir}/wheezy/template/ext/*.py[co]
%attr(755,root,root) %{py_sitedir}/wheezy/template/ext/*.so
%{py_sitedir}/wheezy.template-%{version}-py*-nspkg.pth
%{py_sitedir}/wheezy.template-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-wheezy.template
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/wheezy.template
%attr(755,root,root) %{_bindir}/wheezy.template-3
%dir %{py3_sitedir}/wheezy
%dir %{py3_sitedir}/wheezy/template
%{py3_sitedir}/wheezy/template/*.py
%{py3_sitedir}/wheezy/template/__pycache__
%attr(755,root,root) %{py3_sitedir}/wheezy/template/*.cpython-*.so
%dir %{py3_sitedir}/wheezy/template/ext
%{py3_sitedir}/wheezy/template/ext/*.py
%{py3_sitedir}/wheezy/template/ext/__pycache__
%attr(755,root,root) %{py3_sitedir}/wheezy/template/ext/*.cpython-*.so
%{py3_sitedir}/wheezy.template-%{version}-py*-nspkg.pth
%{py3_sitedir}/wheezy.template-%{version}-py*.egg-info
%endif
