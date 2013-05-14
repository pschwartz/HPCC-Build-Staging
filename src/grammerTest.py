from __future__ import print_function
from parsley import makeGrammar
from HPCC.package import Package
from HPCC.config import Config

with open('grammer/package.parsley') as f:
    packageNameGrammar = f.read()

packages = ['hpccsystems-platform_community-4.0.0-0.el5.x86_64.rpm',
            'hpccsystems-platform_community-4.0.0-rc2precise_amd64.deb',
            'hpccsystems-platform_community-3.10.5-1closedown.el5.x86_64.rpm',
            'hpccsystems-platform_community-3.10.7-1closedown.el5.x86_64.rpm',
            'hpccsystems-eclide_community-4.1.0-closedown0Windows-i386.exe']

conf = Config('build-staging.json')

PackageName = makeGrammar(packageNameGrammar, conf.parsley, name="PackageName")

for package in packages:
    packageInfo = Package.PackageFactory(package, config=conf, **(PackageName(package).package()))
    print(packageInfo.toDict())
    print(packageInfo.dist)
    print(packageInfo)
    print(packageInfo.name)
