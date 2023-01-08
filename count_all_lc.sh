var1=$(ls easy | wc -l)
var2=$(ls medium | wc -l)
var3=$(ls hard | wc -l)

echo "TOTAL: " "$(($var1 + $var2 + $var3))"

echo "============================"

echo "Easy: " $var1
echo "Medium: " $var2
echo "Hard: " $var3
