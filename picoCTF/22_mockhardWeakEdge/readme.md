# start
start by downloading the file this is pptm file that is a powerpoint presenatation and there is one catch that this files are also zip files so unzip the fiel navigate into `ppt` directory navigate `slideMaster` directory then you will find a file names hidden try getting content from it. It seems like a `base64` encoded message but there are space to use command: <br> 
```bash
cat hidden | sed 's/ //g'
```
In this sed is tool for string maipulations s means substitute and then after forward slash we proivde the char to substitute here it is white space so there is space then another forward slash for mentioning the char with which we will replace this that is black so again forward slash and g for global. <br> 
Got the text give it base64 decoder and get the flag 
# boom !!!
```
picoCTF{D1d_u_kn0w_ppts_r_z1p5}
```
