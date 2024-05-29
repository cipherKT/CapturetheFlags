# start
Download the zipfile <br>
```bash
curl -O https://artifacts.picoctf.net/c_titan/160/challenge.zip
```
Unzip the file  <br>
```bash
unzip challenge.zip
```

you will get a [drop-in](../16_timeMachine/drop-in/) in this there is a [message.txt](../16_timeMachine/drop-in/message.txt) file <br>
this message says checkfor git commit history  <br>
```bash
git reflog
```
and .... <br>
# Boom !!! got the flag 
```txt
picoCTF{t1m3m@ch1n3_186cd7d7}
```
