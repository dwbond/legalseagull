#!/bin/bash

while read line
do
	arr=( $line )
	url=${arr[0]}
	unset arr[0]
	category=${arr[@]}
	mkdir "$category"
	curl $url | sed '0,/^<h1>topic/d' | sed -n -e '0,/^<!--/p' | sed '$d' | sed '$d' | sed 's/">.*//' | sed 's/<p><a href="/http:\/\/www.law.cornell.edu/' > "$category/contents.html"
done < $1
