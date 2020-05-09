import os
import json
import pandas as pd
from twython import Twython


def get_tweets():
    creds = get_credentials()
    print(f"key is : {creds['api_key']}")
    # Instantiate an object
    python_tweets = Twython(creds['api_key'], creds['api_secret_key'])

    # Create our query
    query = {'q': '$prty',
             'result_type': 'popular',
             'count': 20,
             'lang': 'en',
             }
    # Search tweets
    dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
    for status in python_tweets.search(**query)['statuses']:
        dict_['user'].append(status['user']['screen_name'])
        dict_['date'].append(status['created_at'])
        dict_['text'].append(status['text'])
        dict_['favorite_count'].append(status['favorite_count'])

    # Structure data in a pandas DataFrame for easier manipulation
    df = pd.DataFrame(dict_)
    df.sort_values(by='favorite_count', inplace=True, ascending=False)
    df.head(5)


def get_credentials():
    with open(os.path.join(os.path.dirname(__file__), '..', '..', 'resources', 'credentials.json')) as f:
        credentials = json.load(f)
    return credentials


if __name__ == '__main__':
    get_tweets()