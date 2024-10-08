# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/giantswarm/crd-docs-generator
%global goipath         github.com/giantswarm/crd-docs-generator
Version:                0.11.1

%gometa -f

%global common_description %{expand:
Tooling to create user-friendly reference documentation for Kubernetes Custom
Resource Definitions (CRDs).}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-giantswarm-crd-docs-generator
Release:        %autorelease
Summary:        Tooling to create user-friendly reference documentation for Kubernetes Custom Resource Definitions (CRDs)

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%if %{without bootstrap}
%build
%gobuild -o %{gobuilddir}/bin/crd-docs-generator %{goipath}
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%endif

# Tests require git and internet access to complete. Disabled
#%%if %{without bootstrap}
#%%if %{with check}
#%%check
#%%gocheck
#%%endif
#%%endif

%if %{without bootstrap}
%files
%license LICENSE
%doc README.md
%{_bindir}/crd-docs-generator
%endif

%gopkgfiles

%changelog
%autochangelog
