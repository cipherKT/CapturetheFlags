# Advent of cyber 2024 day 1
Start by accessing the machines using your desired option. I used openvpn to connect to the vpn and then access the *IP*. <br>
This is a website to convert youtube videos to .mp3 format so add one URL in it and download the zip file containing .mp3 file. <br>
Here you will get two files *song.mp3* and *somg.mp3*. Here things become suspicious as there are two songs one with spelling mistake so try running exiftool on it as mentioned in rooom.<br>
Here you will get to know that *somg.mp3* is not a song but a powershell script which looks for *crypto wallets* in system and then look for stored credentials of *chrome* and *firefox* and then sends that to *c2* server in order to gain confidential informations.<br>
Now using this information try to answer the questions of room 

1. author of song?<br>
ans -
- run exiftool on song.mp3 and you will get the answer 
```bash
Tyler Ramsbey
```

