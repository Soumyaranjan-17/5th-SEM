# 7. WASCP to print the numbers from n down to 1 using while loop.

#!/bin/bash
read -p "Enter a number: " n

while [ $n -ge 1 ]
do
  echo -n "$n "
  ((n--))
done
echo
