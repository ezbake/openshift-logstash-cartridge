%global cartridgedir %{_libexecdir}/openshift/cartridges/logstash

Summary:        Embedded logstash support for OpenShift
Name:           openshift-origin-cartridge-logstash
Version:        0.0.2
Release:        1%{?dist}
Group:          Development/Languages
License:        ASL 2.0
URL:            https://github.com/ezbake/openshift-logstash-cartridge
Source0:        https://github.com/ezbake/openshift-logstash-cartridge/repository/openshift-logstash-cartridge.tar.gz

Requires:       logstash >= 1.4.2
Requires:       logstash-contrib  >= 1.4.2
Provides:       openshift-origin-cartridge-logstash
BuildArch:      noarch


%description
Logstash cartridge for openshift. (Cartridge Format V2)

%prep
%setup -q -n logstash-cartridge

%build
%__rm -f *.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}


%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}/metadata

%changelog
* Tue Sep 16 2014 Sapan Shah <sshah@42six.com> 0.0.1
- Initial creation
