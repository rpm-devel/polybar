#
# spec file for package polybar
#

Name:           polybar
Version:        3.7.2
Release:        1%{?dist}
Summary:        A fast and easy-to-use status bar
License:        MIT
URL:            https://github.com/polybar/polybar
Source:         https://github.com/polybar/polybar/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.1
BuildRequires:  pkgconfig
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-wm-devel
# optional dependency
BuildRequires:  pkgconfig(alsa)
# main dependency
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  wireless-tools-devel

%description
A fast and easy-to-use status bar for tilling WM

%prep
%setup -q

%build
%cmake
make

%install
%cmake_install

%files
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions
%dir %{_datadir}/doc/%{name}
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions
%{_bindir}/%{name}
%{_bindir}/%{name}-msg
%{_datadir}/doc/%{name}/config
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/zsh/site-functions/_%{name}_msg

%changelog
* Fri Apr 24 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 3.7.2-1
- Update to 3.7.2
- Modernize spec for EL10
