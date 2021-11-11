#!/bin/bash
curl  https://finance.yahoo.com/quote/TSLA/history/ | html2text | sed -n '/Date/,$p' | sed -n '/*Close/q;p'

