import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

list_df = pd.DataFrame(columns=['曲名', '歌詞'])

# 歌詞一覧ページ（嵐）
for page in range(1, 3):
	url = 'https://www.uta-net.com/artist/3891/0/' + str(page) + '/'
	# 曲ページURL
	base_url = 'https://www.uta-net.com'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')
	links = soup.find_all('td', class_='side td1')
	for link in links:
		a = base_url + (link.a.get('href'))

		# 歌詞詳細ページ
		response = requests.get(a)
		soup = BeautifulSoup(response.text, 'lxml')
		song_names = soup.find('div', class_='title')
		song_name = song_names.text
		song_name = song_name.replace('\n','')

		song_lyrics = soup.find('div', itemprop='lyrics')
		song_lyric = song_lyrics.text
		song_lyric = song_lyric.replace('\n','')
		time.sleep(1)

		tmp_se = pd.DataFrame([song_name, song_lyric], index=list_df.columns).T
		list_df = list_df.append(tmp_se)

print(list_df)

list_df.to_csv('list.csv', mode = 'a', encoding='cp932')