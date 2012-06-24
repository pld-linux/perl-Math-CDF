#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	CDF
Summary:	Math::CDF - probabilities and quantiles for several statistical functions
Summary(pl):	Math::CDF - prawdopodobie�stwa i kwantyle dla niekt�rych funkcji statystycznych
Name:		perl-Math-CDF
Version:	0.1
Release:	2
# non-commercial because of some parts of DCDFLIB
License:	non-commercial
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7866c7b6b9d27f0ce4b7637334478ab7
Patch0:		%{name}-system-dcdflib.patch
BuildRequires:	dcdflib.c-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a Perl interface to the DCDFLIB. Functions are
available for 7 continuous distributions (Beta, Chi-square, F, Gamma,
Normal, Poisson and T-distribution) and for two discrete distributions
(Binomial and Negative Binomial). Optional non-centrality parameters
are available for the Chi-square, F and T-distributions. Cumulative
probabilities are available for all 9 distributions and quantile
functions are available for the 7 continuous distributions.

%description -l pl
Ten modu� udost�pnia perlowy interfejs do biblioteki DCDFLIB. Dost�pne
s� funkcje dla 7 rozk�ad�w ci�g�ych (Beta, Chi-kwadrat, F, Gamma,
normalnego, Poissona, t Studenta) oraz dw�ch dyskretnych (dwumianowego
i odwrotnego dwumianowego). Dost�pne s� opcjonalne parametry
niecentralno�ci dla rozk�ad�w Chi-kwadrat, F i t Studenta. Funkcje
rozk�adu prawdopodobie�stwa s� dost�pne dla wszystkich 9 rozk�ad�w, a
funkcje kwantyli dla 7 ci�g�ych rozk�ad�w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Math/CDF.pm
%dir %{perl_vendorarch}/auto/Math/CDF
%{perl_vendorarch}/auto/Math/CDF/CDF.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/CDF/CDF.so
%{perl_vendorarch}/auto/Math/CDF/autosplit.ix
%{_mandir}/man3/*
