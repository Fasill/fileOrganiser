import os,shutil


image_foramts = ["jpg","png","jpeg","gif","webp","tiff"]
audio_formats = ["mp3","wav"]
video_formats = ["mp4","avi","webm"]
docs_formats = ["ai","alt","txt","rtf","docx"]
program_formats = ["exe","msi", "apk"]
compressed_formats = ["zip","tar","iso","rar"]



while True:
    files = os.listdir("./")
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
                
                




        