#Parental Control - browsing notifier (browser history checker)
script runs on _childs_ pc in the background, sampling browsers histories - sends simple summary to designated _parental_ email address

**credentials.py**: &nbsp; &nbsp; sender mail &nbsp;+&nbsp; pw  &nbsp;+&nbsp;  receipients mail list

<br>

###Linux:

install python3 (sqlite3 should be included, if not: should be installed: "sudo apt install sqlite")

**copy**: <br> 
&nbsp; _chk_his.py_ <br>
&nbsp; _chk_his_env.py_ <br>
&nbsp; _chk_his.sh__ <br>
&nbsp; _credentials.py_ &nbsp; &nbsp; ---> &nbsp; &nbsp;  ~/_"install~dir"_/chk_his

**chmod** +x shk_his.sh

**crontab** -e      ----->    @reboot $HOME/_"install~dir"_/chk_his/chk_his.sh

<br>

###Windows:

install python3 (sqlite3 should be included, if not: should be installed)

**copy**: <br>
&nbsp; _chk_his.py_  <br>
&nbsp; _chk_his_env.py_  <br>
&nbsp; _chk_his.bat_ <br>
&nbsp; _credentials.py_ &nbsp; &nbsp;   ---> &nbsp; %HOMEDRIVE%%HOMEPATH%\\_"install~dir"_\chk_his &nbsp; 
                                                      _(C:\Users\ u-s-e-r \"install~dir"\chk_his)_  
                                                             
"**start**" --> "run" --> "shell:startup"

put "**chk_his.vbs**" file inside a dir that opened by above command

<br><br>
 
###TODO:
- installer~
- online registration - credentials
- white list online handle (get_yield)




