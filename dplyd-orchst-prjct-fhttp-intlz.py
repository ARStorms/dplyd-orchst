import dplyd_lib
import json
import os
import re
import sys
#### 1 ####
intrf1 = '''server {{
        server_name {0};
        listen 80;
        return 301 https://{0}$request_uri;
}}
server {{
        server_name {0};
        listen 1080;
        return 301 https://{0}:1443$request_uri;
}}
'''
intrf2 = '''server {{
        server_name {0};
        listen 80;
        return 301 http://{1}$request_uri;
}}
server {{
        server_name {0};
        listen 1080;
        return 301 http://{1}:1080$request_uri;
}}
'''
#### 2 ####
cnfgr = dplyd_lib.PrdctPrfl__load (sys.argv [1])
intrf = ""
_bg05 = intrf1.format (cnfgr ["prmryDnsId"] )
intrf = intrf + _bg05
for domain in cnfgr ["scndrDnsId"]:
        _ce05 = intrf2.format (domain, cnfgr["prmryDnsId"])
        intrf = intrf + _ce05
####
_bh05 = "/etc/nginx/dplyd/http-{0}.conf".format (sys.argv [1])
_bh10 = open (_bh05, "w").write (intrf)
