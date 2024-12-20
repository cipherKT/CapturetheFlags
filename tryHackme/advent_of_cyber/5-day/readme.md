# Advent of cyber 2024 day 4
Start by accessing the machines using your desired option. I used openvpn to connect to the vpn and then access the IP.<br>
This is a website that is used to monitor the traffic to server and it contains too many good options like filtering using dates, filtering the sourceIP and type of the process and others are there too you can explore them.<br>
This was pretty easy task as it was fully guided room read the instruction carefully and you will be able to complete this room in less than an hour. <br> 

## Writeup
Start by going to `burpusite` and then look at the request and as mentioned load the payload that will give you `wish.txt` file in response and since we need to iterate over 20 request it is better to use intruder instead of repeater in intruder start by loading the request and choose `sniper attack` in this add the `wish_$0$.txt` here 0 is in dollars so intruder will iterate this and will send this as request. Now in payload set the numbers from `0 to 20` and then start the attack it will send 21 request and then will give you all responses which you can check one by one and in my case the response 15 had the flag which was `THM{Brut3f0rc1n6_mY_w4y}` and then in changelog there was another flag `THM{m4y0r_m4lw4r3_b4ckd00rs}` and these are the answers luckily.<br>

1. What is the flag discovered after navigating through the wishes?
```bash
THM{Brut3f0rc1n6_mY_w4y}
```
2. What is the flag seen on the possible proof of sabotage?
```bash
THM{m4y0r_m4lw4r3_b4ckd00rs}
```
