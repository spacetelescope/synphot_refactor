#! /bin/csh
#First of all, throw away the comments;
# then extract only the file name and the pin/don't pin flag. 

grep -v ^# list.ACS.txt | awk '{print $12 $2}'  > acs_pinlist.txt
