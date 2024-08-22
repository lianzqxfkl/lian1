"'我的主页'"
import time
import streamlit as st
import random
page = st.sidebar.radio('我的首页',['我的游戏','我的题目','我的智慧词典','我的留言','我的随机摇人','我的设置'])
def page1 ():
    '我的游戏'
    st.write('我的游戏')
    st.write('现代巷战1.0.exe')
    exe_file_path = "现代巷战1.0.exe"  
    with open(exe_file_path, "rb") as file:  
        btn = st.download_button(  
        label="下载EXE文件",  
        data=file,  
        file_name="现代巷战1.0.exe",  
        mime="application/octet-stream"  )
    st.write('现代巷战2.0.exe')
    exe_file_path = "现代巷战2.0.exe"  
    with open(exe_file_path, "rb") as file:  
        btn = st.download_button(  
        label="下载EXE文件",  
        data=file,  
        file_name="现代巷战2.0.exe",  
        mime="application/octet-stream"  )
    st.write('雪人集心（食品版）')
    exe_file_path = "雪人集心（食品版）.zip"  
    with open(exe_file_path, "rb") as file:  
        btn = st.download_button(  
        label="下载EXE文件",  
        data=file,  
        file_name="雪人集心（食品版）.zip",  
        mime="application/zip"  )
            
def page2 ():
    '我的题目'
    st.write("一.单选题")
    st.write('1.turtle库有哪一些功能？')
    dx1 = st.radio(' ',['  ','A.制作游戏','B.三维建模','C.绘制图案','D.分析数据'])
    if dx1 == 'C.绘制图案':
        st.write('恭喜，选对了')
    elif dx1 in ['A.制作游戏','B.三维建模','D.分析数据']:
        st.write('再想想')
    else:
        st.write('勾选单选项即可。')
        
    st.write('2.以下哪个库能实现3d建模？')
    dx2 = st.radio(' ',['  ','A.turtle','B.time','C.streamlit','D.VPython'])
    if dx2 == 'D.VPython':
        st.write('恭喜，选对了')
    elif dx2 in ['A.turtle','B.time','C.streamlit']:
        st.write('再想想')
    else:
        st.write('勾选单选项即可。')

    st.write('3.以下哪行代码会报错？')
    dx3 = st.radio(' ',['  ','A.print(‘aaa’)','B.int(‘qqq’)','C.f = []','D.s = 0'])
    if dx3 == 'B.int(‘qqq’)':
        st.write('恭喜，选对了')
    elif dx3 in ['A.print(‘aaa’)','C.f = []','D.s = 0']:
        st.write('再想想')
    else:
        st.write('勾选单选项即可。')

    st.write('二.多选题')
    st.write('4.下面哪些小程序可以嵌入网页？')
    dx4_1 = st.checkbox('turtle绘画作品')
    dx4_2 = st.checkbox('pygeme游戏作品')
    dx4_3 = st.checkbox('pillow图片处理')
    dx4_4 = st.checkbox('random随机数字')
    d1 = st.button('答案4')
    if d1:
        if dx4_1 == False and dx4_2 == False and dx4_3 == True and dx4_4 == True:
            st.write("恭喜，选对了")
        elif dx4_1 == False and dx4_2 == False and dx4_3 == False and dx4_4 == False:
            st.write('勾选单选项即可。')
        else:
            st.write('再想想')

    st.write('5.下面哪些是分开私网公网的原因？')
    dx5_1 = st.checkbox('容易管理')
    dx5_2 = st.checkbox('网速更快')
    dx5_3 = st.checkbox('不得不为')
    dx5_4 = st.checkbox('更加安全')
    d2 = st.button('答案5')
    if d2:
        if dx5_1 == False and dx5_2 == False and dx5_3 == True and dx5_4 == False:
            st.write("恭喜，选对了")
        elif dx5_1 == False and dx5_2 == False and dx5_3 == False and dx5_4 == False:
            st.write('勾选单选项即可。')
        else:
            st.write('再想想')
    
    st.write('三.判断题')
    st.write('6.分开私网公网是不得不为之的举动')
    yes = st.button('对')
    no = st.button('错')
    if yes:
        st.write("恭喜，选对了")
    elif no:
        st.write('再想想')
def page3 ():
    '我的智慧词典'
    st.write('智慧词典')
    with open('words_space.txt','r',encoding='utf-8-sig') as f:
        words_lish = f.read().split('\n')
    for i in range(len(words_lish)):
        words_lish[i] = words_lish[i].split('#')
    words_dicts = {}
    for i in words_lish:
        words_dicts[i[1]] = [int(i[0]),i[2]]
    word = st.text_input('请输入查询单词')
    if word in words_dicts:
        st.write(words_dicts[word])
def page4 ():
    '我的留言'
    name = st.text_input('我是')
    now_message = st.text_input('想说的话')
    messages_lish = []
    if name and now_message:
        messages_lish.append(name + ':' + now_message + '1')
        with open('leave_message.txt','a') as f:
            message = ''
            for i in messages_lish:
                message += '\n' + i 
            message = message[:-1]
            f.write(message)
        st.write('已留言给作者')
def page5 ():
    '我的随机摇人'
    st.text('随机摇人')
    number = st.slider('选择人数', 2, 11, 2)
    names = []
    for i in range(number):
        names.append(st.text_input('第' + str(i+1) +'人'))
    random.shuffle(names)
    st.write('被摇到的人：' + names[0])
def page6 ():
    '我的设置'
    st.write('我的设置')
    tsxz = st.radio('特效选择',['不开','雪花','气球'])
    if tsxz == '雪花':
        st.snow()
    if tsxz == '气球':
        st.balloons()
    st.write('评价')
    nm = st.toggle('不匿名')
    pj = st.radio('评价',['优','良','中','差'])
    name = '匿名者'
    if nm:
        name = st.text_input('请问名字？')
    b = st.button('确定')
    if b:
        with open('evaluates.txt','a') as f:
            f.write('\n' + name + '评价:' + pj)
            st.write('谢谢评价')
    m = st.text_input('输入密码可获得更多信息。')
    if m == '1290':
        st.write('设计者:练梓岐')
        
    
if page == '我的游戏':
    page1()
elif page == '我的题目':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言':
    page4()
elif page == '我的随机摇人':
    page5()
elif page == '我的设置':
    page6()
#'python -m streamlit run C:\Users\Administrator\Desktop\链子其\练梓岐网页.py'    