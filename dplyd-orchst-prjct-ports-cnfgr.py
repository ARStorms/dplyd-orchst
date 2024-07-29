import  dplyd_lib
import  json
import  sys
####  1 ####
ports = sys.argv [2].split (":")
_be05 = dplyd_lib.PrdctPrfl__load (sys.argv [1])
_bf05 = int (_be05 ["altdPortBlock"])
_bf10 = int (_be05 ["size"])
_bf10 =(_bf05 + _bf10 ) - 1
_bf05 = _bf05 + 10000
_bf10 = _bf10 + 10000
for port in ports:
        _ce05 = 0
        try:    _ce05 = int (port)
        except  Exception as e:
                print ("'{0}' is an invalid port no".format (port))
                sys.exit (1)
        ####
        if _ce05 != 80 and _ce05 != 1080 and _ce05 != 443 and _ce05 != 1443 and (_ce05 < _bf05 or    _ce05 > _bf10):
                print ("Project not authorized to use port {0}".format (port))
                sys.exit (1)
        ####
####  2 ####
_bg05 = open ("/etc/dplyd/{0}".format (sys.argv [1]), "r")
_bg05 = json.loads (_bg05.read ( ) )
_bg05 ["activePort"] = sys.argv  [2]
_bh05 = open ("/etc/dplyd/{0}".format (sys.argv [1]), "w")
json.dump (_bg05, _bh05, indent=8)
_bh05.write  ("\n")
