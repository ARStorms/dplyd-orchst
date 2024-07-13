import  json
import  re
import  sys
#### 1 ####
if len (sys.argv) < 2: print ("Project ID not provided"); sys.exit (1)
if len (sys.argv) < 3: print ("Primary DNS ID not provided"); sys.exit (1)
if len (sys.argv) < 4: sys.argv.append ("")
sys.argv [2] = sys.argv [2].lower ()
sys.argv [3] = sys.argv [3].lower ()
_bb05 = sys.argv [2].split (":")
_bb10 = sys.argv [3].split (":")
if len (   _bb05) > 1: print ("Primary DNS ID can only be one"); sys.exit (1)
if re.match (r'^([a-z0-9\-]+\.)*[a-z0-9\-]+$', _bb05 [0]) == None:
        print ("Primary DNS ID invalid")
        sys.exit (1)
####
for dnsId  in   _bb10:
        if dnsId.strip () == "": continue
        if re.match (r'^([a-z0-9\-]+\.)*[a-z0-9\-]+$', dnsId ) == None:
                print ("Secondary DNS ID {0} invalid".format ( dnsId ))
                sys.exit (1)
        ####
####
#### 2 ####
_bc01 = open ("/etc/dplyd/{0}".format (sys.argv [1]) , "r")
_bd01 = json.loads ( _bc01.read ( ) )
_bd01 ["prmryDnsId"] = sys.argv [2]
_bd01 ["scndrDnsId"] = sys.argv [3].split (":")
if _bd01 ["scndrDnsId"] [0] == "": _bd01 ["scndrDnsId"] = []
_be01 = open ("/etc/dplyd/{0}".format (sys.argv [1]), "w")
json.dump (_bd01, _be01, indent=8); _be01.write ("\n")
