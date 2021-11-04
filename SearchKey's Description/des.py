'''
import requests
import bs4 as bs
import re
import codecs


f= codecs.open('key.txt', 'r', encoding='utf-8',errors='ignore')
t=f.read()

f2= codecs.open('des.txt', 'w', encoding='utf-8',errors='ignore')
f3= codecs.open('desx.txt', 'w', encoding='utf-8',errors='ignore')

URLS=[]
url = 'https://www.google.com/search?q='
u2=''
t=t.split('\n')
for i in t:
	u2=url
	i=i.replace(' ','+')
	u=u2+i+'+wiki&lr=lang_en'
	URLS.append(u)

txt=''
txtx=''
so=0
print(len(URLS))
for ur in URLS:
	des=''
	v=requests.get(ur)
	v=v.text

	soup=bs.BeautifulSoup(v,'lxml')
	a=soup.find_all('a')

	link=a[16].get('href')
	try:
		x=re.search('http.*&sa',link)
		if x:
			link=x.group()[:-3].replace('25','')

		v=requests.get(link)
		v=v.text
		soup=bs.BeautifulSoup(v,'lxml')
		p=soup.find_all('p')
		pp=len(p)
		i=0
		for i in range(pp):
			des=des+p[i].text+' '
	except:
		des='doanducmanh'
		f3.write(ur+'---Khong tim thay\n')

	f2.write(des+'===')
	so=so+1
	print('Done: '+str(so))


f2.close()
f.close()
f3.close()

'''
import requests
import bs4 as bs
import re
import codecs




f= codecs.open('key.txt', 'r', encoding='utf-8',errors='ignore')
t=f.read()

f2= codecs.open('des.txt', 'w', encoding='utf-8',errors='ignore')


URLS=[]
url = 'https://www.google.com/search?q='

t=t.split('\n')
for i in t:
	u=url
	i=i.replace(' ','+')
	u=u+i+'+wiki&lr=lang_en'
	URLS.append(u)

txt=''

so=0
for ur in URLS:
	des=''
	v=requests.get(ur)
	v=v.text
	soup=bs.BeautifulSoup(v,'lxml')
	a=soup.find_all('a')

	link=a[16].get('href')

	try:
		x=re.search('http.*&sa',link)
		if x:
			link=x.group()[:-3].replace('25','')

		if 'en.wiki'in link:
			v=requests.get(link)
			v=v.text
			soup=bs.BeautifulSoup(v,'lxml')
			p=soup.find_all('p')

			try:
				for i in range(10):
					des=des+p[i].text+' '
			except:
				des='doanducmanh'


		else:
			des='doanducmanh'

	except:
		des='doanducmanh'

	# if (len(des)>100000 or len(des)<1000):
	# 	des='doanducmanh'


	txt=txt+des+'==='
	so=so+1
	print('Done: '+str(so))

f2.write(txt)

f2.close()
f.close()

