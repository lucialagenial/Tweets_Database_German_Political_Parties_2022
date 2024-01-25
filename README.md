# **Tweets Database: German Political Parties 2022**
This repository holds a database containing the tweets shared by the main German political parties in 2022. The databased was acquired during the last third of 2022 and beginning of 2023, a couple of months of the changes made in the X (then Twitter) API. 
The scrapping of these tweets was a crucial part of the field work for my doctoral research project titled "Discourses on Radical Right Identity on Social Media. The case of the German political party Alternative for Germany on Twitter", as part of the Doctoral Program on Management of Culture ([Doctorado en Gestión de la Cultura](https://gestioncultural.udgvirtual.udg.mx/)) of the University of Guadalajara, Mexico. 
My aim with these databases it to give public access to the information, now that the new X APIs, both v2. and v1.1, have undergone significant modifications in terms of accessibility and monetization. 

### **Outline**
```
 ./Tweets_Database-German-Political-Parties_2022 /
│
├── Code/
│   ├── Twitter_timeline_query_by_user.pycsv
│   └── X_timeline_query-by-userID_2024.py
│
├── Data_Tweets/
│   ├── AfD-tweets_2022.csv
│   ├── CDU-tweets.csv
│   ├── CSU-tweets.csv
│   ├── die_Gruenen-tweets.csv
│   ├── dieLinke-tweets.csv
│   ├── FDP-tweets.csv
│   └── SPD-tweets.csv
│
└── README.md
```

### **Database**
The databases are composed by comma-separated values ```(.csv)``` files, which store tabular data. The columns of each datafile are the following:
* ```Datetime```: string that stores a data value as a contiguous series of fields that represents each time unit (year, month, day, and so forth) in the data type declaration.
* ```Tweet Id```: The integer representation of the unique identifier for this Tweet.
* ```Text```: The actual UTF-8 text of the Tweet. See [twitter-text](https://developer.twitter.com/en/docs/counting-characters) for details on what characters are currently considered valid.
* ```favorite_count```: Public engagement metrics for the Tweet at the time of the request for favorite counts.
* ```retweet_count```: Public engagement metrics for the Tweet at the time of the request for retweets of the original tweet.

Regarding the data, the accounts from which the timelines were scraped are the following: 

* [@AfD](https://twitter.com/AfD) – Alternative für Deutschland
* [@Die_Gruenen](https://twitter.com/Die_Gruenen) – Bündnis 90/die Grünen
* [@CDU](https://twitter.com/Cdu) – Christlich Demokratische Union Deutschlands
* [@spdde](https://twitter.com/spdde) – Sozialdemokratische Partei Deutschlands
* [@fdp](https://twitter.com/fdp) – Freie Demokraten
* [@CSU](https://twitter.com/csu) – Christlich-Soziale Union
* [@dieLinke](https://twitter.com/dielinke) – Die Linke 

### **Python Code – Twitter/X Timeline Tweet Scrapers**
In this repository you will also find the original code for timeline scrapping using the ```Tweepy``` library for Python, 
which was written before May 2023 for the original ```API v1.1```, as well as a newer version of a similar code now modified for the ```API v2``` aimed to be
used with X’s ```Basic``` package.



**For further information:**

[Tweepy client user timeline documentation](https://docs.tweepy.org/en/stable/api.html#tweepy.API.user_timeline)

[X Developer licenses and accesses](https://developer.twitter.com/en/docs/twitter-api)


### **Disclaimer:** 
These resources are being shared for pure scientific and analytical purposes. I do now own the information; all the data
is publicly available in the timelines of the previously mentioned accounts. My attempt is just to provide a systematized
and structured representation of the information for further analysis. Information of the tweets and public metrics might 
vary with time.



**If you use any of this information, please reference:**


```2024```- Morales Lizarraga, Lucia
