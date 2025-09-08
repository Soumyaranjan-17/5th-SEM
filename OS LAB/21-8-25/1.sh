# 1. WASCP to print the first 10 natural number using for loop and while loop.

#!/bin/bash
# Using for loop
echo "First 10 natural numbers using for loop:"
for ((i=1; i<=10; i++))
do
  echo -n "$i "
done

echo -e "\nFirst 10 natural numbers using while loop:"
# Using while loop
i=1
while [ $i -le 10 ]
do
  echo -n "$i "
  ((i++))
done
