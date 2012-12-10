%define oname		fuse-utils

Name:		fuse-emulator-utils
Version:	1.0.0
Release:	2
Summary:	A few tools to deal with ZX Spectrum emulator files
License:	GPLv2+
Group:		Emulators
URL:		http://fuse-emulator.sourceforge.net/
Source0:	%{oname}-%{version}.tar.gz
Patch0:		fuse-dso.patch
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	libspectrum-devel >= 1.0.0
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	autoconf
BuildRequires:	gettext-devel

%rename fuse-utils

%description
The Fuse utilities are a few tools which may be of occasional use when
dealing with ZX Spectrum emulator files. They were originally
distributed with Fuse, the Free Unix Spectrum Emulator, but are now
independent of Fuse and can be used on their own.

The available utilities are:

* createhdf: create an empty .hdf IDE hard disk image.
* listbasic: list the BASIC in a snapshot or tape file.
* rzxcheck: verify the digital signature in an RZX file.
* rzxdump: list the contents of an RZX input recording file.
* rzxtool: add, extract or remove the embedded snapshot from an RZX file,
  or compress or uncompress the file.
* scl2trd: convert .scl disk images to .trd disk images.
* snap2tzx: convert snapshots to TZX tape images.
* snapconv: convert between snapshot formats.
* tapeconv: convert between .tzx and .tap files.
* tzxlist: list the contents of a TZX file.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1

%build
autoreconf
%configure
%make LIBS="-lgcrypt"

%install
%makeinstall

%files
%defattr(0644,root,root,0755)
%doc README AUTHORS ChangeLog
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/*/*


%changelog
* Wed Jul 27 2011 Andrey Bondrov <abondrov@mandriva.org> 1.0.0-1mdv2012.0
+ Revision: 691965
- Fix BuildRequires
- Fix BuildRequires
- imported package fuse-emulator-utils


* Sun Jul 24 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 1.0.0-1mdv2011.0
- New version 1.0.0
- Import from PlF
- Remove PLF reference

* Thu Jan  8 2009 Guillaume Bedot <littletux@zarb.org> 0.10.0.1-1plf2009.1
- 0.10.0.1

* Mon Jan 28 2008 Guillaume Bedot <littletux@zarb.org> 0.9.0-1plf2008.1
- 0.9.0

* Mon May 14 2007 Guillaume Bedot <littletux@zarb.org> 0.8.0.1-1plf2008.0
- 0.8.0.1
- drop source1 (now included in release)

* Wed May  2 2007 Guillaume Bedot <littletux@zarb.org> 0.8.0-1plf2008.0
- 0.8.0
- add missing ide.h
- drop conflicts (it prevented install...)

* Wed Jul 26 2006 Guillaume Bedot <littletux@zarb.org> 0.7.0-5plf2007.0
- fix conflicts

* Fri Jul 21 2006 Guillaume Bedot <littletux@zarb.org> 0.7.0-4plf2007.0
- conflicts with old fuse-utils package

* Wed Jul 19 2006 Guillaume Bedot <littletux@zarb.org> 0.7.0-3plf2007.0
- rebuild

* Wed Mar 15 2006 Guillaume Bedot <littletux@zarb.org> 0.7.0-2plf
- renamed fuse-emulator-utils
- updated URL
- use mkrel

* Mon Jul 19 2004 Miguel Barrio Orsikowsky <megamik@zarb.org> 0.7.0-1plf
- new version

* Sun May 9 2004 Miguel Barrio Orsikowsky <megamik@zarb.org> 0.6.2-1plf
- introduce in PLF
- new version
- changed spec file to meet Mandrake's skel.spec
- repackaged sources into bz2 format
- updated description and summary
- drop patch0

* Sat Feb 07 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.6.1-4mdk
- rebuild
- patch0 to not use gcrypt function (devel is still need)

* Mon Dec 15 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.6.1-3mdk
- introduce in contrib
  
* Sat Nov 1 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.6.1-2mdk
- made some fixes and cosmetic changes to the spec file

* Thu Sep 2 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.6.1-1mdk
- new version
- changed libspectrum0-devel intro libspectrum2-devel in BuildRequires

* Thu May 22 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.6.0-2mdk
- added BuildRequires

* Sun Apr 27 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.6.0-1mdk
- new version

* Fri Apr 25 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.5.1-1mdk
- first version of the package
- spec file written using Mandrake RPM HOWTO 1.1.1
