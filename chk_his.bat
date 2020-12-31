REM schedule: weekly(everyday)-->c:\Program Files\chk_his\chk_his.bat
REM Advanced options: ">> c:\Program Files\chk_his\chk_his.log 2>&1"

c:
cd c:\Program Files\chk_his

echo 'job start:' >> chk_his.log
echo %date% %time% >> chk_his.log

REM let the network connect~~ on reboot
timeout 25

python chk_his.py
