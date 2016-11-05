#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-htmltools
Version  : 0.3.5
Release  : 3
URL      : https://cran.r-project.org/src/contrib/htmltools_0.3.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/htmltools_0.3.5.tar.gz
Summary  : Tools for HTML
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-htmltools-lib
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-htmltools package.
Group: Libraries

%description lib
lib components for the R-htmltools package.


%prep
%setup -q -c -n htmltools

%build
export LANG=C

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library htmltools
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/htmltools/DESCRIPTION
/usr/lib64/R/library/htmltools/INDEX
/usr/lib64/R/library/htmltools/Meta/Rd.rds
/usr/lib64/R/library/htmltools/Meta/hsearch.rds
/usr/lib64/R/library/htmltools/Meta/links.rds
/usr/lib64/R/library/htmltools/Meta/nsInfo.rds
/usr/lib64/R/library/htmltools/Meta/package.rds
/usr/lib64/R/library/htmltools/NAMESPACE
/usr/lib64/R/library/htmltools/NEWS
/usr/lib64/R/library/htmltools/R/htmltools
/usr/lib64/R/library/htmltools/R/htmltools.rdb
/usr/lib64/R/library/htmltools/R/htmltools.rdx
/usr/lib64/R/library/htmltools/help/AnIndex
/usr/lib64/R/library/htmltools/help/aliases.rds
/usr/lib64/R/library/htmltools/help/htmltools.rdb
/usr/lib64/R/library/htmltools/help/htmltools.rdx
/usr/lib64/R/library/htmltools/help/paths.rds
/usr/lib64/R/library/htmltools/html/00Index.html
/usr/lib64/R/library/htmltools/html/R.css
/usr/lib64/R/library/htmltools/tests/test-all.R
/usr/lib64/R/library/htmltools/tests/testthat/template-document.html
/usr/lib64/R/library/htmltools/tests/testthat/test-deps.r
/usr/lib64/R/library/htmltools/tests/testthat/test-tags.r
/usr/lib64/R/library/htmltools/tests/testthat/test-template.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/htmltools/libs/htmltools.so
