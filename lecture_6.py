import time
import requests
from datetime import datetime
import pickle
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

start = time.time()


def main():
    
    # url = "https://api.pushshift.io/reddit/search"
    # list_class = pullshiftpull()

    # for cls in list_class:
    #     print(cls.body)
    #     print()
    
    # picklefile = open("2019_data.pkl",'wb')
    # pickle.dump(list_class, picklefile)

    picklefile = open("2019_data.pkl",'rb')
    early_class = pickle.load(picklefile)

    picklefile = open("2021_data.pkl",'rb')
    later_class = pickle.load(picklefile)

    dates =[]
    text = []

    for cls in later_class:
        dates.append(cls.created_utc)
        text.append(cls.body)


    df_later = pd.DataFrame({"dates": dates, "body": text})
    print(df_later.shape)
    dates = []
    text = []

    for cls in early_class:
        dates.append(cls.created_utc)
        text.append(cls.body)

    df_earlier = pd.DataFrame({"dates": dates, "body": text})
    print(df_earlier.shape)
    

    df_earlier['days'] = df_earlier.dates.apply(extractDay)

    df_earlier['polar_sent'] = df_earlier.body.apply(determineSentimentPolarity)

    print(df_earlier.head())

    df_later['days'] = df_later.dates.apply(extractDay)

    df_later['polar_sent'] = df_later.body.apply(determineSentimentPolarity)

    print(df_later.head())

    


    print(df_earlier.days.value_counts())
    print()
    limit = len(df_later.days.value_counts().tolist())

    total_summation = []

    for i in range(1, limit + 1):
      oneTotal = df_earlier['polar_sent'][df_earlier['days'] == i].sum()
      total_summation.append(oneTotal/df_earlier['days'].value_counts().tolist()[i-1])

    print(total_summation)

    total_summation1 = []

    for i in range(1, limit + 1):
      oneTotal = df_later['polar_sent'][df_later['days'] == i].sum()
      total_summation1.append(oneTotal/df_later['days'].value_counts().tolist()[i-1])

    print(total_summation1)

    x = list(range(1, 8))
    fig, ax = plt.subplots()
    ax.plot(x, total_summation, color = "black", label="earlier")
    ax.plot(x, total_summation1, color = "red", label="later")

    leg = ax.legend()
    plt.show()

def determineSentimentPolarity(row):
  sid = SentimentIntensityAnalyzer()
  cs = sid.polarity_scores(row)
  return cs['compound']


def extractDay(row):
  dt = datetime.fromtimestamp(row)
  return dt.day

class redditSubmission:
    def __init__(self):
        self.body = ""
        self.created_utc = ""




def pullshiftpull():
    start_stamp = 1554073200
    end_stamp = 1554678000

    # start_stamp = 1617231600
    # end_stamp = 1617836400

    subreddit = "ireland"

    url = "https://api.pushshift.io/reddit/search/?limit=100&after={}&before={}&subreddit={}"

    list_class = []

    while start_stamp < end_stamp:
        time.sleep(1)

        update_url = url.format(start_stamp, end_stamp, subreddit)
        print(update_url)
        json = requests.get(update_url)
        print(json.status_code)
        json_data = json.json()
        if 'data' not in json_data:
            break
        else:
            json_data = json_data['data']
            print(len(json_data))
            if len(json_data) == 0:
                print('No more data to harvest')
                break
            try:
                start_stamp = json_data[-1]['created_utc']
            except:
                start_stamp = end_stamp
            print(datetime.fromtimestamp(start_stamp))

            list_class = processJsonData(json_data, list_class)

    return list_class



def processJsonData(data, list_class):
    for item in data:
        redCls = redditSubmission()
        redCls.body = item['body']
        redCls.created_utc = item['created_utc']
        list_class.append(redCls)
    return list_class


main()
print("\n"+50*'#')
print(time.time()-start)
print("\n"+50*'#')