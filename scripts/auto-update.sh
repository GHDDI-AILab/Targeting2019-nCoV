#!/bin/sh

ROOT="/home/ghddiai/Targeting2019-nCoV"
cd $ROOT
echo Current workspace: `pwd`

conda activate covid19

########################
# Update markdwon
########################

embedding-htmls() {
    if ! [[ $(git status) =~ "working tree clean" ]]; then
        echo "embedding-htmls"

        python scripts/embed_html.py --source_file "docs/preclinical_backup.md" --embedded_file "docs/file/list.html" --placeholder '<iframe src="list.html">' --target_file "docs/preclinical.md"

        python scripts/embed_html.py --source_file "docs/research_progress_backup.md" --embedded_file "docs/file/ldatopics.html" --placeholder '<iframe src="ldatopics.html">' --target_file "docs/research_progress.md"

        python scripts/embed_html.py --source_file "docs/CN_preclinical_backup.md" --embedded_file "docs/file/list.html" --placeholder '<iframe src="list.html">' --target_file "docs/CN_preclinical.md"

        python scripts/embed_html.py --source_file "docs/CN_research_progress_backup.md" --embedded_file "docs/file/ldatopics.html" --placeholder '<iframe src="ldatopics.html">' --target_file "docs/CN_research_progress.md"
    fi
}

embedding-htmls

########################
# git auto
########################

# Only once
# bash scripts/git-auto -d $ROOT -i 20 -b master -s origin -m "gh-deploy" -o -p

# Loop
nohup bash scripts/git-auto -d $ROOT -i 86400 -b master -s origin -m "gh-deploy" -p >> logs/auto-update.log &


