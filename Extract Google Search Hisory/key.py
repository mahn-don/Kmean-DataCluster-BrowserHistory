import browserhistory as bh
from urllib.parse import unquote
import re


def get_key():

	history=bh.get_browserhistory()

	txt=''
	ls=[]

	a=open('key.txt','w',encoding='utf-8')

	history=bh.get_browserhistory()
	for browser_name,history_list in history.items():
		for tup in history_list:
			if ('google' in tup[0]) and ('search' in tup[0]):

				x=re.search("q=.*&r",tup[0])
				if x:
					x=x.group()[2:-2]
					# print(x)
					x2=re.search(".*&t",x)
					x3=re.search(".*&s",x)

					if x2:
						x=x2.group()[:-2]
					elif x3:
						x=x3.group()[:-2]
					if len(x)<50:
						ls.append(x)
				xx=re.search("q=.*&oq",tup[0])
				if xx:

					xx=xx.group()[2:-3]
					# print (xx)
					x2=re.search(".*&t",xx)
					x3=re.search(".*&r",xx)
					if x2:
						xx=x2.group()[:-2]
					elif x3:
						xx=x3.group()[:-2]
					if len(xx)<50:
						ls.append(xx)

	for i in ls:
		txt=txt+i+'\n'
	txt=txt.replace('+',' ')
	txt = unquote(txt)

	a.write(txt)
	a.close()
	


get_key()
