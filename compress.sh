#!/usr/bin/env bash
rm kordex0com.zip
BASE_FILES="application.py development.ini requirements.txt setup.py"
APP_FILES="$(find kordex0 -name "*py")"
FILES="${BASE_FILES} ""${APP_FILES}"
FILELINES=""
for f in $(echo $FILES | tr " " "\n")
do
    FILELINES+="$f\n"
done
echo -e $FILELINES | zip -@ kordex0com.zip