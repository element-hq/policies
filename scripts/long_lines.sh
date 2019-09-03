#!/bin/sh
#
# Quick-and-dirty script to fold long paragraphs but leave title text alone.
# Can be used as a git pre-commit hook.

if [[ "$1" == "--all" ]]; then
    CHANGED_FILES=$(find docs -name '*.md')
else
    CHANGED_FILES=$(git diff --staged --name-only | grep "^.*\.md\$")
fi

FILES_CONTAINING_LONG_LINES=()
for FILE in $CHANGED_FILES; do
    if [ "$(grep "^[^#].\{80\}" $FILE | wc -l)" -gt 0 ]; then
        FILES_CONTAINING_LONG_LINES+=( "$FILE" )
    fi
done

if [ "$FILES_CONTAINING_LONG_LINES" != "" ]; then
    echo "Warning: Long lines of paragraph text identified"
    echo "================================================"
    for FILE in ${FILES_CONTAINING_LONG_LINES[@]}; do
        echo "  $FILE"
    done
    exec < /dev/tty
    read -p "Do you want to fix? (Long titles will not be modified; default no):" MODIFY
    shopt -s nocasematch
    for FILE in $FILES_CONTAINING_LONG_LINES; do
        TEMPFILE=$(echo "/tmp/`basename $FILE`.`date +%s`.tmp")
        while IFS= read -r LINE; do
            if [[ $LINE == "#"* ]]; then
                echo $LINE >> $TEMPFILE
            else
                echo $LINE | fold -s -w 80 >> $TEMPFILE
            fi
        done < $FILE
        mv $TEMPFILE $FILE
    done
fi
exit 1
