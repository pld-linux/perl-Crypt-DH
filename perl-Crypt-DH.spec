%define		pdir	Crypt
%define		pnam	DH
%include	/usr/lib/rpm/macros.perl
Summary:	Crypt::DH Perl module - Diffie-Hellman key exchange system implementation
Summary(pl.UTF-8):	Moduł Perla Crypt::DH - implementacja systemu wymiany kluczy Diffie-Hellman
Name:		perl-Crypt-DH
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5494c91420bf77de4af808fcafb6c3ce
URL:		http://search.cpan.org/dist/Crypt-DH/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.56
BuildRequires:	perl-Math-BigInt >= 1.60
BuildRequires:	perl-Math-BigInt-GMP >= 1.24
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.60
Requires:	perl-Math-BigInt-GMP >= 1.24
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::DH is a Perl implementation of the Diffie-Hellman key exchange
system. Diffie-Hellman is an algorithm by which two parties can agree
on a shared secret key, known only to them. The secret is negotiated
over an insecure network without the two parties ever passing the
actual shared secret, or their private keys, between them.

%description -l pl.UTF-8
Crypt::DH to perlowa implementacja systemu wymiany kluczy
Diffie-Hellman. Jest to algorytm, w którym dwie strony mogą zgodzić
się na wspólny tajny klucz, znany tylko im. Klucz jest negocjowany po
nie zabezpieczonej sieci bez przesyłania właściwego klucza ani
prywatnych kluczy między stronami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%{perl_vendorlib}/Crypt/DH.pm
%{_mandir}/man3/*
