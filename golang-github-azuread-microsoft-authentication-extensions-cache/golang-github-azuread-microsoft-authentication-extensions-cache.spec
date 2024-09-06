# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/AzureAD/microsoft-authentication-extensions-for-go
%global goipath         github.com/AzureAD/microsoft-authentication-extensions-for-go
Version:                0.1.1
%global tag             cache/v0.1.1

%gometa -f

%global common_description %{expand:
Secure cross-platform token cache for MSAL public client apps.}

%global golicenses      LICENSE
%global godocs          cache/README.md

Name:           golang-github-azuread-microsoft-authentication-extensions-cache
Release:        %autorelease
Summary:        Secure cross-platform token cache for MSAL public client apps

License:        BSD-3-Clause AND MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

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