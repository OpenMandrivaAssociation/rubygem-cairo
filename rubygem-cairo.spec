# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	cairo

Summary:	Ruby binding of cairo
Name:		rubygem-%{rbname}

Version:	1.12.9
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
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
%setup -q

%build
%gem_build

%install
%gem_install

%files
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/%{rbname}/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/%{rbname}/context/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_sitearchdir}/%{rbname}.so

%files doc
%doc %{gem_dir}/doc/%{rbname}-%{version}
%doc %{gem_dir}/gems/%{rbname}-%{version}/README.rdoc

%files devel
%{ruby_sitearchdir}/*.h


%changelog

