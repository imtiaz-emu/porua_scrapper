# Porua scrapper

## Project Setup
1. Clone https://github.com/imtiaz-emu/porua_scrapper.git
2. Go to project directory and install dependencies
 Command: `pip install -r requirements.txt`

Scrap list of books, categories, authors from different sites 

To run a spider go to project folder and run on terminal:

`scrapy crawl categories -o categories.json`

This will create a **categories.json** file which contains the scrap data.

Create a seperate `config.py` file. Where, you'll put the `SITE_URL`
