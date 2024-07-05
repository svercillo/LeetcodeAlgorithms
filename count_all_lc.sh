# Assign the number of files in the 'easy' directory to var1
var1=$(ls easy | wc -l)

# Assign the number of files in the 'medium' directory to var2
var2=$(ls medium | wc -l)

# Assign the number of files in the 'hard' directory to var3
var3=$(ls hard | wc -l)

# Calculate total
total=$(($var1 + $var2 + $var3))

# Calculate the percentage of each directory
easy_percentage=$(awk "BEGIN { pc=100*$var1/$total; i=int(pc); print (pc-i<0.5)?i:i+1 }")
medium_percentage=$(awk "BEGIN { pc=100*$var2/$total; i=int(pc); print (pc-i<0.5)?i:i+1 }")
hard_percentage=$(awk "BEGIN { pc=100*$var3/$total; i=int(pc); print (pc-i<0.5)?i:i+1 }")

echo "TOTAL: " $total

echo "============================"

echo "Easy: " $var1 "("$easy_percentage"%)"
echo "Medium: " $var2 "("$medium_percentage"%)"
echo "Hard: " $var3 "("$hard_percentage"%)"