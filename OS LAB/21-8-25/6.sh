# 6. WASCP to count the number of words and lines in a given file.

#!/bin/bash
read -p "Enter file name: " filename

if [ -f "$filename" ]; then
  lines=$(wc -l < "$filename")
  words=$(wc -w < "$filename")
  echo "Lines: $lines"
  echo "Words: $words"
else
  echo "File does not exist."
fi

