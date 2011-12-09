# revision 24723
# category Package
# catalog-ctan /macros/latex/contrib/apa6
# catalog-date 2011-12-02 13:40:26 +0100
# catalog-license lppl1.3
# catalog-version 1.02
Name:		texlive-apa6
Version:	1.02
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
The class provides a full set of facilities in three different
output modes (journal-like appearance, double-spaced
manuscript, LaTeX-like document), in contrast to the earlier
apa6e, which only formats double-spaced manuscripts in APA
style. The class formats documents in APA style (6th Edition).
It is built on the apa class (which is no longer maintained),
and has been updated to comply with 6th-Edition requirements.
The class can mask author identity for copies for use in masked
peer review.

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/apa6/apa6.cls
%{_texmfdistdir}/tex/latex/apa6/config/APAamerican.txt
%{_texmfdistdir}/tex/latex/apa6/config/APAdutch.txt
%{_texmfdistdir}/tex/latex/apa6/config/APAendfloat.cfg
%{_texmfdistdir}/tex/latex/apa6/config/APAenglish.txt
%{_texmfdistdir}/tex/latex/apa6/config/APAgreek.txt
%doc %{_texmfdistdir}/doc/latex/apa6/README
%doc %{_texmfdistdir}/doc/latex/apa6/apa6.pdf
%doc %{_texmfdistdir}/doc/latex/apa6/pseudoTeX/apa6.ptex
%doc %{_texmfdistdir}/doc/latex/apa6/samples/Figure1.pdf
%doc %{_texmfdistdir}/doc/latex/apa6/samples/bibliography.bib
%doc %{_texmfdistdir}/doc/latex/apa6/samples/longsample.pdf
%doc %{_texmfdistdir}/doc/latex/apa6/samples/longsample.tex
%doc %{_texmfdistdir}/doc/latex/apa6/samples/shortsample.pdf
%doc %{_texmfdistdir}/doc/latex/apa6/samples/shortsample.tex
#- source
%doc %{_texmfdistdir}/source/latex/apa6/apa6.dtx
%doc %{_texmfdistdir}/source/latex/apa6/apa6.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
