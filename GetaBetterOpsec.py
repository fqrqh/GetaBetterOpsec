import customtkinter
from selenium import webdriver
import webbrowser


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text="")
        self.label.grid(row=0, column=0, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("850x500")
        self.title("GetaBetterOpsec")
        self.iconbitmap("icon.ico")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.label = customtkinter.CTkLabel(
            self,
            text="This is GetaBetterOpsec",
            fg_color="transparent"
        )

        self.btn = customtkinter.CTkButton(
            self,
            text="RundScan"
        )
        self.btn1= customtkinter.CTkButton(
            self,
            text="Run a Quick Scan"
        )
        self.btn2= customtkinter.CTkButton(
            self,
            text="Settings"
        )
        self.label.place(x=55, y=90)
        self.btn.place(x=55, y=190)
        self.btn1.place(x=55, y=190)
        self.btn2.place(x=55, y=280)
        self.btn.grid(row=0, column=0, pady=20)

    
    def cleanfrr(self):
        print("sa clean la")
    # driver = webdriver.choice
    # driver.delete_all_cookies()



app = App()
app.mainloop()