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
        messagebox.showerror("Info", "Please Select Container")
    
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
                messagebox.showerror("Info", "Please Insert Name and Tag.")
            else:
                messagebox.showinfo("Info", "Container Commiting...")
                command = "docker commit " + ent1.get() + " " + commit_ent3.get() + ":" + commit_ent4.get()
                os.system(command)
                time.sleep(0.5)
                commit.destroy()
                lb1.delete(0,END)
                container_list_check()
                image_list_check()

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
        messagebox.showerror("Info", "Please Select Container")    
    else:
        messagebox.showinfo("Info", "Container will be Start")
        command = "docker start " + ent1.get()
        os.system(command)
        time.sleep(0.5)
        lb1.delete(0,END)
        container_list_check()
    


def stop_btn_action():
    if(len(ent1.get())==0):
        messagebox.showerror("Info", "Please Select Container")
    else:
        messagebox.showinfo("Info", "Container will be Stop")
        command = "docker stop " + ent1.get()
        os.system(command)
        time.sleep(0.5)
        lb1.delete(0,END)
        container_list_check()

def remove_btn_action():
    if(len(ent1.get())==0):
        messagebox.showerror("Info", "Please Select Container")
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
            image_list_check()

        remove_cancle_btn = Button(remove)
        remove_cancle_btn.config(command=remove_cancel_btn_action)
        remove_cancle_btn.config(text="Cancel")
        remove_cancle_btn.place(x=100, y=100, width=80, height=60)

        remove_summit_btn = Button(remove)
        remove_summit_btn.config(command=remove_summit_btn_action)
        remove_summit_btn.config(text="Summit")
        remove_summit_btn.place(x=220, y=100, width=80, height=60)




















##########################################################
# tab2

def image_list_check():

    global front_image_list
    
    os.system(str("docker images > ./docker_images"))

    f = open("./docker_images", "rt", encoding="utf-8")
    name = f.readlines()
    f.close()
    os.system("rm ./docker_images")
    
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

    image_list = []
    front_image_list = []
    image_name_list = []
    for i in range(len(var_list)):
        temp=[]
        temp = ' '.join(var_list[i]).split()
        #print(temp[-1])
        image_list.append(temp)
    image_list = image_list[1:]
    #print(image_list)

    for i in range(len(image_list)):
        front_image_list.append(image_list[i][0] + ":" + image_list[i][1])
    #print(front_image_list)

    for i in range(len(front_image_list)):
        t2_lb1.insert(i, front_image_list[i])


def t2_refresh_button_action():
    t2_lb1.delete(0,END)
    image_list_check()


def t2_undo_select_container():
    t2_ent1.delete(0,len(t2_ent1.get()))

def t2_select_image():
    idx = t2_lb1.curselection()
    idx = t2_lb1.index(idx)
    #print(int(idx))
    t2_ent1.delete(0,len(t2_ent1.get()))
    t2_ent1.insert(0, str(front_image_list[idx]))



def t2_rmi_btn_action():
    if(len(t2_ent1.get())==0):
        messagebox.showerror("Info", "Please Select image")
    else:
        remove = Toplevel(win,width=400, height=200)
        remove.grab_set()
        remove.title("image remove")
        #commit.option_add("*Font", "Arial 15")
        remove.resizable(False, False)

        remove_lab1 = Label(remove)
        remove_lab1.place(x=130, y=30, width=200, height=30)
        remove_lab1.config(text="Are You Sure?")
        
        def remove_cancel_btn_action():
            remove.destroy()

        def remove_summit_btn_action():
            messagebox.showinfo("Info", "Image will be remove")
            command = "docker rmi -f " + t2_ent1.get()
            os.system(command)
            remove.destroy()
            time.sleep(0.5)
            t2_lb1.delete(0,END)
            image_list_check()

        remove_cancle_btn = Button(remove)
        remove_cancle_btn.config(command=remove_cancel_btn_action)
        remove_cancle_btn.config(text="Cancel")
        remove_cancle_btn.place(x=100, y=100, width=80, height=60)

        remove_summit_btn = Button(remove)
        remove_summit_btn.config(command=remove_summit_btn_action)
        remove_summit_btn.config(text="Summit")
        remove_summit_btn.place(x=220, y=100, width=80, height=60)   



def t2_tag_btn_action():
    if(len(t2_ent1.get())==0):
        messagebox.showerror("Info", "Please Select image")
    
    else:
        t2_tag = Toplevel(win,width=600, height=400)
        t2_tag.grab_set()
        t2_tag.title("Image Tag")
        #commit.option_add("*Font", "Arial 15")
        t2_tag.resizable(False, False)


        t2_tag_title = Label(t2_tag)
        t2_tag_title.config(font="Arial 18")
        t2_tag_title.config(text="Image Tag")
        t2_tag_title.place(x=20, y=10, width=560, height=30)

        t2_tag_lab1 = Label(t2_tag)
        t2_tag_lab1.place(x=20, y=80, width=180, height=30)
        t2_tag_lab1.config(text="Image_name")
        
        t2_tag_ent1 = Entry(t2_tag)
        t2_tag_ent1.insert(0, str(t2_ent1.get()))
        t2_tag_ent1.place(x=210, y=80, width=300, height=30)

        t2_tag_lab2 = Label(t2_tag)
        t2_tag_lab2.place(x=20, y=150, width=560, height=30)
        t2_tag_lab2.config(text="Insert New Image Name")

        t2_tag_lab3 = Label(t2_tag)
        t2_tag_lab3.place(x=20, y=210, width=180, height=30)
        t2_tag_lab3.config(text="Image Name : ")

        t2_tag_ent3 = Entry(t2_tag)
        t2_tag_ent3.place(x=210, y=210, width=300, height=30)
        
        t2_tag_lab4 = Label(t2_tag)
        t2_tag_lab4.place(x=20, y=270, width=180, height=30)
        t2_tag_lab4.config(text="Image Tag : ")

        t2_tag_ent4 = Entry(t2_tag)
        t2_tag_ent4.place(x=210, y=270, width=300, height=30)

        def t2_tag_cancel_btn_action():
            t2_tag.destroy()

        def t2_tag_summit_btn_action():
            if(len(t2_tag_ent3.get())==0 or len(t2_tag_ent4.get())==0):
                messagebox.showerror("Info", "Please Insert Name and Tag.")
            else:
                messagebox.showinfo("Info", "Image Tagging will be done.")
                command = "docker tag " + t2_ent1.get() + " " + t2_tag_ent3.get() + ":" + t2_tag_ent4.get()
                os.system(command)
                time.sleep(0.5)
                t2_tag.destroy()
                t2_lb1.delete(0,END)
                image_list_check()

        t2_commit_cancle_btn = Button(t2_tag)
        t2_commit_cancle_btn.config(command=t2_tag_cancel_btn_action)
        t2_commit_cancle_btn.config(text="Cancel")
        t2_commit_cancle_btn.place(x=360, y=320, width=100, height=60)

        t2_commit_summit_btn = Button(t2_tag)
        t2_commit_summit_btn.config(command=t2_tag_summit_btn_action)
        t2_commit_summit_btn.config(text="Summit")
        t2_commit_summit_btn.place(x=480, y=320, width=100, height=60)




def t2_pull_btn_action():
    t2_pull = Toplevel(win,width=600, height=250)
    t2_pull.grab_set()
    t2_pull.title("Image Pull")
    #t2_pull.option_add("*Font", "Arial 15")
    t2_pull.resizable(False, False)

    t2_pull_title = Label(t2_pull)
    t2_pull_title.config(font="Arial 18")
    t2_pull_title.config(text="Image Pull")
    t2_pull_title.place(x=20, y=10, width=560, height=30)

    t2_pull_lab1 = Label(t2_pull)
    t2_pull_lab1.place(x=20, y=60, width=230, height=30)
    t2_pull_lab1.config(font="Arial 12")
    t2_pull_lab1.config(text="Insert Pull Image name : ")

    t2_pull_ent1 = Entry(t2_pull)
    #t2_pull_ent1.insert(0, str(t2_ent1.get()))
    t2_pull_ent1.place(x=210, y=60, width=360, height=30)

    t2_pull_lab2 = Label(t2_pull)
    t2_pull_lab2.place(x=20, y=110, width=230, height=30)
    t2_pull_lab2.config(font="Arial 12")
    t2_pull_lab2.config(text="Insert Pull Image tag : ")

    t2_pull_ent2 = Entry(t2_pull)
    #t2_pull_ent1.insert(0, str(t2_ent1.get()))
    t2_pull_ent2.place(x=210, y=110, width=360, height=30)

    def t2_pull_cancel_btn_action():
        t2_pull.destroy()

    def t2_pull_summit_btn_action():
        if(len(t2_pull_ent1.get())==0):
            messagebox.showerror("Info", "Please Insert Image:Tag.")
        else:
            messagebox.showinfo("Info", "Image Pull will be start. \n Please Check Console.")
            command = "docker pull " + t2_pull_ent1.get() + ":" + t2_pull_ent2.get()
            os.system(command)
            time.sleep(0.5)
            t2_pull.destroy()
            t2_lb1.delete(0,END)
            image_list_check()


    t2_commit_cancle_btn = Button(t2_pull)
    t2_commit_cancle_btn.config(command=t2_pull_cancel_btn_action)
    t2_commit_cancle_btn.config(text="Cancel")
    t2_commit_cancle_btn.place(x=350, y=170, width=100, height=60)

    t2_commit_summit_btn = Button(t2_pull)
    t2_commit_summit_btn.config(command=t2_pull_summit_btn_action)
    t2_commit_summit_btn.config(text="Summit")
    t2_commit_summit_btn.place(x=475, y=170, width=100, height=60)





def t2_push_btn_action():
    if(len(t2_ent1.get())==0):
        messagebox.showerror("Info", "Please Select image")
    
    else:
        messagebox.showinfo("Info", "Image Push Will be Start. \n Please Check Console.")
        command = "docker push " + t2_ent1.get()




















# ------------------------------------------------------
# gui main
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


















##########################################################
# image tab
# tab 2
# 라벨
t2_lab1 = Label(tab2)
t2_lab1.place(x=20, y=10, width=490, height=30)
t2_lab1.config(text="Imagea List")

# 리스트 박스 설명
t2_lab2 = Label(tab2)
t2_lab2.place(x=20, y=45, width=490, height=30)
t2_lab2.config(font="Arial 10")
t2_lab2.config(text="Name          :          tag")


# 리스트박스
t2_lb1 = Listbox(tab2)
image_list_check()
t2_lb1.config(font="Arial 13")
t2_lb1.place(x=20, y=70, width=590, height=410)

t2_xscrollbar = Scrollbar(tab2, orient="horizontal")
t2_xscrollbar.config(command=lb1.xview)
t2_xscrollbar.place(x=20, y=480, width=590, height=20)

t2_yscrollbar = Scrollbar(tab2, orient="vertical")
t2_yscrollbar.config(command=lb1.yview)
t2_yscrollbar.place(x=610, y=70, width=20, height=410)

# 새로고침 버튼
t2_refresh_button = Button(tab2, text="Reload")
t2_refresh_button.config(command=t2_refresh_button_action)
t2_refresh_button.place(x=470, y=40, width=140, height=25)

# Button
t2_up_btn = Button(tab2, text="Undo")
t2_up_btn.config(command=t2_undo_select_container)
t2_up_btn.place(x=130, y=510, width=160, height=30)

t2_select_btn = Button(tab2, text="Select")
t2_select_btn.config(command=t2_select_image)
t2_select_btn.place(x=330, y=510, width=160, height=30)

# 선택된 컨테이너 라벨
t2_lab3 = Label(tab2)
t2_lab3.place(x=20, y=550, width=280, height=30)
t2_lab3.config(text="Selected image : ")

# 선택된 이미지 이름
t2_ent1 = Entry(tab2)
t2_ent1.place(x=200, y=550, width=650, height=30)

pull_btn = Button(tab2, text="Pull")
pull_btn.config(command=t2_pull_btn_action)
pull_btn.place(x=650, y=120, width=200, height=60)

push_btn = Button(tab2, text="Push")
push_btn.config(command=t2_push_btn_action)
push_btn.place(x=650, y=230, width=200, height=60)

tag_btn = Button(tab2, text="Tag")
tag_btn.config(command=t2_tag_btn_action)
tag_btn.place(x=650, y=340, width=200, height=60)

rmi_btn = Button(tab2, text="Remove")
rmi_btn.config(command=t2_rmi_btn_action)
rmi_btn.place(x=650, y=450, width=200, height=60)












#--------------------------------------------
# Copyright
copyright = Label(
    win,
    font=("Helvetica", 9))
copyright.config(text="Made By Suseong,Yang      Email : tntjd5596@miruware.com      2021.07.06")
copyright.place(x=470, y=605, width=500, height=30)



win.mainloop()