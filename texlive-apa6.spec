Name:		texlive-apa6
Version:	67848
Release:	1
Summary:	Format documents in APA style (6th edition)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/apa6
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apa6.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/apa6
%doc %{_texmfdistdir}/doc/latex/apa6
#- source
%doc %{_texmfdistdir}/source/latex/apa6

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
