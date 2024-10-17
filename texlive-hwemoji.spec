Name:		texlive-hwemoji
Version:	65001
Release:	2
Summary:	Unicode emoji support for pdfLaTeX with sequences
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hwemoji
License:	lppl1.3c cc-by-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hwemoji.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hwemoji.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides direct support for Unicode emoji in
pdfLaTeX, with full access to emoji sequences including but not
limited to flag sequences, diversity modifier sequences, and
tag sequences. Emojis are displayed through Twemoji digital
assets, as licensed under the CC-BY 4.0.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hwemoji
%doc %{_texmfdistdir}/doc/latex/hwemoji

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
