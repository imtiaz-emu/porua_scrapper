# porua_scrapper
Scrap list of books, categories, authors from different sites 

To run a spider go to project folder and run on terminal:

`scrapy crawl categories -o categories.json`

This will create a **categories.json** file which contains the scrap data.

Create a seperate `config.py` file. Where, you'll put the `SITE_URL`
