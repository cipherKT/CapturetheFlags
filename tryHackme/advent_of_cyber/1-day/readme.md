# Advent of cyber 2024 day 1
Start by accessing the machines using your desired option. I used openvpn to connect to the vpn and then access the *IP*. <br>
This is a website to convert youtube videos to .mp3 format so add one URL in it and download the zip file containing .mp3 file. <br>
Here you will get two files *song.mp3* and *somg.mp3*. Here things become suspicious as there are two songs one with spelling mistake so try running exiftool on it as mentioned in rooom.<br>
Here you will get to know that *somg.mp3* is not a song but a powershell script which looks for *crypto wallets* in system and then look for stored credentials of *chrome* and *firefox* and then sends that to *c2* server in order to gain confidential informations.<br>
Now using this information try to answer the questions of room 

1. author of song?<br>
- run exiftool on song.mp3 and you will get the answer 
```bash
Tyler Ramsbey
```
2. The malicious PowerShell script sends stolen info to a C2 server. What is the URL of this C2 server? <br>
- After running exiftool of somg.mp3 you get powershell script which is available on github you can check it and you will get the url of file in raw form and you can check the C2 servers url on it. <br> 

3. Who is M.M? Maybe his Github profile page would provide clues? <br>
- After finding the profile of Mayor Malware you can find the name on profile of the user 
```bash
Mayor Malware
```
4. What is the number of commits on the GitHub repo where the issue was raised?<br>
- This can be easily verified by just looking at repo's home page and answer is: <br>
```
1
```

