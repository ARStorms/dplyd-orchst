#!/bin/sh
################################################################################################
# 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012 #
################################################################################################
import getpass
import ipaddress
import json
import os
import re
import sys
################################################################################################
# 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012 #
################################################################################################
if len (sys.argv ) < 2:
        print ("Registry IP/Domain not provided")
        sys.exit (1)
##
if len (sys.argv ) < 3:
        print ("Registry user not provided")
        sys.exit (1)
##
if len (sys.argv ) < 4:
        print ("Container name not provided")
        sys.exit (1)
##
_ba01 = sys.argv [1]
_bb01 = sys.argv [2]
_bc01 = sys.argv [3]
_bd01 = ""
try:
        _bd01 = open (
                "/home/{0}/.RgstryUserPswrd".format(getpass.getuser ( )), "r"
        ).read().strip ( )
        
except  Exception as e:
        print ("Registry user password loading failed [{0}]".format (e))
        sys.exit (1)
##
################################################################################################
_ba01 = _ba01.split (":")
try:
        ipaddress.ip_address (_ba01 [0])
except  Exception as  e:
        if re.search (r'^[a-zA-Z0-9]+(\-[a-zA-Z0-9]+)*(\.[a-zA-Z0-9]+(\-[a-zA-Z0-9]+)*)*$', _ba01 [0]) == None:
                print ("Registry IP/Domain is invalid")
                sys.exit (2)
        ##
##
if len (_ba01) > 1:
        _ba01 [1] = int (_ba01 [1])
        if _ba01 [1] < 1 or _ba01 [1] > 65535:
                print ("Registry IP/Domain is invalid")
                sys.exit (2)
        ##
##
if re.search (r'^.+$', _bb01) == None:
        print ("Registry user is invalid")
        sys.exit (2)
##
if re.search (r'^[a-zA-Z0-9]+([\-\_\.\+][a-zA-Z0-9]+)*(\/[a-zA-Z0-9]+([\-\_\.\+][a-zA-Z0-9]+)*)*\:[a-zA-Z0-9]+([\-\_\.\+][a-zA-Z0-9]+)*$', _bc01) == None:
        print ("Container name is invalid")
        sys.exit (2)
##
if re.search (r'^.+$', _bd01) == None:
        print ("Registry user password is invalid")
        sys.exit (2)
##
open ("/home/{0}/.RgstryUserPswrd".format (getpass.getuser ()), "w").write (_bd01)
