import os
import colorama
from colorama import Fore, Back
import getpass
import platform
import wmi
import ctypes
import tkinter


colorama.init()

#============================#

fetch_color = Fore.CYAN+Back.BLACK
text_color = Fore.WHITE
username = getpass.getuser()
lib_num = str(len(os.popen('pip list').read().split('\n')))


def get_uptime():

    lib = ctypes.windll.kernel32
    t = lib.GetTickCount64()
    t = int(str(t)[:-3])
    
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)
    
    uptime = f"{hour:02}:{mins:02}:{sec:02}"

    return uptime


def get_resolution():

    root = tkinter.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    resolution = f"{width}x{height}"

    return resolution


gpu_name = os.popen('wmic path win32_VideoController get name').read().split('\n')[4]

total_memory = os.popen('systeminfo | findstr /C:"Total Physical Memory"').read()[27:-4].replace(',','.')
used_memory = str( round( float(total_memory) - float(os.popen('systeminfo |find "Available Physical Memory"').read()[27:-4].replace(',','.')) , 3) )

#============================#


nfetch= ['',
f"                            .oodMMMM              {fetch_color+username+text_color}@{fetch_color+os.environ['COMPUTERNAME']}",
f"                   .oodMMMMMMMMMMMMM              {text_color}----------------",
f"       ..oodMMM  MMMMMMMMMMMMMMMMMMM              {fetch_color}OS: {text_color + platform.system()} {platform.release()} [{platform.architecture()[0]}]",
f" oodMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM              {fetch_color}Host: {text_color + wmi.WMI().Win32_ComputerSystem()[0].Model}",
f" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM              {fetch_color}Kernel: {text_color + platform.version()}",
f" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM              {fetch_color}Uptime: {text_color + get_uptime()}",
f" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM              {fetch_color}Libraries: {text_color + lib_num}",
f" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM              {fetch_color}Shell: {text_color}cmd",
f" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM              {fetch_color}Resolution: {text_color + get_resolution()}",
f"                                                  {fetch_color}CPU: {text_color + platform.processor()}",
f" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM              {fetch_color}GPU: {text_color + gpu_name}",
f" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM              {fetch_color}Memory: {text_color + used_memory}MiB / {total_memory}MiB",
f" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM",
f" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM              {Back.BLACK}    {Back.RED}    {Back.GREEN}    {Back.YELLOW}    {Back.BLUE}    {Back.MAGENTA}    {Back.CYAN}    {Back.WHITE}    ",
f" MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM              {Back.LIGHTBLACK_EX}    {Back.LIGHTRED_EX}    {Back.LIGHTGREEN_EX}    {Back.LIGHTYELLOW_EX}    {Back.LIGHTBLUE_EX}    {Back.LIGHTMAGENTA_EX}    {Back.LIGHTCYAN_EX}    {Back.LIGHTWHITE_EX}    ",
f" `^^^^^^MMMMMMM  MMMMMMMMMMMMMMMMMMM",
f"       ````^^^^  ^^MMMMMMMMMMMMMMMMM",
f"                      ````^^^^^^MMMM"
]


joint = '\n'+ fetch_color

print(joint.join(nfetch))
