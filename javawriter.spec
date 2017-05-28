%{?_javapackages_macros:%_javapackages_macros}

Name:          javawriter
Version:       2.5.1
Release:       4%{?dist}
Summary:       A Java API for generating .java source files
License:       ASL 2.0
Group:         Development/Java
URL:           https://github.com/square/javapoet
Source0:       https://github.com/square/javapoet/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

%if 0
# Test deps
BuildRequires: mvn(junit:junit)
# Unavailable test deps
BuildRequires: mvn(org.easytesting:fest-assert-core:2.0M8)
%endif

BuildArch:     noarch

%description
A utility class which aids in generating Java source files.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n javapoet-%{name}-%{version}

%pom_xpath_remove "pom:dependency[pom:scope = 'test']" 

%pom_remove_plugin :maven-checkstyle-plugin

%mvn_file : %{name}

%build

# Unavailable test deps: org.easytesting:fest-assert-core:2.0M8
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.md CONTRIBUTING.md README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 gil cattaneo <puntogil@libero.it> 2.5.1-1
- initial rpm
