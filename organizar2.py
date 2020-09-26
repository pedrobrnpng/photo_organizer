from pathlib import Path 
import os
import shutil
import time
from progress.bar import IncrementalBar

currentpath = os.getcwd()

destination = Path(currentpath,"final")

if not os.path.isdir(destination):
	os.mkdir(destination)

if not os.path.isdir(Path(destination,"erros")):
	os.mkdir(Path(destination,"erros"))

itemlist = os.listdir(currentpath)
bar = IncrementalBar('Countdown', max = len(itemlist))
analisados = 0

for item in itemlist:

	existeano = False
	existemes = False
	existedia = False

	destination = Path(currentpath,"final")
	finallist = os.listdir(destination)

	if(item == "final"):
		continue 

	if os.path.isdir(os.path.join(currentpath,item)):

		tmp = item.split("-",3)

		for pasta in finallist:
			if os.path.isdir(os.path.join(destination,pasta)):
				if pasta == tmp[0]:
					existeano = True
					break

		destination = Path(destination,tmp[0])	
		if not existeano:
			os.mkdir(destination)

		finallist = os.listdir(destination)

		for pasta in finallist:
			if os.path.isdir(os.path.join(destination,pasta)):
				if pasta == tmp[1]:
					existemes = True
					break
		
		destination = Path(destination,tmp[1])
		if not existemes:
			os.mkdir(destination)
		finallist = os.listdir(destination)

		for pasta in finallist:
			for pasta in finallist:
				if os.path.isdir(os.path.join(destination,pasta)):
					if pasta == tmp[2][:2]:
						existedia = True
						break

		destination = Path(destination,tmp[2][:2])

		if not existedia:
			os.mkdir(destination)

		
		currentlist = os.listdir(Path(currentpath,item))

		for ficheiro in currentlist:
			original = os.getcwd()

			formato = ficheiro[-5:].split(".")

			if (formato[1].lower() == "jpg") or (formato[1].lower() == "png") or (formato[1].lower() == "dng") or \
					(formato[1].lower() == "mp4") or (formato[1].lower() == "jpeg") or (formato[1].lower() == "3gp") or \
					(formato[1].lower() =="mov") or (formato[1].lower() == "gif") or (formato[1].lower() == "cr2") or \
					(formato[1].lower() =="mpeg"):
				original = Path(currentpath,item)
				original = Path(original,ficheiro)
				destination2 = Path(destination,ficheiro)
				
				shutil.copyfile(original, destination2)

			elif formato[1].lower() == "json":
				continue

			else:
				original = Path(currentpath,item)
				original = Path(original,ficheiro)
				destination2 = Path(currentpath,"final\\erros")
				destination2 = Path(destination2,ficheiro)
				shutil.copyfile(original, destination2)
	
	bar.next()

bar.finish()