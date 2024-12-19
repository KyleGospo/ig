# Generated by go2rpm 1.14.0 (and then modified for go-vendor-tools)

# https://github.com/inspektor-gadget/inspektor-gadget
# https://github.com/microsoft/azurelinux/tree/3.0/SPECS/ig
%global goipath         github.com/inspektor-gadget/inspektor-gadget
Version:                0.34.0

%gometa -L -f

Name:           golang-github-inspektor-gadget
Release:        %autorelease
Summary:        Inspektor Gadget is a set of tools and framework for data collection and system inspection on Kubernetes clusters and Linux hosts using eBPF
# Validated by trivy
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}

%global _description %{expand:
Inspektor Gadget is a collection of tools (or gadgets) to debug and inspect
Kubernetes resources and applications.
It manages the packaging, deployment and execution of eBPF programs in a
Kubernetes cluster, including many based on BCC tools, as well as some
developed specifically for use in Inspektor Gadget.
It automatically maps low-level kernel primitives to high-level Kubernetes
resources, making it easier and quicker to find the relevant information.

This package contains ig, the local CLI flavor of Inspektor Gadget.
}

# spectool -g golang-github-inspektor-gadget.spec
Source0:        %{gosource}
# go_vendor_archive create golang-github-inspektor-gadget.spec 
Source1:        %{archivename}-vendor.tar.xz
# Fix for trivy being unable to detect some licenses
# go_vendor_license --config go-vendor-tools.toml explicit -f vendor/github.com/go-errors/errors/LICENSE.MIT MIT
# go_vendor_license --config go-vendor-tools.toml explicit -f vendor/github.com/google/shlex/COPYING Apache-2.0
# go_vendor_license --config go-vendor-tools.toml explicit -f vendor/github.com/BurntSushi/toml/COPYING MIT
Source2:        go-vendor-tools.toml

BuildRequires:  go-vendor-tools

%description
%{_description}

%prep
%goprep -A
# Required to unpack vendor on top of main
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%generate_buildrequires
%go_vendor_license_buildrequires -c %{SOURCE2}

%build
%gobuild -o %{gobuilddir}/bin/build/ig %{goipath}/cmd/ig

%install
%go_vendor_license_install -c %{SOURCE2}

mkdir -p "%{buildroot}/%{_bindir}"
install -D -m0755 bin/build/ig %{buildroot}/%{_bindir}

%check
%go_vendor_license_check -c %{SOURCE2}

set -e
set -o pipefail

# Inspektor Gadget provides unit tests but they rely on several components which
# are not present in the chroot used to build and test the package, among
# others:
# * runc: https://github.com/inspektor-gadget/inspektor-gadget/blob/3c8d1455525b/pkg/container-hook/tracer.go#L302
# * dockerd: https://github.com/inspektor-gadget/inspektor-gadget/blob/3c8d1455525b/pkg/container-utils/testutils/docker.go#L67
# Even if we recreate a proper testing environment, we will still have problems
# as, for example, the path tested will be inside the chroot while ig reports
# the full path from host point of view.
# For all these reasons, we will skip the unit tests and rather run a small
# integration test.
# Moreover, Inspektor Gadget CI covers Azure Linux extensively:
# https://github.com/inspektor-gadget/inspektor-gadget/pull/1186/commits/066bf618d158
if [ -d /sys/kernel/debug/tracing ]; then
  sleep inf &
  sleep_pid=$!
  ./bin/build/ig snapshot process --host | grep -qP "sleep\s+${sleep_pid}"
  kill $sleep_pid
else
  echo "Skipping ig check as prerequisites are not satisfied in the chroot"
fi

%files -f %{go_vendor_license_filelist}
%{_bindir}/ig

%changelog
* Wed Nov 27 2024 Kyle Gospodnetich <kylego@microsoft.com> - 0.34.0-1
- Bump to version 0.34.0

* Tue Oct 15 2024 Muhammad Falak <mwani@microsoft.com> - 0.32.0-2
- Pin golang version to <= 1.22

* Tue Oct 01 2024 Kyle Gospodnetich <kylego@microsoft.com> - 0.32.0-2
- Vendor dependencies with go-vendor-tools for Fedora Linux

* Tue Sep 03 2024 Francis Laniel <flaniel@linux.microsoft.com> - 0.32.0-1
- Bump to version 0.32.0

* Tue Aug 06 2024 Francis Laniel <flaniel@linux.microsoft.com> - 0.31.0-1
- Bump to version 0.31.0

* Mon Jul 01 2024 Francis Laniel <flaniel@linux.microsoft.com> - 0.30.0-1
- Bump to version 0.30.0
- Update how binary version is set while building

* Fri May 31 2024 Francis Laniel <flaniel@linux.microsoft.com> - 0.29.0-1
- Bump to version 0.29.0

* Tue Mar 12 2024 Francis Laniel <flaniel@linux.microsoft.com> - 0.26.0-1
- Bump to version 0.26.0

* Tue Mar 14 2023 Francis Laniel <flaniel@linux.microsoft.com> - 0.25.0-2
- Fix %check.

* Tue Feb 14 2023 Francis Laniel <flaniel@linux.microsoft.com> - 0.25.0-1
- Original version for Azure Linux
- License Verified
