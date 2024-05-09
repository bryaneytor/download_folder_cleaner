# Quick program for cleaning and sorting files on the download folder on Windows
import os 

dl = 'C:\\Users\\b-san\\Downloads'

for file in os.listdir(dl):
    print(file, end=' \n')
    
img_ext = {'dir':dl+'\\images',
           'exts':["jpg", "jpeg", "gif", "webp", "png", "svg"]}

doc_ext = {'dir':dl+'\\docfiles', 
            'exts': ["xlsx", "csv", "ods", "drawio", "doc", "pdf", "txt", "docx"]}

audio_ext = {'dir':dl+'\\audio',
            'exts': ["mp3", "ogg", "wav", "m4a"]}

video_ext = {'dir':dl+'\\video',
            'exts': ["mp4", "mkv", "flv", "webm", "wmv", "m4p", "3gp", "mpg", "mpeg"]}

exe_ext = {'dir':dl+'\\executables', 
           'exts': ["exe", "bat", "msi"]}

comp_ext = {'dir':dl+'\\compressed',
            'exts': ["zip", "rar", "7z", "tar"]}

conf_ext = {'dir':dl+'\\config',
            'exts': ["ini", "conf", "yaml", "json"]}

dicts = [img_ext, doc_ext, audio_ext, video_ext, exe_ext, comp_ext, conf_ext]

def if_exists(dir: str):
    # This function checks if a 'dir' exists on a path, if not it creates it
    if os.path.isdir(dir):
        return
    else:
        os.mkdir(dir)

if_exists(exe_ext['dir'])    # For .exe and .inst kind of files
if_exists(audio_ext['dir'])  # For .mp3, .ogg, flac or any other sound file i have on the downloads folder
if_exists(doc_ext['dir'])    # For any .doc, .pdf and document related files
if_exists(img_ext['dir'])    # For .png, .jpg, .gif, and any other image file in the download folder
if_exists(video_ext['dir'])  # For any video source files like .mp4, .mkv or whatever else is there
if_exists(comp_ext['dir'])   # For any rar, zip, 7z files.
if_exists(conf_ext['dir'])   # For basic config files like .ini, .yaml, .conf, etc...

# Now we take a look at the whole download folder file by file to start moving and cleaning.
for file in os.listdir(dl):
    # First we need to make sure the file we are reading is a file and not a folder.
    if os.path.isfile(dl+'\\'+file):
        # Then we split the file name by '.' so we can get the extension at the end of the list that it returns
        ext = str(file).split(".")[-1]
        
        # Now we compare this extension with all the lists we have above to see if 
        # the file extension matches the with one of the extensions on the lists
        
        # Optimization attempt
        # Quite succesfull
        for _list in dicts:
            if ext in _list['exts']:
                os.rename(src=dl+"\\"+file, dst=_list['dir']+"\\"+file)