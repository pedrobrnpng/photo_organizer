from enum import Enum
from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path
import os 
import shutil

currentpath = os.getcwd()

final = Path(currentpath,"final")

if not os.path.isdir(final):
	os.mkdir(final)

if not os.path.isdir(Path(final,"erros")):
	os.mkdir(Path(final,"erros"))

itemlist = os.listdir(currentpath)

for item in itemlist:
	
	existeano = False
	existemes = False
	existedia = False

	final = Path(currentpath,"final")
	finallist = os.listdir(final)

	if(item == "final"):
		continue 

	if os.path.isdir(currentpath):
		listadir = os.listdir(final)

		tmpfile = item[-5:]
		tmp = tmpfile.split(".")

		if ("jpg" ==  tmp[1].lower()):

			img = Image.open(Path(currentpath,item))
			info = img.getexif()
			
			for tag,value in info.items(): 
        
				key = TAGS.get(tag,tag)
				
				if(key=="DateTime"):
					data = value[:10].split(":",3)

					for pasta in listadir:
						if os.path.isdir(os.path.join(final,pasta)):
							if pasta == data[0]:
								existeano = True
								break
					
					final = Path(final,data[0])
					
					if not existeano:
						os.mkdir(final)

					listadir = os.listdir(final)	
					
					for pasta in listadir:
						if os.path.isdir(os.path.join(final,pasta)):
							if pasta == data[1]:
								existemes = True
								break

					final = Path(final,data[1])
					
					if not existemes:
						os.mkdir(final)

					listadir = os.listdir(final)	

					for pasta in listadir:
						if os.path.isdir(os.path.join(final,pasta)):
							if pasta == data[2]:
								existedia = True
								break

					final = Path(final,data[2])
					
					if not existedia:
						os.mkdir(final)	

					original = Path(currentpath,item)
					target = Path(final,item)
					shutil.copy(original, target)

				else:
					continue

			original = Path(currentpath,item)
			target = Path(final,item)
			shutil.copy(original, target)	

		else:
			original = Path(currentpath,item)
			target = Path(final,"erros")
			shutil.copy(original, target)	
	else: 
		continue
