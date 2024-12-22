# Advent of cyber 2024 day 4
Start by accessing the machines using your desired option. I used openvpn to connect to the vpn and then access the IP.<br>
This is a website that is used to monitor the traffic to server and it contains too many good options like filtering using dates, filtering the sourceIP and type of the process and others are there too you can explore them.<br>
This was pretty easy task as it was fully guided room read the instruction carefully and you will be able to complete this room in less than an hour. <br> 

## Writeup
Start by opening the `burpsuite` and its proxy browser and paste the `url` of the bank's website and then as guided in room go through the instructions and do the transaction more than balance using race conditions in tester account and now we need to do the same in glitch's account so that we can get the flag so i just copied requests of $200 for 15 times and send them in parallel manner and boom!! got the flag. 

1. What is the flag value after transferring over $2000 from Glitch's account?
```bash
THM{WON_THE_RACE_007}
```
