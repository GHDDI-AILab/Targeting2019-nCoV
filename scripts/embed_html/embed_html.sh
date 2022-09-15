#!/bin/sh

list=`cat list.html`
# echo "${list_html}"
# sed -i -r 's/<iframe src="list.html">/$list_html/g' preclinical.md

placeholder='<iframe src="list.html">'
# sed -i "s/${placeholder}/${list}/" preclinical.md
# sed -i -r "s/${placeholder}/${list}/g" preclinical.md
