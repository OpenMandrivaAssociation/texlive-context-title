Name:		texlive-context-title
Version:	47085
Release:	1
Summary:	Place document titles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/context-title
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-title.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-title.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The title module provides the \placetitle command to put a
title block into your document. With the command \setuptitle
values can be set for \placetitle and change the formatting of
the content.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/context/third/title
%{_texmfdistdir}/tex/context/interface/third/*
%doc %{_texmfdistdir}/doc/context/third/title

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
