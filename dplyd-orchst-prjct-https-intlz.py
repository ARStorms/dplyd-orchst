import  dplyd_lib
import  getpass
import  json
import  os
import  re
import  subprocess
import  sys
#### 01 ####
intrf1 = '''server {{
        server_name {0};
        listen 443;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
        location / {{
                proxy_pass https://localhost:{1};
                proxy_http_version 1.1;
                proxy_set_header Host {0};
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto https;
                proxy_set_header X-Forwarded-Server $host;
        }}
}}
server {{
        server_name {0};
        listen 1443;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
        location / {{
                proxy_pass https://localhost:{2};
                proxy_http_version 1.1;
                proxy_set_header Host {0};
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto https;
                proxy_set_header X-Forwarded-Server $host;
        }}
}}
'''
intrf2 = '''server {{
        server_name {0};
        listen 443;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
        return 301 https://{1}$request_uri;
}}
server {{
        server_name {0};
        listen 1443;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
        return 301 https://{1}:1443$request_uri;
}}
'''
#### 02 ####
cnfgr = dplyd_lib.PrdctPrfl__load (sys.argv [1])
_bb05 = cnfgr ["scndrDnsId"]
_bb05.insert (0, cnfgr ["prmryDnsId"])
for domain in _bb05:
        _ce05 = subprocess.run (["certbot", "certonly", "--standalone", "-n", "-d", domain])
        if _ce05.returncode != 0:
                print ("Domain certificate generation failed. [{0}]".format (domain))
                sys.exit (1)
        ####
####
#### 03 ####
_be05 = sys.argv [1].replace ("prjct-", "")
_be10 = re.sub (r'^0', "", _be05)
_be15 = int  ( _be10 ,16)
_bf05 = ((_be15 - 1) * 4) + 2000 + 3
_bf10 = ((_be15 - 1) * 4) + 2000 + 4
intrf = ""
_bg05 = intrf1.format ( cnfgr ["prmryDnsId"], _bf05, _bf10 )
intrf = intrf + _bg05
for domain in cnfgr ["scndrDnsId"]:
        _ce05 = intrf2.format (domain, cnfgr ["prmryDnsId"])
        intrf = intrf + _ce05
####
_bh05 = "/etc/nginx/dplyd/htts-{0}.conf".format (sys.argv [1])
_bh10 = open (_bh05, "w").write (intrf)
