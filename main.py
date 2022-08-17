#솔터고 프로그래밍 동아리 과제
import os
import shutil
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

query = input("크롤링 할 이미지의 주제를 입력하세요 (예: 동물, 음식...)\n>>>") #사용자 인풋 받기
driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()
driver.get('https://images.google.com/') #구글로 이동
box = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input') #검색창 잡기
box.send_keys(query) 
box.send_keys(Keys.ENTER) #검색어 치고 엔터
 
 
for i in range(1, 10): #10번 반복
   
    try:
        img = driver.find_element(by=By.XPATH, value='//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img')
        img.screenshot('./images/' + str(i) + '.png') #i번째 이미지 받기
        time.sleep(0.2)
 
    except: # 예외처리  
        continue
 
driver.close()

images = "./images" #크롤링된 사진이 있는 폴더

for filename in os.listdir(images):
    im = Image.open(images + '/' + filename) #이미지 열기
    im.show() #이미지 표시
    what = input("이미지를 분류해주세요. 빈칸 입력시 '알 수 없음'으로 분류됩니다.\n>>>")
    if what == '': #빈칸 입력시 '알 수 없음'으로 분류
        what = '알 수 없음'
    if os.path.isdir(images + '/' + what) == False: #폴더가 이미 존재하는지 확인
        os.mkdir(images + '/' + what) #없으면 폴더 생성
    shutil.move(images + '/' + filename, images + '/' + what + '/' + filename) #파일 옮기기


