# 3. WASCP to design a simple calculator using case statement.

#!/bin/bash
echo "Enter two numbers:"
read a
read b

echo "Choose operation: + - * /"
read op

case $op in
  +) echo "$a + $b = $((a + b))" ;;
  -) echo "$a - $b = $((a - b))" ;;
  \*) echo "$a * $b = $((a * b))" ;;  # Escape * with backslash
  /) echo "$a / $b = $((a / b))" ;;
  *) echo "Invalid operator" ;;
esac
