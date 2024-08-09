#pip install selenium (라이브러리 다운로드) 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request


#크롬 드라이버 다운로드 후 같은 디렉토리에서 진행
# https://googlechromelabs.github.io/chrome-for-testing/
 


################################크롬 브라우저 열기###############################
service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
 

################################크롬 브라우저에서 검색###############################

#검색어 변경해줘야 함 
#broken Plastic Road Barrier
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("broken Plastic Road Barrier" + Keys.ENTER)

################################Scroll Down & View More ###############################
#Scroll Down
elem = driver.find_element(By.TAG_NAME, 'body')
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

#View More
try:
    view_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'mye4qd')))
    view_more_button.click()
    for i in range(80):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass

################################이미지 다운로드하기 ###############################

images = driver.find_elements(By.CSS_SELECTOR, ".YQ4gaf")
links = []

# YQ4gaf 클래스의 이미지 수집 및 zr758c 클래스 건너띄기
for image in images:
    img_src = image.get_attribute('src')
    if img_src is not None:
        # 특정 클래스 체크 (예: 'zr758c' 클래스 제외)
        class_name = image.get_attribute('class')
        if 'zr758c' not in class_name:
            links.append(img_src)

print('찾은 이미지의 개수 : ', len(links))

################################경로 설정하기 ###############################
import urllib.request

for k, i in enumerate(links):
    url = i
    #print(url) #유효한 url인지 확인
    urllib.request.urlretrieve(url, r'C:\Users\최민혁\Desktop\mydataset\barrier\barrier_image' + str(k) + '.jpg')


print('다운로드를 완료하였습니다.')

driver.quit()
#class name 
#'barrier', 'direct', 'drum', 'porthole', 'rubbercone', 'tubular'
