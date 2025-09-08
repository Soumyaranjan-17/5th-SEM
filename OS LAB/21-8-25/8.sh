# 8. WASCP that greets each loggedIn user "Good morning or Good evening" on the current system time

#!/bin/bash
hour=$(date +%H)

if [ "$hour" -lt 12 ]; then
  greet="Good morning"
else
  greet="Good evening"
fi

users=$(who | awk '{print $1}' | sort | uniq)

for user in $users
do
  echo "$greet, $user!"
done
