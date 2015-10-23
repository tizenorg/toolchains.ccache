#
# spec file for package ccache
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           ccache
Version:        3.1.6
Release:        %{?release_prefix:%{release_prefix}.}1.45.%{?dist}%{!?dist:tizen}
VCS:            external/ccache#submit/trunk/20121019.073148-0-g536e9709d258b29d750fb49566c21895e8c73815
Summary:        A Fast C/C++ Compiler Cache

License:        GPLv3+
Url:            http://ccache.samba.org/
Group:          Development/Languages/C and C++
Source0:        http://samba.org/ftp/ccache/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  zlib-devel
Provides:       distcc:/usr/bin/ccache

%description
ccache is a compiler cache. It speeds up recompilation by caching the result of
previous compilations and detecting when the same compilation is being done
again. Supported languages are C, C++, Objective-C and Objective-C++.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS.* GPL-3.0.txt INSTALL.* LICENSE.* MANUAL.* NEWS.* README.*
%doc %{_mandir}/man1/ccache.1%{ext_man}
%{_bindir}/ccache

%changelog
* Mon Sep 16 2013 UkJung Kim <ujkim@samsung.com> - submit/trunk/20121019.073148 
- PROJECT: external/ccache
- COMMIT_ID: 536e9709d258b29d750fb49566c21895e8c73815
- PATCHSET_REVISION: 536e9709d258b29d750fb49566c21895e8c73815
- CHANGE_OWNER: \"UkJung Kim\" <ujkim@samsung.com>
- PATCHSET_UPLOADER: \"UkJung Kim\" <ujkim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/103321
- PATCHSET_REVISION: 536e9709d258b29d750fb49566c21895e8c73815
- TAGGER: UkJung Kim <ujkim@samsung.com>
- Gerrit patchset approval info:
- UkJung Kim <ujkim@samsung.com> Verified : 1
- Newton Lee <newton.lee@samsung.com> Code Review : 2
- CHANGE_SUBJECT: Initial commit
- [Version] 3.1.6
- [Project] GT-I8800
- [Title] Initial commit
- [BinType] PDA
- [Customer] Open
- [Issue#] N/A
- [Problem] N/A
- [Cause] N/A
- [Solution]
- [Team] SCM
- [Developer] UkJung Kim <ujkim@samsung.com>
- [Request] N/A
- [Horizontal expansion] N/A
- [SCMRequest] N/A
* Sun Aug 21 2011 asterios.dramis@gmail.com
- update to ccache-3.1.6
  - Rewrite argument to --sysroot if CCACHE_BASEDIR is used.
  - Don't crash if getcwd() fails.
  - Fixed alignment of "called for preprocessing" counter.
* Mon Jun  6 2011 puzel@novell.com
- update to ccache-3.1.5
  - Added a new statistics counter named ``called for
    preprocessing''.
  - The original command line is now logged to the file specified
    with `CCACHE_LOGFILE`.
  - Improved error logging when system calls fail.
  - Added support for rewriting absolute paths in
    `-F`/`-iframework` GCC options.
  - Improved order of statistics counters in `ccache -s` output.
  - The `-MF`/`-MT`/`-MQ` options with concatenated argument are
    now handled correctly when they are last on the commandline.
  - ccache is now bug compatible with GCC for the `-MT`/`-MQ`
    options with concatenated arguments.
  - Fixed a minor memory leak.
  - Systems that lack (and don't need to be linked with) libm are
    now supported.
* Wed Feb 16 2011 asterios.dramis@gmail.com
- update to ccache-3.1.4
  - Made a work-around for a bug in gzputc() in zlib 1.2.5.
  - Corrupt manifest files are now removed so that they won't block direct
    mode hits.
  - ccache now copes with file systems that don't know about symbolic links.
  - The file handle in now correctly closed on write error when trying to
    create a cache dir tag.
- Spec file updates:
  - Changes based on rpmdevtools templates and spec-cleaner run.
  - Updated Summary: and %%description.
  - Made it compile with external zlib instead of the bundled copy.
  - Added also the html files in the %%doc section.
* Mon Nov 29 2010 puzel@novell.com
- update to ccache-3.1.3
  - The -MFarg, -MTarg and -MQarg compiler options (i.e, without
    space between option and argument) are now handled correctly.
* Mon Nov 22 2010 puzel@novell.com
- update to ccache-3.1.2
  - bail out on too hard compiler options '-fdump-*'
  - NULL return values from malloc/calloc of zero bytes are now
    handled correctly
  - improved documentation on which information is included in the
    hash sum
  - made the 'too new header file' test case work on file systems
    with unsynchronized clocks
  - the test suite now also works on systems that lack a /dev/zero
* Mon Nov  8 2010 puzel@novell.com
- update to ccache-3.1.1
  - ccache now falls back to preprocessor mode when a non-regular
    include file (device, socket, etc) has been detected so that
    potential hanging due to blocking reads is avoided.
  - CRC errors are now detected when decompressing compressed files
    in the cache.
  - Fixed potential object file corruption race on NFS.
  - Minor documentation corrections.
  - Fixed configure detection of ar.
  - ccache development version (set by dev.mk) now works with gits
    whose `describe` command doesn't understand `--dirty`.
* Fri Sep 17 2010 puzel@novell.com
- update to ccache-3.1
  - features:
  - Added support for hashing the output of a custom command
    (e.g. `$compiler --version`) to identify the compiler
    instead of stat-ing or hashing the compiler binary.
  - Added support for caching compilations that use precompiled
    headers.
  - Locking of the files containing statistics counters is now
    done using symlinks instead of POSIX locks.
  - Manifest files are now updated without the need of taking
    locks.
  - Added `.cp` and `.CP` as known C++ suffixes.
  - Improved logging.
  - bugfixes:
  - Non-fatal error messages are now never printed to stderr but
    logged instead.
  - Fixed a bug affecting failing commands when `--ccache-skip` is
    used.
  - Made `--ccache-skip` work for all options.
  - EINTR is now handled correctly.
* Fri Jul 16 2010 puzel@novell.com
- update to ccache-3.0.1
  - bugfixes:
  - The statistics counter ``called for link'' is now correctly
    updated when linking with a single object file.
  - Fixed a problem with out-of-source builds.
* Mon Jul 12 2010 puzel@novell.com
- update to ccache-3.0
  - notable changes:
  - The way the hashes are calculated has changed, so you won't get
  cache hits for compilation results stored by older ccache
  versions. Because of this, you might as well clear the old
  cache directory with `ccache --clear` if you want, unless you
  plan to keep using an older ccache version.
  - ccache now has a ``direct mode'' where it computes a hash of
  the source code (including all included files) and compiler
  options without running the preprocessor. By not running the
  preprocessor, CPU usage is reduced; the speed is somewhere
  between 1 and 5 times that of ccache running in traditional
  mode, depending on the circumstances. The speedup will be
  higher when I/O is fast (e.g., when files are in the disk
  cache).  The direct mode can be disabled by setting
  +CCACHE_NODIRECT+.
  - Support has been added for rewriting absolute paths to relative
  paths when hashing, in order to increase cache hit rate when
  building the same source code in different directories even
  when compiling with `-g` and when using absolute include
  directory paths. This is done by setting the `CCACHE_BASEDIR`
  environment variable to an absolute path that specifies which
  paths to rewrite.
  - Object files are now optionally stored compressed in the cache.
  The runtime cost is negligible, and more files will fit in the
  ccache directory and in the disk cache. Set `CCACHE_COMPRESS`
  to enable object file compression. Note that you can't use
  compression in combination with the hard link feature.
  - A `CCACHE_COMPILERCHECK` option has been added. This option
  tells ccache what compiler-identifying information to hash to
  ensure that results retrieved from the cache are accurate.
  Possible values are: none (don't hash anything), mtime (hash
  the compiler's mtime and size) and content (hash the content of
  the compiler binary). The default is mtime.
- see /usr/share/doc/packages/ccache/NEWS.txt for complete
  release notes
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Sep 29 2005 dmueller@suse.de
- add norootforbuild
* Wed Sep 28 2005 dmueller@suse.de
- add norootforbuild
* Thu Oct 21 2004 ltinkl@suse.cz
- update to version 2.4
* Mon Sep 29 2003 ltinkl@suse.cz
- update to version 2.3
* Wed Jul  9 2003 ltinkl@suse.cz
- updated sources to version 2.2
* Fri Mar 28 2003 vbobek@suse.cz
- provides binary from older distcc package [#25806]
* Mon Feb 10 2003 vbobek@suse.cz
- initial suse release 2.1.1
