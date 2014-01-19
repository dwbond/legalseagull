#!/bin/bash

for directory in Abortion
do
  while read line
  do
    url=( $line )
    filename=$( echo $url | sed 's/\(.*\)\/\(.*\/\)//')
    curl $url | sed '0,/^<casecontent>/d' | sed -n -e '0,/<\/casecontent/p' | sed '$d' > "$directory/$filename"
  done < "$directory/contents.html"
done
