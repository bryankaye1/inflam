date=$1
filename=$2

drugname=`python assign_drug.py $filename`

echo cp data/$filename/$date/${date}-${drugname}.dat
