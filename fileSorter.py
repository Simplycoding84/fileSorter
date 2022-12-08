import re
import os
import shutil
import pprint

audioPattern = re.compile(r'[.mp3]$')
documentPattern = re.compile(r'([.pdf]|[.doc]|[.docx])$')
videoPattern = re.compile(r'([.mp4]|[.3gp][.mpeg][.VOB])$')

path = r"folderToSort"

os.chdir(path)

files = os.listdir()
audio = []
video = []
document = []

folders = ['audios','videos','documents']
for folder in folders:
    if folder not in files:
        os.makedirs(folder)
    
    else:
        print(folder + ' already in place')


for file in files:
    if audioPattern.search(file) != None:
        audio.append(file)
        try:
            shutil.move(f"{path}\\{file}", r'folderToSort\audios')
            pprint.pprint(file + ' has been added to audios.')
        except:
            os.unlink(file)

    elif documentPattern.search(file) != None:
        document.append(file)
        try:
            shutil.move(f"{path}\\{file}", r'folderToSort\documents')
            pprint.pprint(file + ' has been added to documents.')
        except:
            os.unlink(file)

    elif videoPattern.search(file) != None:
        video.append(file)
        try:
            shutil.move(f"{path}\\{file}", r'folderToSort\videos')
            pprint.pprint(file + ' has been added to videos.')
        except:
            os.unlink(file)
        
    else:
        pprint.pprint(file+ ' not recognised!!')

