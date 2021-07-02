import requests
from PIL import Image as im
from datetime import datetime, timedelta
import PIL
#from tkinter import *  ;preparing for gui

#GETTING THE IMAGES; FOR URLS EDIT LINKS FILE 
with open('links' )as file:
    obsah = file.read()
    splitted = obsah.split()

#PUSHING TIME TO URL
now = datetime.now()
def ceil(dt,delta):
    return dt + (datetime.min-dt)%delta

full_selc_time = str(ceil(now,timedelta(minutes=15)).strftime('%H%M'))
print('stripping selc time to ', full_selc_time)
end_utc_time = str(int(full_selc_time) - 200)

if '45' in full_selc_time:
    end_utc_time = str(int(full_selc_time[:2]+'30')-200)

if int(end_utc_time) >= 2100:
    end_utc_time = '2100'

regex = ['00','45']
nul = regex[0]
nul2 = regex[1]

if int(end_utc_time) <= 115:
    end_utc_time = '0115'

print('using utc time ', end_utc_time)
pre_date = now.strftime('%Y%D')
post_date = pre_date[:6] + pre_date[7:9]

workdate = post_date+'.'+end_utc_time+'.0.png'
url1 = splitted[0][:79]+workdate
url2 = splitted[1]
print('clouds: using '+url1)
print('map: using '+url2)
print('if you want to continue, press enter')
input()

#DOWNLOADING FILES
r = requests.get(url1, allow_redirects=True)
print("exit code is ", r)
filename = "data0.png"
if r.status_code == 404:
    
    url = splitted[0][:79]+post_date+'.'+str((int(end_utc_time)-55))+'.0.png'
    r = requests.get(url,allow_redirects=True)
    print('code was 404, trying older pic ',url)

open(filename,"wb").write(r.content)
print("writing to file")

r = requests.get(url2, allow_redirects=True)
print("exit code is ", r)
filename = "data1.png"
open(filename,"wb").write(r.content)
print("writing to file")

#OPENING FILES
back = im.open('data0.png')
fore = im.open('data1.png')

#MERGING AND SAVING 
final_filename = "radar_"+post_date+'-'+full_selc_time+'.png'
radar_image = im.alpha_composite(fore.convert('RGBA'), back.convert('RGBA'))
radar_image.save(final_filename)
print('image is saved in ' + final_filename)
radar_image.show()
