%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	DH
Summary:	Crypt::DH Perl module - Diffie-Hellman key exchange system implementation
Summary(pl):	Modu³ Perla Crypt::DH - implementacja systemu wymiany kluczy Diffie-Hellman
Name:		perl-Crypt-DH
Version:	0.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e0af4baf9d5c9089ca8f1ad316701a82
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Crypt-Random >= 0.33
BuildRequires:	perl-Math-Pari >= 2.001804
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Crypt-Random >= 0.33
Requires:	perl-Math-Pari >= 2.001804
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::DH is a Perl implementation of the Diffie-Hellman key exchange
system. Diffie-Hellman is an algorithm by which two parties can agree
on a shared secret key, known only to them. The secret is negotiated
over an insecure network without the two parties ever passing the
actual shared secret, or their private keys, between them.

%description -l pl
Crypt::DH to perlowa implementacja systemu wymiany kluczy
Diffie-Hellman. Jest to algorytm, w którym dwie strony mog± zgodziæ
siê na wspólny tajny klucz, znany tylko im. Klucz jest negocjowany po
nie zabezpieczonej sieci bez przesy³ania w³a¶ciwego klucza ani
prywatnych kluczy miêdzy stronami.

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
