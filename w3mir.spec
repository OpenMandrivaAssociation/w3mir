%define version 1.0.10
%define release 9

Summary:	All purpose HTTP copying and mirroring tool
Name: 		w3mir
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		https://www.cpan.org
Source0:	http://search.cpan.org/CPAN/authors/id/J/JA/JANL/%{name}-%{version}.tar.bz2
BuildArch:	noarch
buildrequires: perl-devel

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
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_bindir}/w3mfix
%{_bindir}/w3mir
%{perl_vendorlib}/htmlop.pm
%{perl_vendorlib}/w3http.pm
%{perl_vendorlib}/w3pdfuri.pm
%{_mandir}/*/*




%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.10-8mdv2010.0
+ Revision: 434696
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.10-7mdv2009.0
+ Revision: 261915
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.10-6mdv2009.0
+ Revision: 255779
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.10-4mdv2008.1
+ Revision: 171168
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0.10-3mdv2008.1
+ Revision: 136571
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Sep 28 2005 Olivier Thauvin <nanardon@mandriva.org> 1.0.10-2mdk
- rebuild

* Wed Sep 22 2004 Stefan van der Eijk <stefan@eijk.nu> 1.0.10-1mdk
- initial package

