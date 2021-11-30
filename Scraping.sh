#!/bin/bash

echo "Enter Stock Symbol: "
read sym

printf "$sym\n" > testinput.txt

curl https://finance.yahoo.com/quote/$sym/history/ | html2text | sed -n '/Date/,$p' | sed -n '/*Close/q;p' >> testinput.txt

