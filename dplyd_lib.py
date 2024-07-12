import json
import os
import re
import sys
################################################################################################
#1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234#
################################################################################################
def ServerPrfl__load ():
        serverPrfl = "";
        try:
                _ce05 = open ("/etc/dplyd/dplyd", "r").read ()
                _ce05 = json.loads (_ce05)
                serverPrfl = _ce05
        except  Exception as e:
                print ("Server profile loading failed. [{0}]".format (e))
                sys.exit (1)
        ####
        try:
                if re.match (r'^[1-9][0-9]*$', str (serverPrfl ["unitCorePower"])) == None:
                        print ("Profile data unitCorePower invalid")
                        sys.exit (1)
                ##
                if re.match (r'^[1-9][0-9]*$', str (serverPrfl ["coreCount"])) == None:
                        print ("Profile data coreCount invalid")
                        sys.exit (1)
                ##
        except  Exception as e:
                print ("Server profile validation failed. [{0}]".format (e))
                sys.exit (1)
        ####
        return serverPrfl
####
def PrdctList__fetch ():
        prjctSize  = [];
        prjctList  = [];
        try:
                _ce05 = os.listdir ("/etc/dplyd")
                prjctList = _ce05
        except  Exception as e:
                print ("Project list loading failed. [{0}]".format (e))
                sys.exit (1)
        ####
        prjctList.sort ()
        for prjct  in prjctList:
                if re.match (r'^prjct-[0-9a-f]{2,2}$', prjct) == None: continue
                try:
                        _de05 = open ("/etc/dplyd/{0}".format (prjct, "r") ).read ()
                        _df05 = json.loads (_de05)
                        if re.match (r'^[1-9][0-9]*$', str (_df05 ["size"])) == None:
                                print ("Project {0} has invalid size '{1}'".format (
                                        prjct, _df05 ["size"]
                                ))
                                sys.exit (1)
                        ####
                        prjctSize.append ([prjct, str (_df05 ["size"])])
                except  Exception as e:
                        print ("Project {0} profile could not be loaded. [{1}]".format (
                                prjct, e
                        ))
                        sys.exit (1)
                ####
        ####
        return prjctSize
####
def PrdctPrfl__load (prdct):
        prdctPrfl = "";
        try:
                _ce05 = open ("/etc/dplyd/{0}".format (prdct), "r").read ()
                _ce05 = json.loads (_ce05)
                prdctPrfl = _ce05
        except  Exception as e:
                print ("Product {0} profile loading failed. [{1}]".format (prdct, e))
                sys.exit (1)
        ####
        try:
                if re.match (r'^[1-9][0-9]*$', str (prdctPrfl ["size"])) == None:
                        print ("Product {0} profile data size invalid".format (prdct))
                        sys.exit (1)
                ##
                for prcsr in prdctPrfl ["acsblPrcsrs"]:
                        if re.match (r'^([0-9]|[1-9][0-9]*)\:[1-9][0-9]*$', prcsr) == None:
                                print ("Product {0} profile data acsblPrcsrs invalid".format (
                                        prdct
                                ) )
                                sys.exit (1)
                        ##
                ##
        except  Exception as e:
                print ("Product {0} profile validation failed. [{1}]".format (prdct, e))
                sys.exit (1)
        ####
        return prdctPrfl
####
