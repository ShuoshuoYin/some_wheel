# coding=utf-8

# This is a module, used as an interface serves the ciga.py
# It implements to extract watermelons' informatioin from a particular frame text
# file. Or rather, get a list of tuple, in which there are cigas' attributes' values
# and y as determined class or label

# Provided we have open the text file delimited by comma,
# and ciga_string is one line

#"color,root,knock,textrue,navel,touch,label
#"green,crul,ringing,clear,plain,smooth,good"
# 青绿，蜷缩，清脆， 清晰，平坦，硬滑， 好瓜

import pandas as pd

def extract_ciga(ciga_data_file_name):
    data = pd.read_csv(ciga_data_file_name)
    return data.to_dict(orient='record')

if __name__ == '__main__':
    data = extract_ciga('test')
    print(data)
