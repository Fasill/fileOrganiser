import os,shutil
import os.path

path_image = "./images"
path_music = "./Music"
path_video = "./video"
path_documents = "./Documents"
path_Programs = "./Programs"
path_Compressed = "./Compressed"
path_others = "./others"



image_foramts = ["jpg","png","jpeg","gif","webp","tiff"]
audio_formats = ["mp3","wav"]
video_formats = ["mp4","avi","webm"]
docs_formats = ["ai","alt","txt","rtf","docx"]
program_formats = ["exe","msi", "apk"]
compressed_formats = ["zip","tar","iso","rar"]

#checking if directory exist
files = os.listdir("./")
is_path_image = os.path.isfile("./images")
is_path_music = os.path.isfile("./Music")
is_path_video = os.path.isfile("./video")
is_path_documents = os.path.isfile("./Documents")
is_path_Programs = os.path.isfile("./Programs")
is_path_Compressed = os.path.isfile("./Compressed")
is_path_others = os.path.isfile("./others")

#makeing dirctory
if is_path_image == True:
        os.mkdir(path_image)
elif is_path_music != True:
    os.mkdir(path_music)
elif is_path_video != True:
    os.mkdir(path_video)
elif is_path_documents != True:
    os.mkdir(path_documents)
elif is_path_Programs != True:
    os.mkdir(path_Programs)
elif is_path_Compressed != True:
    os.mkdir(path_Compressed)
elif is_path_others != True:
    os.mkdir(path_others)
else:
    pass


while True:
    
    for file in files:
        if os.path.isfile(file) and file != "app.py":
            ext = (file.split(".")[-1]).lower()
            if ext in image_foramts:
                shutil.move(file,"images/"+file)
            elif ext in audio_formats:
                shutil.move(file,"Music/"+file)
            elif ext in video_formats:
                shutil.move(file,"Video/"+file)
            elif ext in docs_formats:
                shutil.move(file,"Documents/"+file)
            elif ext in program_formats:
                shutil.move(file,"Programs/"+file)
            elif ext in compressed_formats:
                shutil.move(file,"Compressed/"+file)
            else:
                shutil.move(file,"others/"+file)
                
                




        
