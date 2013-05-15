#! /bin/csh
set x = $1
sed -i 's/bz_13/pickles_uk_9/' $x
sed -i 's/bz_23/pickles_uk_20/' $x
sed -i 's/bz_24/pickles_uk_23/' $x
sed -i 's/bz_41/pickles_uk_63/' $x
sed -i 's/bz_71/pickles_uk_121/' $x
sed -i 's/bz_76/pickles_uk_127/' $x
sed -i 's|grid/bz77|grid/pickles/dat_uvk|' $x
