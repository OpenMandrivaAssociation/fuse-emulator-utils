%define oname		fuse-utils
Name:			fuse-emulator-utils
Version:		1.0.0
Release:		%mkrel 1

Summary:	A few tools to deal with ZX Spectrum emulator files
License:	GPLv2+
Group:		Emulators
URL:		http://fuse-emulator.sourceforge.net/
Source0:	%{oname}-%{version}.tar.gz

BuildRequires:	libz-devel
BuildRequires:	libspectrum-devel >= 1.0.0
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

Obsoletes:	fuse-utils
Provides:	fuse-utils

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

%build
autoreconf
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README AUTHORS ChangeLog
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/*/*

