
#  Flask: Using APIs

## What is an API? 
API stands for Application Programming Interface which is a set of subroutine definitions, protocols, and tools for building application software. It defines communictaion between various software components. Commercial sites create API's to make their data availible for people to use. 


## How to get an API Key 
Certain apps require authentication to control the number of requests a user makes to ensure they don't get overloaded. 

For example, for twitter you go to 

https://apps.twitter.com/

Click cretae a new app. Fill the name, purpose, and put a random website into website. Then create it. 

Once you have created the new app go to keys and access tokens and click 'generate consumer key and secret'

Copy the keys into the Flask application using 

```python
    consumer_key = "XXX"
    consumer_secret = "XXX"
    access_token = "XXX"
    acess_token_secret = "XXX"
```

and then authenticate twitter with 
```python
twitter = Twitter( auth=OAuth(access_token, acess_token_secret, consumer_key, consumer_secret) )
```

Inside of main, you can actually call twitter and get data using the API. The documentation describes how to get information.  https://developer.twitter.com/en/docs


With other apps such as Wikipedia though, there is no authentication. You can just import wikipedia, which is a python package that gives you access to the API. 


## Getting information from Twitter 

To get the information you can search by a query using 
```python
    query = "#" + input
    my_tweets = twitter.search.tweets(q=query)
```

It will return to you data in a json format, from which you can extact what data you need. 
JSON stands for Javascript Object Notation, which is a minimal, readable format for structuring data. It will look something like: 
data = 
{
 "created_at":"Thu Apr 06 15:24:15 +0000 2017",
 "id": 850006245121695744,
 "id_str": "850006245121695744",
 "text": "1/ Today we’re sharing our vision for the future of the Twitter API platform!nhttps://t.co/XweGngmxlP",
 "user": { 
        "name" : "Aria"
    },  
 "entities": ["entity1", "entity2"]
}

To access when it was created you woul access data['created_at'] to get back "Thu Apr 06 15:24:15 +0000 2017". 

You can alos have nested data and lists in your data. For intsance, data['user']['name'] returns Aria. 

You can also have lists. For instance, data['entities'][0] returns "entity1"

In the twitter example, yo ucan search by a query and get every related hashtag using the code below. You can add this to your main function in app.py. 

```python
    query = "#" + input
    my_tweets = twitter.search.tweets(q=query)
    hashtags = "RELATED HASHTAGS: " 
    if (len(my_tweets['statuses']) != 0):
        for i in range(len(my_tweets['statuses'][0]['entities']['hashtags'])):
            hashtags += my_tweets['statuses'][0]['entities']['hashtags'][i]['text'] + "  "
```


## Getting information from Wikipedia 

For wikipedia, you can use 

```python
wikipedia.search(input)
```

to search for a input and will recieve a list of elements that resulted from the search. 
You can pick the first one by indexing and get the title and content. 



```python
    wiki_title =  "WIKIPEDIA ARTICLE TITLE: "
    wiki_information = "WIKIPEDIA INFORMATION: "
    if (len(wikipedia.search(input)) != 0):
        wiki_title += wikipedia.page(wikipedia.search(input)[0]).title + "  \n\n"
        wiki_information = "INFORMATION: " + wikipedia.page(wikipedia.search(input)[0]).content + "  \n\n"
```



##  Putting everything together 

Put both the blob fetching data from wikipedia and the one for twitter into the main function and return hashtags + wiki_title +  wiki_information

Run the server and make sure your flask app is working. Then try the challenge on your own. 

## Challenge: Spotify 

Look up the documentation for spotify and figure out how to search song on spotify and return the first result. 

