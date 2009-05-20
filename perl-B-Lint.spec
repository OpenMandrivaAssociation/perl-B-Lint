
%define realname   B-Lint
%define version    1.11
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Adds debugging stringification to B::
Source:     http://www.cpan.org/modules/by-module/B/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Test::More)
Requires:   perl-devel

BuildArch: noarch

%description
The B::Lint module is equivalent to an extended version of the *-w* option
of *perl*. It is named after the program _lint_ which carries out a similar
process for C programs.





%prep
%setup -q -n %{realname}-%{version} 

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


