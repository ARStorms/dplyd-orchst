import  getpass
import  json
import  os
import  re
import  sys
#### 01 ####
def fetchPlates (path):
        _ba01 = []
        for root, dirs, files in os.walk(path): ##
                for drctry in dirs :
                        _ba01.append (os.path.join (root, drctry))
        return _ba01
startCode = """#!/bin/sh
#Prepare site for launch
echo "Preparing site for launch..."
podman stop --all --time 300
pulse=$(podman   ps    | grep software)
while [ "$pulse" != "" ]
do
        sleep 1
done
podman container rm -a
pulse=$(podman   ps -a | grep software)
while [ "$pulse" != "" ]
do
        sleep 1
done
podman unshare chown -R 0:0 .prmtr
podman unshare chown -R 0:0 .plate
podman unshare chown -R 0:0 .store
#Launch
echo "Launching..."
pulse=$(podman images | grep {8})
if [ "$pulse" == "" ]
then
        podman container rm -a
        podman image     rm -a
        podman pull {8}:{9}
fi
podman tag {8}:{9} software:latest
cuser=$(podman run --rm software id | sed -E 's/\(.+gid.+//' | sed 's/uid=//')
podman unshare chown -R $cuser:$cuser .prmtr
podman unshare chown -R $cuser:$cuser .plate
podman unshare chown -R $cuser:$cuser .store
podman run --name software -it \\
--cpuset-cpus {1} --cpus {0} --memory-swap {2}k --memory {3}k {10} --env-file $HOME/.prmtr {4} -v $HOME/.store:{5}:Z \\
{6} \
--sysctl net.ipv4.ip_local_port_range="{7}" \
software:latest
"""
#### 02 ####
try:
        #### 01 ####
        _ba01 = open(".profile","r")
        _bb01 = json.load (_ba01)
        #### 02 ####
        _bd11 = int (_bb01 ["size"]) / int (_bb01 ["system"]["unitCorePower"] )
        _bd12 = ""
        for cpu in   _bb01 ["acsblPrcsrs"]:
                cpu = re.sub (r'\:[0-9]*$',"", cpu)
                _bd12 = _bd12 + ",{0}".format (cpu)
        #####
        _bd12 = _bd12 [1:]
        _bd13 = int ((_bb01 ["size"] * 1) * 0.75 * 1024)
        _bd14 = int ((_bb01 ["size"] * 1) * 0.75 * 1024)
        _bd16 = ""
        for plate in os.listdir (".plate"):
                _ca00 = plate.replace ("=", "/")
                if _ca00 == "": continue
                _ca01 = '-v "$HOME/.plate/{0}:{1}:Z" '.format (plate, _ca00)
                _bd16 = _bd16 + _ca01
        ####
        _bd17 = "/var/dplyd"
        if "storeMountPoint" in _bb01: _bd17 = _bb01 ["storeMountPoint"]
        if "activePort"  not in _bb01: _bb01 ["activePort"] = ""
        _bd18 = ""
        for port in _bb01 ["activePort"].split (":"):
                if   port == "": continue
                _ca01 = ""
                _cb01 = getpass.getuser ().replace ("prjct-", "")
                _cd05 = re.sub (r'^0', "", _cb01)
                _cd10 = int  ( _cd05 ,16)
                _cd15 = ((_cd10 - 1) * 4) + 2000 + 1
                _cd20 = ((_cd10 - 1) * 4) + 2000 + 2
                _cd25 = ((_cd10 - 1) * 4) + 2000 + 3
                _cd30 = ((_cd10 - 1) * 4) + 2000 + 4
                if   int ( port) ==   80: _ca01 = "-p {0}:80   \\\n".format (_cd15)
                elif int ( port) == 1080: _ca01 = "-p {0}:1080 \\\n".format (_cd20)
                elif int ( port) ==  443: _ca01 = "-p {0}:443  \\\n".format (_cd25)
                elif int ( port) == 1443: _ca01 = "-p {0}:1443 \\\n".format (_cd30)
                elif int ( port) >= 10001 and int (port) <= 35000:
                          _ca01 = "-p {0}:{1} \\\n".format (port, port)
                ####
                _bd18 = "{0}{1} ".format(_bd18, _ca01)
        #####
        _bd19 = int (_bb01 ["altdPortBlock"])
        _bd20 =(_bd19 -1)+ int (_bb01 ["size"])
        _bd19 = _bd19 + 35000
        _bd20 = _bd20 + 35000
        _bd25 = "{0} {1}".format (_bd19, _bd20)
        _bd26 = _bb01 [ "sftwr"]
        _bd27 = ""
        _bd28 = _bd26.split(":")
        if "shmSize" in _bb01: _bd27 = _bb01 [ "shmSize" ]
        if _bd27 != "": _bd27= _bd27 = "--shm-size {0}b".format (_bd27)
        #### 03 ####
        _be01 = startCode.format (
                _bd11 , _bd12, _bd13, _bd14, _bd16, _bd17,_bd18, _bd25,_bd28[0],_bd28 [1],_bd27,
        )
        _bf00 = getpass.getuser ().replace ("prjct-", "")
        _bf01 = open (
                "/home/{0}/.local/bin/dplyd-orchst-prjct-launchCode".format (getpass.getuser()),
                "w"
        )
        _bf01.write  (_be01)
#        print (_be01 )
except  Exception as e:
        print ("Launch failed: {0}".format (e))  
        sys.exit (1)
