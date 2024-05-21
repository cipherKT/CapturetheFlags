# start

I first inserted the text visible on the input box and it worked 
Now if you inspect the site and try to check for cookies you will notice that each cookie had a uniwue id 
try entering the random values like 2,3,4,5 you and reload the webpage and then you will notice there is some text on each id that is 
"I love chocolate chip cookies" for the value 1 and for each value there is different cookie names associated 
so start entering values and sequence and i guess we will find something 
We can enter different values and try so for this we can automate this using burpsuite 
Open the burpsuite and go to proxy and open the burp browser and paste the link given -> [here](http://mercury.picoctf.net:21485/check)
Make sure intercept is off and go then start the intruder bu right clicking the responce in http history of the burpsuite's proxy tab
Now in intruder select the value where we can enter the values for different cookies and run it from -1 to 30 and 
Check the responce in tabular form and you will notice that the value at 20 has something different it is of length 1267 and others are in range of 1900s so try checking the response of that cookie value 
# BOOM!!!
got the flag 
picoCTF{3v3ry1_l0v3s_c00k135_94190c8a}

I found it at the value being 18 It is random so you can get it at different values so this is how you can solve this CTF's question

