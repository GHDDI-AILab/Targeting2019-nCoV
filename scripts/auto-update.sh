#!/bin/sh

ROOT="/home/ghddiai/Targeting2019-nCoV"
cd $ROOT
echo `pwd`


########################
# Update markdwon
########################

# embed("preclinical_backup.md", "list.html", '<iframe src="list.html">', "preclinical.md")
# embed("research_progress_backup.md", "ldatopics.html", '<iframe src="ldatopics.html">', "research_progress.md")
# embed("CN_preclinical_backup.md", "list.html", '<iframe src="list.html">', "CN_preclinical.md")
# embed("CN_research_progress_backup.md", "ldatopics.html", '<iframe src="ldatopics.html">', "CN_research_progress.md")

python scripts/embed_html.py --source_file "docs/preclinical_backup.md" --embedded_file "docs/file/list.html" --placeholder '<iframe src="list.html">' --target_file "docs/preclinical.md"

python scripts/embed_html.py --source_file "docs/research_progress_backup.md" --embedded_file "docs/file/ldatopics.html" --placeholder '<iframe src="ldatopics.html">' --target_file "docs/research_progress.md"

python scripts/embed_html.py --source_file "docs/CN_preclinical_backup.md" --embedded_file "docs/file/list.html" --placeholder '<iframe src="list.html">' --target_file "docs/CN_preclinical.md"

python scripts/embed_html.py --source_file "docs/CN_research_progress_backup.md" --embedded_file "docs/file/ldatopics.html" --placeholder '<iframe src="ldatopics.html">' --target_file "docs/CN_research_progress.md"


########################
# git auto
########################

bash scripts/git-auto -d $ROOT -i 20 -b master -s origin -m "gh-deploy" -o -p


