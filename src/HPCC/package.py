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