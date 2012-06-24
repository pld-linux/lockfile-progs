Summary:	Programs for locking and unlocking files and mailboxes
Summary(pl):	Programy do blokowania i odblokowywania plik�w i skrzynek pocztowych
Name:		lockfile-progs
Version:	0.1.10
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.debian.org/debian/pool/main/l/lockfile-progs/%{name}_%{version}.tar.gz
# Source0-md5:	f1edd71fed7e18dde3b3c46464e06e29
BuildRequires:	liblockfile-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes several programs to safely lock and unlock files
and mailboxes from the command line.

These include:
- lockfile-create
- lockfile-remove
- lockfile-touchlock
- mail-lock
- mail-unlock
- mail-touchlock.

These programs use liblockfile to perform the file locking and
unlocking.

%description -l pl
Ten pakiet zawiera kilka program�w do bezpiecznego blokowania i
odblokowywania plik�w i skrzynek pocztowych z linii polece�:
- lockfile-create
- lockfile-remove
- lockfile-touchlock
- mail-lock
- mail-unlock
- mail-touchlock.

Programy te wykorzystuj� bibliotek� liblockfile do wykonywania
blokowania i odblokowywania plik�w.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a man/* $RPM_BUILD_ROOT%{_mandir}/man1

echo '.so lockfile-progs.1' > lockfile-progs.1
install lockfile-progs.1 $RPM_BUILD_ROOT%{_mandir}/man1/lockfile-create.1
install lockfile-progs.1 $RPM_BUILD_ROOT%{_mandir}/man1/lockfile-remove.1
install lockfile-progs.1 $RPM_BUILD_ROOT%{_mandir}/man1/lockfile-touch.1
install lockfile-progs.1 $RPM_BUILD_ROOT%{_mandir}/man1/mail-lock.1
install lockfile-progs.1 $RPM_BUILD_ROOT%{_mandir}/man1/mail-unlock.1
install lockfile-progs.1 $RPM_BUILD_ROOT%{_mandir}/man1/mail-touchlock.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_bindir}/lockfile-create
%attr(755,root,root) %{_bindir}/lockfile-remove
%attr(755,root,root) %{_bindir}/lockfile-touch
%attr(755,root,root) %{_bindir}/mail-lock
%attr(755,root,root) %{_bindir}/mail-touchlock
%attr(755,root,root) %{_bindir}/mail-unlock
%{_mandir}/man1/lockfile-create.1*
%{_mandir}/man1/lockfile-progs.1*
%{_mandir}/man1/lockfile-remove.1*
%{_mandir}/man1/lockfile-touch.1*
%{_mandir}/man1/mail-lock.1*
%{_mandir}/man1/mail-touchlock.1*
%{_mandir}/man1/mail-unlock.1*
