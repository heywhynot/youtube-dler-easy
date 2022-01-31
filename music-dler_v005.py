import subprocess
import os
import time
import yt_dlp

#version 31 Jan 2022

'''
to dl
https://www.youtube.com/c/WelcomeHomeMusic/videos?view=0&sort=p&flow=grid
https://www.youtube.com/user/BlackmillMusic/videos
https://www.youtube.com/user/MORchillstep/videos?view=0&sort=p&flow=grid
https://www.youtube.com/c/SickChillz/videos
'''


what_to_dl = 0   # 0 is audio, 1 is HD video
path_to_dl = "C:\youtube-dl\z-2022_01_18-MrSuicideSheep"   #where is stuff being dl'ed to, replace with where you want to go

list001 = [    


"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),
"    ".strip(),

]



'''
https://www.youtube.com/watch?v=iqEuJDQbGXg&ab_channel=ArcticEmpire

'''


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
        subprocess.run(f'yt-dlp "{i}"')   #"-f" is download high quality video w/ audio
    if len(i) > 10 and what_to_dl == 0:
        subprocess.run(f'yt-dlp -f 251 "{i}"')   #"-f 251" is download high quality audio only

'''
Instructions:  

pip install youtube-dl  #download youtube-dl if you don't have already

pip install youtube-dl --upgrade       #update youtube-dl
pip install yt_dlp -U      #update yt-dlp   (use either yt_dlp or yt-dlp)    ** this version is more updated that the origial youtube-dl module, code is amended to use this one

# Audio Download
youtube-dl -F "https://www.youtube.com/watch?v=cEJVfovEarw"     # gives all types to fidn out which one you want to dl for the next line below
youtube-dl -f 150 "https://www.youtube.com/watch?v=cEJVfovEarw"     # download the 150 type
-251 for audio

# Video Download
youtube-dl "https://www.youtube.com/watch?v=cEJVfovEarw"     # download highest quality audio+video merged
'''