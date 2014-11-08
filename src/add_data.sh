date=$1
filename=$2

drugname=`python assign_drug.py $filename`

fpn=~/Desktop/python/${filename}
dest=~/Desktop/inflam/data/${date}-${drugname}-${filename}
cp $fpn $dest
#echo git add -$dest

#echo msg="added $filename"
#echo git commit -m "'$msg'"
#echo ="new file added to repo '$msg'"
