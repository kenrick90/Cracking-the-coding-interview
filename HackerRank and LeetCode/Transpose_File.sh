#!/bin/bash
  
numberOfRow=$(head -1 $1 | wc -w)
i=1

while [ $i -le $numberOfRow ]
do
        awk "{print \$$i}" $1 | paste -s -d " "
        ((i=$i+1))
done
