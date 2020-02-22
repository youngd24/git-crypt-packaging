Summary: git-crypt enables transparent encryption and decryption of files in a git repository
Name: git-crypt
Version: 0.6.0
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
Url: https://github.com/AGWA/git-crypt
Source: https://github.com/AGWA/git-crypt/archive/%{version}.tar.gz
BuildRequires: openssl-devel
BuildRequires: gcc-c++
Requires: git
Requires: openssl

%description
git-crypt enables transparent encryption and decryption of files in a git repository. Files which you choose to protect are encrypted when committed, and decrypted when checked out. git-crypt lets you freely share a repository containing a mix of public and private content. git-crypt gracefully degrades, so developers without the secret key can still clone and commit to a repository with encrypted files. This lets you store your secret material (such as keys or passwords) in the same repository as your code, without requiring you to lock down your entire repository.

%prep
%setup -q 

%build
make %{?_smp_mflags} 

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 git-crypt %{buildroot}%{_bindir}/git-crypt
%{__install} -D -d -m0755 %{buildroot}/%{_defaultdocdir}/git-crypt-%{version}
%{__install} -D -m 0644 AUTHORS %{buildroot}/%{_defaultdocdir}/git-crypt-%{version}/
%{__install} -D -m 0644 COPYING %{buildroot}/%{_defaultdocdir}/git-crypt-%{version}/
%{__install} -D -m 0644 NEWS %{buildroot}/%{_defaultdocdir}/git-crypt-%{version}/
%{__install} -D -m 0644 README %{buildroot}/%{_defaultdocdir}/git-crypt-%{version}/

%post

%preun

%files
%doc AUTHORS COPYING NEWS README 
%{_bindir}/git-crypt

%changelog
* Fri Feb 21 2020 Darren Young <youngd24@gmail.com - 0.6.0-1
- Version 0.6.0

* Thu Apr 13 2017 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.5.0-1
- Bumped to version 0.5.0
- Modified Source/Url location to new github repo

* Thu Apr 16 2015 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.4.2-1
- Bumped to version 0.4.2

* Fri Jul 18 2014 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.3-1
- Initial spec file

