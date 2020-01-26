# nCov_Info_Share
Information sharing portal about nCov/SARS/MERS for drug discovery
URL of the online portal: https://ghddi-ailab.github.io/nCov_Info_Share/

## A Short Tutorial for Content Contributor
### Contribute Content
Write your contents in markdown format and save them in /docs folder, with file extention **.md**

### Organize Pages
Specify your content in `mkdocs.yml`, section `nav` as follows:
```
    - nCov:
      - todo I: todo_I.md
      - todo II: todo_II.md
```
in which `nCov` will be top level folder, and `todo I` and `todo II` will be the second level pages

### Publish to Github Pages
just by `mkdocs gh-deploy`