# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/tetratelabs/wazero
%global goipath         github.com/tetratelabs/wazero
Version:                1.8.0

%gometa -f

%global common_description %{expand:
Wazero: the zero dependency WebAssembly runtime for Go developers.}

%global golicenses      LICENSE NOTICE
%global godocs          examples CONTRIBUTING.md RATIONALE.md README.md\\\
                        cmd/wazero/README.md imports/README.md example\\\
                        example site/README.md docs site/content/_index.md\\\
                        site/content/specs.md\\\
                        site/content/community/_index.md\\\
                        site/content/community/history.md\\\
                        site/content/community/users.md\\\
                        site/content/languages/_index.md\\\
                        site/content/languages/rust.md\\\
                        site/content/languages/tinygo.md\\\
                        site/content/languages/zig.md

Name:           golang-github-tetratelabs-wazero
Release:        %autorelease
Summary:        Wazero: the zero dependency WebAssembly runtime for Go developers

License:        Apache-2.0
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

%if %{without bootstrap}
%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%endif

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%if %{without bootstrap}
%files
%license LICENSE NOTICE
%doc examples CONTRIBUTING.md RATIONALE.md README.md cmd/wazero/README.md
%doc imports/README.md example example site/README.md docs
%doc site/content/_index.md site/content/specs.md
%doc site/content/community/_index.md site/content/community/history.md
%doc site/content/community/users.md site/content/languages/_index.md
%doc site/content/languages/rust.md site/content/languages/tinygo.md
%doc site/content/languages/zig.md
#%%{_bindir}/*
%endif

%gopkgfiles

%changelog
%autochangelog
