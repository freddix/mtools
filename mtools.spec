Summary:	Programs to access DOS disks w/o mounting them
Name:		mtools
Version:	4.0.18
Release:	1
License:	GPL
Group:		Applications/File
#Source0Download: http://mtools.linux.lu/download.html
Source0:	http://mtools.linux.lu/%{name}-%{version}.tar.bz2
# Source0-md5:	a23646617546bf6ad56f061d8b283c85
Source1:	%{name}.conf
Patch0:		%{name}-pmake.patch
URL:		http://mtools.linux.lu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mtools is a collection of utilities to access MS-DOS disks from Unix
without mounting them. It supports Win'95 style long file names, OS/2
Xdf disks, ZIP/JAZ disks and 2m disks (store up to 1992k on a high
density 3 1/2 disk).

%prep
%setup -q
%patch0 -p1

%build
cp /usr/share/automake/config.sub .
%{__autoconf}
%configure \
	--disable-floppyd

%{__make} \
	MYCFLAGS="%{rpmcflags} -Wall"

makeinfo --force mtools.texi
touch mtools.*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README Release.notes
%attr(755,root,root) %{_bindir}/amuFormat.sh
%attr(755,root,root) %{_bindir}/lz
%attr(755,root,root) %{_bindir}/m*
%attr(755,root,root) %{_bindir}/tgz
%attr(755,root,root) %{_bindir}/uz
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mtools.conf
%{_mandir}/man1/m*.1*
%{_mandir}/man5/mtools.5*
%{_infodir}/mtools.info*

