# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/inspektor-gadget/inspektor-gadget
%global goipath         github.com/inspektor-gadget/inspektor-gadget
Version:                0.32.0

# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
# ---
# New Fedora packages should use %%gometa -f, which makes the package
# ExclusiveArch to %%golang_arches_future and thus excludes the package from
# %%ix86. If the new package is needed as a dependency for another package,
# please consider removing that package from %%ix86 in the same way, instead of
# building more go packages for i686. If your package is not a leaf package,
# you'll need to coordinate the removal of the package's dependents first.
# ---
# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
%gometa -L -f

%global common_description %{expand:
The eBPF tool and systems inspection framework for Kubernetes, containers and
Linux hosts.}

%global golicenses      LICENSE LICENSE-bpf.txt
%global godocs          docs examples CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        MAINTAINERS.md README.md charts/README.md\\\
                        charts/gadget/README.md.gotmpl\\\
                        charts/gadget/templates/NOTES.txt gadgets/README-\\\
                        flags.template gadgets/README.md\\\
                        gadgets/README.template\\\
                        gadgets/audit_seccomp/README.md\\\
                        gadgets/audit_seccomp/README.mdx\\\
                        gadgets/fsnotify/README.md\\\
                        gadgets/fsnotify/README.mdx\\\
                        gadgets/profile_blockio/README.md\\\
                        gadgets/profile_blockio/README.mdx\\\
                        gadgets/snapshot_process/README.md\\\
                        gadgets/snapshot_process/README.mdx\\\
                        gadgets/snapshot_socket/README.md\\\
                        gadgets/snapshot_socket/README.mdx\\\
                        gadgets/top_file/README.md\\\
                        gadgets/top_file/README.mdx gadgets/top_tcp/README.md\\\
                        gadgets/top_tcp/README.mdx\\\
                        gadgets/trace_bind/README.md\\\
                        gadgets/trace_bind/README.mdx\\\
                        gadgets/trace_capabilities/README.md\\\
                        gadgets/trace_capabilities/README.mdx\\\
                        gadgets/trace_dns/README.md\\\
                        gadgets/trace_dns/README.mdx\\\
                        gadgets/trace_exec/README.md\\\
                        gadgets/trace_exec/README.mdx\\\
                        gadgets/trace_lsm/README.md\\\
                        gadgets/trace_lsm/README.mdx\\\
                        gadgets/trace_malloc/README.md\\\
                        gadgets/trace_malloc/README.mdx\\\
                        gadgets/trace_mount/README.md\\\
                        gadgets/trace_mount/README.mdx\\\
                        gadgets/trace_oomkill/README.md\\\
                        gadgets/trace_oomkill/README.mdx\\\
                        gadgets/trace_open/README.md\\\
                        gadgets/trace_open/README.mdx\\\
                        gadgets/trace_signal/README.md\\\
                        gadgets/trace_signal/README.mdx\\\
                        gadgets/trace_sni/README.md\\\
                        gadgets/trace_sni/README.mdx\\\
                        gadgets/trace_ssl/README.md\\\
                        gadgets/trace_ssl/README.mdx\\\
                        gadgets/trace_tcp/README.md\\\
                        gadgets/trace_tcp/README.mdx\\\
                        gadgets/trace_tcpconnect/README.md\\\
                        gadgets/trace_tcpconnect/README.mdx\\\
                        gadgets/trace_tcpdrop/README.md\\\
                        gadgets/trace_tcpdrop/README.mdx\\\
                        gadgets/trace_tcpretrans/README.md\\\
                        gadgets/trace_tcpretrans/README.mdx\\\
                        hack/boilerplate.go.txt\\\
                        pkg/btfgen/btfs/arm64/README.md\\\
                        pkg/btfgen/btfs/x86/README.md examples\\\
                        pkg/gadgets/README.md pkg/gadgets/trace/tcpdrop/trace\\\
                        r/dropreasongen/dropreason.md.tmpl\\\
                        tools/demos/README.md tools/monitoring/README.md

Name:           golang-github-inspektor-gadget
Release:        %autorelease
Summary:        The eBPF tool and systems inspection framework for Kubernetes, containers and Linux hosts

License:        GPL-2.0-only AND Apache-2.0
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
for cmd in gadget-container/cleanup gadget-container/entrypoint gadget-container/gadgettracermanager gadget-container/hooks/nri gadget-container/hooks/oci gadgets/trace_dns/go gadgets/trace_exec/go gadgets/trace_mount/go gadgets/trace_open/go integration/ig/non-k8s integration/k8s pkg/gadgets/trace/tcpdrop/tracer/dropreasongen tools/dnstester tools/eks-cleanup tools/testjson2md; do
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
%license LICENSE LICENSE-bpf.txt
%doc docs examples CODE_OF_CONDUCT.md CONTRIBUTING.md MAINTAINERS.md README.md
%doc charts/README.md charts/gadget/README.md.gotmpl
%doc charts/gadget/templates/NOTES.txt gadgets/README-flags.template
%doc gadgets/README.md gadgets/README.template gadgets/audit_seccomp/README.md
%doc gadgets/audit_seccomp/README.mdx gadgets/fsnotify/README.md
%doc gadgets/fsnotify/README.mdx gadgets/profile_blockio/README.md
%doc gadgets/profile_blockio/README.mdx gadgets/snapshot_process/README.md
%doc gadgets/snapshot_process/README.mdx gadgets/snapshot_socket/README.md
%doc gadgets/snapshot_socket/README.mdx gadgets/top_file/README.md
%doc gadgets/top_file/README.mdx gadgets/top_tcp/README.md
%doc gadgets/top_tcp/README.mdx gadgets/trace_bind/README.md
%doc gadgets/trace_bind/README.mdx gadgets/trace_capabilities/README.md
%doc gadgets/trace_capabilities/README.mdx gadgets/trace_dns/README.md
%doc gadgets/trace_dns/README.mdx gadgets/trace_exec/README.md
%doc gadgets/trace_exec/README.mdx gadgets/trace_lsm/README.md
%doc gadgets/trace_lsm/README.mdx gadgets/trace_malloc/README.md
%doc gadgets/trace_malloc/README.mdx gadgets/trace_mount/README.md
%doc gadgets/trace_mount/README.mdx gadgets/trace_oomkill/README.md
%doc gadgets/trace_oomkill/README.mdx gadgets/trace_open/README.md
%doc gadgets/trace_open/README.mdx gadgets/trace_signal/README.md
%doc gadgets/trace_signal/README.mdx gadgets/trace_sni/README.md
%doc gadgets/trace_sni/README.mdx gadgets/trace_ssl/README.md
%doc gadgets/trace_ssl/README.mdx gadgets/trace_tcp/README.md
%doc gadgets/trace_tcp/README.mdx gadgets/trace_tcpconnect/README.md
%doc gadgets/trace_tcpconnect/README.mdx gadgets/trace_tcpdrop/README.md
%doc gadgets/trace_tcpdrop/README.mdx gadgets/trace_tcpretrans/README.md
%doc gadgets/trace_tcpretrans/README.mdx hack/boilerplate.go.txt
%doc pkg/btfgen/btfs/arm64/README.md pkg/btfgen/btfs/x86/README.md examples
%doc pkg/gadgets/README.md
%doc pkg/gadgets/trace/tcpdrop/tracer/dropreasongen/dropreason.md.tmpl
%doc tools/demos/README.md tools/monitoring/README.md
# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
# ---
# New Fedora packages should not use globs to avoid installing conflicting
# binaries.
# Write a _bindir line per each of the binaries the package will install.
# ---
# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
%{_bindir}/*
%endif

%gopkgfiles

%changelog
%autochangelog