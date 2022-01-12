from gtts import gTTS
from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()

root.withdraw()
root.call('wm','attributes','.','-topmost',True)
txt_file_path = askopenfilename(multiple=True)

with open(txt_file_path[0],'r', encoding = 'utf8') as txt:
    file_speech = txt.read()

text_2_speech = file_speech.replace('\n','')
speech_file = gTTS(text_2_speech, tld='com.vn', lang='vi')
speech_file.save(txt_file_path[0].replace('.txt','.mp3'))