import  json
import  re
import  sys
###########
if len (sys.argv) < 2:
        print ("Project ID not provided")
        sys.exit (1)
if sys.argv [1] == "":
        print ("Project ID not valid"   )
        sys.exit (1)
if len (sys.argv) < 3:
        print ("Primacy DNS ID not provided")
        sys.exit (1)
sys.argv [2] = sys.argv [2].lower ( )
if re.match (r'^(([a-z0-9\-]+\.)*[a-z0-9\-]+\:)+$', sys.argv [2]) == False:
        print ("Primary DNS ID not valid"  )
        sys.exit (1)
if len (sys.argv) < 4: sys.argv.append ("" )
sys.argv [3] = sys.argv [3].lower ( )
if sys.argv [3] != "" and re.match(r'^(([a-z0-9\-]+\.)*[a-z0-9\-]+\:)+$', sys.argv [3]) == False:
        print ("Secondary DNS ID not valid")
        sys.exit (1)
###########
_bc01 = open  ("/etc/dplyd/{0}/profile".format (sys.argv [1]), "r")
_bd01 = json.loads ( _bc01.read ( ) )
_bd01 ["prmryDnsId"] = sys.argv [2]
_bd01 ["scndrDnsId"] = sys.argv [3].split (":")
if _bd01 ["scndrDnsId"] [0] == "": _bd01 ["scndrDnsId"] = []
_be01 = open  ("/etc/dplyd/{0}/profile".format (sys.argv [1]), "w")
json.dump (_bd01, _be01, indent=8); _be01.write ("\n")
