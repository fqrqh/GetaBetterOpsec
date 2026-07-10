import customtkinter
from pywinauto import application
from system_info import sysinfo
import webbrowser
from PIL import Image
import psutil
import functions
import platform
import os
import time

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        label = customtkinter.CTkLabel(self, text="")
        label.pack(padx=20, pady=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("890x500")
        self.title("WindowsUtility")
        self.iconbitmap('icon.ico')


        my_image = customtkinter.CTkImage(
        light_image=Image.open("icon.ico"),
         
        size=(150, 150)
        )


        

        image_label = customtkinter.CTkLabel(self, image=my_image, text="")
        image_label.place(x=25, y=40)


        

        
        
        title_label = customtkinter.CTkLabel(
        self,
        text="WindowsUtility",
        font=("Consolas", 14, "bold")
        )

        self.Label = customtkinter.CTkLabel(
            self,
            text="Essential Tweaks",
            font=("Consolas", 14, "bold")
        )    
        self.Label.place(x=250,y=20)

        self.Label1 = customtkinter.CTkLabel(
            self,
            text="Advanced Tweaks",
            font=("Consolas", 14, "bold")
        )    
        self.Label1.place(x=250,y=180)

        

        self.Label2 = customtkinter.CTkLabel(
            self,
            text="Performance Plans",
            font=("Consolas", 14, "bold")
        )    
        self.Label2.place(x=250,y=350)


        self.Label4 = customtkinter.CTkLabel(
            self,
            text="Customize Preferences",
            font=("Consolas", 14, "bold")
        )    
        self.Label4.place(x=510,y=20)

        

        self.frame = customtkinter.CTkFrame(
            self,
            width=600,height=470
        )
        self.frame.place(x=250,y=16)
        self.frame.lower(self.Label)
    


        self.credits = customtkinter.CTkLabel(
        self,
        text="Made by [fqrqh]",
        font=("Consolas", 13, "bold")
        )
        self.credits.place(x=50,y=470)
        title_label.place(x=40, y=10)


        ## ESSENTIAL ##

        self.check_var = customtkinter.StringVar(value="off")
        self.check = customtkinter.CTkCheckBox(
            self,
            text="Restore Point -Create",
            checkbox_width=13,
            checkbox_height=13,
 
            variable=self.check_var,
            onvalue="on",
            offvalue="off"
        )
        self.check.place(x=255,y=60)

        self.check_var = customtkinter.StringVar(value="off")
        self.check1 = customtkinter.CTkCheckBox(
            self,
            text="Disk Cleanup -Enable",
            checkbox_width=13,
            checkbox_height=13,

            variable=self.check_var,
            onvalue="on",
            offvalue="off"
        )
        self.check1.place(x=255,y=90)

        self.check_var = customtkinter.StringVar(value="off")
        self.check2 = customtkinter.CTkCheckBox(
            self,
            text="Location Tracking -Disable",
            checkbox_width=13,
            checkbox_height=13,
  
            variable=self.check_var,
            onvalue="on",
            offvalue="off"
        )
        self.check2.place(x=255,y=120)

        self.check_var = customtkinter.StringVar(value="off")
        self.check3 = customtkinter.CTkCheckBox(
            self,
            text="Activity History -Disable",
            checkbox_width=13,
            checkbox_height=13,
    
            variable=self.check_var,
            onvalue="on",
            offvalue="off"
        )
        self.check3.place(x=255,y=150)

        ## END OF CHECKS ##



        self.check_var = customtkinter.StringVar(value="off")
        self.check5 = customtkinter.CTkCheckBox(
            self,
            text="Widget -Remove",
            checkbox_width=13,
            checkbox_height=13,

            variable=self.check_var,
            onvalue="on",
            offvalue="off"
        )
        self.check5.place(x=255,y=220)

        self.check_var = customtkinter.StringVar(value="off")
        self.check6 = customtkinter.CTkCheckBox(
            self,
            text="Background Apps -Disable",
            checkbox_width=13,
            checkbox_height=13,
            variable=self.check_var,
            onvalue="on",
            offvalue="off"
        )
        self.check6.place(x=255,y=250)

        self.check_var = customtkinter.StringVar(value="off")
        self.check7 = customtkinter.CTkCheckBox(
            self,
            text="Fullscreen Optimisation -Disable",
            checkbox_width=13,
            checkbox_height=13,
            variable=self.check_var,
            onvalue="on",
            offvalue="off"
        )
        self.check7.place(x=255,y=280)

        self.check_var = customtkinter.StringVar(value="off")
        self.check8 = customtkinter.CTkCheckBox(
            self,
            text="Visual Effects -Enable",
            checkbox_width=13,
            checkbox_height=13,
            variable=self.check_var,
            onvalue="on",
            offvalue="off"
        )
        self.check8.place(x=255,y=310)





        self.button5 = customtkinter.CTkButton(
            self,
            text="Ultimate Perfomance Enable",
            font=("Consolas", 13, "bold"),
            width=150
           
        )
        self.button5.place(x=252,y=390)

        self.button6 = customtkinter.CTkButton(
            self,
            text="Ultimate Performance Disable",
            font=("Consolas", 13, "bold"),
            width=150
           
        )
        self.button6.place(x=252,y=420)







        self.switch_var = customtkinter.StringVar(value="off")

        self.switch = customtkinter.CTkSwitch(
        self,
        text="Dark Theme for Windows",
        variable=self.switch_var,
        command=self.darktheme,
        onvalue="on",
        offvalue="off"
        )
        self.switch.place(x=510,y=50)

        self.switch_var = customtkinter.StringVar(value="off")

        self.switch1 = customtkinter.CTkSwitch(
        self,
        text="LogScreen Acrylic Blur",
        variable=self.switch_var,
        onvalue="on",
        offvalue="off"
        )
        self.switch1.place(x=510,y=80)

        self.switch_var = customtkinter.StringVar(value="off")

        self.switch2 = customtkinter.CTkSwitch(
        self,
        text="Mouse Acceleration",
        variable=self.switch_var,
        onvalue="on",
        offvalue="off"
        )
        self.switch2.place(x=510,y=110)

        self.switch_var = customtkinter.StringVar(value="off")

        self.switch3 = customtkinter.CTkSwitch(
        self,
        text="Taskbar Centered Icons",
        variable=self.switch_var,
        onvalue="on",
        offvalue="off"
        )
        self.switch3.place(x=510,y=140)

        self.switch_var = customtkinter.StringVar(value="off")

        self.switch3 = customtkinter.CTkSwitch(
        self,
        text="Taskbar Search Icon",
        variable=self.switch_var,
        onvalue="on",
        offvalue="off"
        )
        self.switch3.place(x=510,y=170)

        self.switch_var = customtkinter.StringVar(value="off")

        self.switch3 = customtkinter.CTkSwitch(
        self,
        text="Taskbar Search Icon",
        variable=self.switch_var,
        onvalue="on",
        offvalue="off"
        )
        self.switch3.place(x=510,y=200)



print("Getting the github rated shi")











       
        

        self.button = customtkinter.CTkButton(
            self,
            text="Apply Tweaks",
            font=("Consolas", 13, "bold"),
            width=180
           
        )
        self.button.place(x=10, y=200)
        self.button1 = customtkinter.CTkButton(
            self,
            text="Remove Tweaks",
            font=("Consolas", 13, "bold"),
            width=180
           
        )
        self.button1.place(x=10, y=240)
        self.button2 = customtkinter.CTkButton(
            self,
            font=("Consolas", 13, "bold"),
            text="",
            width=180
           
        )
        self.button2.place(x=10, y=280)

        self.button4 = customtkinter.CTkButton(
            self,
            font=("Consolas", 13, "bold"),
            text="Show Installed Tweaks",
            width=180
           
        )
        self.button4.place(x=10, y=320)

        self.button3 = customtkinter.CTkButton(
            self,
            font=("Consolas", 13, "bold"),
            text="Exit",
            command=self.exitbtn,
            width=180
           
        )
        self.button3.place(x=10, y=430)

    

        
     
    def exitbtn(self):
        exit()
    

    

    def darktheme(self):

        commandt = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f"
        self.button2.configure(text="Done")
        os.system(commandt)
        print("done")



# os.getlogin()
app = App()
app.mainloop()
