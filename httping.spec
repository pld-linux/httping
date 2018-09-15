Summary:	Ping-like tool for HTTP requests
Summary(pl.UTF-8):	Narzędzie do "pingowania" poprzez protokół HTTP
Name:		httping
Version:	2.5
Release:	2
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.vanheusden.com/httping/%{name}-%{version}.tgz
# Source0-md5:	a92976c06af8b80af17f70f0cb059bdc
URL:		http://www.vanheusden.com/httping/
BuildRequires:	fftw3-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
httping is a "ping"-like tool for HTTP requests. Give it a URL and it
will show how long it takes to connect, send a request, and retrieve
the reply (only the headers). It can be used for monitoring or
statistical purposes (measuring latency).

%description -l pl.UTF-8
httping jest narzędziem podobnym do pinga, służącym do wysyłania
zapytań HTTP. Po podaniu URL-a httping pokazuje jak wiele czasu
zajmuje połączenie, wysłanie zapytania i otrzymanie odpowiedzi (tylko
nagłówki). Httping może być używany do monitorowania lub do celów
statystycznych.

%prep
%setup -q

%build
cat << EOF > makefile.inc
SSL=yes
NC=yes
FW=yes
EOF

%{__make} \
	CC="%{__cc}" \
	DEBUG="" \
	OFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang httping

%clean
rm -rf $RPM_BUILD_ROOT

%files -f httping.lang
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/httping
%{_mandir}/man1/httping.1*
%lang(nl) %{_mandir}/nl/man1/httping-nl.1*
%lang(ru) %{_mandir}/ru/man1/httping-ru.1*
