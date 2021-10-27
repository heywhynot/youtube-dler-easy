import subprocess
import os
import time

what_to_dl = 1   # 1 is audio, 1 is HD video
path_to_dl = "C:\youtube-dl\z-20211015-video"   #where is stuff being dl'ed to, replace with where you want to go
list001 = [    #replace with links you want to dl

#"  https://www.youtube.com/watch?v=T6uwY5D6djk&ab_channel=AfreecaTVeSports ".strip(),
#"  https://www.youtube.com/watch?v=5BqJVl9_8iM&ab_channel=SpencerRice  ".strip(),
"    ".strip(),
#"  https://www.youtube.com/watch?v=diRbPWS7VBI&t=400s&ab_channel=LaurenMiller  ".strip(),
#"  https://www.youtube.com/watch?v=UkDic2INzUA&ab_channel=Sprott  ".strip(),
"    ".strip(),
"  https://vimeo.com/455509012/553b7eb5f8  ".strip(),

]



try:    
    os.mkdir(path_to_dl)      #used to make directory if required, delete if already exists
except FileExistsError:     
    pass

os.chdir(path_to_dl)
print(os.getcwd(), '  <-- files are going here')



if what_to_dl == 0:
    print('downloading audio')

if what_to_dl == 1:
    print('downloading HD Video')




dl_counter = 1

for i in list001:
    if i.strip() == '':  #if no text
        continue
    time.sleep(0.05)
    print(f'currently on {dl_counter}')
    dl_counter += 1
    if len(i) > 10 and what_to_dl == 1:
        subprocess.run(f'youtube-dl "{i}"')   #"-f" is download high quality video w/ audio
    if len(i) > 10 and what_to_dl == 0:
        subprocess.run(f'youtube-dl -f 251 "{i}"')   #"-f 251" is download high quality audio only

'''
Instructions:  

pip install youtube-dl  #download youtube-dl if you don't have already

pip install youtube-dl --upgrade       #update youtube-dl

# Audio Download
youtube-dl -F "https://www.youtube.com/watch?v=cEJVfovEarw"     # gives all types to fidn out which one you want to dl for the next line below
youtube-dl -f 150 "https://www.youtube.com/watch?v=cEJVfovEarw"     # download the 150 type
-251 for audio

# Video Download
youtube-dl "https://www.youtube.com/watch?v=cEJVfovEarw"     # download highest quality audio+video merged
'''