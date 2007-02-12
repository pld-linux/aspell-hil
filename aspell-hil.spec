Summary:	Hiligaynon dictionary for aspell
Summary(pl.UTF-8):	Słownik hiligainon dla aspella
Name:		aspell-hil
Version:	0.11
%define	subv	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/hil/aspell5-hil-%{version}-%{subv}.tar.bz2
# Source0-md5:	6ce553007a773a1c2ffd68b660ddb60b
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hiligaynon dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik hiligainon (lista słów) dla aspella.

%prep
%setup -q -n aspell5-hil-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
