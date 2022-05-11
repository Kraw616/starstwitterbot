# Welcome to Stars the Twitter Sentiment Analyzer!
Authors: Jacob Krawitz, Aleksander DeMaio, Jordan Wells

Professor/Course: Dr. Silveyra/CS Cue (CSI-370) Project 

Muhlenberg College, 2022

## Description: 

This Python project aims to predict the zodiac/star sign of a given tweet's author based on the "emotional profiles" of typical users that allign with that star sign. In other words, the average emotional profile of a tweet of a certain sign (what percent of an average tweet is "positive", "negative", etc.) is compared to the emotional profile of an inputted tweet, and the closest average in value is the model's prediction. 

To interact with Twitter's API and collect tweets, we used the Tweepy Python library. To generate these emotional profiles/perform emotional analysis of tweets, we used the NRClex library. To run our demo, we use Jupyter Notebook for organization and the ability to easily manage large datasets.

As of now, our model only predicts Libra and Cancer for a given tweet. This is likely due to the way we are calculating the closest star sign motional profile, as well as inconsistencies in data collection. In the future, we would hope to collect more data and devise a way to better predict a given tweet's zodiac sign.


## How to Install and Run the Project

In general, the data collection is already performed and should not be overwritten. The only part that needs to be run is the Jupyter Notebook file called Final_Demo.ipynb in the folder Final_Demo, which is what these steps describe:

1. Download the source code, and make sure that the Final_Demo.ipynb fil is located in the Final_Demo folder of the program. Be sure that the jsons folder is formatted the same as the GitHub repository; a subfolder within a parent directory containing all the Python files.
2. Install Jupyter Notebook using the following command in Terminal: `pip install jupyterlab`
3. Open Terminal and at your root directory (or the folder of the downloaded source code), type `jupyter notebook` and navigate to the Final_Demo folder and open the file Final_Demo.ipynb.
4. Run each cell line-by-line until Step 3., where you will want to input the tweet text of the tweet you want to analyze. 
5. Run each cell until step 7, which will output the prediction that the model generates! (**NOTE** Only predicts Libra or Cancer due to data-collection deficiencies and suboptimal calculations of nearest average)

For more on Jupyter Notebook and how to use it, see [here](https://jupyter-notebook.readthedocs.io/en/stable/).


To modify the project to scrape/collect your own Tweets, see the following instructions:

1. Download the library Tweepy by typing `pip install tweepy` into Terminal.
2. Download the library NLTK and NRClex by typing `pip install nltk` and `pip install nrclex` respectively.
3. Create a Twitter Developer account [here](https://developer.twitter.com/en)
4. From your developer portal, create a new project and generate 5 tokens needed: API Key and Secret, Bearer Token, Access Token and Secret
5. In the config.py, edit these global variables to match your tokens
6. Replicate the folder setup in the GitHub repository, or **be sure** to change filepaths in source code.
7. If you would like to get initial horoscope tweets from other sources, modify the accounts.csv file.
8. Run getting_tweets.py (**NOTE** These steps require the computer to stay on until the process terminates, which may be a long time due to rate limits set by Twitter (15 min intervals). I recommend the `caffeinate` [command in Terminal](https://ss64.com/osx/caffeinate.html).
9. Run getting_liking_users.py 
10. Run getting_user_tweets.py (The longest!)
11. Run analyze_user_time_line.py
12. See the previous steps of instructions!

