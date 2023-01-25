#GUI Graphics
#importing all the required modules
import requests #for sending sms message to the targeted mobile number
import tkinter #the most important module for creating gui
from tkinter import *
from tkinter import ttk #ttk is the main function for creating and running the root variable
from tkinter import messagebox #for displaying the message box as a seperate terminal window
from tkinter import scrolledtext
import random #for generating a random bill number
import datetime #for printing the current date and time on the bill
from tkinter import filedialog

#For developing these kind of interfaces first develop the user interface and then take care of the backend functions
#--------------------------------------BACKEND FUNCTIONS-----------------------------------
#function for intilizing the cost of individual items and for calculating cost and add taxes to it and thus finally generating the bill
def total_bills():
    #intilize the cost of individual drinks
    lassi_price=50
    cofee_price=20
    tea_price=10
    juice_price=30
    shakes_price=50
    shikanji_price=15
    redbull_price=150
    milk_price=10
    #intilize the cost of each food item
    roti_price=5
    dalmakhani_price=120
    mutterpanner_price=150
    paratha_price=40
    mixveg_price=70
    omelete_price=20
    vegbiriyani_price=120
    rice_price=50
    #getting the number of quantites of drinks
    lassi_q=lassi_qty.get()
    cofee_q=cofee_qty.get()
    tea_q=tea_qty.get()
    juice_q=juice_qty.get()
    shakes_q=shakes_qty.get()
    shikanji_q=shikanji_qty.get()
    milk_q=milk_qty.get()
    redbull_q=redbull_qty.get()
    #getting the number of quantites of food items
    roti_q=roti_qty.get()
    dalmakhani_q=dalmakhani_qty.get()
    mutterpanner_q=mutterpanner_qty.get()
    paratha_q=paratha_qty.get()
    mixveg_q=mixveg_qty.get()
    omelete_q=omelete_qty.get()
    vegbiriyani_q=vegbiriyani_qty.get()
    rice_q=rice_qty.get()
    #validating if the correct number of quantites are entered
    if lassi_var.get()==0:
        lassi_q=0
    elif lassi_var.get()==1 and lassi_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        lassi_q=0

    if cofee_var.get()==0:
        cofee_q=0
    elif cofee_var.get()==1 and cofee_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        cofee_q=0

    if tea_var.get()==0:
        tea_q=0
    elif tea_var.get()==1 and tea_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        tea_q=0

    if juice_var.get()==0:
        juice_q=0
    elif juice_var.get()==1 and juice_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        juice_q=0        

    if shakes_var.get()==0:
        shakes_q=0
    elif shakes_var.get()==1 and shakes_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        shakes_q=0    

    if shikanji_var.get()==0:
        shikanji_q=0
    elif shikanji_var.get()==1 and shikanji_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        shikanji_q=0  

    if redbull_var.get()==0:
        redbull_q=0
    elif redbull_var.get()==1 and redbull_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        redbull_q=0      

    if milk_var.get()==0:
        milk_q=0
    elif milk_var.get()==1 and milk_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        milk_q=0    

    #validating for the food items
    if roti_var.get()==0:
        roti_q=0
    elif roti_var.get()==1 and roti_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        roti_q=0    

    if dalmakhani_var.get()==0:
        dalmakhani_q=0
    elif dalmakhani_var.get()==1 and dalmakhani_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        dalmakhani_q=0    

    if mutterpanner_var.get()==0:
        mutterpanner_q=0
    elif mutterpanner_var.get()==1 and mutterpanner_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        mutterpanner_q=0    

    if paratha_var.get()==0:
        paratha_q=0
    elif paratha_var.get()==1 and paratha_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        paratha_q=0    

    if mixveg_var.get()==0:
        mixveg_q=0
    elif mixveg_var.get()==1 and mixveg_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        mixveg_q=0    

    if omelete_var.get()==0:
        omelete_q=0
    elif omelete_var.get()==1 and omelete_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        omelete_q=0  

    if vegbiriyani_var.get()==0:
        vegbiriyani_q=0
    elif vegbiriyani_var.get()==1 and vegbiriyani_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        vegbiriyani_q=0  

    if rice_var.get()==0:
        rice_q=0
    elif rice_var.get()==1 and rice_qty.get()==" ":
        messagebox.showerror("error","Please enter quantity")
        rice_q=0  

    #calculating the drinks cost for each drink
    total_lassi_price=lassi_price*int(lassi_q)
    total_cofee_price=cofee_price*int(cofee_q)
    total_tea_price=tea_price*int(tea_q)
    total_juice_price=juice_price*int(juice_q)
    total_shakes_price=shakes_price*int(shakes_q)
    total_shikanji_price=shikanji_price*int(shikanji_q)
    total_milk_price=milk_price*int(milk_q)
    total_redbull_price=redbull_price*int(redbull_q)

    total_drinks_cost=total_lassi_price+total_cofee_price+total_tea_price+total_juice_price+total_shakes_price+total_shikanji_price+total_redbull_price+total_milk_price

    if drinks_cost.get()!=" ":
        drinks_cost.delete(0,"end")
        drinks_cost.insert("end",total_drinks_cost)
    else:
        drinks_cost.insert("end",total_drinks_cost)    

    #calculating individual cost of each food item
    total_roti_price=roti_price*int(roti_q)
    total_dalmakhani_price=dalmakhani_price*int(dalmakhani_q)
    total_mutterpanner_price=mutterpanner_price*int(mutterpanner_q)
    total_mixveg_price=mixveg_price*int(mixveg_q)
    total_vegbiriyani_price=vegbiriyani_price*int(vegbiriyani_q)
    total_omelete_price=omelete_price*int(omelete_q)
    total_paratha_price=paratha_price*int(paratha_q)
    total_rice_price=rice_price*int(rice_q)

    total_food_cost=total_dalmakhani_price+total_mixveg_price+total_mutterpanner_price+total_omelete_price+total_paratha_price+total_roti_price+total_rice_price+total_vegbiriyani_price
   
    if foods_cost.get()!=" ":
        foods_cost.delete(0,"end")
        foods_cost.insert("end",total_food_cost)
    else:
        foods_cost.insert("end",total_food_cost) 

    #for calculating the service tax on orders
    if service_charge_cost.get()!=" ":
        service_charge_cost.delete(0,"end")
        service_charge_cost.insert(0,"10")
    else:
        service_charge_cost.insert(0,"10")      

    fc=int(foods_cost.get())
    dc=int(drinks_cost.get())
    
    total_paid_tax=fc+dc
    total_paid_tax=total_paid_tax*8/100

    if paid_tax_cost.get()!=" ":
        paid_tax_cost.delete(0,"end")
        paid_tax_cost.insert(0,total_paid_tax)
    else:
        paid_tax_cost.insert(0,total_paid_tax)
    
    total_sub_cost=fc+dc+int(service_charge_cost.get())

    if sub_total_cost.get()!=" ":
        sub_total_cost.delete(0,"end")
        sub_total_cost.insert(0,total_sub_cost)
    else:
        sub_total_cost.insert(0,total_sub_cost)

    if total_cost_cost.get()!=" ":
        total_cost_cost.delete(0,"end")
        total_cost_cost.insert(0,float(total_sub_cost+total_paid_tax))
    else:
        total_cost_cost.insert(0,float(total_sub_cost+total_paid_tax))

    #---------------------TOTAL BILL RECEIPT------------------------------------------------
    today=datetime.date.today()
    if bill_details.get(1.0,"end")!=" ":
        bill_details.delete(1.0,"end")
        bill_details.insert(1.0,f"Billno-{random.randint(100,1000)}\t{today}============ITEMS(q)\t\tAmount==========\n{'Lassi('+str(lassi_q)+')'+'     '+str(int(lassi_q)*lassi_price)+'     'if lassi_var.get()==1 else''} {'Cofee('+str(cofee_q)+')'+'     '+str(int(cofee_q)*cofee_price)+'     'if cofee_var.get()==1 else''}  {'tea('+str(tea_q)+')'+'     '+str(int(tea_q)*tea_price)+'     'if tea_var.get()==1 else''} {'Juice('+str(juice_q)+')'+'     '+str(int(juice_q)*juice_price)+'     'if juice_var.get()==1 else''}  {'Shakes('+str(shakes_q)+')'+'     '+str(int(shakes_q)*shakes_price)+'     'if shakes_var.get()==1 else''}{'Milk('+str(milk_q)+')'+'     '+str(int(milk_q)*milk_price)+'     'if milk_var.get()==1 else''} {'Shikanji('+str(shikanji_q)+')'+'     '+str(int(shikanji_q)*shikanji_price)+'     'if shikanji_var.get()==1 else''} {'Redbull('+str(redbull_q)+')'+'     '+str(int(redbull_q)*redbull_price)+'     'if redbull_var.get()==1 else''}{'Roti('+str(roti_q)+')'+'     '+str(int(roti_q)*roti_price)+'     'if roti_var.get()==1 else''}{'Dalmakhani('+str(dalmakhani_q)+')'+'     '+str(int(dalmakhani_q)*dalmakhani_price)+'     'if dalmakhani_var.get()==1 else''} {'Mutterpanner('+str(mutterpanner_q)+')'+'     '+str(int(mutterpanner_q)*mutterpanner_price)+'     'if mutterpanner_var.get()==1 else''} {'Paratha('+str(paratha_q)+')'+'     '+str(int(paratha_q)*paratha_price)+'     'if paratha_var.get()==1 else''} {'Mixveg('+str(mixveg_q)+')'+'     '+str(int(mixveg_q)*mixveg_price)+'     'if mixveg_var.get()==1 else''} {'Omelete('+str(omelete_q)+')'+'     '+str(int(omelete_q)*omelete_price)+'     'if omelete_var.get()==1 else''} {'Vegbiriyani('+str(vegbiriyani_q)+')'+'     '+str(int(vegbiriyani_q)*vegbiriyani_price)+'     'if vegbiriyani_var.get()==1 else''} {'Rice('+str(rice_q)+')'+'     '+str(int(rice_q)*rice_price)+'     'if rice_var.get()==1 else''}")  

    #----------------------------------------total button ended------------------------------

#-----------------------FOR SAVE BUTTON------------------------------------------------------
def save():
    root.filename=filedialog.asksaveasfile(mode="w",defaultextension='.txt')
    if root.filename is None:
        return
    file_save=str(bill_details.get(1.0,END))
    root.filename.write(file_save)
    root.filename.close()
#-------------------------end for save button-----------------------------------------------------

#----------------DRINKS CHECK BUTTON VALIDATION--------------------------------------------
#for making green color when we select the check button for a particular food item or drink
#FOR LASSI
def lassi_chk():
    if lassi_var.get()==1:
        lassi_qty['state']="normal"
        lassi_qty['bg']="#00ff00"
        lassi_qty['fg']="white"
    else:
        lassi_qty['state']="disabled"   
#For coffee
def cofee_chk():
    if cofee_var.get()==1:
        cofee_qty['state']="normal"
        cofee_qty['bg']="#00ff00"
        cofee_qty['fg']="white"
    else:
        cofee_qty['state']="disabled"
#for tea
def tea_chk():
    if tea_var.get()==1:
        tea_qty['state']="normal"
        tea_qty['bg']="#00ff00"
        tea_qty['fg']="white"
    else:
        tea_qty['state']="disabled"
#for juice
def juice_chk():
    if juice_var.get()==1:
        juice_qty['state']="normal"
        juice_qty['bg']="#00ff00"
        juice_qty['fg']="white"
    else:
        juice_qty['state']="disabled"       
#for shakes
def shakes_chk():
    if shakes_var.get()==1:
        shakes_qty['state']="normal"
        shakes_qty['bg']="#00ff00"
        shakes_qty['fg']="white"
    else:
        shakes_qty['state']="disabled"
#for milk
def milk_chk():
    if milk_var.get()==1:
        milk_qty['state']="normal"
        milk_qty['bg']="#00ff00"
        milk_qty['fg']="white"
    else:
        milk_qty['state']="disabled"                     
#for shikanji
def shikanji_chk():
    if shikanji_var.get()==1:
        shikanji_qty['state']="normal"
        shikanji_qty['bg']="#00ff00"
        shikanji_qty['fg']="white"
    else:
        shikanji_qty['state']="disabled"           
#for redbull
def redbull_chk():
    if redbull_var.get()==1:
        redbull_qty['state']="normal"
        redbull_qty['bg']="#00ff00"
        redbull_qty['fg']="white"
    else:
        redbull_qty['state']="disabled"                           
#for food items check buttons
#for roti
def roti_chk():
    if roti_var.get()==1:
        roti_qty['state']="normal"
        roti_qty['bg']="#00ff00"
        roti_qty['fg']="white"
    else:
        roti_qty['state']="disabled" 
#for dalmakni            
def dalmakhani_chk():
    if dalmakhani_var.get()==1:
        dalmakhani_qty['state']="normal"
        dalmakhani_qty['bg']="#00ff00"
        dalmakhani_qty['fg']="white"
    else:
        dalmakhani_qty['state']="disabled"
#for mutterpanner        
def mutterpanner_chk():
    if mutterpanner_var.get()==1:
        mutterpanner_qty['state']="normal"
        mutterpanner_qty['bg']="#00ff00"
        mutterpanner_qty['fg']="white"
    else:
        mutterpanner_qty['state']="disabled"
#for paratha
def paratha_chk():
    if paratha_var.get()==1:
        paratha_qty['state']="normal"
        paratha_qty['bg']="#00ff00"
        paratha_qty['fg']="white"
    else:
        paratha_qty['state']="disabled"
#for mixveg
def mixveg_chk():
    if mixveg_var.get()==1:
        mixveg_qty['state']="normal"
        mixveg_qty['bg']="#00ff00"
        mixveg_qty['fg']="white"
    else:
        mixveg_qty['state']="disabled"               
#for omelete
def omelete_chk():
    if omelete_var.get()==1:
        omelete_qty['state']="normal"
        omelete_qty['bg']="#00ff00"
        omelete_qty['fg']="white"
    else:
        omelete_qty['state']="disabled"    
#for vegbiriyani
def vegbiriyani_chk():
    if vegbiriyani_var.get()==1:
        vegbiriyani_qty['state']="normal"
        vegbiriyani_qty['bg']="#00ff00"
        vegbiriyani_qty['fg']="white"
    else:
        vegbiriyani_qty['state']="disabled"  
#for rice
def rice_chk():
    if rice_var.get()==1:
        rice_qty['state']="normal"
        rice_qty['bg']="#00ff00"
        rice_qty['fg']="white"
    else:
        rice_qty['state']="disabled"  
#-------------end for check buttons-----------------

#------------------CODE FOR CALCULATOR-------------------------
def nine():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","9")
    else:
        result.insert("end","9")
def eight():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","8")
    else:
        result.insert("end","8")
def seven():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","7")
    else:
        result.insert("end","7")
def six():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","6")
    else:
        result.insert("end","6")
def five():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","5")
    else:
        result.insert("end","5")
def four():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","4")
    else:
        result.insert("end","4")
def three():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","3")
    else:
        result.insert("end","3")                
def two():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","2")
    else:
        result.insert("end","2")        
def one():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","1")
    else:
        result.insert("end","1")
def zero():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","0")
    else:
        result.insert("end","0")      
def plus():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","+")
    else:
        result.insert("end","+")       
def minus():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","-")
    else:
        result.insert("end","-")         
def multiply():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","*")
    else:
        result.insert("end","*")     
def divide():
    if 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
        result.insert("end","/")
    else:
        result.insert("end","/")            
def equal():
    if result.get()=="":
        result.insert("end","error")
    elif result.get()[0]=="0" or result.get()[0]=="+" or result.get()[0]=="-" or result.get()[0]=="*" or result.get()[0]=="/":
        result.delete(0,"end")         
        result.insert("end","error")
    elif 'error' in result.get() or'=' in result.get():
        result.delete(0,"end")
    else:
        res=result.get()
        res=eval(res)
        result.insert("end","=")
        result.insert("end",res)
def clear():
    result.delete(0,"end")
#---------------end of calculator code------------------------
#---------------code for send button--------------------------
def send():
    root=tkinter.Tk()
    root.geometry("600x800")
    root.bg("white")


    frame4=Frame(root,width=300,height=60,relief=RIDGE,borderwidth=5,bg="#248aa2",highlightbackground="white",highlightcolor="white",highlightthickness=2)
    frame4.place(x=0,y=0)

    l2=Label(frame4,text="Send Bill",font=("roboto",22,'bold'),bg="#248aa2",fg="ffffff")
    l2.place(x=85,y=1)
    
    frame5=Frame(root,width=300,height=340,relief=RIDGE,borderwidth=5,bg="#248aa2",highlightbackground="white",highlightcolor="white",highlightthickness=2) 
    frame5.place(x=0,y=55)

    innerframe5=Frame(frame5,width=285,height=325,relief=RIDGE,borderwidth=5,bg="#248aa2",highlightbackground="white",highlightcolor="white",highlightthickness=2)    
    innerframe5.place(x=0,y=0)
     
    l3=LabelFrame(innerframe5,text="Send Bill through SMS",width=270,height=310,borderwidth=5,bg="white")
    l3.place(x=2,y=2)
 
    l4=Label(innerframe5,text="Phone Number",font=("verdana",10,'bold'))
    l4.place(x=40,y=40)

    number=Entry(innerframe5,width=30,borderwidth=2)
    number.place(x=40,y=70)

    l5=Label(innerframe5,text="Bill Details",font=("verdana",10,'bold'))
    l5.place(x=40,y=100)

    b_detail=scrolledtext.ScrolledText(innerframe5,width=23,height=7,relief=RIDGE,borderwidth=2)
    b_detail.place(x=40,y=130)

    b_detail.insert(1.0,bill_details.get(1.0,END))
    #code to send the bill using phone number
    def send_bill():
        ph_number=number.get()
        messages=b_detail.get("1.0","end-1c")

        if ph_number=="":
            messagebox.showerror("Error","please fill the phone number")
        elif messages=="":
            messagebox.showerror("Error","please fill the bill details")
        else:
            url="https://www.fast2sms.com/dev/bulk"
            api="3HOoNASIfJx6VZRDwhy1vmp7XQGPUektFWil9K2zMnqT40Y8brcgdFqvae5Ij7Kb2OfPBZ0CtsHQMTYw"
            querystring={"authorization":api,"sender_id":"FSTSMS","message":messages,"language":'english',"route":'p',"numbers":ph_number}
            headers={
                "cache control":"no cache"
            }
            requests.request("GET",url,headers=headers,params=querystring)

            messagebox.showinfo("SMS SENT","BILL HAS BEEN SENT TO YOUR NUMBER")
    send_msg=Button(innerframe5,text="SEND",relief=RAISED,borderwidth=2,font=("impact",8,'bold'),bg="#248aa2",fg="white",padx=20,command=send_bill)
    send_msg.place(x=100,y=255)

    root.mainloop()
#-------------------------------------------END FOR SEND BUTTON CODE-----------------------
#-------------------------------------------CODE FOR EXIT BUTTON--------------------------
def exit():
    message=messagebox.askquestion("Notepad","Do you want to exit the application")
    if message=="yes":
        root.destroy()
    else:
        "return"
#----------------------------------------------END FOR EXIT BUTTON CODE-------------------

#--------------------------------------CODE FOR CLEAR BUTTON-------------------------------

def cleared_bill():
    #----FOR DRINKS----
    lassi_qty.delete(0,'end')
    lassi.deselect()
    lassi_qty["state"]="disabled"

    cofee_qty.delete(0,'end')
    cofee.deselect()
    cofee_qty["state"]="disabled"

    tea_qty.delete(0,'end')
    tea.deselect()
    tea_qty["state"]="disabled"

    juice_qty.delete(0,'end')
    juice.deselect()
    juice_qty["state"]="disabled"

    shakes_qty.delete(0,'end')
    shakes.deselect()
    shakes_qty["state"]="disabled"

    milk_qty.delete(0,'end')
    milk.deselect()
    milk_qty["state"]="disabled"

    shikanji_qty.delete(0,'end')
    shikanji.deselect()
    shikanji_qty["state"]="disabled"

    redbull_qty.delete(0,'end')
    redbull.deselect()
    redbull_qty["state"]="disabled"

    #---FOR FOOD ITEMS---
    roti_qty.delete(0,'end')
    roti.deselect()
    roti_qty["state"]="disabled"

    dalmakhani_qty.delete(0,'end')
    dalmakhani.deselect()
    dalmakhani_qty["state"]="disabled"

    mutterpanner_qty.delete(0,'end')
    mutterpanner.deselect()
    mutterpanner_qty["state"]="disabled"

    paratha_qty.delete(0,'end')
    paratha.deselect()
    paratha_qty["state"]="disabled"

    mixveg_qty.delete(0,'end')
    mixveg.deselect()
    mixveg_qty["state"]="disabled"

    omelete_qty.delete(0,'end')
    omelete.deselect()
    omelete_qty["state"]="disabled"

    vegbiriyani_qty.delete(0,'end')
    vegbiriyani.deselect()
    vegbiriyani_qty["state"]="disabled"

    rice_qty.delete(0,'end')
    rice.deselect()
    rice_qty["state"]="disabled"

    #-----------TOTAL COST------
    drinks_cost.delete(0,'end')
    foods_cost.delete(0,"end")
    service_charge_cost.delete(0,'end')
    paid_tax_cost.delete(0,'end')
    sub_total_cost.delete(0,'end')
    total_cost_cost.delete(0,'end')

    #-------BILL DETAILS---------
    bill_details.delete(0,'end')
    #--------------------END--------------------------------------------------



#---------------------------------------THE GUI INTERFACE STARTED---------------------------
#creating the root variable for main GUI
root=tkinter.Tk()
root.title("RESTAURANT_BILL_GENERATOR_GUI")
root.maxsize(650,390)
root.minsize(650,390)
root.geometry("1010x530")

#creating the frames
frame=Frame(root,width=650,height=70,relief=RIDGE,borderwidth=5,bg="blue")
frame.place(x=0,y=0)

#creating the label
l1=Label(frame,text="Hotel Management System",font=("roboto",30,'bold'),bg="orange",fg="white")#instead of hotel management system we can write the name of the respective hotel.
l1.place(x=10,y=6)

#creating another frame
frame1=Frame(root,width=450,height=230,relief=RIDGE,borderwidth=5,bg="white")
frame1.place(x=0,y=70)
innerframe1=Frame(frame1,width=150,height=220,relief=RIDGE,borderwidth=5,bg="white")
innerframe1.place(x=0,y=0)
#---------------------------------------------------------------------------------------------------------
#creating label
drinks=LabelFrame(innerframe1,text="Drinks",width=135,height=205,borderwidth=5,bg="white")
drinks.place(x=2,y=2)

#creating check buttons as well as entries for drinks

#for lassi
lassi_var=IntVar()
lassi=Checkbutton(drinks,text="Lassi",font=("verdana",8,'bold'),variable=lassi_var,onvalue=1,offvalue=0,command=lassi_chk)
lassi.place(x=2,y=2)
lassi_qty=Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state='disabled')
lassi_qty.place(x=74,y=2)

#for coffee
cofee_var=IntVar()
cofee=Checkbutton(drinks,text="Cofee",font=("verdana",8,'bold'),variable=cofee_var,onvalue=1,offvalue=1,command=cofee_chk)
cofee.place(x=2,y=22)
cofee_qty=Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state='disabled')
cofee_qty.place(x=74,y=22)

#for tea
tea_var=IntVar()
tea=Checkbutton(drinks,text="Tea",font=("verdana",8,'bold'),variable=tea_var,onvalue=1,offvalue=0,command=tea_chk)
tea.place(x=2,y=44)
tea_qty=Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
tea_qty.place(x=74,y=44)

#for juice
juice_var=IntVar()
juice=Checkbutton(drinks,text="Juice",font=("verdana",8,'bold'),variable=juice_var,onvalue=1,offvalue=0,command=juice_chk)
juice.place(x=2,y=66)
juice_qty=Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
juice_qty.place(x=74,y=66)

#for shakes
shakes_var=IntVar()
shakes=Checkbutton(drinks,text="Shakes",font=("verdana",8,'bold'),variable=shakes_var,onvalue=1,offvalue=0,command=shakes_chk)
shakes.place(x=2,y=88)
shakes_qty=Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
shakes_qty.place(x=74,y=88)

#for milk
milk_var=IntVar()
milk=Checkbutton(drinks,text="Milk",font=("verdana",8,'bold'),variable=milk_var,onvalue=1,offvalue=0,command=milk_chk)
milk.place(x=2,y=110)
milk_qty=Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
milk_qty.place(x=74,y=110)

#for shikanji
shikanji_var=IntVar()
shikanji=Checkbutton(drinks,text="Shikanji",font=("verdana",8,'bold'),variable=shikanji_var,onvalue=1,offvalue=0,command=shikanji_chk)
shikanji.place(x=2,y=132)
shikanji_qty=Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
shikanji_qty.place(x=74,y=132)

#for redbull
redbull_var=IntVar()
redbull=Checkbutton(drinks,text="Redbull",font=("verdana",8,'bold'),variable=redbull_var,onvalue=1,offvalue=0,command=redbull_chk)
redbull.place(x=2,y=154)
redbull_qty=Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
redbull_qty.place(x=74,y=154)
#--------------------------------------------------------------------------------------------------------------
#creating another frame for foods
innerframe2=Frame(frame1,width=290,height=220,relief=RIDGE,borderwidth=3,bg="white")
innerframe2.place(x=151,y=0)

#creating the label foods
foods=LabelFrame(innerframe2,text="Foods",width=275,height=205,borderwidth=3,bg="white")
foods.place(x=2,y=2)

#creating food items labels as well as entries
#roti
roti_var=IntVar()
roti=Checkbutton(foods,text="Roti",font=("verdana",8,'bold'),variable=roti_var,onvalue=1,offvalue=0,command=roti_chk)
roti.place(x=2,y=2)
roti_qty=Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
roti_qty.place(x=140,y=2)

#dalmakhani
dalmakhani_var=IntVar()
dalmakhani=Checkbutton(foods,text="Dal Makhani",font=("verdana",8,'bold'),variable=dalmakhani_var,onvalue=1,offvalue=0,command=dalmakhani_chk)
dalmakhani.place(x=2,y=22)
dalmakhani_qty=Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
dalmakhani_qty.place(x=140,y=22)

#mutterpanner
mutterpanner_var=IntVar()
mutterpanner=Checkbutton(foods,text="Mutterpanner",font=("verdana",8,'bold'),variable=mutterpanner_var,onvalue=1,offvalue=0,command=mutterpanner_chk)
mutterpanner.place(x=2,y=44)
mutterpanner_qty=Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
mutterpanner_qty.place(x=140,y=44)

#paratha
paratha_var=IntVar()
paratha=Checkbutton(foods,text="Paratha",font=("verdana",8,'bold'),variable=paratha_var,onvalue=1,offvalue=0,command=paratha_chk)
paratha.place(x=2,y=66)
paratha_qty=Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
paratha_qty.place(x=140,y=66)

#mixveg
mixveg_var=IntVar()
mixveg=Checkbutton(foods,text="Mixveg",font=("verdana",8,'bold'),variable=mixveg_var,onvalue=1,offvalue=0,command=mixveg_chk)
mixveg.place(x=2,y=88)
mixveg_qty=Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
mixveg_qty.place(x=140,y=88)

#omelete
omelete_var=IntVar()
omelete=Checkbutton(foods,text="Omelete",font=("verdana",8,'bold'),variable=omelete_var,onvalue=1,offvalue=0,command=omelete_chk)
omelete.place(x=2,y=110)
omelete_qty=Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
omelete_qty.place(x=140,y=110)

#vegbiriyani
vegbiriyani_var=IntVar()
vegbiriyani=Checkbutton(foods,text="Vegbiriyani",font=("verdana",8,'bold'),variable=vegbiriyani_var,onvalue=1,offvalue=0,command=vegbiriyani_chk)
vegbiriyani.place(x=2,y=132)
vegbiriyani_qty=Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
vegbiriyani_qty.place(x=140,y=132)

#rice
rice_var=IntVar()
rice=Checkbutton(foods,text="Rice",font=("verdana",8,'bold'),variable=rice_var,onvalue=1,offvalue=0,command=rice_chk)
rice.place(x=2,y=154)
rice_qty=Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
rice_qty.place(x=140,y=154)
#-------------------------------------------------------------------------------------------

#creating frame2
frame2=Frame(root,width=450,height=90,relief=RIDGE,borderwidth=5,bg="white")
frame2.place(x=0,y=300)
#creating innerframe 3
innerframe3=Frame(frame2,width=440,height=80,relief=RIDGE,borderwidth=3,bg="red")
innerframe3.place(x=0,y=0)

cost_of_drinks=Label(innerframe3,text="Cost of Drinks",font=("verdana",8,'bold'))
cost_of_drinks.place(x=2,y=2)
drinks_cost=Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
drinks_cost.place(x=130,y=0)

cost_of_foods=Label(innerframe3,text="Cost of Foods",font=("verdana",8,'bold'))
cost_of_foods.place(x=2,y=24)
foods_cost=Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
foods_cost.place(x=130,y=22)

service_charge=Label(innerframe3,text="Service Charge",font=("verdana",8,'bold'))
service_charge.place(x=2,y=46)
service_charge_cost=Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
service_charge_cost.place(x=130,y=44)

paid_tax=Label(innerframe3,text="Paid tax",font=("verdana",8,'bold'))
paid_tax.place(x=250,y=2)
paid_tax_cost=Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
paid_tax_cost.place(x=330,y=0)

sub_total=Label(innerframe3,text="Sub total",font=("verdana",8,'bold'))
sub_total.place(x=250,y=24)
sub_total_cost=Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
sub_total_cost.place(x=330,y=22)

total_cost=Label(innerframe3,text="Total Cost",font=("verdana",8,'bold'))
total_cost.place(x=250,y=46)
total_cost_cost=Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
total_cost_cost.place(x=330,y=44)
#-------------------------------------------------------------------------
#creating frame3
frame3=Frame(root,borderwidth=5,width=200,height=320,relief=RIDGE,bg="#33ff49")
frame3.place(x=450,y=70)

innerframe4=Frame(frame3,width=190,height=310,borderwidth=3,relief=RIDGE,bg="#33ff49")
innerframe4.place(x=0,y=0)

#for calculator gui
result=Entry(innerframe4,relief=SUNKEN,width=28,borderwidth=3)
result.place(x=0,y=2)

nine=Button(innerframe4,text="9",padx=15,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=nine)
nine.place(x=0,y=24)
eight=Button(innerframe4,text="8",padx=15,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=eight)
eight.place(x=48,y=24)
seven=Button(innerframe4,text="7",padx=15,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=seven)
seven.place(x=96,y=24)
plus=Button(innerframe4,text="+",padx=6,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=plus)
plus.place(x=144,y=24)

six=Button(innerframe4,text="6",padx=15,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=six)
six.place(x=0,y=47)
five=Button(innerframe4,text="5",padx=15,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=five)
five.place(x=48,y=47)
four=Button(innerframe4,text="4",padx=15,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=four)
four.place(x=96,y=47)
minus=Button(innerframe4,text="-",padx=8,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=minus)
minus.place(x=144,y=47)

three=Button(innerframe4,text="3",padx=15,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=three)
three.place(x=0,y=70)
two=Button(innerframe4,text="2",padx=15,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=two)
two.place(x=48,y=70)
one=Button(innerframe4,text="1",padx=15,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=one)
one.place(x=96,y=70)
multiply=Button(innerframe4,text="*",padx=7,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=multiply)
multiply.place(x=144,y=70)

zero=Button(innerframe4,text="0",padx=15,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=zero)
zero.place(x=0,y=93)
clear=Button(innerframe4,text="C",padx=15,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=clear)
clear.place(x=48,y=93)
equal=Button(innerframe4,text="=",padx=15,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=equal)
equal.place(x=96,y=93)
divide=Button(innerframe4,text="/",padx=7,relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),command=divide)
divide.place(x=144,y=93)

#for creating bill details
bill_details=scrolledtext.ScrolledText(innerframe4,width=23,height=9,relief=SUNKEN,borderwidth=2)
bill_details.place(x=0,y=130)

#for creating additional buttons
#for total
total=Button(innerframe4,text="Total",relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),bg="red",fg="white",command=total_bills)
total.place(x=0,y=280)

#for save
save=Button(innerframe4,text="Save",relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),bg="red",fg="white",command=save)
save.place(x=43,y=280)

#for send
send=Button(innerframe4,text="Send",relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),bg="red",fg="white",command=send)
send.place(x=86,y=280)

#for exit
exit=Button(innerframe4,text="Exit",relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),bg="red",fg="white",command=exit)
exit.place(x=129,y=280)

#for clear
c=Button(innerframe4,text="C",relief=RAISED,borderwidth=2,font=("verdana",8,'bold'),bg="red",fg="white",command=clear)
c.place(x=165,y=280)
#-----------------------------------THE GUI INTERFACE COMPLETED-----------------------------------------
root.mainloop()

