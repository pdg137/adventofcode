# read coords into x and y vars
readarray -t x <<< $(cut -d, -f1 data09.txt)
readarray -t y <<< $(cut -d, -f2 data09.txt)

max=0
for ((i = 0; i < ${#x[@]}; i++))
do
    for ((j = 0; j < ${#x[@]}; j++))
    do
        x1=${x[i]}
        y1=${y[i]}
        x2=${x[j]}
        y2=${y[j]}

        if [[ $x1 -lt $x2 ]]
        then w=$(($x2-$x1+1))
        else w=$(($x1-$x2+1))
        fi
        if [[ $y1 -lt $y2 ]]
        then h=$(($y2-$y1+1))
        else h=$(($y1-$y2+1))
        fi

        area=$(($w*$h))
        if [[ $max -lt $area ]]
        then max=$area
        fi
        #echo $x1,$y1-$x2,$y2: ${w}x${h} = $(($w*$h)) - max $max
    done
done

echo $max
