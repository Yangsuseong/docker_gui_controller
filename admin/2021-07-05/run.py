import os
import time
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import time



def container_list_check():
    global container_list
    global front_container_list
    global container_name_list

    user_name = str(os.popen("whoami").read())
    user_name = user_name.rstrip('\n')
    #print(user_name)

    os.system(str("docker ps -a > ./docker_container"))

    f = open("./docker_container", "rt", encoding="utf-8")
    name = f.readlines()
    f.close()
    os.system("rm ./docker_container")
    
    name = "".join(name).split("\n")

    var = 0
    var_list = []

    for i in range(len(name)):
        #print(i)
        var = "".join(name[i]).split(" ")
        #print(var)
        var_list.append(var)

    var_list = var_list[:-1]

    #print(var_list)

    container_list = []
    front_container_list = []
    container_name_list = []
    for i in range(len(var_list)):
        temp=[]
        temp = ' '.join(var_list[i]).split()
        #print(temp[-1])
        container_list.append(temp)
    container_list = container_list[1:]
    #print(container_list)

    #print("           ")

    for i in range(len(container_list)):
        front_container_list.append(container_list[i][-1] + "        " + container_list[i][6] + "       " + container_list[i][3] + " " +container_list[i][4] + "         " + container_list[i][1])
        container_name_list.append(container_list[i][-1])
    #print(front_container_list)
    for i in range(len(front_container_list)):
        lb1.insert(i, str(front_container_list[i]))


def refresh_button_action():
    lb1.delete(0,END)
    container_list_check()


def undo_select_container():
    ent1.delete(0,len(ent1.get()))

def select_image():
    idx = lb1.curselection()
    idx = lb1.index(idx)
    #print(int(idx))
    ent1.delete(0,len(ent1.get()))
    #ent1.insert(0, str(lb1.get(idx)))
    ent1.insert(0, str(container_name_list[idx]))
    




def commit_btn_action():
    if(len(ent1.get())==0):
        messagebox.showinfo("Info", "Please Select Container")
    
    else:
        commit = Toplevel(win,width=600, height=400)
        commit.grab_set()
        commit.title("Container Commit")
        #commit.option_add("*Font", "Arial 15")
        commit.resizable(False, False)


        commit_title = Label(commit)
        commit_title.config(font="Arial 18")
        commit_title.config(text="Container Commit")
        commit_title.place(x=20, y=10, width=560, height=30)

        commit_lab1 = Label(commit)
        commit_lab1.place(x=20, y=80, width=180, height=30)
        commit_lab1.config(text="container_name")
        
        commit_ent1 = Entry(commit)
        commit_ent1.insert(0, str(ent1.get()))
        commit_ent1.place(x=210, y=80, width=300, height=30)

        commit_lab2 = Label(commit)
        commit_lab2.place(x=20, y=150, width=560, height=30)
        commit_lab2.config(text="Insert New Image Name")

        commit_lab3 = Label(commit)
        commit_lab3.place(x=20, y=210, width=180, height=30)
        commit_lab3.config(text="Image Name : ")

        commit_ent3 = Entry(commit)
        commit_ent3.place(x=210, y=210, width=300, height=30)
        
        commit_lab4 = Label(commit)
        commit_lab4.place(x=20, y=270, width=180, height=30)
        commit_lab4.config(text="Image Tag : ")

        commit_ent4 = Entry(commit)
        commit_ent4.place(x=210, y=270, width=300, height=30)

        def commit_cancel_btn_action():
            commit.destroy()

        def commit_summit_btn_action():
            if(len(commit_ent3.get())==0 or len(commit_ent4.get())==0):
                messagebox.showinfo("Info", "Please Insert Name and Tag.")
            else:
                messagebox.showinfo("Info", "Container Commiting...")
                command = "docker commit " + ent1.get() + " " + commit_ent3.get() + ":" + commit_ent4.get()
                os.system(command)
                time.sleep(0.5)
                commit.destroy()
                lb1.delete(0,END)
                container_list_check()

        commit_cancle_btn = Button(commit)
        commit_cancle_btn.config(command=commit_cancel_btn_action)
        commit_cancle_btn.config(text="Cancel")
        commit_cancle_btn.place(x=360, y=320, width=100, height=60)

        commit_summit_btn = Button(commit)
        commit_summit_btn.config(command=commit_summit_btn_action)
        commit_summit_btn.config(text="Summit")
        commit_summit_btn.place(x=480, y=320, width=100, height=60)



def start_btn_action():
    if(len(ent1.get())==0):
        messagebox.showinfo("Info", "Please Select Container")    
    else:
        messagebox.showinfo("Info", "Container will be Start")
        command = "docker start " + ent1.get()
        os.system(command)
        time.sleep(0.5)
        lb1.delete(0,END)
        container_list_check()
    


def stop_btn_action():
    if(len(ent1.get())==0):
        messagebox.showinfo("Info", "Please Select Container")
    else:
        messagebox.showinfo("Info", "Container will be Stop")
        command = "docker stop " + ent1.get()
        os.system(command)
        time.sleep(0.5)
        lb1.delete(0,END)
        container_list_check()

def remove_btn_action():
    if(len(ent1.get())==0):
        messagebox.showinfo("Info", "Please Select Container")
    else:
        remove = Toplevel(win,width=400, height=200)
        remove.grab_set()
        remove.title("Container remove")
        #commit.option_add("*Font", "Arial 15")
        remove.resizable(False, False)

        remove_lab1 = Label(remove)
        remove_lab1.place(x=130, y=30, width=200, height=30)
        remove_lab1.config(text="Are You Sure?")
        
        def remove_cancel_btn_action():
            remove.destroy()

        def remove_summit_btn_action():
            messagebox.showinfo("Info", "Container will be remove")
            command = "docker rm -f " + ent1.get()
            os.system(command)
            remove.destroy()
            time.sleep(0.5)
            lb1.delete(0,END)
            container_list_check()

        remove_cancle_btn = Button(remove)
        remove_cancle_btn.config(command=remove_cancel_btn_action)
        remove_cancle_btn.config(text="Cancel")
        remove_cancle_btn.place(x=100, y=100, width=80, height=60)

        remove_summit_btn = Button(remove)
        remove_summit_btn.config(command=remove_summit_btn_action)
        remove_summit_btn.config(text="Summit")
        remove_summit_btn.place(x=220, y=100, width=80, height=60)







# ------------------------------------------------------
# gui
win = Tk()
win.title("MW Docker")
win.option_add("*Font", "Arial 15")
win.resizable(False, False)

notebook=Notebook(win, width=900, height=600)
notebook.pack()

tab1=Frame(win)
notebook.add(tab1, text="     Containers     ")
tab2=Frame(win)
notebook.add(tab2, text="     Images     ")



# 로고
lab_img = Label(win)
img = PhotoImage(file = "/home/miruware/yss/test/miruware_logo.png", master=win)
img = img.subsample(3)
lab_img.config(image=img)
lab_img.place(x=700, y=40)


#################################################
# tab 1
# 라벨
lab1 = Label(tab1)
lab1.place(x=20, y=10, width=490, height=30)
lab1.config(text="Container List")

# 리스트 박스 설명
lab2 = Label(tab1)
lab2.place(x=20, y=45, width=490, height=30)
lab2.config(font="Arial 10")
lab2.config(text="Name                    Status                    uptime                    base image")


# 리스트박스
lb1 = Listbox(tab1)
container_list_check()
lb1.config(font="Arial 12")
lb1.place(x=20, y=70, width=590, height=410)

xscrollbar = Scrollbar(tab1, orient="horizontal")
xscrollbar.config(command=lb1.xview)
xscrollbar.place(x=20, y=480, width=590, height=20)

yscrollbar = Scrollbar(tab1, orient="vertical")
yscrollbar.config(command=lb1.yview)
yscrollbar.place(x=610, y=70, width=20, height=410)

# 새로고침 버튼
refresh_button = Button(tab1, text="Reload")
refresh_button.config(command=refresh_button_action)
refresh_button.place(x=470, y=40, width=140, height=25)

# Button
up_btn = Button(tab1, text="Undo")
up_btn.config(command=undo_select_container)
up_btn.place(x=130, y=510, width=160, height=30)

select_btn = Button(tab1, text="Select")
select_btn.config(command=select_image)
select_btn.place(x=330, y=510, width=160, height=30)

# 선택된 컨테이너 라벨
lab3 = Label(tab1)
lab3.place(x=20, y=550, width=280, height=30)
lab3.config(text="Selected Container Name : ")

# 선택된 이미지 이름
ent1 = Entry(tab1)
ent1.place(x=290, y=550, width=320, height=30)

#------------------------------------
# 우측 버튼

commit_btn = Button(tab1, text="Commit")
commit_btn.config(command=commit_btn_action)
commit_btn.place(x=650, y=130, width=200, height=60)

start_btn = Button(tab1, text="Start")
start_btn.config(command=start_btn_action)
start_btn.place(x=650, y=240, width=200, height=60)

stop_btn = Button(tab1, text="Stop")
stop_btn.config(command=stop_btn_action)
stop_btn.place(x=650, y=350, width=200, height=60)

remove_btn = Button(tab1, text="remove")
remove_btn.config(command=remove_btn_action)
remove_btn.place(x=650, y=460, width=200, height=60)



#--------------------------------------------
# Copyright
copyright = Label(
    win,
    font=("Helvetica", 9))
copyright.config(text="Made By Suseong,Yang      Email : tntjd5596@miruware.com      2021.07.05")
copyright.place(x=470, y=605, width=500, height=30)



win.mainloop()