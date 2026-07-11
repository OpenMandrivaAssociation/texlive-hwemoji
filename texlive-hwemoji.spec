%global tl_name hwemoji
%global tl_revision 65001

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Unicode emoji support for pdfLaTeX with sequences
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hwemoji
License:	lppl1.3c cc-by-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hwemoji.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hwemoji.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides direct support for Unicode emoji in pdfLaTeX, with
full access to emoji sequences including but not limited to flag
sequences, diversity modifier sequences, and tag sequences. Emojis are
displayed through Twemoji digital assets, as licensed under the CC-BY
4.0.

