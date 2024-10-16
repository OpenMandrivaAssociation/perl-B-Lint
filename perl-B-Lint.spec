%define upstream_name    B-Lint
%define upstream_version 1.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	7
License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Adds debugging stringification to B::
Source:     http://www.cpan.org/modules/by-module/B/%{upstream_name}-%{upstream_version}.tar.gz
Url:        https://search.cpan.org/dist/%{upstream_name}
BuildRoot:  %{_tmppath}/%{upstream_name}-%{upstream_version}
BuildRequires: perl-devel
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Test::More)

%description
The B::Lint module is equivalent to an extended version of the *-w* option
of *perl*. It is named after the program _lint_ which carries out a similar
process for C programs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.120.0-5
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.120.0-4
+ Revision: 680655
- mass rebuild

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-3mdv2011.0
+ Revision: 597091
- rebuild

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-2mdv2011.0
+ Revision: 562416
- rebuild

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 561019
- update to 1.12

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-3mdv2011.0
+ Revision: 555687
- rebuild

* Mon May 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-2mdv2010.0
+ Revision: 379620
- removing noarch tag since module insists on installing in archlib
- using %%perl_convert_version macro

* Wed May 20 2009 Jérôme Quelin <jquelin@mandriva.org> 1.11-2mdv2010.0
+ Revision: 378037
- bumping mkrel
- adding missing requires

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.11-1mdv2010.0
+ Revision: 374335
- import perl-B-Lint


* Mon May 11 2009 cpan2dist 1.11-1mdv
- initial mdv release, generated with cpan2dist

