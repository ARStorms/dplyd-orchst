import dplyd_lib
import json
import math
import re
import sys
################################################################################################
#1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234#
################################################################################################
#### 1 ####: Validate input
if len (sys.argv) < 2: print ("Project size not provided"); sys.exit (1)
prjctSize = 0
try:####
        prjctSize = int (sys.argv [1])
except  Exception as e:
        print ("Project size invalid")
        sys.exit (1)
####
#### 2 ####: Load server profile
serverPrfl = dplyd_lib.ServerPrfl__load ()
#### 3 ####: Fetch list of products and respective sizes
prjctList  = dplyd_lib.PrdctList__fetch ()
#### 4 ####: Check if space is available
prcsrUsage = [0 for _ in range (int (serverPrfl ["coreCount"]))]
for prjct in prjctList:
        _ce05 = dplyd_lib.PrdctPrfl__load (prjct [0])
        for acsblPrcsr in _ce05 ["acsblPrcsrs"]:
                _de05 = acsblPrcsr.split (":")
                _de11 = int (_de05 [0])
                _de12 = int (_de05 [1])
                prcsrUsage [_de11] = prcsrUsage [_de11] + _de12
        ####
####
cpctyLeftForDstrbt = prjctSize
acsblPrcsrs = []
for _ce05 , _ce10 in enumerate (reversed (prcsrUsage)):
        #### 1 ####
        if cpctyLeftForDstrbt <= 0: break
        _ce05 = abs (_ce05 - (len (prcsrUsage) - 1))
        _cf05 = int (serverPrfl ["unitCorePower"]) - _ce10
        if _cf05 == 0: continue
        #### 2 ####
        nextCpctyToRsrv = cpctyLeftForDstrbt
        if nextCpctyToRsrv > int (serverPrfl ["unitCorePower"]):
                nextCpctyToRsrv = int (serverPrfl ["unitCorePower"])
        ##
        if _cf05 < nextCpctyToRsrv: continue
        #### 3 ####
        acsblPrcsrs.append ("{0}:{1}".format(_ce05, nextCpctyToRsrv))
        cpctyLeftForDstrbt = cpctyLeftForDstrbt - nextCpctyToRsrv
####
_be05 = float (prjctSize)  / float (serverPrfl ["unitCorePower"])
_bf05 = math.ceil (_be05)
if len(acsblPrcsrs) < _bf05:
        print ("Server available capacity not enough to power project")
        sys.exit (1)
##
#### 5 ####: Create project
#--- 1 ---#
lastPrjctId = 0
if len (prjctList) > 0:
        _ce05 = prjctList [len (prjctList) - 1 ]
        _ce05 = _ce05 [0].replace ("prjct-", "")
        if re.match (r'^[0-9a-f]{2,2}$' , _ce05) == None:
                print ("Project '{0}' with invalid id found".format (_ce05 [0]))
                sys.exit (1)
        ##
        _ce10 = re.sub (r'^0', "", _ce05)
        _ce15 = int ( _ce10, 16)
        lastPrjctId = _ce15
##
try:
        _ce05 = int (serverPrfl ["lastPrjctId"])
        if _ce05 > lastPrjctId: lastPrjctId = _ce05
except  Exception as e:
        pass
##
newPrjctId = lastPrjctId +  1
newPrjctId = hex (newPrjctId)
newPrjctId = re.sub (r'^0x', "", newPrjctId)
if len (newPrjctId) < 2: newPrjctId = "0{0}".format (newPrjctId)
newPrjctId = "prjct-{0}".format (newPrjctId)
#--- 2 ---#
acsblPrcsrs.reverse ()
#--- 3 ---#
ntwrkPortBlock = 0
for prjct in prjctList:
        _ce05  = int (prjct [1])
        ntwrkPortBlock = ntwrkPortBlock + _ce05
####
ntwrkPortBlock = ntwrkPortBlock + 1
#--- 4 ---#
serverPrfl ["lastPrjctId"] = lastPrjctId + 1
_bh05 = json.dumps (serverPrfl  , indent=8 )
_bh05 = _bh05 + "\n"
newPrjctPrfl = """{{
        "size": {0},
        "acsblPrcsrs": {1},
        "altdPortBlock": {2},
        "system": {{
                "unitCorePower": {3},
                "coreCount": {4}
        }}
}}
""".format (
        prjctSize, acsblPrcsrs, ntwrkPortBlock, int (serverPrfl ["unitCorePower"]),
        int (serverPrfl ["coreCount"])
)
newPrjctPrfl = newPrjctPrfl.replace ("'", '"')
open  ("/etc/dplyd/dplyd"                  , "w").write (_bh05)
open  ("/etc/dplyd/{0}".format (newPrjctId), "w").write (newPrjctPrfl)
print (newPrjctId)
