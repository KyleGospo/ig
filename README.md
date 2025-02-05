# Bumping Inspektor Gadget in Fedora

This document describes how to bump Inspektor Gadget in Fedora.
The whole process can be achieved in a fedora container ran as the following:

```bash
$ docker run -ti --rm -v $(pwd):/work -w /work fedora
```

## Tools needed

Along this process, you would need several tools available in different packages:

```bash
$ sudo dnf install -y fedora-packager go go-rpm-macros go-vendor-tools trivy
```

## Updating the version

The following line needs to be updated to reflect the version bump:

```rpm
...
%global goipath         github.com/inspektor-gadget/inspektor-gadget
Version:                0.37.0
...
```

## Getting the sources

We first need to fetch the latest source:

```bash
$ spectool -g inspektor-gadget.spec
...
Downloaded: inspektor-gadget-0.37.0.tar.gz
```

We should now get all the dependencies and create an archive for them:

```bash
$ go_vendor_archive create inspektor-gadget.spec
* Treating /work/inspektor-gadget-0.37.0.tar.gz as an archive. Unpacking...
$ go mod tidy
...
$ go mod vendor
Creating archive...
```

This operation should have created the `inspektor-gadget-0.37.0.tar.gz` and `inspektor-gadget-0.37.0-vendor.tar.xz` archives:

```bash
$ ls -1
go-vendor-tools.toml
inspektor-gadget-0.37.0-vendor.tar.xz
inspektor-gadget-0.37.0.tar.gz
inspektor-gadget.spec
```

## Building the package

We have all the files needed to build the package, let's build it:

```bash
$ fedpkg --release f40 local
...
Wrote: .../inspektor-gadget-0.37.0-1.fc40.src.rpm
Wrote: .../x86_64/inspektor-gadget-debugsource-0.37.0-1.fc40.x86_64.rpm
Wrote: .../x86_64/inspektor-gadget-0.37.0-1.fc40.x86_64.rpm
...
```

Everything was built and tested, you should now have the package available:

```bash
$ rpm -ql x86_64/inspektor-gadget-0.37.0-1.fc40.x86_64.rpm
/usr/bin/ig
...
/usr/share/licenses/inspektor-gadget
/usr/share/licenses/inspektor-gadget/LICENSE
/usr/share/licenses/inspektor-gadget/LICENSE-bpf.txt
...
```

Congratulations! You successfully built Inspektor Gadget Fedora package!

## Testing in a Container

Let's now test `ig` in-situ:

```bash
$ docker run -ti --rm -v $(pwd):/work -w /work fedora
# Install the new package
[root@139a35ba4247 work]# dnf install -y x86_64/inspektor-gadget-0.37.0-1.fc40.x86_64.rpm
...
Complete!
[root@139a35ba4247 work]# ig --help
Collection of gadgets for containers

Usage:
  ig [command]

...
```
