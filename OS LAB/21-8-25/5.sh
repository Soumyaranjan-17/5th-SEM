# 5. WASCP to check wheather the number or string is a pallindrome or not.

#!/bin/bash
read -p "Enter a string or number: " input

rev=$(echo "$input" | rev)

if [ "$input" == "$rev" ]; then
  echo "$input is a palindrome."
else
  echo "$input is not a palindrome."
fi

