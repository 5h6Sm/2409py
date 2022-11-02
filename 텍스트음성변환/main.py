from gtts import gTTS  # 텍스트를 음성으로 변환
from playsound import playsound  # mp3 파일을 파이썬으로 재생하기 위한 라이브러리
file_path = 'Mydata.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()
tts = gTTS(text=read_file, lang='ko')
mp = ('텍스트음성변환\schoolsong.mp3')
tts.save(mp)

# playsound(mp)
