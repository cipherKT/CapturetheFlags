# start
Open the PcapNg-file it is a packet capture file so open it in wireshark  <br>
It is clearly seen that there are 987 packets over the duration of 23s. This traffic is of a less active network <br> 
Now after going into statistics protocol hierarchy it is clear that most of the traffic is of http  <br>
So checking the conversation in statistics most of the traffic is divided in 4 conversation  <br>
1. 192.168.38.104 -> 18.222.37.134
2. 192.168.38.104 -> 169.254.169.254
3. 192.168.38.104 -> 192.168.38.103
4. 192.168.38.104 -> 192.168.38.105 

So we will check the traffic of each conversation one by one  <br> 
checking the traffic of first conversation:  <br>
Apply filter IPv4 section of conversation select the 192.168.38.104 and then right click apply as a filter in that select the bidirectional filter A <-> B <br> 
We have recieved 12 packets out of this there are 2 http packets in second packet there is something similar to flag cvpbPGS{c33xno00_1_f33_h_qrnqorrs} <br> 

clearly this is a cipher so lets decode its encryption formula <br> 
after observing it is clear that this runs on a formula (+13)%26 <br> 
so whatever the char is it is converted to its ascii value and then cipher is applied and then again converted to char values <br> 
So we can do this manually I have mentioned the decryption table in crack.txt 

# Boom !!!

```
picoCTF{p33kab00_1_s33_u_deadbeef}
```


