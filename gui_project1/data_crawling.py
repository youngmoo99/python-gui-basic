from cgitb import text
from fileinput import filename
from urllib import response
import requests
import tkinter as tk
from bs4 import BeautifulSoup
from tkinter import *
from urllib.request import urlopen
import re
import time
import csv


root = tk.Tk()
root.title("Auto Crawling") #타이틀
root.geometry("800x600")

# 한글만 크롤링 csv 파일로 저장 
def save_myfile():
    myurl = txt_dest_path.get()
    url = requests.get(myurl)
    if url.status_code == 200:
        url.raise_for_status()
        soup = BeautifulSoup(url.text, "lxml")
        soup1 = str(soup)
        result = re.sub('[a-zA-Z0-9]', '',soup1)
        result = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]','',result)
        filename = time.strftime("C:/temp/%Y%m%d-%H%M%S.csv")
        f = open(filename, 'w', encoding='utf-8-sig', newline='')
        writer = csv.writer(f)
        writer.writerow(result)

# url 크롤링 한글만 출력
def browse_extraction():
    myurl = txt_dest_path.get()
    url = requests.get(myurl)
    if url.status_code == 200:
        print("오류없음")
        url.raise_for_status()
        soup = BeautifulSoup(url.text, "lxml")
        soup1 = str(soup)
        #hangul = re.compile('[\uAC00-\uD7A3]')
        #hangul = re.compile('[^a-zA-Z0-9]+')
        result = re.sub('[a-zA-Z0-9]', '',soup1)
        result = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]','',result)
        #result = hangul.findall(soup1)
        text_file.delete("1.0", END)
        text_file.insert(END, result)
             
        
    else:
        print("오류발생")
   
    
#URL 입력 프레임 
path_frame = LabelFrame(root)
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

label1 = Label(path_frame, text ="URL")
label1.pack(side="left")


#입력칸
txt_dest_path = Entry(path_frame) 
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)


btn_dest_path = Button(path_frame, text="추출", width=10, command=browse_extraction)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 출력 프레임 
output_frame = Frame(root)
output_frame.pack(fill="both", padx=5, pady=5) 

scrollbar = Scrollbar(output_frame)
scrollbar.pack(side ="right", fill ="y")

text_file = Text(output_frame, height=28,yscrollcommand=scrollbar.set)
text_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=text_file.yview)


#저장 ,닫기 프레임 
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)
btn_close = Button(frame_run, padx=5, pady=5, text="닫기",width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start=Button(frame_run, padx=5, pady=5, text="저장", width=12,command=save_myfile)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False,False) 
root.mainloop() 