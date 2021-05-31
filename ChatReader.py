from dhooks import Webhook
import time, os
print("Expando's Chat Reader!\n")
hook = Webhook("your webhook")

Lunar = True

if Lunar == True:
    logLoc = open((os.path.expanduser("~")) + r'\.lunarclient\offline\1.8\logs\latest.log', "r")
else:
    logLoc = open((os.path.expanduser("~")) + r'\AppData\Roaming\.minecraft\logs', "r")
    
stopwords=['[Client thread/INFO]: [CHAT]']

while True:
    loglines = logLoc.readline()
    if loglines.find('CHAT') >=0:
    
        for word in stopwords:
            if word in loglines:              
                loglines=loglines.replace(word,"")
        
        hook.send(loglines)
        print("Sent " + logLines)
        
