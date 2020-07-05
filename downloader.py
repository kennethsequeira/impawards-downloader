import urllib3.request
from tqdm import tqdm

website = 'http://www.impawards.com' #declare website url

'''movie_name = input('Enter movie name as is on site upto .html or _ver: ') #movie name to be sanitized

year = input('Enter Year of release (check the url): ') #movie release year

size = input('Choose size. One of none, xlg, xxlg: ') #poster size

web_url = website+'/'+ year + '/posters/' + movie_name'''

a = input('Enter start range for poster: ')
b = input('Enter end range for poster: ')
http = urllib3.PoolManager()

def download_img(file_name):
    with open(file_name, 'wb') as f:
        f.write(req.data)

if int(a) <= 0 or int(b) <= 0 or a==b :
    print('invalid range')
else:
    for i in tqdm(range(int(b)-int(a)+1), total=int(b)-int(a)+1,initial=int(a)):
        print (i)
        '''if i == 0:
            pass
        #for version 1 of posters, skip ver_def download_img(i):
        elif i == 1:
            file_name = web_url + '_' + size + '.jpg'
            req = http.request('GET',file_name)
            if req.status == 200:
                print('downloading '+ file_name)
                download_img(movie_name + '_ver' + str(i) + '_' + size + '.jpg')
            else:
                print (file_name + ' does not exist. Check size availability')
        
        #download for remaining posters
        else:
            file_name = web_url + '_ver' + str(i) + '_' + size + '.jpg'
            req = http.request('GET', file_name)
            if req.status == 200:
                download_img(movie_name + '_ver' + str(i) + '_' + size + '.jpg')
                print('downloading '+ file_name)
            else:
                print (file_name + ' does not exist. Check size availability')'''
