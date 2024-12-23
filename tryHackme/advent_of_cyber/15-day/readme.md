# Advent of cyber 2024 day 4
Start by accessing the machines using your desired option. I used openvpn to connect to the vpn and then access the IP.<br>
This is a website that is used to monitor the traffic to server and it contains too many good options like filtering using dates, filtering the sourceIP and type of the process and others are there too you can explore them.<br>
This was pretty easy task as it was fully guided room read the instruction carefully and you will be able to complete this room in less than an hour. <br> 

- Use the "Security" tab within Event Viewer to answer questions 1 and 2.
1. On what day was Glitch_Malware last logged in?

Answer format: DD/MM/YYYY
```bash
07/11/2024
```
2. What event ID shows the login of the Glitch_Malware user?
```bash
4624
```
3. Read the PowerShell history of the Administrator account. What was the command that was used to enumerate Active Directory users?
```bash
Get-ADUser -Filter * -Properties MemberOf | Select-Object Name
```
4. Look in the PowerShell log file located in `Application and Services Logs -> Windows PowerShell`. What was Glitch_Malware's set password?
```bash
SuperSecretP@ssw0rd!
```
5. Review the Group Policy Objects present on the machine. What is the name of the installed GPO?
```bash
Malicious GPO - Glitch_Malware Persistence
```
