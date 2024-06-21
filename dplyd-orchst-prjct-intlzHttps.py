import  getpass
import  json
import  os
import  subprocess
import  sys
#########
if len (sys.argv) < 2:
        print ("Project ID not provided")
        sys.exit (1)
if sys.argv [1] == "":
        print ("Project ID is  invalid" )
        sys.exit (1)
#########
intrfc = '''server {{
	server_name {0};
	listen 443 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:1{1}43;
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
	listen 444 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:1{1}44;
		proxy_http_version 1.1;
		proxy_set_header Host {0};
		proxy_set_header X-Real-IP {0};
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto https;
                proxy_set_header X-Forwarded-Server $host;
	}}
}}
server {{
	server_name {0};
	listen 445 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:1{1}45;
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
	listen 446 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:1{1}46;
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
	listen 447 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:1{1}47;
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
	listen 448 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:1{1}48;
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
	listen 449 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:1{1}49;
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
	listen 450 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:1{1}50;
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
	listen 451 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:1{1}51;
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
	listen 452 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:1{1}52;
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
	listen 10443 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:3{1}43;
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
	listen 10444 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:3{1}44;
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
	listen 10445 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:3{1}45;
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
	listen 10446 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:3{1}46;
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
	listen 10447 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:3{1}47;
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
	listen 10448 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:3{1}48;
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
	listen 10449 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:3{1}49;
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
	listen 10450 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:3{1}50;
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
	listen 10451 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:3{1}51;
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
	listen 10452 ssl;
	ssl_certificate_key /etc/letsencrypt/live/{0}/privkey.pem;
        ssl_certificate     /etc/letsencrypt/live/{0}/fullchain.pem;
	location / {{
		proxy_pass https://localhost:3{1}52;
		proxy_http_version 1.1;
		proxy_set_header Host {0};
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto https;
                proxy_set_header X-Forwarded-Server $host;
	}}
}}
'''
#########
cnfgrt = open ("/dplyd/{0}/profile".format (sys.argv [1]), "r")
cnfgrt = json.load (cnfgrt)
_be01  = cnfgrt ["sltnPrjctId"] + ".a.deployed.arstorms.org"
_bf01  = cnfgrt ["dnsId"]
_bf01.insert (0, _be01)
for domain in _bf01:
        _ca01 = subprocess.run (["certbot", "certonly", "--standalone", "-n", "-d", domain])
        if _ca01.returncode != 0:
                print ("Could not get certificate: {0}".format (domain))
                sys.exit (1)
        _ce01 = intrfc.format (domain, sys.argv [1].replace ("prjct-", ""))
        _cf01 = domain.split  (".")
        _cf01.reverse ()
        _cg01 = "/etc/nginx/dplyd/htts_" + "_".join (_cf01) + ".conf"
        _ch01 = open  (_cg01 , "w")
        _ch01.write (_ce01 )
