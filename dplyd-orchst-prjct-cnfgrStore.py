import json
import os
import sys
######## 01: Determine what value to work with
_ba01 = "/var/dplyd"
if len (sys.argv) > 2:
        if os.path.isabs (sys.argv [2]) == False:
                print ("Store mount point is not an absolute path")
                sys.exit (1)
        _ba01 = sys.argv [2]
######## 02: Save data
_bb01 =  open ("/dplyd/{0}/profile".format (sys.argv [1]), "r")
_bc01 = _bb01.read ()
try:
        _ca01 = json.loads (_bc01)
        _ca01 ["storeMountPoint"]  = _ba01
        _bb01 = open ("/dplyd/{0}/profile".format (sys.argv [1]), "w")
        json.dump (_ca01, _bb01, indent=8)
        _bb01.write ("\n")
except  Exception as e:
        print ("Could not save data: ({0})".format (e))
