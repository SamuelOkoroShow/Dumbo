youtubeStuff = open('youtubeads.txt')
writeFileThingy = open('youtube_blocked_domains.js', 'w')

front_string = '"*://*.'
back_string = '/*",\n'

for line in youtubeStuff:
	writeFileThingy.write(front_string+line.strip()+back_string)
writeFileThingy.close()