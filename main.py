# NOTE: this example requires PyAudio because it uses the Microphone class
import time
import speech_recognition as sr
import crud_sheet
import handler

# 調用後台 thread
def callback(recognizer, audio):
    try:
        print("語音辨識中")
        audio_text = recognizer.recognize_google(audio, language='zh-TW')
        arab_text = handler.replace_cn_num_with_arab_num(audio_text)
        # print(f'{audio_text}')
        print(f'{arab_text}')
        
        if handler.get_number_and_grade(arab_text):
            number, grade = handler.get_number_and_grade(arab_text)
            try:
                print(f"{number=}, {grade=}")
                crud_sheet.register_grades("測試", number, grade)
            except:
                print("語音錯誤")
    except sr.UnknownValueError:
        print("聽不到你的聲音")
    except sr.RequestError as e:
        print("無法訪問google語音辨識API; {0}".format(e))

def test_microphone():
    r = sr.Recognizer()
    m = sr.Microphone()
    # print(sr.Microphone.list_microphone_names())
    for device_index in sr.Microphone.list_working_microphones():
        m = sr.Microphone(device_index=device_index)
        print(m)
        break
    else:
        print("找不到麥克風")

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
        time.sleep(0.1)
if __name__ == "__main__":
    main(init_data = False)