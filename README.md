# Porua scrapper
Scrap list of books, categories, authors from different sites

## Project Setup
1. Clone https://github.com/imtiaz-emu/porua_scrapper.git

2. Create a seperate `config.py` file. Where, you'll put the `SITE_URL`

3. Go to project directory and install dependencies
 Command: `pip install -r requirements.txt`

4. To run Category spider go to project folder and run on terminal:
    `scrapy crawl categories -o data/categories.json`
    This will create a **categories.json** file which contains the scrap data.

5. To run Sub Category spider go to project folder and run on terminal:
    `scrapy crawl categories -o data/sub_categories.json`
    This will create a **sub_categories.json** file which contains the scrap data.    

6. To run Author spider go to project folder and run on terminal 
    `scrapy crawl authors -o data/authors.json` 
    This will create a **author.json** file which contains the scrap data.
    
7. To run Author Detail spider go to project folder and run on terminal 
    `scrapy crawl author_details -o data/author_details.json` 
    This will create a **author_details.json** file which contains the scrap data.    








