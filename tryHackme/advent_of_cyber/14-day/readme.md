# Advent of cyber 2024 day 4
Start by accessing the machines using your desired option. I used openvpn to connect to the vpn and then access the IP.<br>
This is a website that is used to monitor the traffic to server and it contains too many good options like filtering using dates, filtering the sourceIP and type of the process and others are there too you can explore them.<br>
This was pretty easy task as it was fully guided room read the instruction carefully and you will be able to complete this room in less than an hour. <br> 

## Writeup
connect to vpn and add the hosts in `/etc/hosts` and then browse the websites you can download the script and then run it and after adding the vpn-IP to burp proxy you will be able to get the requests and then it is cake walk form there. 
## here are the commands to get the scripts 

```curl 
curl -O https://github.com/cipherKT/CapturetheFlags/blob/main/tryHackme/advent_of_cyber/14-day/route-elf-traffic.sh
```
```bash
chmod +x route-elf-traffic.sh
```
1. What is the name of the CA that has signed the Gift Scheduler certificate?
```bash
THM
```
2. Look inside the POST requests in the HTTP history. What is the password for the snowballelf account?
```bash
c4rrotn0s3
```
3. Use the credentials for any of the elves to authenticate to the Gift Scheduler website. What is the flag shown on the elves’ scheduling page?
```bash
THM{AoC-3lf0nth3Sh3lf}
```
4. What is the password for Marta May Ware’s account?
```bash
H0llyJ0llySOCMAS!
```
5. Mayor Malware finally succeeded in his evil intent: with Marta May Ware’s username and password, he can finally access the administrative console for the Gift Scheduler. G-Day is cancelled!
What is the flag shown on the admin page?
```bash
THM{AoC-h0wt0ru1nG1ftD4y}
```
