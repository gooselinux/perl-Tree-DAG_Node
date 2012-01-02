Name:           perl-Tree-DAG_Node
Version:        1.06
Release:        6.1%{?dist}
Summary:        Class for representing nodes in a tree

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Tree-DAG_Node/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CO/COGENT/Tree-DAG_Node-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This class encapsulates/makes/manipulates objects that represent nodes
in a tree structure. The tree structure is not an object itself, but
is emergent from the linkages you create between nodes.  This class
provides the methods for making linkages that can be used to build up
a tree, while preventing you from ever making any kinds of linkages
which are not allowed in a tree (such as having a node be its own
mother or ancestor, or having a node have two mothers).


%prep
%setup -q -n Tree-DAG_Node-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{perl_vendorlib}/Tree/
%{_mandir}/man3/*.3pm*


%changelog
* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.06-6.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-4
- fix source url

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-3
- Rebuild for perl 5.10 (again)

* Thu Jan 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-2
- rebuild for new perl

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.06-1
- 1.06

* Wed Oct 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.05-4.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Fri Sep  8 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-4
- Rebuild for FC6.

* Wed Feb 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-3
- Rebuild for FC5 (perl 5.8.8).

* Fri Jul  1 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-2
- Dist tag.

* Thu Dec 30 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.05-0.fdr.1
- Update to 1.05.

* Sun Jul 04 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.04-0.fdr.1
- First build.
