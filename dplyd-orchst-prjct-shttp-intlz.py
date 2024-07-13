import  dplyd_lib
import  getpass
import  json
import  os
import  re
import  sys
#### 01 ####
intrf1 = '''server {{
        server_name {0};
        listen 80;
        location / {{
                proxy_pass http://localhost:{1};
                proxy_http_version 1.1;
                proxy_set_header Host {0};
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto http;
                proxy_set_header X-Forwarded-Server $host;
        }}
}}
server {{
        server_name {0};
        listen 1080;
        location / {{
                proxy_pass http://localhost:{2};
                proxy_http_version 1.1;
                proxy_set_header Host {0};
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto http;
                proxy_set_header X-Forwarded-Server $host;
        }}
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
#### 02 ####
_be05 = sys.argv [1].replace ("prjct-", "")
_be10 = re.sub (r'^0', "", _be05)
_be15 = int  ( _be10 ,16)
_bf05 = ((_be15 - 1) * 4) + 2000 + 1
_bf10 = ((_be15 - 1) * 4) + 2000 + 2
cnfgr = dplyd_lib.PrdctPrfl__load (sys.argv [1])
intrf = ""
_bg05 = intrf1.format ( cnfgr ["prmryDnsId"], _bf05, _bf10 )
intrf = intrf + _bg05
for domain in cnfgr ["scndrDnsId"]:
        _ce05 = intrf2.format (domain, cnfgr ["prmryDnsId"])
        intrf = intrf + _ce05
####
_bh05 = "/etc/nginx/dplyd/http-{0}.conf".format (sys.argv [1])
_bh10 = open (_bh05, "w").write (intrf)
