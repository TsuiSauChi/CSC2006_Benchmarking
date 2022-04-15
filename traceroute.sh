max=75
for i in `seq 2 $max`
do
    traceroute 192.168.196.149 >> test4.txt
done
