#!/bin/bash
echo "Enter the marks of Six subjects : "
read m1 m2 m3 m4 m5 m6
let total=$m1+$m2+$m3+$m4+$m5+$m6
let per=(total/6)
echo student total marks:$total
echo Student percentage :$per
if [ $per -ge 69 ]
then
echo gread :Distinctional
elif [ $per -ge 59 -a $per -lt 70 ]
then
echo Gread :FirstClass
elif [ $per -ge 49 -a $per -lt 60 ]
then
echo Gread :Secondclass
elif [ $per -ge 50 -a $per -lt 60 ]
then
echo Gread :D
elif [ $per -ge 40 ] && [ $per -lt 50 ]
then
echo Gread :Pass
else
echo "Gread :F(fail) "
fi
