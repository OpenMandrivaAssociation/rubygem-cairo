
%define	gem_name	cairo

Summary:	Ruby binding of cairo
Name:		rubygem-%{gem_name}

Version:	1.16.5
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	rubygems-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  rubygem(pkg-config)
BuildRequires:  ruby-devel
BuildRequires:	rubygem-native-package-installer
Obsoletes:      ruby-cairo = 1.12.9

%description
Ruby binding of cairo.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%package    devel
Summary:    Development files for %{name}
Group:      Development/Ruby

%description	devel
Development files for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}



%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install 

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gem_dir} %{buildroot}%{gem_extdir_mri}

/bin/rm -r .%{gem_dir}/gems/%{gem_name}-%{version}/ext/

cp -a .%{gem_dir}/* \
    %{buildroot}/%{gem_dir}/

cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so,*.h} \
    %{buildroot}/%{gem_extdir_mri}/


%files
%{gem_dir}/gems/%{gem_name}-%{version}/lib/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/lib/%{gem_name}/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/lib/%{gem_name}/context/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/samples/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/samples/agg/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/test/*.rb
%{gem_spec}
%{gem_dir}/cache/*.gem
%{gem_extdir_mri}/%{gem_name}.so
%{gem_extdir_mri}/%{gem_name}gem_build_complete
%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_dir}/gems/%{gem_name}-%{version}/[A-Z]*


%files devel
%{gem_extdir_mri}/*.h
