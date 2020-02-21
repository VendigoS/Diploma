import os
import subprocess

from tkinter import filedialog
from tkinter import *
from tkinter.messagebox import *

from default_data import all_methods, lang_fits, space_statement, end_statement
from mongo_handler import get_mongo_param, get_mongo, set_mongo
from test_module import Tokenizer, Parser, du_maker, df_maker, du_testing, style_testing
from utils import run_process

class MainApp(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        self.author = ""
        self.version = "1.0.0"
        self.logfile = "cts.log"
        self.language = "python"
        self.output_to_screen = True
        self.output_logs = False
        self.output_bugs = True
        self.indents_space = 4

        self.pack(expand=YES, fill=BOTH)
        self.createWidgets()
        self.master.title('Code Testing System (с) Lakshtovskiy Ivan')
        self.master.geometry("1300x700+100+20")
        self.master.resizable(width=False, height=False)

        self.mongo_address = "mongodb://localhost:27017/"
        self.mongo_db = "python"
        self.mongo_token_collection = "tokens"
        self.mongo_exprs_collection = "rules"
        self.mongo_db_bt = "bug_tracking"
        self.mongo_bugs_collection = "bugs"
        self.bad_tokens_list = ["undefined"]
        self.rules = "PEP8"
        self.rewrite_bugs = False
        self.rewrite_bugs_list = []
        self.rewrite_bugs_by_list = []

    def createWidgets(self):
        self.codeName = ""
        self.allCodes = []
        self.current_text = ""

        self.make_code()
        self.make_options()
        self.make_inform()
        self.make_left_panel()
        self.make_toolbar()
        self.make_settins_value()
        self.make_start_button()


    def change_method(self):
        fit = {}
        for i in range(0, len(self.CB)):
            if self.cb_var[i].get() == 0:
                for k in range(i + 1, len(self.CB)):
                    if all_methods[self.CB[k].cget("text")] > all_methods[self.CB[i].cget("text")]:
                        self.CB[k].configure(state="disabled")
                        self.cb_var[k].set(0)
            elif self.cb_var[i].get() == 1:
                for k in range(i + 1, len(self.CB)):
                    if all_methods[self.CB[k].cget("text")] == all_methods[self.CB[i].cget("text")] + 1:
                        self.CB[k].configure(state="normal")


    def make_code(self):
        self.CodeFrame = Frame(self)
        self.CodeFrame.place(x=450, y=100)
        self.codeName_label = Label(self.CodeFrame, text='Current code:', height=1, width=35)
        # self.codeName_label.grid(row=0, column=0)
        self.codeName_label.pack(side=TOP)
        self.TextBox = Text(self.CodeFrame, relief=SUNKEN, state='disabled') #text window
        sbar = Scrollbar(self.CodeFrame)
        self.TextBox.config(yscrollcommand=sbar.set, relief=SUNKEN, width=60, height=35, bg='white')
        sbar.config(orient="vertical", command=self.TextBox.yview)
        # self.TextBox.grid(row=1, column=0)
        self.TextBox.pack(side=LEFT, fill=BOTH)
        sbar.pack(side=RIGHT, fill=Y)
        # sbar.grid(row=1, column=1)

    def make_options(self):
        self.ModeFrame = Frame(self)
        self.ModeFrame.place(x=200, y=100)
        Label(self.ModeFrame, text='Doings with code', height=5, width=25).grid(row=0, column=0)
        methodsBox = Frame(self.ModeFrame)
        methodsBox.grid(row=1, column=0)
        bufRow = 1
        self.CB = []
        self.cb_var = []
        for item in all_methods.keys():
            self.cb_var.append(IntVar())
            self.CB.append(Checkbutton(methodsBox, text=item, variable=self.cb_var[len(self.cb_var) - 1], onvalue=1, offvalue=0, state="disabled", command=self.change_method))
            self.CB[bufRow - 1].grid(row=bufRow, column=0, sticky='w')
            bufRow += 1

        Label(self.ModeFrame, text='Open sources:', height=5, width=20).grid(row=2, column=0)
        sbar = Scrollbar(self.ModeFrame)
        self.CodesBox = Listbox(self.ModeFrame, relief=SUNKEN)
        sbar.config(command=self.CodesBox.yview)
        self.CodesBox.config(yscrollcommand=sbar.set, width=35)
        self.CodesBox.grid(row=3, column=0)
        sbar.grid(row=3, column=1)
        self.CodesBox.bind('<Double-1>', self.change_code)

    def make_inform(self):
        self.infoFrame = Frame(self)
        self.infoFrame.place(x=1000, y=100)
        Label(self.infoFrame, text='Methods output:', height=1, width=25).pack(side=TOP)
        sbar = Scrollbar(self.infoFrame)
        self.infoBox = Text(self.infoFrame, relief=SUNKEN, width=30, height=10)
        sbar.config(command=self.infoBox.yview)
        self.infoBox.config(yscrollcommand=sbar.set)
        self.infoBox.pack(side=LEFT, fill=BOTH)
        sbar.pack(side=RIGHT, fill=Y)

        self.bugsFrame = Frame(self)
        self.bugsFrame.place(x=1000, y=300)
        Label(self.bugsFrame, text='The found bugs:', height=1, width=25).pack(side=TOP)
        sbar2=Scrollbar(self.bugsFrame)
        self.bugBox=Listbox(self.bugsFrame, relief=SUNKEN, width=40)
        sbar2.config(command=self.bugBox.yview)
        self.bugBox.config(yscrollcommand=sbar2.set)
        self.bugBox.pack(side=LEFT, fill=BOTH)
        sbar2.pack(side=RIGHT, fill=Y)



    def make_left_panel(self):
        self.menuFrame = Frame(self)
        self.menuFrame.place(x=10, y=150)
        btn1 = Button(self.menuFrame, text="Testing\nsystem", bg="snow", font="Times 20", height=8, width=10)
        btn1.grid(row=0, column=0)
        btn2 = Button(self.menuFrame, text="Bug-tracking\nsystem",font="Times 20", height=8, width=10, command=self.forget_st)
        btn2.grid(row=1, column=0)

    def make_toolbar(self):
        self.toolFrame = Frame(self)
        self.toolFrame.place(x=10, y=20)
        btn1 = Button(self.toolFrame, text="Open file", font="Times 10", height=1, width=15, command=self.open_file)
        btn1.grid(row=0, column=0)
        btn2 = Button(self.toolFrame, text="Settings", font="Times 10", height=1, width=15, command=self.create_settings_win)
        btn2.grid(row=0, column=1)
        btn3 = Button(self.toolFrame, text="Output settings", font="Times 10", height=1, width=15, command=self.create_output_win)
        btn3.grid(row=0, column=2)

    def make_settins_value(self):
        self.outputFrame = Frame(self)
        self.outputFrame.place(x=450, y=10)
        Label(self.outputFrame, text='log file:', height=1, width=15).grid(row=0, column=0)
        self.logFileBox = Text(self.outputFrame, relief=SUNKEN, state='normal')
        self.logFileBox.config(relief=SUNKEN, width=15, height=1)
        self.logFileBox.delete(1.0, END)
        self.logFileBox.insert(1.0, self.logfile)
        self.logFileBox.configure(state="disabled")
        self.logFileBox.grid(row=1, column=0)

        Label(self.outputFrame, text='language:', height=1, width=15).grid(row=0, column=1)
        self.langBox = Text(self.outputFrame, relief=SUNKEN, state='normal')
        self.langBox.delete(1.0, END)
        self.langBox.insert(1.0, self.language)
        self.langBox.config(relief=SUNKEN, width=15, height=1)
        self.langBox.configure(state="disabled")
        self.langBox.grid(row=1, column=1)

        Label(self.outputFrame, text='Show process:', height=1, width=15).grid(row=0, column=2)
        self.indentsBox = Text(self.outputFrame, relief=SUNKEN, state='normal')
        self.indentsBox.delete(1.0, END)
        if self.output_to_screen:
            self.indentsBox.insert(1.0, "Yes")
        else:
            self.indentsBox.insert(1.0, "No")
        self.indentsBox.config(relief=SUNKEN, width=15, height=1)
        self.indentsBox.configure(state="disabled")
        self.indentsBox.grid(row=1, column=2)

        Label(self.outputFrame, text='Indent amount:', height=1, width=15).grid(row=0, column=3)
        self.indentsSpaceBox = Text(self.outputFrame, relief=SUNKEN, state='normal')
        self.indentsSpaceBox.delete(1.0, END)
        self.indentsSpaceBox.insert(1.0, self.indents_space)
        self.indentsSpaceBox.config(relief=SUNKEN, width=15, height=1)
        self.indentsSpaceBox.configure(state="disabled")
        self.indentsSpaceBox.grid(row=1, column=3)

    def make_start_button(self):
        self.startButtonFrame = Frame(self)
        self.startButtonFrame.place(x=1050, y=500)
        btn1 = Button(self.startButtonFrame, text="Start test!", font="Times 15", height=1, width=15, command=self.start_testing)
        btn1.grid(row=0, column=0)

    def change_code(self, event):
        self.deal_with_text(self.CodesBox.get(ACTIVE))

    def open_file(self):
        self.codeName = filedialog.askopenfilename(title="Choose the file", filetypes=[('Supported types', ('.txt', '.py', 'cs')),
                                                              ('text files', '.txt'), ('python files', '.py'),
                                                              ('All files', '*')])
        for item in self.allCodes:
            if item == self.codeName:
                showerror('Names are same!',
                          'You try to add the file with the same name of open files. Choose another or delete existing')
                return

        if not self.codeName:
            return

        self.allCodes.append(self.codeName)
        self.deal_with_text(self.codeName)

    def deal_with_text(self, filename):
        if not filename:
            return
        self.after_choose_text_win()
        self.codeName = filename
        with open(filename) as file:
            self.current_text = file.read()

        self.clear_dynamic_items()
        self.draw_codes_box()
        self.draw_text_box(self.current_text)
        head, tail = os.path.split(self.codeName)
        head, file_extension = os.path.splitext(self.codeName)
        if file_extension in lang_fits.keys():
            self.language = lang_fits[file_extension]
        else:
            self.language = "python"

        self.langBox.configure(state='normal')
        self.langBox.delete(1.0, END)
        self.langBox.insert(1.0, self.language)
        self.langBox.configure(state="disabled")

        self.codeName_label.configure(text="Current code: {0}".format(tail))

    def clear_dynamic_items(self):
        self.infoBox.delete('1.0', END)
        self.TextBox.config(state='normal')
        self.TextBox.delete('1.0', END)
        self.TextBox.config(state='disable')
        self.bugBox.delete(0, END)
        for i in range(0, len(self.CB)):
            self.CB[i].configure(state="disabled")
            self.cb_var[i].set(0)
        self.CB[0].configure(state="normal")


    def draw_codes_box(self):
        self.CodesBox.delete(0, END)
        for item in self.allCodes:
            self.CodesBox.insert(END, item)


    def draw_text_box(self, text):
        self.TextBox.config(state='normal')
        self.TextBox.insert('1.0', text)
        self.TextBox.config(state='disable')

    def after_choose_text_win(self):
        self.afterWindow = Toplevel(master=self, width=300, height=150)
        self.afterWindow.grab_set()
        self.afterWindow.resizable(width=False, height=False)
        self.afterWindow.title("Choose indent")
        self.afterWindowFrame = Frame(self.afterWindow)
        self.afterWindowFrame.place(x=10, y=10)
        Label(self.afterWindowFrame, text='Is the language sensitive to indents:', height=1, width=35, font="Times 12").grid(row=0, column=0)
        self.sensitiveCBVar = IntVar()
        self.sensitiveCB = Checkbutton(self.afterWindowFrame, variable=self.sensitiveCBVar, command=self.change_sensitive_var)
        self.sensitiveCB.grid(row=1, column=0)
        Label(self.afterWindowFrame, text='Type space of indent:', height=1, width=35, font="Times 12").grid(row=2, column=0)
        self.sensitiveBox = Text(self.afterWindowFrame, relief=SUNKEN, state='disabled', width=10, height=1)
        self.sensitiveBox.grid(row=3, column=0)
        Button(self.afterWindowFrame, text="OK", command=self.afterWindow_close).grid(row=4, column=0)

    def change_sensitive_var(self):
        if self.sensitiveCBVar.get() == 1:
            self.sensitiveBox.configure(state="normal")
        else:
            self.sensitiveBox.configure(state="disabled")

    def afterWindow_close(self):
        if self.sensitiveCBVar.get() == 1:
            try:
                self.indents_space = int(self.sensitiveBox.get("1.0", END))
            except ValueError:
                return
        else:
            self.indents_space = ""

        self.indentsSpaceBox.configure(state="normal")
        self.indentsSpaceBox.delete(1.0, END)
        self.indentsSpaceBox.insert(1.0, self.indents_space)
        self.indentsSpaceBox.configure(state="disabled")
        self.afterWindow.destroy()


    def create_settings_win(self):
        self.settingsWindow = Toplevel(master=self, width=600, height=600)
        self.settingsWindow.grab_set()
        self.settingsWindow.title("Settings of interaction with DB")
        self.settingsWindow.resizable(width=False, height=False)
        self.settingsWindowFrame = Frame(self.settingsWindow)
        self.settingsWindowFrame.place(x=10, y=10)

        Label(self.settingsWindowFrame, text='Socket address of DB:', height=1, width=35, font="Times 12").grid(row=0,
                                                                                                              column=0)
        self.socketDBBox = Text(self.settingsWindowFrame, relief=SUNKEN, state='normal', width=30, height=1)
        self.socketDBBox.delete("1.0", END)
        self.socketDBBox.insert("1.0", self.mongo_address)
        self.socketDBBox.grid(row=0, column=1)

        Label(self.settingsWindowFrame, text='', height=1).grid(row=1, column=0)
        Label(self.settingsWindowFrame, text='Address of DB:', height=1, width=35, font="Times 12").grid(row=2,
                                                                                                       column=0)
        self.addressDBBox = Text(self.settingsWindowFrame, relief=SUNKEN, state='normal', width=30, height=1)
        self.addressDBBox.delete("1.0", END)
        self.addressDBBox.insert("1.0", self.mongo_db)
        self.addressDBBox.grid(row=2, column=1)

        Label(self.settingsWindowFrame, text='', height=1).grid(row=3, column=0)
        Label(self.settingsWindowFrame, text='Collection tokens:', height=1, width=35, font="Times 12").grid(row=4,
                                                                                                       column=0)
        self.tokenCollectionBox = Text(self.settingsWindowFrame, relief=SUNKEN, state='normal', width=30, height=1)
        self.tokenCollectionBox.delete("1.0", END)
        self.tokenCollectionBox.insert("1.0", self.mongo_token_collection)
        self.tokenCollectionBox.grid(row=4, column=1)

        Label(self.settingsWindowFrame, text='', height=1).grid(row=5, column=0)
        Label(self.settingsWindowFrame, text='Collection expressions:', height=1, width=35, font="Times 12").grid(row=6,
                                                                                                           column=0)
        self.exprsCollectionBox = Text(self.settingsWindowFrame, relief=SUNKEN, state='normal', width=30, height=1)
        self.exprsCollectionBox.delete("1.0", END)
        self.exprsCollectionBox.insert("1.0", self.mongo_exprs_collection)
        self.exprsCollectionBox.grid(row=6, column=1)

        Label(self.settingsWindowFrame, text='', height=1).grid(row=7, column=0)
        Label(self.settingsWindowFrame, text='Bug-tracking DB address:', height=1, width=35, font="Times 12").grid(row=8,
                                                                                                           column=0)
        self.bugTrackingBox = Text(self.settingsWindowFrame, relief=SUNKEN, state='normal', width=30, height=1)
        self.bugTrackingBox.delete("1.0", END)
        self.bugTrackingBox.insert("1.0", self.mongo_db_bt)
        self.bugTrackingBox.grid(row=8, column=1)

        Label(self.settingsWindowFrame, text='', height=1).grid(row=9, column=0)
        Label(self.settingsWindowFrame, text='Collection bugs:', height=1, width=35, font="Times 12").grid(row=10,
                                                                                                            column=0)
        self.bugsCollectionBox = Text(self.settingsWindowFrame, relief=SUNKEN, state='normal', width=30, height=1)
        self.bugsCollectionBox.delete("1.0", END)
        self.bugsCollectionBox.insert("1.0", self.mongo_bugs_collection)
        self.bugsCollectionBox.grid(row=10, column=1)

        Label(self.settingsWindowFrame, text='', height=1).grid(row=11, column=0)
        Label(self.settingsWindowFrame, text='List bad tokens (names, delim with comm ","):', height=1, width=35,
              font="Times 10").grid(row=12, column=0)
        self.badTokensBox = Text(self.settingsWindowFrame, relief=SUNKEN, state='normal', width=30, height=1)
        self.badTokensBox.delete("1.0", END)
        data = ','.join('{}'.format(item) for item in self.bad_tokens_list)
        self.badTokensBox.insert("1.0", data)
        self.badTokensBox.grid(row=12, column=1)

        Label(self.settingsWindowFrame, text='', height=1).grid(row=13, column=0)
        Label(self.settingsWindowFrame, text='Rewrite bugs:', height=1, width=35,
              font="Times 10").grid(row=14, column=0)
        self.rewriteBugsCBVar = IntVar()
        self.rewriteBugsCB = Checkbutton(self.settingsWindowFrame, variable=self.rewriteBugsCBVar, command=self.change_rewrite_bugs_var)
        self.rewriteBugsCB.grid(row=14, column=1)
        if self.rewrite_bugs:
            self.rewriteBugsCBVar.set(1)
        else:
            self.rewriteBugsCBVar.set(0)

        Label(self.settingsWindowFrame, text='', height=1).grid(row=15, column=0)
        Label(self.settingsWindowFrame, text='Rewrite fields :', height=1, width=35,
              font="Times 12").grid(row=16, column=0)
        self.rewriteBugsBox = Text(self.settingsWindowFrame, relief=SUNKEN, state='normal', width=30, height=1)
        self.rewriteBugsBox.delete("1.0", END)
        if self.rewrite_bugs_list:
            data = ','.join('{}'.format(item) for item in self.rewrite_bugs_list)
            self.rewriteBugsBox.insert("1.0", data)
        self.rewriteBugsBox.configure(state="disabled")
        self.rewriteBugsBox.grid(row=16, column=1)

        Label(self.settingsWindowFrame, text='', height=1).grid(row=17, column=0)
        Label(self.settingsWindowFrame, text='        rewrite by (field):', height=1, width=35,
              font="Times 12").grid(row=18, column=0)
        self.rewriteBugsByBox = Text(self.settingsWindowFrame, relief=SUNKEN, state='normal', width=30, height=1)
        self.rewriteBugsByBox.delete("1.0", END)
        if self.rewrite_bugs_by_list:
            data = ','.join('{}'.format(item) for item in self.rewrite_bugs_by_list)
            self.rewriteBugsByBox.insert("1.0", data)
        self.rewriteBugsByBox.configure(state="disabled")
        self.rewriteBugsByBox.grid(row=18, column=1)

        Label(self.settingsWindowFrame, text='', height=1).grid(row=19, column=0)
        Label(self.settingsWindowFrame, text='Standart Rules:', height=1, width=35,
              font="Times 12").grid(row=20, column=0)
        self.standartRulesBox = Text(self.settingsWindowFrame, relief=SUNKEN, state='normal', width=30, height=1)
        self.standartRulesBox.delete("1.0", END)
        self.standartRulesBox.insert("1.0", self.rules)
        self.standartRulesBox.grid(row=6, column=1)
        self.standartRulesBox.grid(row=20, column=1)
        Label(self.settingsWindowFrame, text='', height=2).grid(row=21, column=0)
        Button(self.settingsWindowFrame, text="OK", command=self.settingsWindow_close, width=30).grid(row=22, column=0, columnspan=2)


    def change_rewrite_bugs_var(self):
        if self.rewriteBugsCBVar.get() == 1:
            self.rewriteBugsBox.configure(state="normal")
            self.rewriteBugsByBox.configure(state="normal")
        else:
            self.rewriteBugsBox.configure(state="disabled")
            self.rewriteBugsByBox.configure(state="disabled")

    def settingsWindow_close(self):
        # if self.sensitiveCBVar.get() == 1:
        #     try:
        #         self.indents_space = int(self.sensitiveBox.get("1.0", END))
        #     except ValueError:
        #         return
        # else:
        #     self.indents_space = ""
        #
        # self.indentsSpaceBox.configure(state="normal")
        # self.indentsSpaceBox.delete(1.0, END)
        # self.indentsSpaceBox.insert(1.0, self.indents_space)
        # self.indentsSpaceBox.configure(state="disabled")
        self.afterWindow.destroy()


    def create_output_win(self):
        self.outputWindow = Toplevel(master=self, width=500, height=300)
        self.outputWindow.grab_set()
        self.outputWindow.title("Settings of output")
        self.outputWindow.resizable(width=False, height=False)

        self.outputWindowFrame = Frame(self.outputWindow)
        self.outputWindowFrame.place(x=10, y=10)

        Label(self.outputWindowFrame, text='', height=1).grid(row=0, column=0)
        Label(self.outputWindowFrame, text='Logs file:', height=1, width=35, font="Times 12").grid(row=1, column=0)
        self.logsFileBox = Text(self.outputWindowFrame, relief=SUNKEN, state='normal', width=30, height=1)
        self.logsFileBox.delete("1.0", END)
        self.logsFileBox.insert("1.0", self.logfile)
        self.logsFileBox.grid(row=1, column=1)

        Label(self.outputWindowFrame, text='', height=1).grid(row=2, column=0)
        Label(self.outputWindowFrame, text='Output logs to screen:', height=1, width=35, font="Times 12").grid(row=3,
                                                                                                               column=0)
        self.outputLogsCBVar = IntVar()
        self.outputLogsCB = Checkbutton(self.outputWindowFrame, variable=self.outputLogsCBVar)
        self.outputLogsCB.grid(row=3, column=1)
        if self.output_logs:
            self.outputLogsCBVar.set(1)
        else:
            self.outputLogsCBVar.set(0)

        Label(self.outputWindowFrame, text='', height=1).grid(row=4, column=0)
        Label(self.outputWindowFrame, text='Output bugs to screen:', height=1, width=35, font="Times 12").grid(row=5,
                                                                                                               column=0)
        self.outputBugsCBVar = IntVar()
        self.outputBugsCB = Checkbutton(self.outputWindowFrame, variable=self.outputBugsCBVar)
        self.outputBugsCB.grid(row=5, column=1)
        if self.output_bugs:
            self.outputBugsCBVar.set(1)
        else:
            self.outputBugsCBVar.set(0)

        Button(self.outputWindowFrame, text="OK", command=self.openWindow_close).grid(row=6, columnspan=2)

    def openWindow_close(self):
        if self.outputBugsCBVar.get() == 1:
            self.output_bugs = True
        else:
            self.output_bugs = False

        if self.outputLogsCBVar.get() == 1:
            self.output_logs = True
        else:
            self.output_logs = False

        if self.output_bugs or self.output_logs:
            self.output_to_screen = True
        else:
            self.output_to_screen = False

        self.indentsBox.configure(state="normal")
        self.indentsBox.delete(1.0, END)
        if self.output_to_screen:
            self.indentsBox.insert(1.0, "Yes")
        else:
            self.indentsBox.insert(1.0, "No")

        self.indentsBox.configure(state="disabled")

        self.logfile = self.logsFileBox.get("1.0", END)
        self.logfile = self.logfile[:-1]
        self.logFileBox.configure(state="normal")
        self.logFileBox.delete(1.0, END)
        self.logFileBox.insert(1.0, self.logfile)
        self.logFileBox.configure(state="disabled")

        self.outputWindow.destroy()

    def forget_st(self):
        self.master.withdraw()
        self.master.update()
        self.master.deiconify()

    def start_testing(self):
        self.logfile = self.logfile.replace("\n","")
        if self.cb_var[0].get() == 0:
            return

        proc = run_process()
        if not self.rewrite_bugs:
            self.current_id = get_mongo_param(help_fields={"program": self.codeName})
            if not self.current_id:
                self.current_id = 0
        else:
            self.current_id = 0

        with open(self.codeName) as file:
            data = file.read()
            tokenizer = Tokenizer(data, current_bug_id=self.current_id, logfile=self.logfile)

        self.current_tokens = get_mongo(mongo_address=self.mongo_address, mongo_db=self.mongo_db,
                                        mongo_collection=self.mongo_token_collection, logfile=self.logfile)
        self.current_tokens.sort(key=lambda x: x.prior)
        tokenizer.get_tokens(self.current_tokens)
        tokenizer.find_bad_tokens(self.bad_tokens_list)

        data = '\n'.join(
            'line: {}; column: {}: {} - {}'.format(str(item.line), str(item.column), item.name, item.obj) for item in
            tokenizer.lexems)
        if self.output_logs:
            self.infoBox.configure(state="normal")
            self.infoBox.insert("1.0", data)
            self.infoBox.configure(state="disabled")
        if self.logfile:
            with open(self.logfile, "a") as file:
                file.write(data)

        bugs = tokenizer.bugs

        if self.cb_var[1].get() == 0:
            bugs_to_output = []
            for bug in bugs:
                bugs_to_output.append(
                    "id: {}. bug: {}. line: {}, column: {}. Description: {}".format(bug.id, bug.object, bug.line,
                                                                                    bug.column, bug.description))

            if self.output_bugs:
                for bug in bugs_to_output:
                    self.bugBox.insert(END, bug)
            return

        self.current_rules = get_mongo(mongo_address=self.mongo_address, mongo_db=self.mongo_db, mongo_collection=self.mongo_exprs_collection,
                                       logfile=self.logfile)
        indents = False
        if self.indents_space > 0:
            indents = True
        parser = Parser(tokenizer.lexems, self.current_rules, end_statement[self.language], indents,
                        space_in_tab=self.indents_space, language=self.language, current_bug_id=tokenizer.current_bug_id)
        parser.get_statements([], [], {}, {}, 0)

        data = '\n'.join(
            'Object: {} on expression: {} on pos {}. Roles: {}. With inner level: {}'.format(item.lexem.obj,
                                                                                             str(item.expr_line),
                                                                                             str(item.expr_pos),
                                                                                             item.role, item.place) for
            item in parser.exprs)
        if self.output_logs:
            self.infoBox.configure(state="normal")
            self.infoBox.insert("1.0", data)
            self.infoBox.configure(state="disabled")
        if self.logfile:
            with open(self.logfile, "a") as file:
                file.write(data)
        for item in parser.bugs:
            bugs.append(item)

        if self.cb_var[2].get() == 0:
            bugs_to_output = []
            for bug in parser.bugs:
                bugs_to_output.append(
                    "id: {}. bug: {}. line: {}, column: {}. Description: {}".format(bug.id, bug.object, bug.line,
                                                                                    bug.column, bug.description))

            if self.output_bugs:
                for bug in bugs_to_output:
                    self.bugBox.insert(END, bug)
            return

        parser.append_parents()
        df = df_maker(parser.exprs, constructs=parser.constructs, logfile=self.logfile)
        data = '\n'.join(
            'Object: {}, mean: {}. Parent: {}. Allow expressions: {}'.format(item['expr'].lexem.obj, item['mean'], item['parent'], item['allow']) for item in df)
        if self.output_logs:
            self.infoBox.configure(state="normal")
            self.infoBox.insert("1.0", data)
            self.infoBox.configure(state="disabled")
        if self.logfile:
            with open(self.logfile, "a") as file:
                file.write(data)
        du = du_maker(parser.exprs, df=df, logfile=self.logfile)
        data = '\n'.join(
            'Object: {}, mean: {}'.format(item['expr'].lexem.obj, item['mean']) for item in du)
        if self.output_logs:
            self.infoBox.configure(state="normal")
            self.infoBox.insert("1.0", data)
            self.infoBox.configure(state="disabled")
        if self.logfile:
            with open(self.logfile, "a") as file:
                file.write(data)
        new_bugs = du_testing(parser.exprs, df=df, du=du, current_id=parser.current_bug_id, logfile=self.logfile)
        for item in new_bugs:
            bugs.append(item)

        current_id = item.id

        if self.cb_var[3].get() == 0:
            bugs_to_output = []
            for bug in new_bugs:
                bugs_to_output.append(
                    "id: {}. bug: {}. line: {}, column: {}. Description: {}".format(bug.id, bug.object, bug.line,
                                                                                    bug.column, bug.description))

            if self.output_bugs:
                for bug in bugs_to_output:
                    self.bugBox.insert(END, bug)
            return

        new_bugs = style_testing(exprs=parser.exprs, df=df, du=du, rule=self.rules, current_id=current_id, language=self.language, indents=indents, logfile=self.logfile)
        for item in new_bugs:
            bugs.append(item)

        bugs_to_output = []
        for bug in new_bugs:
            bugs_to_output.append("id: {}. bug: {}. line: {}, column: {}. Description: {}".format(bug.id, bug.object, bug.line, bug.column, bug.description))

        if self.output_bugs:
            for bug in bugs_to_output:
                self.bugBox.insert(END, bug)

        for bug in bugs:
            bug.author = self.author
            bug.program = self.codeName
            bug.version = self.version
            print(bug.object, bug.line, bug.column, bug.description)

        set_mongo(self.mongo_address, mongo_db=self.mongo_db_bt, mongo_collection=self.mongo_bugs_collection, collection_to_read=bugs, rewrite=self.rewrite_bugs,
                  check_on_rewrite=self.rewrite_bugs_list, hint_fields=self.rewrite_bugs_by_list, logfile=self.logfile)

        if proc:
            subprocess.Popen.kill(proc)

if __name__ == '__main__':
    MainApp().mainloop()

