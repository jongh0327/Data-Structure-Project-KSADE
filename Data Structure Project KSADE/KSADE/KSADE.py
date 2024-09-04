#-*-coding:utf-8-*-

from Tkinter import*
import csv_to_text
import KSADE_Optimal 
import KSADE_Quick
from time import*

window=Tk()
window.title("KSADE")
####################################################
Image=Frame(window)
main=Frame(window)
convertCSV=Frame(window,bd=30)
match=Frame(window,bd=30)

main_image=PhotoImage(file="KSADE.gif")
image1=Label(Image,image=main_image)
image1.grid(row=0,columnspan=2) 

main_CSV_b=Button(main,text="Transfer .csv to .txt",command=lambda:transfer(main,convertCSV),font=("Courier",18))
main_CSV_b.grid(row=1,columnspan=2)

main_label=Label(main,text="",font=("Courier",18))
main_label.grid(row=2,columnspan=2)

main_match_b=Button(main,text="Find Match",command=lambda: transfer(main,match),font=("Courier",18))
main_match_b.grid(row=3,columnspan=2)

main_label2=Label(main,text="",font=("Courier",18))
main_label2.grid(row=4,columnspan=2)

main_label3=Label(main,text='Made By \n16-073 이수성 & 16-081 이종현',font=("Courier",15))
main_label3.grid(row=5,columnspan=2)
####################################################
convertCSV_text=Label(convertCSV,text="Input name of CSV data file.",font=("Courier",17))
convertCSV_text.grid(row=0,columnspan=2)

csv_input=StringVar(value="NewCollectionName.csv")
csv_Entry=Entry(convertCSV,textvariable=csv_input,font=("Courier",20),width=30)
csv_Entry.grid(row=1,column=0)

convertCSV_b=Button(convertCSV,text="Convert csv to .txt",command=lambda: csv_text(csv_input.get()),font=("Courier",13))
convertCSV_b.grid(row=1,column=1)

convertCSV_notice=Label(convertCSV,text="",font=("Courier",17))
convertCSV_notice.grid(row=2,columnspan=2)

CSV_back_b=Button(convertCSV,text="Back",command=lambda: transfer(convertCSV,main),font=("Courier",18))
CSV_back_b.grid(row=3,columnspan=2)
####################################################
match_text=Label(match,text="Input name of .txt file to find Trade Matchings\nex)textFile.txt",font=("Courier",17))
match_text.grid(row=0,columnspan=2)

match_input=StringVar(value="Trade_test.txt")
match_Entry=Entry(match,textvariable=match_input,font=("Courier",17),width=30)
match_Entry.grid(row=1,columnspan=2)

quick_b=Button(match,text="Quick Match",command=lambda: quickSearch(match_input.get()),font=("Courier",18))
quick_b.grid(row=2,columnspan=2)

optimal_EntryText=Label(match, text="\nThreshold(3~7)\nSmall : Fast, Incorrect\nBig : Slooow, Precise",font=("Courier",12))
optimal_EntryText.grid(row=3,column=0)

threshold=IntVar(value="4")
optimal_Entry=Entry(match,textvariable=threshold,font=("Courier",17),width=2)
optimal_Entry.grid(row=3,column=1,sticky="W")

optimal_b=Button(match,text="Optimal Match",command=lambda: optimalSearch(match_input.get(),threshold.get()),font=("Courier",18))
optimal_b.grid(row=4,columnspan=2)

match_back_b=Button(match,text="back",command=lambda: transfer(match,main),font=("Courier",18))
match_back_b.grid(row=5,columnspan=2)

#match_notice=Label(match,text="",font=("Courier",17))
#match_notice.grid(row=6,columnspan=2)

match_result=Label(match,text="",font=("Courier",12))
match_result.grid(row=7,columnspan=2)
####################################################
Image.pack()
main.pack()
####################################################
def transfer(a,b):
    a.pack_forget()
    b.pack()
    
    convertCSV_notice.config(text="")
    #match_notice.config(text="")
    match_result.config(text="")

def csv_text(csvInput):
    a=csv_to_text.main(csvInput)          #실제 코드
    if a=="Error":
        convertCSV_notice.config(text="Wrong File Name. Please Check Again.")
    else:
        convertCSV_notice.config(text="Convert Successful!!")
    #convertCSV.pack_forget()
    #match.pack()

def quickSearch(text_input):
    #match_notice.config(text="")
    match_result.config(text="")
    a=KSADE_Quick.main(text_input)
    if a=="Error":
        match_result.config(text="Wrong File Name. Please Check Again.")
    else:
        result="--------------------------Result--------------------------\n"
        for i in a:
            result+=str(i)[1:-1]+"\n"
        match_result.config(text=result)

def optimalSearch(text_input,threshold):
    #match_notice.config(text="")
    match_result.config(text="")
    start=time()
    a=KSADE_Optimal.main(text_input,threshold)
    end=time()
    if a=="Error":
        match_result.config(text="Wrong File Name. Please Check Again.")
    elif a==None:
        result="--------------------------Result--------------------------\n"    
        result+="No Such Match\nTry increasing the Threshold"
        match_result.config(text=result)
    else:
        result="--------------------------Result--------------------------\n"    
        for i in a:
            for j in i:
                result+=str([j[0],j[1]+1,j[2]+1])
            result+="\n"
        result+="\nTime Elapsed = "
        result+=str(end-start)
        match_result.config(text=result)


mainloop()