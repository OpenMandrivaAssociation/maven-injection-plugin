%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-injection-plugin
Version:        1.0.2
Release:        12.2
Summary:        Bytecode injection at Maven build time
Group:		Development/Java
License:        LGPLv2+
URL:            http://www.jboss.org
BuildArch:      noarch

# svn export http://anonsvn.jboss.org/repos/labs/labs/jbossbuild/maven-plugins/tags/maven-injection-plugin-1.0.2/
# tar cafJ maven-injection-plugin-1.0.2.tar.xz maven-injection-plugin-1.0.2
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  maven-local
BuildRequires:  mvn(javassist:javassist)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)

%description
This package provides capability to perform bytecode injection
as part of build.

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-11
- Update to current packaging guidelines

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.2-10
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.2-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Oct 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-6
- Remove unneeded BuildRequires

* Mon Jul 23 2012 Marek Goldmann <mgoldman@redhat.com> - 1.0.2-5
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 29 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.2-2
- Removinng unnecessary requires

* Mon Aug 01 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.2-1
- Initial packaging


