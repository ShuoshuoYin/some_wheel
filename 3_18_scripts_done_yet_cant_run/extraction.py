# coding=utf-8

# This is a module, used as an interface serves the ciga.py
# It implements to extract watermelons' informatioin from a particular frame text
# file. Or rather, get a list of tuple, in which there are cigas' attributes' values
# and y as determined class or label

# Provided we have open the text file delimited by comma,
# and ciga_string is one line

#"color,root,knock,texture,navel,touch,label
#"green,crul,ringing,clear,plain,smooth,good"
# ÇàÂÌ£¬òéËõ£¬Çå´à£¬ ÇåÎú£¬Æ½Ì¹£¬Ó²»¬£¬ ºÃ¹Ï
# ÎÚºÚ£¬ÉÔòé£¬×ÇÏì£¬ ÉÔÄ££¬ÉÔ°¼£¬ÈíÕ´£¬ »³¹Ï
# Ç³°×£¬Ó²Í¦£¬³ÁÃÆ£¬ Ä£ºı£¬°¼Ïİ£¬


import pandas as pd

def extract_ciga(ciga_data_file_name):
    data = pd.read_csv(ciga_data_file_name, encoding='gbk')
    return data.to_dict(orient='record')

if __name__ == '__main__':
    data = extract_ciga('data.csv')
    print(data)
