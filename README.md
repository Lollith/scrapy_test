# scrapy_test

The goal of this project is to create a dataset containing comments left by movie enthusiasts on Allociné. The desired outcome is a CSV file with the columns: title, review, and stars.

"Title" represents the movie title, "review" corresponds to the comment, and "stars" indicates the number of stars given by the movie enthusiast (on a scale of 1 to 5).

1. setting up the miniconda environnement
- scrapy
- flake8
=> environment.yml

For recreate the environment :
```conda env create -f environment.yml```

2. Creating a Project
```scrapy startproject datasets```

3. Items Creation
title, review, stars

4. Spider creation 
name = "reviews_allocine"

5. start the spider
```scrapy crawl reviews_allocine```

6. Parsing

7. instanciation and CSV creation
```scrapy crawl reviews_allocine -o reviews_allocine.csv```


