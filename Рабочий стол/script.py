#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from random import choice



def get_proxy_list():
	url = 'https://hidemy.name/ru/proxy-list/?maxtime=500&type=s#list'
	ua = {'User-agent': 'Mozilla/5.0'}

	r = requests.get(url, headers=ua)
	soup = BeautifulSoup(r.text, 'lxml')
	ip_port = []
	for ip in soup.find_all('td', class_='tdl'):
		ip_port.append('https://' + ip.text + ':' + ip.next_sibling.text)
	return ip_port
		



def test_proxy():
	proxy_list = get_proxy_list()
	print('-----------------')
	print('hidemy.name proxy parse')
	print('-----------------')
	print(proxy_list)
	print('-----------------')
	ua = {'User-agent': 'Mozilla/5.0'}
	url = 'https://2ip.ru/'
	working_proxy = []
	for i in proxy_list:
		proxy = {'https' : i}
		try:
			req = requests.get(url, headers=ua, proxies=proxy)
			print(req.status_code)
			html = BeautifulSoup(req.text, 'lxml').find('big', id='d_clip_button')
			print(html.text)
			req.status_code = int(req.status_code)
			if req.status_code == 200:
				working_proxy.append(i)
		except:
			pass
	print('-----------------')
	print('Работающие прокси')
	print('-----------------')
	print(working_proxy)
	return working_proxy






if __name__== "__main__":
	test_proxy()