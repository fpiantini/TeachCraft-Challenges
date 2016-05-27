#!/bin/bash

if [ $# -lt 1 ]; then
  echo "please specity a Minecraft server IP"
  exit 1
fi

newip=$1
tmpfile=/tmp/newip.py

for file in *.py; do
  rm -f $tmpfile
  cat $file | sed 's/address="\([^"]*\)"/address="'${newip}'"/' > $tmpfile
  rm -f $file.py.saved
  mv $file $file.py.saved
  mv $tmpfile $file
done

exit 0


