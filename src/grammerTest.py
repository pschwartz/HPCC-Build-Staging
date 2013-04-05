from __future__ import print_function
from parsley import makeGrammar
from HPCC.package import Package

with open('grammer/package.parsley') as f:
    packageNameGrammar = f.read()

#  version = :ver ?(ver in ubuntu_versions) -> x

packages = ['hpccsystems-platform_community-4.0.0-0.el5.x86_64.rpm',
            'hpccsystems-platform_community-4.0.0-rc2precise_amd64.deb',
            'hpccsystems-platform_community-3.10.5-1closedown.el5.x86_64.rpm',
            'hpccsystems-platform_community-3.10.7-1closedown.el5.x86_64.rpm',
            'hpccsystems-eclide_community-4.1.0-closedown0Windows-i386.exe']

version = ['el5', 'el6', 'suse12.2', 'suse12.3', 'lucid', 'oneiric',
           'precise', 'quantal', 'squeeze','Windows']
arch = ['i686', 'x86_64', 'i386', 'amd64']
ext = ['rpm', 'deb', 'msi', 'zip', 'exe', 'dmg']

config = {
  'version': version,
  'arch': arch,
  'ext': ext
}

PackageName = makeGrammar(packageNameGrammar, config, name="PackageName")

for package in packages:
    packageInfo = Package.PackageFactory(package, **(PackageName(package).package()))
    print(packageInfo.toDict())
    print(packageInfo.dist)
    print(packageInfo)
    print(packageInfo.name)

#print(globals())
