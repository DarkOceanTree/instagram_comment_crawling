from pandas.io.formats.format import buffer_put_lines
from selenium import webdriver
from time import sleep, time
from openpyxl import Workbook
import pandas as pd
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo

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
            openChromeButton.destroy()
            msgSet("크롬 실행 완료")
            msgSet("selenium(크롬)을 종료하면 프로그램을 다시 시작하세요")
    driver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver

def autoButton():
    global login
    
    if not driver:
        driverOpen()
            
    if not login:
        driver.get("https://www.instagram.com/accounts/login/")
        driver.implicitly_wait(10)
        instaLogin(idText.get(), passwordText.get())
        idText.config(text= '')
        passwordText.config(text= '')
        driver.implicitly_wait(10)
        login = TRUE
    
    url = urlText.get()
    
    if url:
        driver.get(url)
        driver.implicitly_wait(10)
        urlText.config(text = '')
        driver.implicitly_wait(10)
        
        instaCommentOpen()
        sleep(.5)
        instaCommentGet()
        showinfo("메세지", "작업 완료")
    else:
        showinfo("메세지", "게시물 링크가 없습니다.")
        
def instaCommentOpenButton():
    instaCommentOpen()
    
def instaRepliesOpenButton():
    instaRepliesClick()

def instaRepliesCloseButton():
    instaRepliesClose()
        
def instaCommentGetButton():
    instaCommentGet()
    
def instaLikeUsersButton():
    instaLikeUsers()
    
def faceBookOpenButton():
    driver.get("https://www.facebook.com/busannamgu")
    
def msgSet(message):
    # messageText.insert(tkinter.END, message + "\n")
    messageText.insert(1.0, message + "\n")
    
wb = Workbook(write_only=True)
ws = wb.create_sheet()
driver = None
login = None

#셀리니움 크롬 드라이버 세팅
options = webdriver.ChromeOptions()
options.add_argument('window-size=800x600')
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인

def driverOpen():
    global driver
    driver = WebDriver().driver
    driver.implicitly_wait(10)
    openChromeButton.destroy()
    commentOpenButton.pack(side=LEFT, padx=10, pady=8, ipady=3)
    repliesOpenButton.pack(side=LEFT, padx=10, pady=8, ipady=3)
    repliesCloseButton.pack(side=LEFT, padx=10, pady=8, ipady=3)
    commentGetButton.pack(side=LEFT, padx=10, pady=8, ipady=3)
    likeUsersButton.pack(side=LEFT, padx=10, pady=8, ipady=3)
    faceBookButton.pack(side=LEFT, padx=10, pady=8, ipady=3)
    faceBookLikeButton.pack(side=LEFT, padx=10, pady=8, ipady=3)
    faceBookCommentButton.pack(side=LEFT, padx=10, pady=8, ipady=3)
    
    
    
def driverOpenButton():
    driverOpen()
    global login
    login = True
    userInfoFrame.destroy()
    driver.get("https://www.instagram.com/")
    msgSet("인스타 로그인 후에 진행해 주세요")

def instaLogin(username, password):
    element_id = driver.find_element_by_name("username")
    element_id.send_keys(username)
    element_password = driver.find_element_by_name("password")
    element_password.send_keys(password)
    sleep(1.5)
    driver.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF').click()
    sleep(2)
    global login
    login = True
    userInfoFrame.destroy()

# 댓글 플러스 버튼 누르기
def instaCommentOpen():
    try:
        driver.find_element_by_css_selector(".qF0y9.Igw0E.IwRSH.YBx95._4EzTm.NUiEW > button")
    except:
        msgSet("댓글 더 보기가 없습니다")
        return

    while True:
        try:
            if driver.find_element_by_css_selector(".C4VMK > ._9qQ0O"):
                sleep(.1)
        except:
            try:
                more_btn = driver.find_element_by_css_selector(".qF0y9.Igw0E.IwRSH.YBx95._4EzTm.NUiEW > button")
                more_btn.click()
            except:
                msgSet("모든 댓글을 열었습니다")
                return

 # 답글 버튼 누르기
def instaRepliesClick():
    try:
        driver.find_element_by_css_selector('._61Di1 > div > button')
        buttons = driver.find_elements_by_css_selector('._61Di1 > div > button')
        for button in buttons:
            button.send_keys(Keys.ENTER)
        msgSet("답글 보기/숨기기 클릭 완료")    
    except:
        msgSet("답글 보기/숨기기가 없습니다")

# 답글 모두 닫기
def instaRepliesClose():
    try:
        button = driver.find_element_by_css_selector('.MGdpg > button')
        buttons = driver.find_elements_by_css_selector('.MGdpg > button')
        for button in buttons:
            button.send_keys(Keys.ENTER)
        msgSet("답글 숨기기 완료") 
    except:
        msgSet("답글 숨기기가 없습니다")
            
 # 댓글 내용 추출
def instaCommentGet():
    try:    
        driver.find_element_by_css_selector(".C4VMK")
    except:
        msgSet("인스타 게시물을 열고 선택해 주세요")
        showinfo("메세지", "인스타 게시물을 열고 선택해 주세요")
        return
    
    ids  = driver.find_elements_by_css_selector(".C4VMK > ._6lAjh")
    replies = driver.find_elements_by_css_selector(".C4VMK > span")
    times = driver.find_elements_by_css_selector(".RhOlS")
    id_f = []
    rp_f = []
    time_f = []

    for time in times:
        time_f.append(time.get_attribute("datetime"))
        
    for id, reply in zip(ids, replies):
        id_a = id.text.strip()
        id_f.append(id_a)

        rp_a = reply.text.strip()
        rp_f.append(rp_a)
        
    msgSet("댓글 내용 불러오기 완료")
        
    data = {"아이디": id_f,
            "코멘트": rp_f,
            "시간": time_f}
    
    df = pd.DataFrame(data)
    outfilenameGet = filedialog.asksaveasfile(filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")), defaultextension=".xlsx")
    outfilename = outfilenameGet.name
    outfilenameGet.close()
    df.to_excel(outfilename, encoding = 'utf-8')
    msgSet(outfilename)
    msgSet("댓글 내용을 저장하였습니다")

def instaLikeUsers():
    try:
        div = driver.find_element_by_css_selector(".i0EQd > div")
    except:
        try:
            lisk_link = driver.find_element_by_css_selector(".zV_Nj")
            lisk_link.send_keys(Keys.ENTER)
            sleep(0.5)
        except :
            msgSet("인스타 게시물을 열고 선택해 주세요")
            showinfo("메세지", "인스타 게시물을 열고 선택해 주세요")
            return
    
    last_height = driver.execute_script("return arguments[0].scrollHeight", div)
    id_f = []
    
    ids  = driver.find_elements_by_css_selector(".HVWg4 span")
    for id in ids:
        id_a = id.text.strip()
        id_f.append(id_a)

    while True:
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", div)
        sleep(0.5)
        ids  = driver.find_elements_by_css_selector(".HVWg4 span")
        
        for id in ids:
            id_a = id.text.strip()
            id_f.append(id_a)

        new_height = driver.execute_script("return arguments[0].scrollHeight", div)
        if new_height == last_height:
            break
        last_height = new_height
    
    msgSet("좋아요 유저 목록 읽기 완료")
    like_ids = []
    for id in id_f:
        if id not in like_ids and id:
            like_ids.append(id)
    
    data = {"아이디": like_ids}
    df = pd.DataFrame(data)
    outfilenameGet = filedialog.asksaveasfile(filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")), defaultextension=".xlsx")
    outfilename = outfilenameGet.name
    outfilenameGet.close()
    df.index += 1
    df.to_excel(outfilename, encoding = 'utf-8')
    msgSet(outfilename)
    msgSet("좋아요 유저 목록 저장 완료")
    
def faceBookComment():
    
    # comment_a = "div.j83agx80.cbu4d94t.buofh1pr.l9j0dhe7 div.cwj9ozl2 > div > ul div.tw6a2znq.sj5x9vvc.d1544ag0.cxgpxx05 span.nc684nl6 > a"
    comment_a = "div.ric4tfvp.mq76vbym > div > div > div.j83agx80.cbu4d94t.buofh1pr.l9j0dhe7 div.cwj9ozl2 ul div.tw6a2znq.sj5x9vvc.d1544ag0.cxgpxx05 span.nc684nl6 > a"
    userId_f = []
    userName_f = []
    
    try:
        comment_as = driver.find_elements_by_css_selector(comment_a)
        
        for href in comment_as:
            href_a = href.get_attribute("href")
            userName_a = href.text.strip()
            if 'profile.php?id=' in href_a:
                userId_a = href_a.split('profile.php?id=')[1].split('&comment_id')[0]
            else:
                userId_a = href_a.split('facebook.com/')[1].split('?comment_id')[0]
            userId_f.append(userId_a)
            userName_f.append(userName_a)
        
        data = {"이름": userName_f,
                "아이디": userId_f}
        df = pd.DataFrame(data)
        outfilenameGet = filedialog.asksaveasfile(filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")), defaultextension=".xlsx")
        outfilename = outfilenameGet.name
        outfilenameGet.close()
        df.index += 1
        df.to_excel(outfilename, encoding = 'utf-8')
        msgSet(outfilename)
        msgSet("페이스북 댓글 목록 저장 완료")
    except print(0):
        pass
    
    
    
def facebookLike():
    
    likeDiv = "div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div.rpm2j7zs.k7i0oixp.gvuykj2m.j83agx80.cbu4d94t.ni8dbmo4.du4w35lb.q5bimw55.ofs802cu.pohlnb88.dkue75c7.mb9wzai9.l56l04vs.r57mb794.l9j0dhe7.kh7kg01d.eg9m0zos.c3g1iek1.otl40fxz.cxgpxx05.rz4wbd8a.sj5x9vvc.a8nywdso"
    likeA = " a.qu0x051f"
    userId_f = []
    userName_f = []
    
    try:
        div = driver.find_element_by_css_selector(likeDiv)
        
        last_height = driver.execute_script("return arguments[0].scrollHeight", div)
        
        while True:
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", div)
            sleep(1)
            
            new_height = driver.execute_script("return arguments[0].scrollHeight", div)
            if new_height == last_height:
                break
            last_height = new_height
        
        likeAs = driver.find_elements_by_css_selector(likeDiv + likeA)
        
        for href in likeAs:
            href_a = href.get_attribute("href")
            userName_a = href.text.strip()
            if 'profile.php?id=' in href_a:
                userId_a = href_a.split('profile.php?id=')[1].split('&__tn')[0]
            else:
                userId_a = href_a.split('facebook.com/')[1].split('?__tn')[0]
            userId_f.append(userId_a)
            userName_f.append(userName_a)
        
        data = {"이름": userName_f,
                "아이디": userId_f}
        df = pd.DataFrame(data)
        outfilenameGet = filedialog.asksaveasfile(filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")), defaultextension=".xlsx")
        outfilename = outfilenameGet.name
        outfilenameGet.close()
        df.index += 1
        df.to_excel(outfilename, encoding = 'utf-8')
        msgSet(outfilename)
        msgSet("페이스북 좋아요 유저 목록 저장 완료")
        
    except print(0):
        pass

# GUI
window=tkinter.Tk()
window.title("제목")
window.geometry("500x280-100+100")
window.resizable(False, False)

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
urlText.pack(fill="x", padx=10, pady=8, ipady=3)

#버튼들
buttonsFrame = Frame(window)
buttonsFrame.pack(side=BOTTOM)
autoStartButton = Button(buttonsFrame, padx=2, pady=1, text="자동 실행", command=autoButton)
autoStartButton.pack(side=LEFT, padx=10, pady=8, ipady=3)
openChromeButton = Button(buttonsFrame, padx=2, pady=1, text="크롬 실행", command=driverOpenButton)
openChromeButton.pack(side=LEFT, padx=10, pady=8, ipady=3)
commentGetButton = Button(buttonsFrame, padx=2, pady=1, text="댓글 저장", command=instaCommentGet)
likeUsersButton = Button(buttonsFrame, padx=2, pady=1, text="좋아요 저장", command=instaLikeUsersButton)
faceBooklikeUsersButton = Button(buttonsFrame, padx=2, pady=1, text="FB좋아요 저장", command=facebookLike)

buttons2Frame = Frame(window)
buttons2Frame.pack(side=BOTTOM)
commentOpenButton = Button(buttons2Frame, padx=2, pady=1, text="댓글 열기", command=instaCommentOpen)
repliesOpenButton = Button(buttons2Frame, padx=2, pady=1, text="답글 클릭", command=instaRepliesClick)
repliesCloseButton = Button(buttons2Frame, padx=2, pady=1, text="답글 닫기", command=instaRepliesClose)

buttons3Frame = Frame(window)
buttons3Frame.pack(side=BOTTOM )
faceBookButton = Button(buttons3Frame, padx=2, pady=1, text="페북 켜기", command=faceBookOpenButton )
faceBookLikeButton = Button(buttons3Frame, padx=2, pady=1, text="좋아요 저장", command=facebookLike)
faceBookCommentButton = Button(buttons3Frame, padx=2, pady=1, text="댓글 저장", command=faceBookComment)





messageFrame = Frame(window)
messageFrame.pack(side=TOP)
messageText = Text(messageFrame, width=60, height=5)
messageText.pack(side=TOP)

window.mainloop()