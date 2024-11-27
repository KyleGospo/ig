# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/sigstore/sigstore
%global goipath         github.com/sigstore/sigstore
Version:                1.8.9

%gometa -f

%global common_description %{expand:
Common go library shared across sigstore services and clients.}

%global golicenses      COPYRIGHT.txt LICENSE
%global godocs          docs README.md

Name:           golang-github-sigstore
Release:        %autorelease
Summary:        Common go library shared across sigstore services and clients

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

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog