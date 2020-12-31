<h1>Parental Control - browsing notifier (browser history checker)</h1>
Script runs hidden on <i>childs</i> PC in the background, sampling browsers histories - sends simple summary to designated <i>parental</i> email address.
<br><br>

create **credentials.py** by copying _"credentials (copy).py"_<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
sender mail &nbsp;+&nbsp; pw  &nbsp;+&nbsp;  receipients mail list

<br>

<h3>Linux:</h3>

_IF NOT INSTALLED:_ install python3<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
(sqlite3 should be included, if not: should be installed: "sudo apt install sqlite")

**copy**: <br> 
&nbsp; _chk_his.py_ <br>
&nbsp; _chk_his_env.py_ <br>
&nbsp; _chk_his.sh_ <br>
&nbsp; _credentials.py_ &nbsp; &nbsp; ---> &nbsp; &nbsp;  $HOME/_"install~dir"_/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        _(example: "/home/pi/Documents/chk_his/")_

**chmod** +x shk_his.sh

**crontab** -e &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp; ---> &nbsp;&nbsp; @reboot &nbsp; $HOME/_"install~dir"_/chk_his.sh

<br>

<h3>Windows:</h3>

_IF NOT INSTALLED:_ install python3<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
(sqlite3 should be included, if not: should be installed)

**copy**: <br>
&nbsp; _chk_his.py_  <br>
&nbsp; _chk_his_env.py_  <br>
&nbsp; _chk_his.bat_ <br>
&nbsp; _install.bat_ <br>
&nbsp; _requirements.txt_ <br>
&nbsp; _credentials.py_ &nbsp;&nbsp;&nbsp;&nbsp; ---> &nbsp; %HOMEDRIVE%%HOMEPATH%\\_"install~dir"_\ <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
<i>(example: C:\Users\ u-s-e-r \\chk_his\\)</i>  
                                                             
"**start**" --> "run" --> "shell:startup"

put "**chk_his.vbs**" file inside a dir that opened by above command

<br><br>
 
<h3>TODO:</h3>
- add Internet Explorer support <br>
- installer~ <br>
- online registration - credentials <br>
- white list online handle (get_yield) <br>




