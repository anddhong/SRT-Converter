import re
from mutagen.mp3 import MP3
import datetime


def srtConverter(textFile,audioFile):

	# Get Length of Audio File
	audio = MP3(audioFile)
	audioTime=audio.info.length

	# Separate for subtitle use
	txt=open(textFile,'r',encoding='utf8').read()
	olength=len(txt)+2	# to account for last two characters
	lst=re.split(', |\. |\.\n|\。',txt)

	for n in range(len(lst)):
		olength-=(len(lst[n])-len(lst[n].strip())+2)	# for last two characters + strip
		lst[n]=lst[n].strip()

	# Put into SRT format
	endTime='00:00:00,000'
	current=0
	with open('srtDemo.srt', 'w',encoding='utf8') as srtFile:
		for num in range(len(lst)):
			seconds=(len(lst[num]))/float(olength)*audioTime
			current+=seconds

			startTime=endTime
			endTime='0'+str(datetime.timedelta(seconds=current))[:11].replace('.',',')
			lst[num]=lst[num].strip()

			# format and write into SRT File
			srtFile.write('%d\n%s\n%s\n\n' % (num+1,startTime+' --> '+endTime,lst[num]))
	print(lst)


srtConverter('mktCmt_US_en.txt',"mktSound.mp3")



'''

def preprocess(file,time):
	txt=open(file,'r').read()
	olength=len(txt)
	lst=re.split(', |\. |.\n',txt)
	timeLst=[]
	for num in range(len(lst)):
		timeLst.append((len(lst[num])+2.00)/float(olength)*time)
		lst[num]=lst[num].strip()
	print(lst)
	return timeLst,lst

def srtConverter(timeLst,lst):
	final=[]
	endTime='00:00:00,000'
	current=0
	for i in range(len(lst)):
		startTime=endTime
		current+=timeLst[i]
		endTime='0'+str(datetime.timedelta(seconds=current))[:11].replace('.',',')
		final.append((i+1,startTime+' --> '+endTime,lst[i]))
		
	with open('srtFile.srt', 'w') as srtFile:
		for line in final:
			srtFile.write('%d\n%s\n%s\n\n' % (line[0],line[1],line[2]))


timeLst,lst=preprocess('mktCmt_US_en_1.txt',audioTime)
print(srtConverter(timeLst,lst))
'''