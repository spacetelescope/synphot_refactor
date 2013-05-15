awk '{print "comp/acs/"$1}' acs_pinlist.txt > combined_pinlist.txt
awk '{print "comp/nicmos/"$1}' nicmos_pinlist.txt >> combined_pinlist.txt
awk '{print "comp/stis/"$1}' stis_pinlist.txt >> combined_pinlist.txt

awk '{print "comp/acs/"$1}' acs_bluelist.txt > combined_bluelist.txt
