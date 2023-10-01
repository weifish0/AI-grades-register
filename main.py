# NOTE: this example requires PyAudio because it uses the Microphone class
import time
import speech_recognition as sr
import crud_sheet
from handler import replace_cn_num_with_arab_num

# 調用後台 thread
def callback(recognizer, audio):
    try:
        print("語音辨識中")
        audio_text = recognizer.recognize_google(audio, language='zh-TW')
        arab_text = replace_cn_num_with_arab_num(audio_text)
        print(f'{audio_text}')
        print(f'{arab_text}')
        
        try:
            first_index = arab_text.find("號")
        except:
            print("沒號")
                    
        try:
            last_index = arab_text.find("分")
        except:
            print("沒分")

        try: 
            number = int(arab_text[:first_index])
        except:
            print("找不到座號")
        
        try: 
            grade = int(arab_text[first_index+1:last_index])
        except:
            print("找不到分數")
        try:
            print(f"{number=}, {grade=}")
            crud_sheet.register_grades("常春藤w1", number, grade)
        except:
            print("語音錯誤")
                
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def main(init_data):
    r = sr.Recognizer()
    m = sr.Microphone()
    if init_data:
        crud_sheet.create_basic_data()
    with m as source:
        r.adjust_for_ambient_noise(source)  # 適應環境噪音


    print("listen in BG")
    # 調用麥克風開始監聽
    stop_listening = r.listen_in_background(m, callback, phrase_time_limit=4)
    
    # `stop_listening` 作為 function被呼叫會停止監聽
    # stop_listening(wait_for_stop=False)

    print("開始辨識")
    while True: 
        time.sleep(0.1)  # we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stopping
        
if __name__ == "__main__":
    init_data = True
    main(init_data)