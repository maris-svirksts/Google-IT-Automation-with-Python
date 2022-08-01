#!/bin/bash

> oldFiles.txt

files=$(grep "jane " ../data/list.txt | cut -d ' ' -f 3)

for f in $files; do
  FILE=$HOME$f; echo "$FILE"
  if test -e $FILE; then
    echo $FILE >> oldFiles.txt; echo
  else
    echo "File doesn't exist"; echo
  fi
done
