#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-htmltools
Version  : 0.5.2
Release  : 64
URL      : https://cran.r-project.org/src/contrib/htmltools_0.5.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/htmltools_0.5.2.tar.gz
Summary  : Tools for HTML
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-htmltools-lib = %{version}-%{release}
Requires: R-base64enc
Requires: R-digest
Requires: R-fastmap
Requires: R-rlang
BuildRequires : R-base64enc
BuildRequires : R-digest
BuildRequires : R-fastmap
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-htmltools package.
Group: Libraries

%description lib
lib components for the R-htmltools package.


%prep
%setup -q -c -n htmltools
cd %{_builddir}/htmltools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641033448

%install
export SOURCE_DATE_EPOCH=1641033448
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library htmltools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library htmltools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library htmltools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/htmltools/DESCRIPTION
/usr/lib64/R/library/htmltools/INDEX
/usr/lib64/R/library/htmltools/Meta/Rd.rds
/usr/lib64/R/library/htmltools/Meta/features.rds
/usr/lib64/R/library/htmltools/Meta/hsearch.rds
/usr/lib64/R/library/htmltools/Meta/links.rds
/usr/lib64/R/library/htmltools/Meta/nsInfo.rds
/usr/lib64/R/library/htmltools/Meta/package.rds
/usr/lib64/R/library/htmltools/NAMESPACE
/usr/lib64/R/library/htmltools/NEWS.md
/usr/lib64/R/library/htmltools/R/htmltools
/usr/lib64/R/library/htmltools/R/htmltools.rdb
/usr/lib64/R/library/htmltools/R/htmltools.rdx
/usr/lib64/R/library/htmltools/help/AnIndex
/usr/lib64/R/library/htmltools/help/aliases.rds
/usr/lib64/R/library/htmltools/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/htmltools/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/htmltools/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/htmltools/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/htmltools/help/figures/logo.png
/usr/lib64/R/library/htmltools/help/figures/plotly-taglist.png
/usr/lib64/R/library/htmltools/help/htmltools.rdb
/usr/lib64/R/library/htmltools/help/htmltools.rdx
/usr/lib64/R/library/htmltools/help/paths.rds
/usr/lib64/R/library/htmltools/html/00Index.html
/usr/lib64/R/library/htmltools/html/R.css
/usr/lib64/R/library/htmltools/tests/test-all.R
/usr/lib64/R/library/htmltools/tests/testthat/_snaps/tag-query.md
/usr/lib64/R/library/htmltools/tests/testthat/_snaps/tags.md
/usr/lib64/R/library/htmltools/tests/testthat/colors-bad.txt
/usr/lib64/R/library/htmltools/tests/testthat/colors-good-expected.txt
/usr/lib64/R/library/htmltools/tests/testthat/colors-good.txt
/usr/lib64/R/library/htmltools/tests/testthat/helper-locale.R
/usr/lib64/R/library/htmltools/tests/testthat/helper-tags.R
/usr/lib64/R/library/htmltools/tests/testthat/template-basic.html
/usr/lib64/R/library/htmltools/tests/testthat/template-document.html
/usr/lib64/R/library/htmltools/tests/testthat/test-colors.R
/usr/lib64/R/library/htmltools/tests/testthat/test-deps.r
/usr/lib64/R/library/htmltools/tests/testthat/test-images.R
/usr/lib64/R/library/htmltools/tests/testthat/test-print.R
/usr/lib64/R/library/htmltools/tests/testthat/test-selector.R
/usr/lib64/R/library/htmltools/tests/testthat/test-tag-query.R
/usr/lib64/R/library/htmltools/tests/testthat/test-tags.r
/usr/lib64/R/library/htmltools/tests/testthat/test-template.R
/usr/lib64/R/library/htmltools/tests/testthat/test-textwriter.r
/usr/lib64/R/library/htmltools/tests/testthat/test-whitespace.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/htmltools/libs/htmltools.so
/usr/lib64/R/library/htmltools/libs/htmltools.so.avx2
/usr/lib64/R/library/htmltools/libs/htmltools.so.avx512
