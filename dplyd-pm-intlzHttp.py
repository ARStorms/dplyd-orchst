import  getpass
import  json
import  os
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
	listen 80;
	location / {{
		proxy_pass http://localhost:1{1}80;
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
	listen 81;
	location / {{
		proxy_pass http://localhost:1{1}81;
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
	listen 82;
	location / {{
		proxy_pass http://localhost:1{1}82;
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
	listen 83;
	location / {{
		proxy_pass http://localhost:1{1}83;
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
	listen 84;
	location / {{
		proxy_pass http://localhost:1{1}84;
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
	listen 85;
	location / {{
		proxy_pass http://localhost:1{1}85;
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
	listen 86;
	location / {{
		proxy_pass http://localhost:1{1}86;
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
	listen 87;
	location / {{
		proxy_pass http://localhost:1{1}87;
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
	listen 88;
	location / {{
		proxy_pass http://localhost:1{1}88;
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
	listen 89;
	location / {{
		proxy_pass http://localhost:1{1}89;
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
	listen 10080;
	location / {{
		proxy_pass http://localhost:3{1}80;
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
	listen 10081;
	location / {{
		proxy_pass http://localhost:3{1}81;
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
	listen 10082;
	location / {{
		proxy_pass http://localhost:3{1}82;
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
	listen 10083;
	location / {{
		proxy_pass http://localhost:3{1}83;
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
	listen 10084;
	location / {{
		proxy_pass http://localhost:3{1}84;
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
	listen 10085;
	location / {{
		proxy_pass http://localhost:3{1}85;
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
	listen 10086;
	location / {{
		proxy_pass http://localhost:3{1}86;
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
	listen 10087;
	location / {{
		proxy_pass http://localhost:3{1}87;
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
	listen 10088;
	location / {{
		proxy_pass http://localhost:3{1}88;
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
	listen 10089;
	location / {{
		proxy_pass http://localhost:3{1}89;
		proxy_http_version 1.1;
		proxy_set_header Host {0};
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto http;
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
        _ce01 = intrfc.format (domain, sys.argv [1].replace ("prjct-", ""))
        _cf01 = domain.split  (".")
        _cf01.reverse ()
        _cg01 = "/etc/nginx/dplyd/http_" + "_".join (_cf01) + ".conf"
        _ch01 = open  (_cg01 , "w")
        _ch01.write (_ce01 )
