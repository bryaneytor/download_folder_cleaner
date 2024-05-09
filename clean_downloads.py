# Quick program for cleaning and sorting files on the download folder on Windows
import os 

dl = 'C:\\Users\\b-san\\Downloads'
dl_exe = dl+'\\executables'
dl_audio = dl+'\\audio'
dl_docs = dl+'\\docfiles'
dl_img = dl+'\\images'
dl_video = dl+'\\video'
dl_comp = dl+'\\compressed'
dl_config = dl+'\\config'

def if_exists(dir: str):
    # This function checks if a 'dir' exists on a path, if not it creates it
    if os.path.isdir(dir):
        return
    else:
        os.mkdir(dir)

# Just to see the files its going to be looking at
for file in os.listdir(dl):
    print(file, end=' \n')

if_exists(dl_exe)    # For .exe and .inst kind of files
if_exists(dl_audio)  # For .mp3, .ogg, flac or any other sound file i have on the downloads folder
if_exists(dl_docs)   # For any .doc, .pdf and document related files
if_exists(dl_img)    # For .png, .jpg, .gif, and any other image file in the download folder
if_exists(dl_video)  # For any video source files like .mp4, .mkv or whatever else is there
if_exists(dl_comp)   # For any rar, zip, 7z files.
if_exists(dl_config) # For basic config files like .ini, .yaml, .conf, etc...

# Here you can add more file extensions to the arrays to fit the files 
# you would most likely want to move to the folders above
img_ext = ["jpg", "jpeg", "gif", "webp", "png", "svg"]
doc_ext = ["xlsx", "csv", "ods", "drawio", "doc", "pdf", "txt", "docx"]
audio_ext = ["mp3", "ogg", "wav", "m4a"]
video_ext = ["mp4", "mkv", "flv", "webm", "wmv", "m4p", "3gp", "mpg", "mpeg"]
exe_ext = ["exe", "bat", "msi"]
comp_ext = ["zip", "rar", "7z", "tar"]
conf_ext = ["ini", "conf", "yaml", "json"]

# Now we take a look at the whole download folder file by file to start moving and cleaning.
for file in os.listdir(dl):
    # First we need to make sure the file we are reading is a file and not a folder.
    if os.path.isfile(dl+'\\'+file):
        # Then we split the file name by '.' so we can get the extension at the end of the list that it returns
        ext = str(file).split(".")[-1]
        
        # Now we compare this extension with all the lists we have above to see if 
        # the file extension matches the with one of the extensions on the lists
        if ext in img_ext:
            os.rename(src=dl+"\\"+file, dst=dl_img+"\\"+file)
        elif ext in doc_ext:
            os.rename(src=dl+"\\"+file, dst=dl_docs+"\\"+file)
        elif ext in audio_ext:
            os.rename(src=dl+"\\"+file, dst=dl_audio+"\\"+file)
        elif ext in video_ext:
            os.rename(src=dl+"\\"+file, dst=dl_video+"\\"+file)
        elif ext in exe_ext:
            os.rename(src=dl+"\\"+file, dst=dl_exe+"\\"+file)
        elif ext in comp_ext:
            os.rename(src=dl+"\\"+file, dst=dl_comp+"\\"+file)
        elif ext in conf_ext:
            os.rename(src=dl+"\\"+file, dst=dl_config+"\\"+file)
        else:
            # You can either delete the remaining ones or just comment this last line and do it yourself in the end :)
            os.remove(dl+"\\"+file)
