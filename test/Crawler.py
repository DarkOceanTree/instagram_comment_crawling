from selenium import webdriver
from time import sleep
from openpyxl import Workbook
import pandas as pd
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller


wb = Workbook(write_only=True)
ws = wb.create_sheet()

#셀리니움 크롬 드라이버 세팅
options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', chrome_options=options)   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', chrome_options=options)

#인스타
def instaLogin(username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    sleep(3)
    element_id = driver.find_element_by_name("username")
    element_id.send_keys(username)
    element_password = driver.find_element_by_name("password")
    element_password.send_keys(password)
    sleep(1.5)
    driver.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF').click()

def instaCommentGet(url, title):
    sleep(3)
    driver.get(url)
    sleep(2)
    
    # 댓글 플러스 버튼 누르기
    while True:
        try: 
            more_btn = driver.find_element_by_css_selector(".qF0y9.Igw0E.IwRSH.YBx95._4EzTm.NUiEW >button")
            more_btn.click()
            sleep(.5)
        except:
            break

    # 대댓글 버튼 누르기
    buttons = driver.find_elements_by_css_selector('li > ul > li > div > button')

    for button in buttons:
        button.send_keys(Keys.ENTER)
        
    # 댓글 내용 추출
    id_f = []
    rp_f = []

    ids  = driver.find_elements_by_css_selector("div.C4VMK > ._6lAjh")
    replies = driver.find_elements_by_css_selector("div.C4VMK > span")

    for id, reply in zip(ids, replies):
        id_a = id.text.strip()
        id_f.append(id_a)

        rp_a = reply.text.strip()
        rp_f.append(rp_a)


        data = {"아이디": id_f,
                "코멘트": rp_f}

    df = pd.DataFrame(data)
    df.to_excel(title +'.xlsx' , encoding = 'utf-8')
    
    
    
instaLogin("godbs631", "dbs631")
instaCommentGet("https://www.instagram.com/p/CVbrJvzJx0Y/?utm_source=ig_web_copy_link", "제12회 평화공원 국회전시회")
