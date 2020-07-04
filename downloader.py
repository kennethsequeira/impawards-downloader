import urllib3.request
#from tqdm import tqdm

website = 'http://www.impawards.com' #declare website url

file_name = input('Enter movie name as is on site upto .html or _ver: ') #movie name to be sanitized

year = input('Enter Year of release (check the url): ') #movie release year

size = input('Choose size. One of none, xlg, xxlg: ') #poster size

web_url = website+'/'+ year + '/posters/' + file_name

a = input('Enter start range for poster: ')
b = input('Enter end range for poster: ')
http = urllib3.PoolManager()

def download_img(i):
    with open(file_name+i+size+'.jpg', 'wb') as f:
        f.write(req.data)

if int(a) <= 0 or int(b) <= 0 or a==b :
    print('invalid range')
else:
    for i in range(int(a),int(b)+1):
        #for version 1 of posters, skip ver_def download_img(i):

        if (i == 1):
            req = http.request('GET',web_url + '_' + size + '.jpg')
            if req.status == 200:
                download_img(str(i))
            else:
                print (web_url + size + '.jpg' + ' does not exist. Check size availability')
        
        #download for remaining posters
        else:
            req = http.request('GET',web_url + '_ver' + str(i) + '_'+ size + '.jpg')
            if req.status == 200:
                download_img(str(i))
            else:
                print (web_url + '_ver'+ str(i) + '_'+ size + '.jpg' + ' does not exist. Check size availability')
