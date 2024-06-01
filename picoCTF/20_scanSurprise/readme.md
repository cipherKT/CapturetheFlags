# start
Run this command to unzip the zip file after downloading it 
```bash
unzip challenge.zip
```
Then just go into the directories you will find a flag.png it is a QR code you can use the tool called zbar to scan that in terminal only<br>
## zbar-tool installation

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install zbar-tools
```

this will install the zbar and now you can go to the directory where there is png file of the qr code and run the following commang: <br>
```bash
zbarimg flag.png -q --raw
```
# boom !!!
```
picoCTF{p33k_@_b00_0194a007}
```
