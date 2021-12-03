import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from selenium import webdriver
import chromedriver_autoinstaller

def urlButton():
    
    print(idText.get());
    print(passwordText.get())
    print(urlText.get())

def website_opener():
    driver = WebDriver().driver
    try:
        print(len(driver.window_handles))
    except:
        showinfo("메세지", "프로그램을 다시 시작하여 주세요.")
    
    
class WebDriver:
    
    class __WebDriver:
        def __init__(self):
            options = webdriver.ChromeOptions()
            options.add_argument('window-size=800x600')
            options.add_argument("disable-gpu")
            options.add_argument("lang=ko_KR")
            chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인
            try:
                self.driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', chrome_options=options)   
            except:
                chromedriver_autoinstaller.install(True)
                self.driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', chrome_options=options)
            self.driver.get("https://www.instagram.com/")

    driver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver

window=tkinter.Tk()

window.title("제목")
window.geometry("500x280+100+100")
window.resizable(False, False)

#ID, PASS 입력창
#크롤링할 URL
#파일이 저장될 경로.

userInfoFrame = Frame(window, width=100, height=100)
userInfoFrame.pack(fill="x", padx=10, pady=5)

idLable = Label(userInfoFrame, width=8, height=1, pady=3, text="인스타 ID")
idLable.pack(side=LEFT, padx=2, pady=5)
idText = Entry(userInfoFrame)
idText.pack(side=LEFT, padx=2, pady=5)

passwordLable = Label(userInfoFrame, width=8, height=1, pady=3, text="Password")
passwordLable.pack(side=LEFT, padx=2, pady=5)
passwordText = Entry(userInfoFrame, show="*")
passwordText.pack(side=LEFT, padx=2, pady=5)

urlFrame = Frame(window, width=100, height=100)
urlFrame.pack(fill="x", padx=10, pady=10)
urlLable = Label(urlFrame, width=8, height=1, pady=3, text="게시물 링크")
urlLable.pack(side=LEFT, padx=2, pady=5)
urlText = Entry(urlFrame)
urlButton = Button(urlFrame, padx=2, pady=1, text="자동 실행", command=urlButton)
urlButton.pack(side=RIGHT, padx=5, pady=8)
urlText.pack(fill="x", padx=10, pady=8, ipady=3)


#크롬실행, 자동수집, 수동수집 (댓글보기, 답글보기)
buttonsFrame = Frame(window)
buttonsFrame.pack(side=BOTTOM)
openChromeButton = Button(buttonsFrame, padx=2, pady=1, text="크롬 실행" , command=website_opener)
openChromeButton.pack(side=LEFT, padx=10, pady=8, ipady=3)
outoCommentsGetButton = Button(buttonsFrame, padx=2, pady=1, text="자동")
outoCommentsGetButton.pack(side=LEFT, padx=10, pady=8, ipady=3)
CommentsGetButton = Button(buttonsFrame, padx=2, pady=1, text="수동")
CommentsGetButton.pack(side=LEFT, padx=10, pady=8, ipady=3)
openCommentsButton = Button(buttonsFrame, padx=2, pady=1, text="댓글로딩")
openCommentsButton.pack(side=LEFT, padx=10, pady=8, ipady=3)

def msgSet(message):
    messageText.insert(tkinter.CURRENT, message + "\n")

messageFrame = Frame(window)
messageFrame.pack(side=BOTTOM)
messageText = Text(messageFrame, width=60, height=5)
messageText.pack(side=TOP)

msgSet("문자열 삽입 테스트")
msgSet("문자열 삽입 테스트2")
msgSet("문자열 삽입 테스트3")
msgSet("문자열 삽입 테스트4")
msgSet("문자열 삽입 테스트5")
msgSet("문자열 삽입 테스트")
msgSet("문자열 삽입 테스트2")
msgSet("문자열 삽입 테스트3")
msgSet("문자열 삽입 테스트4")
msgSet("문자열 삽입 테스트5")

window.mainloop()


