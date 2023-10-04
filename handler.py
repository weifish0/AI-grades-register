cn_to_arab_dict = {
        # 基本
        '一': '1',
        '二': '2',
        '三': '3',
        '四': '4',
        '五': '5',
        '六': '6',
        '七': '7',
        '八': '8',
        '九': '9',
        
        # 特殊
        '零': '0',
    }


'''
case_a:  十*
         十
    
case_b:  *十

case_c:  *十*
'''
def case_prefilter(text, pre_index, latter_index):
    if text[pre_index] not in cn_to_arab_dict:
        return case_a(text, latter_index)
    else:
        if text[latter_index] not in cn_to_arab_dict:
            return case_b(text, pre_index)
        else:
            return case_c(text, pre_index, latter_index)

# 十*
# 十
def case_a(text, latter_index):
    if text[latter_index] not in cn_to_arab_dict: 
        # 十
        text = text.replace('十', '10', 1)
    else:
        # 十*
        text = text.replace('十', '1', 1)
        text = text.replace(text[latter_index], cn_to_arab_dict[text[latter_index]], 1)
    return text


# *十
def case_b(text, pre_index):
    text = text.replace(text[pre_index], cn_to_arab_dict[text[pre_index]], 1)
    text = text.replace('十', '0', 1)
    return text


# *十*
def case_c(text, pre_index, latter_index):
    text = text.replace(text[pre_index], cn_to_arab_dict[text[pre_index]], 1)
    text = text.replace(text[latter_index], cn_to_arab_dict[text[latter_index]], 1)
    text = text.replace('十', '', 1)
    return text


def replace_cn_num_with_arab_num(text: str) -> str:

    if '一百' in text:
        text = text.replace('一百', '100')
    
    # 10~99
    while '十' in text:
        index_limit = False
        
        cn_ten_index = text.find('十')
        
        if cn_ten_index == 0:
            latter_index = cn_ten_index+1
            text = case_a(text, latter_index)
        elif cn_ten_index == len(text)-1:
            pre_index = cn_ten_index-1
            # 此值錯誤不影響
            latter_index = cn_ten_index
            text = case_prefilter(text, pre_index, latter_index)
        else:
            pre_index = cn_ten_index-1
            latter_index = cn_ten_index+1
            text = case_prefilter(text, pre_index, latter_index)

    # 0~9
    for text_char in text:
        if text_char in cn_to_arab_dict:
            text = text.replace(text_char, cn_to_arab_dict[text_char], 1)
    return text

def get_number_and_grade(text) -> str:
    try:
        first_index = text.find("號")
    except:
        print("沒號")
        return False
                
    try:
        last_index = text.find("分")
    except:
        print("沒分")
        return False

    try: 
        number = int(text[:first_index])
    except:
        print("找不到座號")
        return False
    
    try: 
        grade = int(text[first_index+1:last_index])
    except:
        print("找不到分數")
        return False
    
    return number, grade
    

if __name__ == '__main__':
    print(replace_cn_num_with_arab_num(input("測試輸入: ")))

        
    