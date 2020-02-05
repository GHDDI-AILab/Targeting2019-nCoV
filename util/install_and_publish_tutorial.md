# Install & Publish Tutorial
The information portal is built upon Github pages + Mkdocs, this tutorial will guide you to install necessary packages and publish content to website.


## Package Install
All the contents of this website are edited with markdown format decorators. The markdown files are then converted to static html pages via `Mkdcos` package. Use the following commands to install necessary packages
```
pip install mkdocs
pip install pymdown-extensions
```

## Publish to Github Pages
* First organize all contents within the `docs` folder.
* Edit website navigation map by editing the `nav` section in `mkdocs.yml`, here is an example

  ```yml
  nav:
      - Home: index.md
      - Data Download:
        - Data Mining: CoV_Experiment_Data.md
        #- Drugs and Candidates: drug_candidates.md
        - Targets: nCov_Targets.md
        - Structures: nCov_Structures.md
        - Research Update: research_progress.md
      - Community Discussion: contact_us.md
      - History: history.md
  ```
* Verify rendering effect.    
  Navigate to the root folder of this repo, type `mkdocs serve` in command line, this will start a website server locally on `127.0.0.1:8000`. You can use your web browser to view the local website, make sure every editted content is rendered properly.
* Officially publish to Github pages    
  Type `mkdocs gh-deploy` in command line.
