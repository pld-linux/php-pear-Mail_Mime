%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_subclass	Mime
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - classes to create and decode mime messages
Summary(pl):	%{_pearname} - klasa do tworzenia i dekodowania wiadomo¶ci mime
Name:		php-pear-%{_pearname}
Version:	1.3.1
Release:	5
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0012fd2406597e60083bc4bce751cef2
Patch0:		%{name}-variable-refs.patch
URL:		http://pear.php.net/package/Mail_Mime/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(pcre)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides classes to deal with creation and manipulation of mime
messages:
- mime.php: Create mime email, with html, attachments, embedded images
  etc.
- mimePart.php: Advanced method of creating mime messages.
- mimeDecode.php - Decodes mime messages to a usable structure.
- xmail.dtd: An XML DTD to acompany the getXML() method of the
  decoding class.
- xmail.xsl: An XSLT stylesheet to transform the output of the
  getXML() method.

In PEAR status of this package is: %{_status}.

%description -l pl
Dostarcza klasy do tworzenia oraz manipulowania wiadomo¶ciami mime:
- mime.php: tworzenie emaili mime, z htmlem, za³±cznikami, obrazkami,
  etc.
- mimePart.php: zaawansowane metody tworzenia wiadomo¶ci mime.
- mimeDecode.php: dekoduje wiadomo¶ci mime do u¿ywalnej struktury.
- xmail.dtd: XML DTD dla metody getXML() klasy dekoduj±cej.
- xmail.xsl: styl XSLT do transformowania wyj¶cia metody getXML().

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*
%{php_pear_dir}/data/%{_pearname}
