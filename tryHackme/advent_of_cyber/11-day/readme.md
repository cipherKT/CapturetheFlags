# Advent of cyber 2024 day 4
Start by accessing the machines using your desired option. I used openvpn to connect to the vpn and then access the IP.<br>
This is a website that is used to monitor the traffic to server and it contains too many good options like filtering using dates, filtering the sourceIP and type of the process and others are there too you can explore them.<br>
This was pretty easy task as it was fully guided room read the instruction carefully and you will be able to complete this room in less than an hour. <br> 

## Writeup
This was pretty basic room it is the first thing a hacker should learn attacking `wi-fi`s and this what this room is just ran sum bunch of commands and boom got the passphrase to get into network. 

1. What is the BSSID of our wireless interface?
```bash
02:00:00:00:02:00
```
2. What is the SSID and BSSID of the access point? Format: SSID, BSSID
```bash
MalwareM_AP, 02:00:00:00:00:00
```
3. What is the BSSID of the wireless interface that is already connected to the access point?
```bash
02:00:00:00:01:00
```
4. What is the PSK after performing the WPA cracking attack?
```bash
fluffy/champ24
```
