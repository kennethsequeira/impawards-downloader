import urllib3.request
import os
from tqdm import tqdm

website = 'http://www.impawards.com' #declare website url

movie_name = input('Enter movie name: ') #movie name to be sanitized

year = input('Enter Year of release: ') #movie release year

size = input('Choose size. One of none, xlg, xxlg: ') #poster size

web_url = website+'/'+ year + '/posters/' + movie_name

a = input('Enter start range for poster: ')
b = input('Enter end range for poster: ')
http = urllib3.PoolManager()

#check for a folder in this directory called downloads. If not, create one

if os.path.exists('downloads'):
    pass
else:
    os.makedirs('downloads')

def download_img(file_name, req):
    with open(os.path.join('downloads',file_name), 'wb') as f: #download files in this folder
        f.write(req.data)

if int(a) <= 0 or int(b) <= 0 or a==b :
    print('invalid range')
else:
    for i in tqdm(range(int(a), int(b)+1)):
        if i == 0:
            pass
        #for version 1 of posters, skip ver_def download_img(i):
        elif i == 1:
            if size == '':
                    file_name = web_url + '.jpg'
            else:    
                file_name = web_url + '_' + size + '.jpg'
            req = http.request('GET',file_name)
            if req.status == 200:
                print('downloading '+ file_name)
                download_img(movie_name + '_ver' + str(i) + '_' + size + '.jpg',req)
            else:
                print(req.status)
                print (file_name + ' does not exist.')
        
        #download for remaining posters
        else:
            if size == '':
                file_name = web_url + '_ver' + str(i) + '.jpg'
            else:
                file_name = web_url + '_ver' + str(i) + '_' + size + '.jpg'
            req = http.request('GET', file_name)
            if req.status == 200:
                download_img(movie_name + '_ver' + str(i) + '_' + size + '.jpg',req)
                print('downloading '+ file_name)
            else:
                print(req.status)
                print(file_name + ' does not exist.')
