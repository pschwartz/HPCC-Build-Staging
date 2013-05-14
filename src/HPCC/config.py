from __future__ import print_function
import os
import simplejson as json


class Config(object):
    """Configuration object for HPCC"""

    def __init__(self, confFile):
        self._stat = os.stat(confFile).st_mtime
        with open(confFile) as f:
            self._config = json.load(f)

    @property
    def config(self):
        return self._config

    @property
    def parsley(self):
        def dedupe(seq):
            keys = {}
            for e in seq:
                keys[e] = 1
            return keys.keys()

        platform = self._config['Platforms']
        ext = []
        versions = []
        for plat in platform:
            ext += plat['ext']
            for vers in plat['versions']:
                versions.append(vers['version'])

        ext = dedupe(ext)
        versions = dedupe(versions)

        config = {
            "ext": ext,
            "arch": self._config["arch"],
            "version": versions,
        }
        return config

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__getitem__(attr)
        elif attr in self._config:
            return self._config[attr]
        else:
            raise AttributeError(attr)

if __name__ == "__main__":
    c = Config("../build-staging.json")
    print(c._config)
    print(c.parsley)
