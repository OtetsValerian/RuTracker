import tkinter as tk
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
import platform


def clicked_save():
    if inp1.get() == '':
        pass
    else:
        with open('logpas.txt', 'w+') as f:
            f.write(inp1.get())
            f.write('\n')
            f.write(inp2.get())
            f.write('\n')
            f.write(inp3.get())
            f.write('\n')
            f.write(inp4.get())
            f.write('\n')
            f.write(inp5.get())
def clicked_start():
    print(platform.architecture())
    print(platform.system())
    with open('logpas.txt', 'r+') as f:
        a = f.read().split('\n')[0:5]
    q = []
    for i in range(len(a)):
        b = a[i]
        q.append(b)

    if entry1.get() != q[0] and entry1.get() != entry2.get():

        options = webdriver.ChromeOptions()
        options.add_argument(f'--proxy-server={entry1.get()}')

        driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        driver.get(entry0.get())
        try:
            driver.implicitly_wait(3)
            keyboard.write(entry2.get())
            keyboard.send('tab')
            driver.implicitly_wait(3)
            keyboard.write(entry3.get())
            keyboard.send('enter')
            vhod = driver.find_element(By.LINK_TEXT, 'Вход').click()
            login = driver.find_element(By.ID, 'top-login-uname')
            login.send_keys(entry4.get())
            password = driver.find_element(By.ID, 'top-login-pwd')
            password.send_keys(entry5.get())
            password.send_keys(Keys.ENTER)
            driver.quit()
            windows.destroy()
        except Exception:
            driver.quit()
            windows.destroy()
        driver.quit()
        windows.destroy()
    elif q[0] == '':
        pass
    else:

        options = webdriver.ChromeOptions()
        options.add_argument(f'--proxy-server={q[0]}')
        driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        driver.get(entry0.get())
        try:
            driver.implicitly_wait(3)
            keyboard.write(q[1])
            keyboard.send('tab')
            driver.implicitly_wait(3)
            keyboard.write(q[2])
            keyboard.send('enter')
            vhod = driver.find_element(By.LINK_TEXT, 'Вход').click()
            login = driver.find_element(By.ID, 'top-login-uname')
            login.send_keys(q[3])
            password = driver.find_element(By.ID, 'top-login-pwd')
            password.send_keys(q[4])
            password.send_keys(Keys.ENTER)
            driver.quit()
            windows.destroy()
        except Exception:
            driver.quit()
            windows.destroy()
time_stop = 10  # 3600
time_start = time.time()
while self.flag:
    time.sleep(0.5)
    if time.time() - time_start < time_stop:
        if self.driver.get_log('driver'):
            if self.driver.get_log('driver')[-1][
                'message'] == "Unable to evaluate script: no such window: target window already closed\nfrom unknown error: web view not found\n":
                self.driver.quit()
                self.flag = False
    else:
        self.driver.quit()
        self.flag = False



windows = tk.Tk()
windows.title("RuTracker")
windows.geometry("280x190")

inp0 = StringVar()

URL = tk.Label(text="URL:")
proxy.place(x=5, y=5)
entry0 = tk.Entry(width=20, textvariable = inp0)
entry0.place(x=150, y=5)

inp1 = StringVar()

proxy = tk.Label(text="Proxy:")
proxy.place(x=5, y=5)
entry1 = tk.Entry(width=20, textvariable = inp1)
entry1.place(x=150, y=5)

inp2 = StringVar()
inp3 = StringVar()

logP = tk.Label(text="Login for proxy:")
logP.place(x=5, y=35)
entry2 = tk.Entry(width=20, textvariable = inp2)
entry2.place(x=150, y=35)
pasP = tk.Label(text="Password for proxy:")
pasP.place(x=5, y=65)
entry3 = tk.Entry(width=20, textvariable = inp3)
entry3.place(x=150, y=65)

inp4 = StringVar()
inp5 = StringVar()

log = tk.Label(text="Login for RuTracker:")
log.place(x=5, y=95)
entry4 = tk.Entry(width=20, textvariable = inp4)
entry4.place(x=150, y=95)
pas = tk.Label(text="Password for RuTracker:")
pas.place(x=5, y=125)
entry5 = tk.Entry(width=20, textvariable = inp5)
entry5.place(x=150, y=125)

btn1 = Button(windows, text="Save", command=clicked_save)
btn1.place(x=5, y=155)

btn = Button(windows, text="Start", command=clicked_start)
btn.place(x=60, y=155)

exit_btn = Button(windows, text="Exit", bg='red', fg='white', command=windows.quit)
exit_btn.place(x=115, y=155)


windows.mainloop()