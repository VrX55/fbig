# coding=utf-8
import os,sys,time,json
from bs4 import BeautifulSoup as parse
import requests as r

def instagram():
	url = raw_input('\n[?] URL : ')
	ct = raw_input('[?] Download? (y/n): ')
	if 'y' in ct:
		bra = raw_input('[?] File Name: ')
		print('[!] Loading...')
		save = r.get(url).text
		soup = parse(save, 'html.parser')
		love = soup.findAll('script', type='text/javascript')
		for heart in love:
			if 'window._sharedData = ' in heart.text:
				jonson = heart.text.replace('window._sharedData = ','').replace(';','')
		jonson = json.loads(jonson)
		jonson = jonson["entry_data"]['PostPage'][0]["graphql"]['shortcode_media']["video_url"]
		time.sleep(5)
		alukar = r.get(jonson)
		pants = open(bra, 'wb')
		pants.write(alukar.content)
		pants.close
		print('[!] Download Succes')
		time.sleep(1)
		print('[!] \x1b[32;1mSuccesfully\x1b[37;1m')
		time.sleep(2)
		os.system('cp '+bra+' /sdcard && rm -rf '+bra)

def facebook():
     try:
	url = raw_input('\n[?] URL : ')
        ct = raw_input('[?] Download? (y/n): ')
        if 'y' in ct:
		file = raw_input('[?] File Name : ')
		print('[!] Loading...')
	        save = r.get(url).text

        	sop = parse(save, "html.parser")
        	res = sop.find("script", type="application/ld+json")
	        a = json.loads(res.text)
        	b = a['contentUrl']
		time.sleep(5)
	        c = r.get(b)
	        d = open(file, 'wb')
	        d.write(c.content)
	        d.close
	        print('[!] Download Succes')
                time.sleep(1)
                print('[!] Copy File to Internal')
                time.sleep(1)
                print('[!] \x1b[32;1mSuccesfully\x1b[37;1m')
                time.sleep(2)
                os.system('cp '+file+' /sdcard && rm -rf '+file)
     except KeyboardInterrupt:
                exit()
     except:
                print('[!]\x1b[31;1m URL FAILED\x1b[37;1m')
                time.sleep(int("2"))
                os.system('python2 dl.py')
                
if __name__ == '__main__':
	os.system('clear')  
	print('''
\x1b[36;1m____ ___   \x1b[31;1m  _ ____ 
\x1b[36;1m|___ |__]\x1b[37;1m __ \x1b[31;1m| | __ 
\x1b[36;1m|    |__]\x1b[31;1m    | |__]\x1b[37;1m instagram: fajarid05_
\x1b[37;1m\x1b[32;1mVIDEO DOWNLOADER    ---------------------\x1b[37;1m\x1b[37;1m''')
	print('''
-MENU:
{\x1b[32;1m01\x1b[37;1m} INSTAGRAM DOWNLOADER
{\x1b[32;1m02\x1b[37;1m} FACEBOOK DOWNLOADER
{\x1b[31;1m00\x1b[37;1m} EXIT\n''')

	while True:

		ask = raw_input('[?]input/> ')
		if ask == '01' or ask == '1':
			instagram()
		elif ask == '02' or ask == '2':
			facebook()
		elif ask == '0' or ask == '00':
			exit('See You....')
		else:
			print('[!] \x1b[31;1minput failed\x1b[37;1m')
			pass