import hashlib
import os


class Package(object):
    '''
    Object representation of a Package file.
    '''
    def __init__(self, **kwargs):
        self.localCache = dict()
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def name(self):
        return '{0}_{1}-{2}-{3}'.format(self.package,
                                        self.project,
                                        self.version,
                                        self.build)

    def md5(self):
        if not 'md5' in self.localCache:
            md5 = hashlib.md5()
            with open(self.filename) as f:
                for chunk in iter(lambda: f.read(8192), ''):
                    md5.update(chunk)
            self.localCache['md5'] = md5.hexdigest()
        return self.localCache['md5']

    def size(self):
        if not 'size' in self.localCache:
            rawSize = os.path.getsize(self.filename)/(1024 * 1024.0)
            self.localCache['size'] = "{:.1f} MB".format(rawSize)
        return self.localCache['size']

    def toDict(self):
        '''
        Return of a dictionary that is used to build json.
        '''
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
