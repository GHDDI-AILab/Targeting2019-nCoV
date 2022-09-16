import argparse
from pathlib import Path


# source = Path("preclinical.md")
# text_source = source.read_text()
# insert = Path("list.html")
# text_insert = insert.read_text()
# text_to_search = '<iframe src="list.html">'
# replacement_text = text_insert
# source.write_text(text_source.replace(text_to_search, replacement_text))


def embed(source_file, embedded_file, placeholder, target_file):
    source = Path(source_file)
    text_source = source.read_text()
    insert = Path(embedded_file)
    text_insert = insert.read_text()
    text_to_search = placeholder
    replacement_text = text_insert
    target = Path(target_file)
    target.write_text(text_source.replace(text_to_search, replacement_text))


# embed("preclinical_backup.md", "list.html", '<iframe src="list.html">', "preclinical.md")
# embed("research_progress_backup.md", "ldatopics.html", '<iframe src="ldatopics.html">', "research_progress.md")

# embed("CN_preclinical_backup.md", "list.html", '<iframe src="list.html">', "CN_preclinical.md")
# embed("CN_research_progress_backup.md", "ldatopics.html", '<iframe src="ldatopics.html">', "CN_research_progress.md")

parser = argparse.ArgumentParser(description="")

parser.add_argument("--source_file", type=str, help="")
parser.add_argument("--embedded_file", type=str, help="")
parser.add_argument("--placeholder", type=str, help="")
parser.add_argument("--target_file", type=str, help="")
args = parser.parse_args()

source_file = args.source_file
embedded_file = args.embedded_file
placeholder = args.placeholder
target_file = args.target_file

# print(args)
embed(source_file, embedded_file, placeholder, target_file)