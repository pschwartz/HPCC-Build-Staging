from __future__ import print_function
from parsley import makeGrammar


class Package(object):
    '''
    Object representation of a Package file.
    '''
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def name(self):
        return '{0}_{1}-{2}-{3}'.format(self.package,
                                        self.project,
                                        self.version,
                                        self.build)

    def toDict(self):
        dictVer = self.version + '-' + self.build
        dictRepr = {
            "Download_Size": "",
            "Version_Number": dictVer,
            "Link_Path": "",
            "Display_Name": "",
            "File_Name": self.filename,
            "Link_Text": "",
            "Type": self.package,
            "Edge_Cast_Path": "",
            "OS": "Ubuntu",
            "MD5": ""
        }
        return dictRepr

    def __repr__(self):
        return '<Package ({0})>'.format(self.filename)

    @staticmethod
    def PackageFactory(packageFile, **kwargs):
        kwargs.update({'filename': packageFile})
        return Package(**kwargs)

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
