%define version 1.0.10
%define release %mkrel 3

Summary:	All purpose HTTP copying and mirroring tool
Name: 		w3mir
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	http://search.cpan.org/CPAN/authors/id/J/JA/JANL/%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

%description
w3mir is a all purpose HTTP copying and mirroring tool. The main focus of w3mir
is to create and maintain a browseable copy of one, or several, remote WWW
site(s). Used to the max w3mir can retreive the contents of several related
sites and leave the mirror browseable via a local web server, or from a
filesystem, such as directly from a CDROM.

w3mir's goal is to be able to make useful mirrors of any reasonable WWW site.
It specifically preserves link integrity within the mirrored documents as well
as the integrity of links outside the mirror, following redirects as needed. If
you want it to. w3mir has a powerful ``multi scope'' mechanism enabeling the
user to make mirrors of several related sites and have links between them refer
to the mirrored documents rather than the original site. w3mir has several
features directed at getting mirrors for CDROM burning and handling of some not
too often seen problems when mirroring.

w3mir supports HTML4, and has partial support for CSS, Java and ActiveX.

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{_bindir}/w3mfix
%{_bindir}/w3mir
%{perl_vendorlib}/htmlop.pm
%{perl_vendorlib}/w3http.pm
%{perl_vendorlib}/w3pdfuri.pm
%{_mandir}/*/*


