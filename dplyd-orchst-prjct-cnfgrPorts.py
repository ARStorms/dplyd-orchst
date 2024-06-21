import  json
import  sys
###########
if len (sys.argv) < 2:
        print ("Project ID not provided")
        sys.exit (1)
if sys.argv [1] == "":
        print ("Project ID is  invalid" )
        sys.exit (1)
if len (sys.argv) < 3:
        print ("Port no not provided")
        sys.exit (1)
if sys.argv [2] == "":
        print ("Port no is  invalid" )
        sys.exit (1)
###########
_ba01 = sys.argv [2].split (":")
for port_  in _ba01:
        port_ = "-" + port_
        port_ = port_.replace ("-0", "")
        port_ = port_.replace ( "-", "")
        _ca01 = int  (port_)
        _cb01 = False
        if (_ca01 >= 80 and _ca01 <= 90) or (_ca01 >= 43 and _ca01 <= 53) or (_ca01 >= 1 and _ca01 <= 10):    _cb01  = True
        if  _cb01 == False:
                print ("A port no is invalid")
                sys.exit (1)
_bc01 = open  ("/dplyd/{0}/profile".format (sys.argv [1]), "r")
_bd01 = json.loads (_bc01.read ( ) )
_bd01 ["activePort"] = sys.argv  [2]
_be01 = open  ("/dplyd/{0}/profile".format (sys.argv [1]), "w")
json.dump (_bd01, _be01, indent=8)
_be01.write ("\n")
