words = {}

# words['tea'] = '茶'  #增加辭典單字            

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
        return lines    

def split(lines):
    new = []
    for line in lines:
        new.append(line.split(', '))
    for word in new:
        print(word, '\n')
    return new

def add(lines):
    for line in lines:
        key = line[0]
        value = line[1]
        words[key] = value
    return words

def lookup():

    start = True
    while start:
        s = input('請輸入你要查的單字或輸入break離開:  ').lower()
        print('\n')
        for key, value in words.items():
            if s == key:
                print (s, ':', value, '\n')

            elif s == value:
                print (s, ':', key, '\n')
                
        if s == 'break':
            start =  False
            
def count():
    print(f'目前字典裡有{len(words.keys())}個單字')

def test():  
    
    def lookup(answer):
        
        for key, value in words.items():
            if answer == key:
                return value

            elif answer == value:
                return key
                
    import random
    bad_words = ['笨死了', '天啊! 這個你也不會', '我傻眼', '我的老天鵝啊...', '你兩歲?', '國小有沒有畢業啊?', '這個你阿罵都會']
    
    choice = input('回答英文or中文?')
    
    if choice == '中文':
        while True:
            if len(words) == 0:
                print('恭喜你把單字背完了!')
                break

            key = random.choice(list(words))   
            print(f"what does {key} mean?'\n'")
            answer = input('answer: ')

            if answer == words[key]:
                print('\n')
                print("'好棒棒!' '\n")
                del words[key]

            elif answer == 'q':
                break
                
            else: 
                print('\n')
                print(random.choice(list(bad_words)))
                print(f'正確答案為: {words[key]}')
                print('\n')
                

                
                
    if choice == '英文':
                 
        while True:
            if len(words) == 0:
                print('恭喜你把單字背完了!')
                break
            value = words[random.choice(list(words))]
            print(f"{value} 是甚麼意思? '\n'")
            answer = input('answer: ')
            if answer == lookup(value):
                print('\n')
                print("好棒棒! '\n'")
                del words[answer]

            elif answer == 'q':
                break
            else:
                print('\n')
                print(random.choice(list(bad_words)))
                print(f'正確答案為: {lookup(value)}')
                print('\n')

def add_new():
    start = True
    while start:
        En = input('請輸入英文:  ')
        Ch = input('請輸入中文:  ')
        if En == 'q' or Ch == 'q':
            break

        else:
            words[En] = Ch
            new = []
            for key, value in words.items():
                s = key + ', ' + value
                new.append(s)

            with open('Walter_dictionary.txt', 'w', encoding = 'utf-8-sig') as f:
                for line in new:
                    f.write(line + '\n')

def show_list():

    length = []
    for word in words:
        length.append(len(word))

    for word in words:
        space = ' '
        print(word, space*(max(length)-len(word)), ': ', words[word])

def tool():
    print("目前有的功能為'count', 'test', 'lookup', 'add', 'list'", '\n')
    s = input('請選擇您要使用的工具:   ')

    if s == 'count':
        return count()
    elif s == 'test':
        test()
    elif s == 'lookup':
        lookup()
    elif s == 'add':
        add_new()
    elif s == 'list':
        show_list() 

def main():
    print("歡迎來到Walter的字典 '\n'")
    lines = read_file('Walter_dictionary.txt')
    lines = split(lines)
    add(lines)
    # print(words.keys()) #show the present key in the dictionary
    # print(words.values()) #show the present value in the dictionary
    tool()



main()


# 答對的題目不要重複出現 (done)
# make list of words alphabetically

