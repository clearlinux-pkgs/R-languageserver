#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-languageserver
Version  : 0.3.10
Release  : 16
URL      : https://cran.r-project.org/src/contrib/languageserver_0.3.10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/languageserver_0.3.10.tar.gz
Summary  : Language Server Protocol
Group    : Development/Tools
License  : MIT
Requires: R-languageserver-lib = %{version}-%{release}
Requires: R-R6
Requires: R-callr
Requires: R-collections
Requires: R-desc
Requires: R-fs
Requires: R-jsonlite
Requires: R-lintr
Requires: R-repr
Requires: R-roxygen2
Requires: R-stringi
Requires: R-styler
Requires: R-xml2
Requires: R-xmlparsedata
BuildRequires : R-R6
BuildRequires : R-callr
BuildRequires : R-collections
BuildRequires : R-desc
BuildRequires : R-fs
BuildRequires : R-jsonlite
BuildRequires : R-lintr
BuildRequires : R-repr
BuildRequires : R-roxygen2
BuildRequires : R-stringi
BuildRequires : R-styler
BuildRequires : R-xml2
BuildRequires : R-xmlparsedata
BuildRequires : buildreq-R

%description
for R. The Language Server protocol is used by an editor client to
    integrate features like auto completion. See

%package lib
Summary: lib components for the R-languageserver package.
Group: Libraries

%description lib
lib components for the R-languageserver package.


%prep
%setup -q -c -n languageserver
cd %{_builddir}/languageserver

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618930458

%install
export SOURCE_DATE_EPOCH=1618930458
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library languageserver
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library languageserver
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library languageserver
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc languageserver || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/languageserver/DESCRIPTION
/usr/lib64/R/library/languageserver/INDEX
/usr/lib64/R/library/languageserver/LICENSE
/usr/lib64/R/library/languageserver/Meta/Rd.rds
/usr/lib64/R/library/languageserver/Meta/features.rds
/usr/lib64/R/library/languageserver/Meta/hsearch.rds
/usr/lib64/R/library/languageserver/Meta/links.rds
/usr/lib64/R/library/languageserver/Meta/nsInfo.rds
/usr/lib64/R/library/languageserver/Meta/package.rds
/usr/lib64/R/library/languageserver/NAMESPACE
/usr/lib64/R/library/languageserver/NEWS.md
/usr/lib64/R/library/languageserver/R/languageserver
/usr/lib64/R/library/languageserver/R/languageserver.rdb
/usr/lib64/R/library/languageserver/R/languageserver.rdx
/usr/lib64/R/library/languageserver/help/AnIndex
/usr/lib64/R/library/languageserver/help/aliases.rds
/usr/lib64/R/library/languageserver/help/languageserver.rdb
/usr/lib64/R/library/languageserver/help/languageserver.rdx
/usr/lib64/R/library/languageserver/help/paths.rds
/usr/lib64/R/library/languageserver/html/00Index.html
/usr/lib64/R/library/languageserver/html/R.css
/usr/lib64/R/library/languageserver/projects/mypackage/DESCRIPTION
/usr/lib64/R/library/languageserver/projects/mypackage/NAMESPACE
/usr/lib64/R/library/languageserver/projects/mypackage/R/mypackage.R
/usr/lib64/R/library/languageserver/tests/testthat.R
/usr/lib64/R/library/languageserver/tests/testthat/helper-utils.R
/usr/lib64/R/library/languageserver/tests/testthat/test-call-hierarchy.R
/usr/lib64/R/library/languageserver/tests/testthat/test-codeunits.R
/usr/lib64/R/library/languageserver/tests/testthat/test-color.R
/usr/lib64/R/library/languageserver/tests/testthat/test-completion.R
/usr/lib64/R/library/languageserver/tests/testthat/test-definition.R
/usr/lib64/R/library/languageserver/tests/testthat/test-folding.R
/usr/lib64/R/library/languageserver/tests/testthat/test-formatting.R
/usr/lib64/R/library/languageserver/tests/testthat/test-highlight.R
/usr/lib64/R/library/languageserver/tests/testthat/test-hover.R
/usr/lib64/R/library/languageserver/tests/testthat/test-langauagecilent.R
/usr/lib64/R/library/languageserver/tests/testthat/test-link.R
/usr/lib64/R/library/languageserver/tests/testthat/test-lintr.R
/usr/lib64/R/library/languageserver/tests/testthat/test-null-root.R
/usr/lib64/R/library/languageserver/tests/testthat/test-references.R
/usr/lib64/R/library/languageserver/tests/testthat/test-rename.R
/usr/lib64/R/library/languageserver/tests/testthat/test-search.R
/usr/lib64/R/library/languageserver/tests/testthat/test-selection.R
/usr/lib64/R/library/languageserver/tests/testthat/test-signature.R
/usr/lib64/R/library/languageserver/tests/testthat/test-stdio.R
/usr/lib64/R/library/languageserver/tests/testthat/test-symbol.R
/usr/lib64/R/library/languageserver/tests/testthat/test-tcp.R
/usr/lib64/R/library/languageserver/tests/testthat/test-unicode-path.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/languageserver/libs/languageserver.so
