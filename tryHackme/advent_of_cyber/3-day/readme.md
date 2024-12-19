# Advent of cyber 2024 day 3
Start by accessing the machines using your desired option. I used openvpn to connect to the vpn and then access the IP.<br>
This is a website that is used to monitor the traffic to server and it contains too many good options like filtering using dates, filtering the sourceIP and type of the process and others are there too you can explore them.<br>
This was pretty easy task as it was fully guided room read the instruction carefully and you will be able to complete this room in less than an hour. <br> 

1. **BLUE**: Where was the web shell uploaded to?
Answer format: /directory/directory/directory/filename.php
```bash
/media/images/rooms/shell.php
```
2. **BLUE**: What IP address accessed the web shell?
```bash
10.11.83.34
```
3. **RED**: What is the contents of the flag.txt?
Try to login using common admin passwords and then in create room there is an option to upload an image there you can upload the `shell.php` and then go to that `url` and then can gain `reverse shell` and then using `ls` you can list the files and there is file named `flag.txt` file and then you can cat that out and get the flag<br>
```bash
THM{Gl1tch_Was_H3r3}
```
