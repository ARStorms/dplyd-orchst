import json
import os
import sys
######## 01: Validate input SHM size
_ba01 = 0
if len (sys.argv) > 2:
        try:
                _ba01 = int (sys.argv [2])
                if _ba01 < 0: raise ValueError ("SHM size is invalid")
        except  Exception as e:
                print ("SHM size is invalid")
                sys.exit (1)
        ####
######## 02: Save new profile
_bb01 =  open ("/etc/dplyd/{0}".format (sys.argv [1]), "r")
_bc01 = _bb01.read ()
try: #
        _ca01 = json.loads(_bc01)
        _ca01 ["shmSize"]  = _ba01
        _bb01 = open ("/etc/dplyd/{0}".format (sys.argv [1]), "w")
        json.dump (_ca01, _bb01, indent=8)
        _bb01.write ("\n")
except  Exception as e:
        print ("Project's profile could not be updated to file. [{0}]".format (e))
