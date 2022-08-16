import os
import time
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

# Docker image list preprocessing
def docker_preprocessing():

    os.system(str("docker images > ./docker_image_list"))

    f = open("./docker_image_list", "rt", encoding="utf-8")
    image = f.readlines()
    f.close()
    #print(image)

    image = "".join(image).split("\n")
    #image = ",".join(image).split(" ")
    #print(image[1])

    var = 0
    var_list = []

    for i in range(len(image)):
        #print(i)
        var = "".join(image[i]).split(" ")
        #print(var)
        var_list.append(var)
        

    var_list = var_list[1:-1]

    #print(var_list)

    image_name = []
    tag = []
    image_id = []
    image_list = []

    idx = 0
    for i in range(len(var_list)):
        temp=[]
        temp = ' '.join(var_list[i]).split()
        #print("temp : ", temp)
        image_name.append(temp[0])
        tag.append(temp[1])
        image_id.append(temp[2])
        image_list.append(temp[0]+ ':' +temp[1])
        #print(" ")
        #print(str(idx) + " : " + temp[0]+ ':' +temp[1])
        image_full_name = str(temp[0]) + ":" + str(temp[1])
        lb1.insert(idx, str(image_full_name))
        idx += 1

    os.system("rm ./docker_image_list")
    
    #return image_list
    
    
    """
    print('image_name : ', image_name)
    print('tag : ', tag)
    print('image_id : ', image_id)
    """
    #print('image list : ', image_list)
    
    #print("docker_preprocessing complete")
    
    # GPU 사용 가능 개수 확인 함수
def gpu_check():
    #os.system(str(ssh_connect.format(**data)) + "nvidia-smi | grep MiB | grep % > /home/" + user_id + "/flask/data/max_gpu_avail")
    current_path = str(os.popen("pwd").read())
    current_path = current_path.rstrip('\n')
    os.system("nvidia-smi | grep MiB | grep % > ./max_gpu_avail")
    #os.system(scp_connect.format(**data) + "max_gpu_avail ./data/")
    f = open("./max_gpu_avail", "rt", encoding="utf-8")
    max_gpu_avail_temp = f.readlines()
    f.close()
    max_gpu_avail = str(len(max_gpu_avail_temp))
    os.system("rm ./max_gpu_avail")
    #print('max_gpu_avail : ',max_gpu_avail)
    #print("gpu_avail() complete")

    if(int(max_gpu_avail)>=1):
        gpu_num_list.append(0)
        for i in range(len(max_gpu_avail)):
            gpu_num_list.append(i+1)
    else:
        gpu_num_list.append(0)
        
def select_image():
        idx = lb1.curselection()
        ent1.delete(0,len(ent1.get()))
        ent1.insert(0, str(lb1.get(idx)))
        
def undo_select_image():
    ent1.delete(0,len(ent1.get()))
    
def container_name_check():
    user_name = str(os.popen("whoami").read())
    user_name = user_name.rstrip('\n')
    #print(user_name)

    os.system(str("docker ps -a | grep -i $(whoami) > ./docker_container_name"))

    f = open("./docker_container_name", "rt", encoding="utf-8")
    name = f.readlines()
    f.close()
    os.system("rm ./docker_container_name")
    
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

    name_list = []
    for i in range(len(var_list)):
        temp=[]
        temp = ' '.join(var_list[i]).split()
        #print(temp[-1])
        name_list.append(temp[-1])

    #print(name_list)

    idx = 0
    container_name = ""
    #for i in range(len(name_list)):
    while True:
        idx_1 = 0
        idx_2 = 0
        temp = user_name + str(idx)
        idx += 1
        #print(len(name_list))
        if(len(name_list) == 0):
            container_name = temp
            break
        for j in name_list:
            if(str(temp) == j):
                #print("name_list :", j, "temp : ", temp)
                continue
            else:
                idx_1 += 1

            if(idx_1 == len(name_list)):
                idx_2 += 1
                container_name = temp
                #print(container_name)
        if (idx_2 == 1):
            break
    return container_name

def cancle_button():
    ent1.delete(0,len(ent1.get()))
    r_ent_name.delete(0,len(r_ent_name.get()))
    r_ent_disk_container.delete(0,len(r_ent_disk_container.get()))
    r_ent_disk_local.delete(0,len(r_ent_disk_local.get()))
    r_ent_port_container.delete(0,len(r_ent_port_container.get()))
    r_ent_port_local.delete(0,len(r_ent_port_local.get()))
    r_ent_command.delete(0,len(r_ent_command.get()))
    
def refresh_image():
    lb1.delete(0,END)
    docker_preprocessing()
    
def summit_button():
    # rm
    rm_command=""
    if(int(check_rm.get())==1):
        rm_command="--rm"
        #print(rm_command)
    
    # gpu
    gpu_command=""
    value = r_combo_gpu.current()
    #print(value)
    if(str(value) != "0"):
        gpu_command = "--gpus " + str(value)
        #print(gpu_command)
        
    # name
    container_name = str(r_ent_name.get())
    container_name_command = "--name " + container_name
    #print(container_name_command)
        
    # mount
    if(int(check_mount.get()==1)):
        mount_path_local = str(r_ent_disk_local.get())
        mount_path_container = str(r_ent_disk_container.get())
        mount_path_command = "-v " + mount_path_local + ":" + mount_path_container
        #print(mount_path_command)
    else:
        mount_path_command=""
        #print("Do not use mount")
        pass
    
    # port
    if(int(check_port_foward.get()==1)):
        port_foward_local = str(r_ent_port_local.get())
        port_foward_container = str(r_ent_port_container.get())
        port_foward_command = "-p " + port_foward_local + ":" + port_foward_container
        #print(port_foward_command)
    else:
        port_foward_command=""
        #print("Do not use port foward")
        pass
    
    # command
    command = str(r_ent_command.get())
    #print(command)
    
    # image
    image_name = str(ent1.get())
    #print(image_name)
    
    time.sleep(1)
    win.destroy()

    if(str(value) != "0"):
        docker_run_command = "nvidia-docker run -ti" + " " + rm_command + " " \
              + gpu_command + " " + container_name_command + " " \
              + mount_path_command + " " + port_foward_command + " " \
              + image_name + " " + command
    else:
        docker_run_command = "docker run -ti" + " " + rm_command + " " \
              + gpu_command + " " + container_name_command + " " \
              + mount_path_command + " " + port_foward_command + " " \
              + image_name + " " + command
    
        
    #print(docker_run_command)
    
    os.system(docker_run_command)
    
    
    
    
###################################################################    
    
win = Tk()
win.geometry("1200x600")
win.title("MW Docker")
win.option_add("*Font", "Arial 15")
win.resizable(False, False)



# 로고
lab_img = Label(win)
img = PhotoImage(file = "./image/miruware_logo.png", master=win)
img = img.subsample(2)
lab_img.config(image=img)
lab_img.place(x=900, y=20)




# 라벨
lab1 = Label(win)
lab1.place(x=20, y=10, width=490, height=30)
lab1.config(text="Docker images")


# 리스트박스
lb1 = Listbox(win)
docker_preprocessing()
lb1.place(x=20, y=50, width=470, height=360)

xscrollbar = Scrollbar(win, orient="horizontal")
xscrollbar.config(command=lb1.xview)
xscrollbar.place(x=20, y=410, width=470, height=20)

yscrollbar = Scrollbar(win, orient="vertical")
yscrollbar.config(command=lb1.yview)
yscrollbar.place(x=490, y=50, width=20, height=360)


# Button
up_btn = Button(win, text="Undo")
up_btn.config(command=undo_select_image)
up_btn.place(x=70, y=470, width=160, height=30)

down_btn = Button(win, text="Select")
down_btn.config(command=select_image)
down_btn.place(x=280, y=470, width=160, height=30)


# 선택된 이미지 이름
ent1 = Entry(win)
ent1.place(x=20, y=530, width=490, height=30)
#ent1.config(text="test")


# 새로고침 버튼
refresh_button = Button(win, text="Reload")
refresh_button.config(command=refresh_image)
refresh_button.place(x=350, y=20, width=160, height=25)


# Right (Selector)
#---------------------------------------------------------------

# --rm option
check_rm = IntVar()
r_check_rm = Checkbutton(win, variable=check_rm, onvalue=1, offvalue=0)
r_check_rm.config(text="Use --rm option            ")
r_check_rm.place(x=530, y=80, width=315, height=30)


# GPU
r_lab_gpu = Label(win)
r_lab_gpu.place(x=530, y=130, width=230, height=30)
r_lab_gpu.config(text="GPU Count ")

#gpu_num_list = [1,2,3,4,5,6,7,8]
gpu_num_list=[]
gpu_check()
r_combo_gpu = ttk.Combobox(win)
r_combo_gpu.config(value = gpu_num_list)
r_combo_gpu.place(x=530, y=160, width=230, height=30)






# Container Name
container_name = container_name_check()

r_lab_name = Label(win)
r_lab_name.place(x=780, y=130, width=400, height=30)
r_lab_name.config(text="Container Name(Do not use space)")

r_ent_name = Entry(win)
r_ent_name.insert(0, str(container_name))
r_ent_name.place(x=780, y=160, width=400, height=30)






# Disk mount
check_mount = IntVar()
r_check_disk = Checkbutton(win, variable=check_mount, onvalue=1, offvalue=0)
r_check_disk.config(text="Use DIsk Mount            ")
r_check_disk.place(x=530, y=220, width=315, height=30)

r_lab_disk_local = Label(win)
r_lab_disk_local.place(x=530, y=250, width=315, height=30)
r_lab_disk_local.config(text="Local Path (Absolute Path)")

r_ent_disk_local = Entry(win)
r_ent_disk_local.place(x=530, y=280, width=315, height=30)

r_lab_disk_container = Label(win)
r_lab_disk_container.place(x=865, y=250, width=315, height=30)
r_lab_disk_container.config(text="Container Path (Absolute Path)")

r_ent_disk_container = Entry(win)
r_ent_disk_container.place(x=865, y=280, width=315, height=30)





# Port Fowarding
check_port_foward = IntVar()
r_check_port = Checkbutton(win, variable=check_port_foward, onvalue=1, offvalue=0)
r_check_port.config(text="Use Port Fowarding      ")
r_check_port.place(x=530, y=330, width=315, height=30)

r_lab_port_local = Label(win)
r_lab_port_local.place(x=530, y=360, width=315, height=30)
r_lab_port_local.config(text="Local Port")

r_ent_port_local = Entry(win)
r_ent_port_local.place(x=530, y=390, width=315, height=30)

r_lab_port_container = Label(win)
r_lab_port_container.place(x=865, y=360, width=315, height=30)
r_lab_port_container.config(text="Container Port")

r_ent_port_container = Entry(win)
r_ent_port_container.place(x=865, y=390, width=315, height=30)


# command
r_lab_command = Label(win)
r_lab_command.place(x=600, y=460, width=315, height=30)
r_lab_command.config(text="Command :")

r_ent_command = Entry(win)
r_ent_command.insert(0,"bash")
r_ent_command.place(x=720, y=460, width=400, height=30)





# Button
cancle_btn = Button(win, text="Reset")
cancle_btn.config(command=cancle_button)
cancle_btn.place(x=950, y=520, width=100, height=50)


summit_btn = Button(win, text="Summit")
summit_btn.config(command=summit_button)
summit_btn.place(x=1070, y=520, width=100, height=50)




#--------------------------------------------
# Copyright
copyright = Label(
    win,
    font=("Helvetica", 9))
copyright.config(text="Made By Suseong,Yang      Email : tntjd5596@miruware.com      2021.08.16")
copyright.place(x=700, y=570, width=500, height=30)



win.mainloop()

