%define upstream_name    Catalyst-Log-Log4perl
Name:		perl-%{upstream_name}
Version:	1.06
Release:	5

Summary:	Integrates Log::Log4perl with Catalyst
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://dev.catalyst.perl.org/repos/Catalyst/trunk/historical/Catalyst-Log-Log4perl
Source0:	https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Log-Log4perl-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Data::Dump)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Log::Log4perl)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Params::Validate)
BuildArch:	noarch

%description
This module provides a the Catalyst::Log manpage implementation that uses
the Log::Log4perl manpage as the underlying log mechanism. It provides all
the methods listed in the Catalyst::Log manpage, with the exception of:

    levels
    enable
    disable

These methods simply return 0 and do nothing, as similar functionality is
already provided by the Log::Log4perl manpage.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.40.0-2mdv2011.0
+ Revision: 654251
- rebuild for updated spec-helper

* Sat Jan 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.40.0-1mdv2011.0
+ Revision: 627143
- import perl-Catalyst-Log-Log4perl


