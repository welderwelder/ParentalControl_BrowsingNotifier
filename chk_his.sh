#!/bin/bash
# crontab -e  <------- @reboot ./~/Documents/chk_his/chk_his.sh &
# crontab -e  <------- @reboot ./$HOME/Documents/chk_his/chk_his.sh &
# crontab -e  <------- @reboot lxterminal --command="/bin/bash --init-file ~/Documents/chk_his/chk_his.sh"
# crontab -e  <------- @reboot $HOME/Documents/chk_his/chk_his.sh  --- need chmod +x  !!!
# crontab -e  <------- */30 * * * * $HOME/Documents/chk_his/chk_his.sh  --- need chmod +x  !!!     # every 30 minutes

cd $HOME/Documents/chk_his/

echo 'job start:' >> chk_his.log
date >> chk_his.log
sleep 25      # let the network connect~~ on reboot

chk_run=`ps x | grep 'python3 chk_his.py' | grep -v "grep"`

if test -z "$chk_run";then
  echo 'inside if:' >> chk_his.log
  date >> chk_his.log
  python3 chk_his.py >> chk_his.log 2>&1  
fi
