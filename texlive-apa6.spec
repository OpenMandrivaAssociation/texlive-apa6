# revision 25403
# category Package
# catalog-ctan /macros/latex/contrib/apa6
# catalog-date 2012-02-15 15:50:59 +0100
# catalog-license lppl1.3
# catalog-version 1.2
Name:		texlive-apa6
Version:	1.20
Release:	1
Summary:	Format documents in APA style (6th edition)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/apa6
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class formats documents in APA style (6th Edition). It
provides a full set of facilities in three different output
modes (journal-like appearance, double-spaced manuscript,
LaTeX-like document), in contrast to the earlier apa6e, which
only formats double-spaced manuscripts in APA style. The class
can mask author identity for copies for use in masked peer
review. Citations are provided using the apacite bundle; the
class requires that package if citations are to be typeset. The
class is a development of the apa class (which is no longer
maintained).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/apa6/apa6.cls
%{_texmfdistdir}/tex/latex/apa6/config/APAamerican.txt
%{_texmfdistdir}/tex/latex/apa6/config/APAbritish.txt
%{_texmfdistdir}/tex/latex/apa6/config/APAdutch.txt
%{_texmfdistdir}/tex/latex/apa6/config/APAendfloat.cfg
%{_texmfdistdir}/tex/latex/apa6/config/APAenglish.txt
%{_texmfdistdir}/tex/latex/apa6/config/APAgerman.txt
%{_texmfdistdir}/tex/latex/apa6/config/APAgreek.txt
%{_texmfdistdir}/tex/latex/apa6/config/APAngerman.txt
%doc %{_texmfdistdir}/doc/latex/apa6/README
%doc %{_texmfdistdir}/doc/latex/apa6/README.txt
%doc %{_texmfdistdir}/doc/latex/apa6/apa6.pdf
%doc %{_texmfdistdir}/doc/latex/apa6/pseudoTeX/apa6.ptex
%doc %{_texmfdistdir}/doc/latex/apa6/samples/Figure1.pdf
%doc %{_texmfdistdir}/doc/latex/apa6/samples/bibliography.bib
%doc %{_texmfdistdir}/doc/latex/apa6/samples/longsample.tex
%doc %{_texmfdistdir}/doc/latex/apa6/samples/shortsample.tex
#- source
%doc %{_texmfdistdir}/source/latex/apa6/apa6.dtx
%doc %{_texmfdistdir}/source/latex/apa6/apa6.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
