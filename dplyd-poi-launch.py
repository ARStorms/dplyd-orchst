import  getpass
import  json
import  os
import  sys
#########
def fetchPlates (path):
        _ba01 = []
        for root, dirs, files in os.walk(path): ##
                for drctry in dirs :
                        _ba01.append (os.path.join (root, drctry))
        return _ba01
startCode = """#!/bin/sh
podman stop software
podman rm   software
cuser=$(podman run --rm software id | sed -E 's/\(.+gid.+//' | sed 's/uid=//')
podman unshare chown -R $cuser:$cuser .prmtr
podman unshare chown -R $cuser:$cuser .plate
podman unshare chown -R $cuser:$cuser .store
podman run --name software -it \\
--cpuset-cpus {1} --cpus {0} --memory-swap {2}k --memory {3}k --shm-size {4}k --env-file $HOME/.prmtr {5} -v $HOME/.store:{6}:z \\
 {7} \
--sysctl net.ipv4.ip_local_port_range="{8}" \
software:latest
"""
#########
try:
        #####
        _ba01 = open(".profile","r")
        _bb01 = json.load (_ba01)
        
        #####
        _bd11 = int (_bb01 ["size"]) / int (_bb01 ["unitCorePower"])
        _bd12 = ""
        for cpu in   _bb01 ["alctdPrcsrs"]: _bd12 = _bd12 + ",{0}".format (cpu)
        _bd12 = _bd12 [1:]
        _bd13 = int ((_bb01 ["size"] * 2) * 0.75 * 1024)
        _bd14 = int ((_bb01 ["size"] / 1) * 0.75 * 1024)
        _bd15 = int ((_bb01 ["size"] / 2) * 0.75 * 1024)
        _bd16 = ""
        for plate in os.listdir (".plate"):
                _ca00 = plate.replace ("=", "/")
                if _ca00 == "": continue
                _ca01 = '-v "$HOME/.plate/{0}:{1}:z" '.format (plate, _ca00)
                _bd16 = _bd16 + _ca01
        _bd17 = "/var/dplyd"
        if "storeMountPoint" in _bb01: _bd17 = _bb01 ["storeMountPoint"]
        if "activePort"  not in _bb01: _bb01 ["activePort"] = ""
        _bd18 = ""
        for port in _bb01 ["activePort"].split (":"):
                if port == "": continue
                _ca01 = ""
                _ca02 = ""
                _cb01 = getpass.getuser ().replace ("prjct-", "")
                _cc01 = port
                if   len (_cc01) == 1 : _cc01 = "0" + _cc01
                if   int ( port) >=80 and int (port) <= 90:
                          _ca01   = "-p 1{0}{1}:{2}    \\\n".format (_cb01,_cc01,_cc01)
                          _ca02   = "-p 3{0}{1}:100{2} \\\n".format (_cb01,_cc01,_cc01)
                elif int ( port) >=43 and int (port) <= 53:
                          _ca01   = "-p 1{0}{1}:4{2}   \\\n".format (_cb01,_cc01,_cc01)
                          _ca02   = "-p 3{0}{1}:104{2} \\\n".format (_cb01,_cc01,_cc01)
                elif int ( port) >= 1 and int (port) <= 10:
                          _da01   = "-" + port
                          _da01   = _da01.replace ("-0", ""  )
                          _da01   = int (_da01.replace ( "-", ""))
                          _da02   = int (_bb01 ["alctdIncmngTcpPortBlock"])
                          _da03   = ((_da02 - 1) * 10) + _da01
                          _da04   = 20000 + _da03
                          _ca01   = "-p {0}:{1} \\\n".format (_da04, _da04)
                else:
                          pass
                if _ca01 != "": _bd18 = "{0}{1} ".format (_bd18, _ca01)
                if _ca02 != "": _bd18 = "{0}{1} ".format (_bd18, _ca02)
        _bd19 = ""
        _bd19_00 = getpass.getuser ().replace ("prjct", "")
        _bd19_00 =_bd19_00.replace ("-0", "")
        _bd19_00 =_bd19_00.replace ( "-", "")
        _bd19_00 = int(_bd19_00    )
        _bd19_01 = 30001
        _bd19_02 = 30000 + int (_bb01["size"])
        if _bd19_02 > 40000: _bd19_02 = 40000
        _bd19 = "{0} {1}".format (_bd19_01, _bd19_02)
        #####
        _be01 = startCode.format (_bd11, _bd12, _bd13, _bd14, _bd15, _bd16, _bd17, _bd18, _bd19)
        _bf01 = open (".local/bin/dplyd-poi-launchCode", "w")
        _bf01.write  (_be01)
        print (_be01 )
except  Exception as e:
        print ("Failed: {0}".format (e))  
        sys.exit (1)
