import os 
import shutil
dir_name=os.path.dirname(os.path.realpath(__file__))
for filename in os.listdir(dir_name):
    if filename.endswith((".png",".jpg",".jpeg")):
        if not os.path.exists("Images"):
            os.mkdir("Images")
        shutil.copy(filename,"Images")
        os.remove(filename)
        print("image done")
    if filename.endswith(("pdf","doc","txt","docx")):
        if not os.path.exists("Documents"):
            os.mkdir("Documents")
        shutil.copy(filename,"Documents")
        os.remove(filename)
        print("Documents is done")
    if filename.endswith(("exe")):
        if not os.path.exists("apps"):
            os.mkdir("apps")
        shutil.copy(filename,"apps")
        os.remove(filename)
        print("apps is done")
    if filename.endswith(("rar","zip")):
        if not os.path.exists("archives"):
            os.mkdir("archives")
        shutil.copy(filename,"archives")
        os.remove(filename)
        print("archives is done")


 




