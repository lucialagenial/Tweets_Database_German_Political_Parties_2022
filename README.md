Overview
This repository holds a database containing the tweets shared by the main German political parties in 2022. The databased was acquired during the last third of 2022 and beginning of 2023, a couple of months of the changes made in the X (then Tweeter) API. 
The scrapping of these tweets was a crucial part of the field work for my doctoral research project titled "Discourses on Radical Right Identity on Social Media. The case of the German political party Alternative for Germany on Twitter", as part of the Doctoral Program on Management of Culture (Gestión de la Cultura) of the University of Guadalajara, Mexico. 
My aim with these databases it to give public access to the information, now that the new X APIs, both v2. and v1.1, have undergone significant modifications in terms of accessibility and monetization. 
Database
The databases are composed by comma-separated values (.csv) files, which stores tabular data. The columns of each datafile are the following:
Datetime: DATETIME stores a data value as a contiguous series of fields that represents each time unit (year, month, day, and so forth) in the data type declaration.
Tweet Id: The integer representation of the unique identifier for this Tweet.
Text: The actual UTF-8 text of the Tweet. See twitter-text for details on what characters are currently considered valid.
favorite_count: Public engagement metrics for the Tweet at the time of the request for favorite counts.
Retweet_count: Public engagement metrics for the Tweet at the time of the request for retweets of the original tweet.
Regarding the data, the accounts from which the timelines were scraped are the following: 
@AfD – Alternative für Deutschland
@Die_Gruenen – Bündnis 90/die Grünen
@CDU – Christlich Demokratische Union Deutschlands
@spdde – Sozialdemokratische Partei Deutschlands
@fdp – Freie Demokraten
@CSU – Christlich-Soziale Union
@dieLinke – Die Linke 
Python Code – Twitter/X Timeline Tweet Scrapers
In this repository you will also find the original code for timeline scrapping using the Tweepy library for Python, which was written before may 2023, as well as a newer version of a similar code now modified for the API v2 aimed to be used with X’s “Basic” package.

For further information see the documentation of Tweepy
Disclaimer: 
These resources are being shared for pure scientific and analytical purposes. I do now own the information; all the data is publicly available in the timelines of the previously mentioned accounts. My attempt is just to provide a systematized and structured representation of the information for further analysis. Information of the tweets and public metrics might vary with time.


2023- Lucia Morales Lizarraga 
![image](https://github.com/lucialagenial/Tweets_Database_German_Political_Parties_2022/assets/69418959/2b840a13-7b4b-455e-993b-6398b232f5c6)
