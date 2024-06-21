import  json
import  math
import  os
import  sys
######## 01: Validate input
ID = 0; size=0; alctdIncmngTcpPortBlock = 0
if  len (sys.argv) < 2:
        print ("Project attribute not provided: ID")
        sys.exit (1)
else:
        try:
                ID = sys.argv [1].replace ("prjct", "")
                ID = ID.replace ("-0", "")
                ID = ID.replace ( "-", "")
                ID = int (ID)
        except  ValueError:
                print ("Project attribute invalid: ID")
                sys.exit  (1)
        if ID < 1 or ID > 32:
                print ("Project attribute invalid: ID")
                sys.exit  (1)
if  len (sys.argv) < 3:
        print ("Project attribute not provided: Size")
        sys.exit (1)
else:
        try:
                size = int (sys.argv [2])
        except  ValueError:
                print ("Project attribute invalid: Size")
                sys.exit (1)
        if size < 1 or size > 524288:
                print ("Project attribute invalid: Size")
                sys.exit (1)
        if math.log (size, 2).is_integer () == False:
                print ("Project attribute invalid: Size")
                sys.exit (1)
if  len (sys.argv) < 4:
        print ("Project attribute not provided: Allocated Incoming TCP Port Block")
        sys.exit (1)
else:
        try:
                alctdIncmngTcpPortBlock = int (sys.argv [3])
        except  ValueError:
                print ("Project attribute invalid: Allocated Incoming TCP Port Block")
                sys.exit (1)
        if alctdIncmngTcpPortBlock < 1 or alctdIncmngTcpPortBlock > 99:
                print ("Project attribute invalid: Allocated Incoming TCP Port Block")
                sys.exit (1)
name = sys.argv [1]
rootPrjctDrctryName = name
######## 02: Fetch host profile
unitCorePower = 0
hostSize = 0
try:
        hostSize = open ("/etc/dplyd/profile")
        hostSize = json.load (hostSize)
        unitCorePower = int  (hostSize ["unitCorePower"])
        hostSize = int (hostSize ["machinePower" ])
except  Exception as e:
        print ("Could not retrieve Host size: ({0})".format (e))
        sys.exit (1)
if unitCorePower < 1 or math.log (unitCorePower, 2).is_integer () == False:
        print ("Host size is invalid"); print (unitCorePower)
        sys.exit (1)
if hostSize < 1 or math.log (hostSize, 2).is_integer () == False:
        print ("Host size is invalid"); print (hostSize)
        sys.exit (1)
if unitCorePower > hostSize:
        print ("Unit core power can not be greater than machine power")
        sys.exit (1)
hostPrcsrs = []
_ba00 = hostSize
while _ba00 > 0:
        hostPrcsrs.append (unitCorePower)
        _ba00 = _ba00 - unitCorePower
######## 03: Determining usage of each processor
_ba01 = os.listdir ("/etc/dplyd")
exstngAlctdIncmngTcpPortBlock = []
for drctry in _ba01:
        if drctry == "profile" or drctry == rootPrjctDrctryName: continue
        try:
                _ca01 = open ("/etc/dplyd/{0}/profile".format (drctry))
                _ca01 = json.load (_ca01)
                _cb01 = int (_ca01 ["size"] )
                _cb02 = _ca01 ["alctdPrcsrs"]
                _cb03 = int (_ca01 ["alctdIncmngTcpPortBlock"])
                if  _cb01 <  1 or math.log (_cb01, 2).is_integer () == False:
                        print ("Existing project attribute invalid: {0}".format (drctry))
                        sys.exit (1)
                if  _cb01 > unitCorePower: _cb01 = unitCorePower
                for prcsr in _cb02:
                        _da01 = int(prcsr)
                        hostPrcsrs [_da01] = hostPrcsrs [_da01] - _cb01
                exstngAlctdIncmngTcpPortBlock.append (_cb03)
        except Exception as e:
                print ("Could not determine usage of each processor: ({0}:{1})".format (drctry, e))
                sys.exit (1)
######## 04: Selecting processors for projet
_bb01 = size
if _bb01 < unitCorePower: _bb01 = unitCorePower
_bb01 =  int (_bb01 / unitCorePower)
_bb05 =_bb01
_bb10 = size
if _bb10 > unitCorePower: _bb10 = unitCorePower
_bb50 = []
_bb75 = hostPrcsrs
_bb75.reverse (  )
for i , prcsr in enumerate (_bb75):
        i = (len(hostPrcsrs)-1) - i
        if _bb05 > 0:
                if _bb10 <= prcsr:
                        _bb05 =_bb05- 1
                        _bb50.append (i)
if len (_bb50)< _bb01:
        print ("Project too big for available capacity")
        sys.exit (1)
######## 05: Checking if 'Allocated Incoming TCP Port Block' is not already in use
for block in exstngAlctdIncmngTcpPortBlock:
        if block == alctdIncmngTcpPortBlock:
                print ("Project attribute already in use: Assigned TCP Incoming Traffic Port Block")
                sys.exit (1)
######## 06: Printing project's profile
profile = {
        "size": size,
        "alctdPrcsrs": _bb50,
        "alctdIncmngTcpPortBlock": alctdIncmngTcpPortBlock,
        "unitCorePower": unitCorePower
}
_bc01 = open ("/etc/dplyd/{0}/profile".format (rootPrjctDrctryName), "w")
json.dump (profile, _bc01, indent=8)
_bc01.write  ("\n")
