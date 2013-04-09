#!.virtenv/bin/python
import sys

sys.path.append("src")

from api import api
api.run(debug = True)