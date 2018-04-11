from tkinter import *
from tkinter.filedialog import askopenfilenames
from loc import Loc
from locm import Locm
from cbo import Cbo
from dit import Dit
from noc import Noc
from wmc import Wmc
class Metrics:
    def __init__(self,master):
        self.label1=Label(master,text="CS693 Project by Aaron Feng",anchor='center',font=("Courier",20))
        self.label1.grid(row=0,column=0,columnspan=8)
        Button(master,text="Select Files",command=self.selectFiles).grid(row=1,column=0,columnspan=8)

        self.chkLoc1=IntVar()
        self.checkButtonLoc1=Checkbutton(master,text='Comments',variable=self.chkLoc1)
        self.checkButtonLoc1.grid(row=2,column=0)
        self.chkLoc2 = IntVar()
        self.checkButtonLoc2 = Checkbutton(master, text='Empty Lines',variable=self.chkLoc2)
        self.checkButtonLoc2.grid(row=3, column=0)
        self.chkLoc3 = IntVar()
        self.checkButtonLoc3 = Checkbutton(master, text='Import Statements',variable=self.chkLoc3)
        self.checkButtonLoc3.grid(row=4, column=0)
        Button(master,text="LOC",command=self.loc).grid(row=2,column=1,rowspan=3)

        Button(master,text="LOCM",command=self.locm).grid(row=2,column=2,rowspan=3)

        Button(master, text="CBO", command=self.cbo).grid(row=2, column=3,rowspan=3)

        self.chkDit1=IntVar()
        self.checkButtonDit1 = Checkbutton(master, text='object Class',variable=self.chkDit1)
        self.checkButtonDit1.grid(row=2, column=4,rowspan=3)
        Button(master, text="DIT", command=self.dit).grid(row=2, column=5,rowspan=3)

        Button(master, text="NOC", command=self.noc).grid(row=2, column=6,rowspan=3)

        self.chkWmc1=IntVar()
        self.checkButtonWmc1 = Checkbutton(master, text='Constructor',variable=self.chkWmc1)
        self.checkButtonWmc1.grid(row=2, column=7, rowspan=3)
        Button(master, text="WMC", command=self.wmc).grid(row=2, column=8,rowspan=3)
        self.label2=Label(master,text="Display result",anchor='center',font=("Courier",10))
        self.label2.grid(row=5,column=0,columnspan=8)
        self.filenames=''
        col_count, row_count = master.grid_size()

        for col in range(col_count):
            master.grid_columnconfigure(col, minsize=80)

    def selectFiles(self):
            self.filenames=askopenfilenames()
            self.label2['text']=''
            for name in self.filenames:
                self.label2['text'] += name +'\n'

    def loc(self):
        if(len(self.filenames)==0):
            self.filenames = askopenfilenames()
        lineCount = 0
        blankLineCount = 0
        commentLineCount = 0
        importLineCount = 0
        final=0
        reportStr='The final result of LOC '
        for name in self.filenames:
            result=Loc(name)
            lineCount+=result.lineCount
            blankLineCount+=result.blankLineCount
            commentLineCount+=result.commentLineCount
            importLineCount+=result.importLineCount
            final = lineCount - blankLineCount - commentLineCount - importLineCount
        if(self.chkLoc1.get()):
            final+=commentLineCount
            reportStr+='with comment lines, '
        if(self.chkLoc2.get()):
            final+=blankLineCount
            reportStr+='empty lines, '
        if(self.chkLoc3.get()):
            final+=importLineCount
            reportStr+='import lines, '
        self.label2['text'] = reportStr + "is " +str(final)

    def locm(self):
        if (len(self.filenames) == 0):
            self.filenames = askopenfilenames()
        reportStr = 'The final result of LOCM is: \n '
        for name in self.filenames:
            result=Locm(name)
            reportStr+=result.result
        self.label2['text'] = reportStr

    def cbo(self):
        if (len(self.filenames) == 0):
            self.filenames = askopenfilenames()
        reportStr = 'The final result of CBO is: \n '
        for name in self.filenames:
            result=Cbo(name)
            reportStr+=result.resultStr
        self.label2['text'] = reportStr

    def dit(self):
        if (len(self.filenames) == 0):
            self.filenames = askopenfilenames()
        reportStr = 'The final result of DIT is: \n '
        for name in self.filenames:
            result=Dit(name,self.chkDit1.get())
            reportStr+=result.reportStr
        self.label2['text'] = reportStr

    def noc(self):
        if (len(self.filenames) == 0):
            self.filenames = askopenfilenames()
        reportStr = 'The final result of NOC is: \n '
        for name in self.filenames:
            result = Noc(name)
            reportStr += result.reportStr
        self.label2['text'] = reportStr

    def wmc(self):
        if (len(self.filenames) == 0):
            self.filenames = askopenfilenames()
        reportStr = 'The final result of WMC is: \n '
        for name in self.filenames:
            result = Wmc(name, self.chkWmc1.get())
            reportStr += result.reportStr
        self.label2['text'] = reportStr
def main():
    root=Tk()
    root.title('Metrics')
    app=Metrics(root)
    root.mainloop()

if __name__=='__main__':
    main()