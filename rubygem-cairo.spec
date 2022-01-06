
Summary:	Ruby binding of cairo
Name:		rubygem-cairo

Version:	1.17.5
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:  pkgconfig(cairo)
BuildRequires:  rubygem-pkg-config
BuildRequires:  ruby-devel
BuildRequires:	rubygem-native-package-installer
Obsoletes:      ruby-cairo = 1.12.9

%description
Ruby binding of cairo.

%package    devel
Summary:    Development files for %{name}
Group:      Development/Ruby

%description	devel
Development files for %{name}.

%prep
%autosetup -p1 -n  %{gem_name}-%{version}

%build
%gem_build

%install
%gem_install 

%files
%{gem_files}

%files devel
%{gem_extdir_mri}/*.h
