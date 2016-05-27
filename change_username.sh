#!/bin/bash

if [ $# -lt 1 ]; then
  echo "please specity a Minecraft player name"
  exit 1
fi

newname=$1
tmpfile=/tmp/newplayer.py

for file in *.py; do
  rm -f $tmpfile
  cat $file | sed "s/talete/$newname/" > $tmpfile
  rm -f $file.py.saved
  mv $file $file.py.saved
  mv $tmpfile $file
done

exit 0


