'''
Authors: 
    Janhangeer Abdur Rahmaan
    Raja Ajmal
'''
import requests
from bs4 import BeautifulSoup
import os
import sys

url = 'http://192.168.2.4:8000/'


def get_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = [link['href'] for link in soup.find_all('a')]

    return links


def download_file(file_url, path):
    r = requests.get(file_url, allow_redirects=True)
    open(path, 'wb').write(r.content)


c_folder = ''
level = 0
folders = ['']
dir_path = os.getcwd()
empty_u = None
def download_all(url1):
    global c_folder, level, folders, dir_path, empty_u, url
    empty_u = '{}'.format(url1)
    path = 'downloads'
    links = get_links(url1)
    folder_links = []
    file_links = []
    for link in links:
        if link[-1] == '/':
            folder_links.append(link)
            path_now = dir_path
            #print(path_now)
            if 'win' in sys.platform:
                os.chdir(path_now+('/'.join(folders)).replace('//', '/').replace('/', '\\').replace('%20', ' '))
                os.makedirs(path_now+('/'.join(folders)).replace('//', '/').replace('/', '\\')+'/'+(link[:]).replace('%20', ' '))
                pf = ('\\'.join([f for f in folders if f])).replace('/', '\\').replace('\\\\', '\\').replace('\\', '\\\\')
    
                print('    '*level, 'folder', link, 'level', level, 'path', pf)
            elif 'linux' in sys.platform:
                pf = os.sep.join([f for f in folders if f]).replace('//', '/')
                
                os.chdir(path_now+os.sep+pf)
                os.makedirs(path_now+os.sep+pf+link)
                
                print('    '*level, 'folder', link, 'level', level, 'path', pf)
            level += 1
            
            folders.append(link)
            try:
                c_folder = link
                download_all(url1 + link)
            except Exception as E:
                print(E)
        else: 
            if 'win' in sys.platform:
                pf = ('\\'.join([f for f in folders if f])).replace('/', '\\').replace('\\\\', '\\').replace('\\', '\\\\')
                print('    '*level, link, 'level', level, 'path', pf)
                # dl = '.'.join(folders)
                # 'http://192.168.100.2:5000/'
                dl = (empty_u+('/'.join(folders)).replace('//', '/').replace('/', '\\')+'/'+link).replace('/\\', '/').replace('\\/', '/')
                dp = dir_path+('/'.join(folders)).replace('//', '/').replace('/', '\\').replace('%20', ' ')
                print('...', dl, dp)
                os.chdir(dp)
                download_file(dl, link.replace('%20', ' '))
            elif 'linux' in sys.platform:
                pf = os.sep.join([f for f in folders if f]).replace('//', '/')
                dl = url+pf+link
                dp = dir_path+os.sep+pf
                
                os.chdir(dp)
                download_file(dl, link)
                
                print('...', dp, dl)
                print('    '*level, link, 'level', level, 'path', pf)
            
    level -= 1
    try:
        folders.pop()
    except:
        pass
    #for l in folder_links:
    #    print(l)
        

download_all(url)





'''
>>> input url
>>> 192..
.
.
.
.
>>> input commands

>>> cd Marksheet
.
.
.
.
>>> download all
>>> download

root/
    f/
        file1
        file2
b/
'''