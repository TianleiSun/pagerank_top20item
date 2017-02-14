for i in {1..11}; 
do python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output.txt;  
cp output.txt input.txt; 
cat /dev/null > output.txt; 
done;