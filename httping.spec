Summary:	Ping-like tool for HTTP requests
Summary(pl):	Narz�dzie do "pingowania" poprzez protok� HTTP
Name:		httping
Version:	1.0.6
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.vanheusden.com/httping/%{name}-%{version}.tgz
# Source0-md5:	22ea1091a7e57a53be4e20fefbe8b93d
Patch0:		%{name}-Makefile.patch
URL:		http://www.vanheusden.com/httping/
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
httping is a "ping"-like tool for HTTP requests. Give it a URL and it
will show how long it takes to connect, send a request, and retrieve
the reply (only the headers). It can be used for monitoring or
statistical purposes (measuring latency).

%description -l pl
httping jest narz�dziem podobnym do pinga, s�u��cym do wysy�ania
zapyta� HTTP. Po podaniu URL-a httping pokazuje jak wiele czasu
zajmuje po��czenie, wys�anie zapytania i otrzymanie odpowiedzi (tylko
nag��wki). Httping mo�e by� u�ywany do monitorowania lub do cel�w
statystycznych.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/httping
