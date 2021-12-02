#!/bin/bash

echo "Enter Stock Symbol to Analyze: "
read sym

echo "" > testinput.txt
printf "$sym\n" > testinput.txt

if curl https://finance.yahoo.com/quote/$sym/history/ | html2text |grep 'Redirecting'; then
	echo "Invalid Stock Symbol!"
else
	curl https://finance.yahoo.com/quote/$sym/history/ | html2text | sed -n '/Date/,$p' | sed -n '/*Close/q;p' | sed '/Dividend/d' | sed '/-/d' >> testinput.txt
fi

python3 app.py
echo "" > testinput.txt