from gtts import gTTS
import os
  
sound = gTTS(
    text='''Desenrola, 
    bate, 
    joga de ladinho!''', 
    lang='pt', 
    slow=False
)
  
sound.save("sound.mp3")
os.system("vlc sound.mp3")