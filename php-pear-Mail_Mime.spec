%define		pearname	Mail_Mime
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - classes to create and decode mime messages
Summary(pl.UTF-8):	%{pearname} - klasa do tworzenia i dekodowania wiadomości mime
Name:		php-pear-%{pearname}
Version:	1.10.1
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	ef4b562fc507fb8b7ec8286df97a9b97
URL:		https://pear.php.net/package/Mail_Mime/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php-pear
Obsoletes:	php-pear-Mail_Mime-tests
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

%description -l pl.UTF-8
Dostarcza klasy do tworzenia oraz manipulowania wiadomościami mime:
- mime.php: tworzenie emaili mime, z htmlem, załącznikami, obrazkami,
  etc.
- mimePart.php: zaawansowane metody tworzenia wiadomości mime.
- mimeDecode.php: dekoduje wiadomości mime do używalnej struktury.
- xmail.dtd: XML DTD dla metody getXML() klasy dekodującej.
- xmail.xsl: styl XSLT do transformowania wyjścia metody getXML().

%prep
%pear_package_setup

install -d examples
mv docs/Mail_Mime/scripts/phail.php examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Mail/*
%{_examplesdir}/%{name}-%{version}
