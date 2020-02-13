# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	gem_name	cairo

Summary:	Ruby binding of cairo
Name:		rubygem-%{gem_name}

Version:	1.14.1
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:  pkgconfig(cairo)
BuildRequires:  rubygem(pkg-config)
BuildRequires:  ruby-devel
Obsoletes:      ruby-cairo

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
%setup -q  -c -T

%gem_install -n %{SOURCE0}

%build
#%%gem_build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gem_dir} %{buildroot}%{gem_archdir}

cp -a .%{gem_dir}/* \
    %{buildroot}/%{gem_dir}/

cp -a .%{gem_archdir}/* \
    %{buildroot}/%{gem_archdir}/

/bin/rm -r %{buildroot}/%{gem_dir}/gems/%{gem_name}-%{version}/ext/

%files
%{gem_dir}/gems/%{gem_name}-%{version}/lib/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/lib/%{gem_name}/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/lib/%{gem_name}/context/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/samples/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/samples/agg/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/test/*.rb
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%{gem_dir}/cache/*.gem
%{gem_extdir_mri}/%{gem_name}.so
%exclude %{gem_extdir_mri}/gem_make.out
%exclude %{gem_extdir_mri}/mkmf.log
%exclude %{gem_extdir_mri}/gem.build_complete
#%exclude %{gem_dir}/Rakefile
%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_dir}/gems/%{gem_name}-%{version}/[A-Z]*


%files devel
%{gem_extdir_mri}/*.h


%changelog

