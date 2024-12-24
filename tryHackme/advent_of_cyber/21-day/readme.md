This is the room about reverse engineering.<br>
Using `pestudio` we can check the details of file and then we can decompile the file to look closer in it.<br> 
First file is just a demo and it is not causing any harm to system so we ran that now our task is to reverse engineer another file and we are asked following: <br>

1. What is the function name that downloads and executes files in the WarevilleApp.exe?
```bash
DownloadAndExecuteFile
```
2. Once you execute the WarevilleApp.exe, it downloads another binary to the Downloads folder. What is the name of the binary?
```bash
explorer.exe
```
3. What domain name is the one from where the file is downloaded after running WarevilleApp.exe?
```bash
mayorc2.thm
```
4. The stage 2 binary is executed automatically and creates a zip file comprising the victim's computer data; what is the name of the zip file?
```bash
CollectedFiles.zip
```
5. What is the name of the C2 server where the stage 2 binary tries to upload files?
```bash
anonymousc2.thm
```
