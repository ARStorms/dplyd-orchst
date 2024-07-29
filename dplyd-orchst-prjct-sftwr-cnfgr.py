import json
import os
import re
import sys
######## 01: Determine what value to work with
_ba01 = ""
if len (sys.argv) > 2:
        if re.search (r'^[a-zA-Z\-\._:0-9]+\/[a-zA-Z\-\._:0-9]+(\/[a-zA-Z\-\._:0-9]+)*$', sys.argv [2]) == None:
                print ("Software path is invalid")
                sys.exit (1)
        _ba01 = sys.argv [2]
######## 02: Save data
_bb01 =  open ("/etc/dplyd/{0}".format (sys.argv [1]), "r")
_bc01 = _bb01.read ()
try: #
        _ca01 = json.loads(_bc01)
        _ca01 ["sftwr"]  = _ba01
        _bb01 = open ("/etc/dplyd/{0}".format (sys.argv [1]), "w")
        json.dump (_ca01, _bb01, indent=8)
        _bb01.write ("\n")
except  Exception as e:
        print ("Project's profile could not be updated to file. [{0}]".format (e))
