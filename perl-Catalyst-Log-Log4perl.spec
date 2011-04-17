%define upstream_name    Catalyst-Log-Log4perl
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Integrates Log::Log4perl with Catalyst
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Catalyst)
BuildRequires: perl(Data::Dump)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Log::Log4perl)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Params::Validate)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


