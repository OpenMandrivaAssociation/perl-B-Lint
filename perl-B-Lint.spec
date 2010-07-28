%define upstream_name    B-Lint
%define upstream_version 1.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Adds debugging stringification to B::
Source:     http://www.cpan.org/modules/by-module/B/%{upstream_name}-%{upstream_version}.tar.gz
Url:        http://search.cpan.org/dist/%{upstream_name}
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


