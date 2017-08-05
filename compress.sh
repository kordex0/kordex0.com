#!/usr/bin/env bash
rm kordex0com.zip
FILES="application.py development.ini requirements.txt setup.py "
FILES+="$(find kordex0 ! -path '*__pycache__*') "
FILES+="$(find .ebextensions) "
FILELINES=""
for f in $(echo $FILES | tr " " "\n")
do
    FILELINES+="$f\n"
done
echo -e $FILELINES | zip -@ kordex0com.zip