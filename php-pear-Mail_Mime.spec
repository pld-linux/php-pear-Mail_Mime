%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_subclass	Mime
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - classes to create and decode mime messages
Summary(pl):	%{_pearname} - klasa do tworzenia i dekodowania wiadomości mime
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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

%description -l pl
Dostarcza klasy do tworzenia oraz manipulowania wiadomościami mime:
- mime.php: tworzenie emaili mime, z htmlem, załącznikami, obrazkami,
  etc.
- mimePart.php: zaawansowane metody tworzenia wiadomości mime.
- mimeDecode.php: dekoduje wiadomości mime do używalnej struktury.
- xmail.dtd: XML DTD dla metody getXML() klasy dekodującej.
- xmail.xsl: styl XSLT do transformowania wyjścia metody getXML().

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*
