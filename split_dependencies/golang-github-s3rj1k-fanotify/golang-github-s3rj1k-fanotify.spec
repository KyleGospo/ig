# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/s3rj1k/go-fanotify
%global goipath         github.com/s3rj1k/go-fanotify
Version:                1.1.0

%gometa -f

%global common_description %{expand:
Golang fanotify example.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-s3rj1k-fanotify
Release:        %autorelease
Summary:        Golang fanotify example

License:        MIT
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