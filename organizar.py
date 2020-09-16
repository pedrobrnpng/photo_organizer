from enum import Enum
from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path
import os 
import shutil

path = r'C:\Users\pedro\Downloads\takeout-20200915T201023Z-001\Takeout\Google Photos'
direc = os.listdir(path)


for dires in direc:
	
	path = r'C:\Users\pedro\Downloads\takeout-20200915T201023Z-001\Takeout\Google Photos'

	if os.path.isdir(os.path.join(path,dires)):
		
		path = Path(path,os.path.join(path,dires))
		fotos = os.listdir(path)

		for file in fotos:

			x = 1
			flag1 = False
			flag2 = False

			final = r'C:\Users\Pedro\Downloads\Final'
			listadir = os.listdir(final)

			tmp = file[5:].split(".")
			print(tmp)
			
			if "jpg" ==  tmp[1]:

				img = Image.open(Path(path,file))

				info=img.getexif()
				
				for tag,value in info.items(): 

					key = TAGS.get(tag,tag)

					if(key=="DateTime"):
						data = value[:10].split(":",3)
						print(data)

						for pasta in listadir:
							if os.path.isdir(os.path.join(final,pasta)):
								if pasta == data[0]:
									flag1 = True
									break
						
						final = Path(final,data[0])
						

						if not flag1:
							os.mkdir(final)

						listadir = os.listdir(final)	
						
						for pasta in listadir:
							if os.path.isdir(os.path.join(final,pasta)):
								if pasta == data[1]:
									flag2 = True
									break

						final = Path(final,data[1])
						

						if not flag2:
							os.mkdir(final)

					if not (key=="DateTime"):		
						original = Path(path,file)
						target = Path(final,"sem data")
						shutil.copy(original, target)
						continue

					else:
						continue

				original = Path(path,file)
				target = Path(final,file)
				print(target)
				shutil.copy(original, target)				

			else:
				original = Path(path,file)
				target = Path(final,"tipos")
				shutil.copy(original, target)
