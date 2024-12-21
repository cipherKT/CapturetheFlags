# Advent of cyber 2024 day 4
Start by accessing the machines using your desired option. I used openvpn to connect to the vpn and then access the IP.<br>
This is a website that is used to monitor the traffic to server and it contains too many good options like filtering using dates, filtering the sourceIP and type of the process and others are there too you can explore them.<br>
This was pretty easy task as it was fully guided room read the instruction carefully and you will be able to complete this room in less than an hour. <br> 

## Writeup
Start by accessing making the payload as mentioned in room and then start listening on port `8888` as mentioned, and then you have every thing ready now as mentioned access the email server and send mail to `marta@socmas.thm` with the `msf4.docm` file you should rename this to something else so that it looks legit, I named if `invoice.docm` and pretended she won a lottery and for product to be owned by her we need to follow protocols and invoice should be signed by her and then forwarded the mail and then after waiting for 1-2 minutes i got reverse shell easily.

1. What is the flag value inside the flag.txt file that’s located on the Administrator’s desktop?
```bash
THM{PHISHING_CHRISTMAS}
```
