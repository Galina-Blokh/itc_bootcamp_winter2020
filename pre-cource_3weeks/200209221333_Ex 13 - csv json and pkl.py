import pandas as pd

'''
Ex 13 - Csv, json and pkl 
CSV, JSON and pkl are three different file formats used for serializing data. CSV and JSON are text formats and pkl is 
a binary format. Read about them and how to use them in python (you can start here: ​CSV​, ​JSON​, and ​pkl​),
 and then write a script that does the following: 
1. Converts the json file comments.json to a csv file named comments.csv 
2. Converts the csv file hw_2500.csv to a json file named hw_2500.csv 
3. Converts the file mlb_players.pkl to both mlb_players.csv and mlb_players.json 
Submit your code to hive. 
Good luck! 
'''
df = pd.read_json(r"~/Downloads/comments.json")
df.to_csv(r"~/Downloads/comments.csv")


csv_file = pd.DataFrame(pd.read_csv(r'~/Downloads/hw_25000.csv'))
csv_file.to_json(r'~/Downloads/hw_25000.json', orient='records')

unpickled_df = pd.DataFrame(pd.read_pickle("~/Downloads/mlb_players.pkl"))
unpickled_df.to_json(r"~/Downloads/mlb_players.json", orient='records')
unpickled_df.to_csv(r"~/Downloads/mlb_players.csv")
