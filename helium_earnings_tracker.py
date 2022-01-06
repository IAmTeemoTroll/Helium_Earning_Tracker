# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:25:19 2022

@author: desmo_sxgiwmz
"""
import requests
import json 
import datetime
import tkinter as tk
from tkinter import ttk


def sav_info(*args):
    
    box=[]
    box2=[]
    box3=[]
    box4=[]
    box5=[]
    box6=[]
    bb=[]
    bb2=[]
    
    #get_miner_address
    
    x=myText.get()
    
    #get_currency_exchange pair
    b1=cmb.get()
    
    #get_equiqment_cost
    y=myText2.get()
    
    

    t1='https://api.helium.io/v1/hotspots/'

    t2=t1 + x

    t3=t1 + x +'/rewards/sum?'




    r=requests.get(t2)
    cont=json.loads(r.content.decode())


    #last_poc_challenge
    p1=cont.get('data',{}).get('timestamp_added')

    start_date=p1[0:10]


    #current_time

    tm1=datetime.date(int(start_date[0:4]),int(start_date[5:7]),int(start_date[8:10]))
    tm2=datetime.date.today()

    dy1=(tm2-tm1).days

    delta=datetime.timedelta(days=1)



    m1='https://api.coingecko.com/api/v3/coins/helium/history?date='
    m2='&localization=false'

    for n in range(dy1+1):
        box.append((tm1+datetime.timedelta(days=n)).strftime("%Y-%m-%d"))
       
    for n in range(dy1+2):   
       box4.append(m1+(tm1+datetime.timedelta(days=n)).strftime("%d-%m-%Y")+m2)

    box4=box4[:-2]

    box2.append(t3+'min_time='+ p1[0:19]+'Z'+'&max_time='+box[1]+'T11:59:59Z')


    for n2 in range(1,len(box[1:])):
        box2.append(t3 +'min_time='+box[n2]+'T11:59:59Z'+'&max_time='+box[n2+1]+'T11:59:59Z')

    for n3 in box2:
        r1=requests.get(n3)
        c1=json.loads(r1.content.decode()).get('data',{}).get('total')
        box3.append(c1)


    for n4 in box4:
        r4=requests.get(n4)
        c4=json.loads(r4.content.decode()).get('market_data',{}).get('current_price',{}).get(b1)
        box5.append(c4)

    for i in range(len(box5)):
        price=float(box3[i])*float(box5[i])
        box6.append(price)

    dd_total=sum(box6)
    dd_ave_price=dd_total/len(box6)

    ove_total=(sum(box3)*box5[-1])
    ove_ave_price=ove_total/len(box3)

    y=float(y)
    td=(y/ove_ave_price)/30

    

    #print('day to day total earnings   = ',"{:.3f}".format(dd_total))
    #print('overall average earnings    = ',"{:.3f}".format(ove_ave_price))
    #print('overall total earnings      = ',"{:.3f}".format(ove_total))
    #print('')
    #print('Time needed for cost-free   = ',"{:.2f}".format(td),' months')
    
    myText3.set('day to day average earnings = '+"{:.3f}".format(dd_ave_price)+' '+b1.upper())
    myText4.set('day to day total earnings       = '+"{:.3f}".format(dd_total)+' '+b1.upper())
    myText5.set('overall average earnings        = '+"{:.3f}".format(ove_ave_price)+' '+b1.upper())
    myText6.set('overall total earnings             = '+"{:.3f}".format(ove_total)+' '+b1.upper())
    myText7.set('time needed for cost-free     = '+"{:.2f}".format(td)+' months')
    
    for c1 in range(0,len(box3)):
        bb.append("{:.3f}".format(box5[c1]))
        bb2.append("{:.3f}".format(box6[c1]))
    # add data to the treeview
    
    
    if tree.get_children():
        for ele in tree.get_children():
            tree.delete(ele)
            
            for c1 in range(0,len(box3)):
                tree.insert('', tk.END, values=box[c1]+'   '+box2[c1][118:128]+'   '+str(box3[c1])+'   '+ bb[c1]+'     '+bb2[c1])
    else:
        for c1 in range(0,len(box3)):
            tree.insert('', tk.END, values=box[c1]+'   '+box2[c1][118:128]+'   '+str(box3[c1])+'   '+ bb[c1]+'     '+bb2[c1])
        
# open tkinter interface
root =tk.Tk()


#change GUID interface
length=600
width=550

root.geometry(str(length)+'x'+str(width))
root.title('Helium Earning Tracker')


#label
x1=50
y1=30


#label
a=tk.Label(root,text='Helium Miner Address').place(x=x1,y=y1,anchor='w')
b=tk.Label(root,text='Currency Exchange').place(x=x1,y=(y1*1.5)+20,anchor='w')

c=tk.Label(root,text='Equiqment Cost').place(x=x1,y=(y1*3)+20,anchor='w')
d=tk.Label(root,text='Result').place(x=x1,y=(y1*4.5)+20,anchor='w')

#miner_address_entry
myText=tk.StringVar()
tk.Entry(root,textvariable=myText).place(x=x1+150,y=y1,anchor='w')

#equiement_cost_entry
myText2=tk.DoubleVar()
tk.Entry(root,textvariable=myText2).place(x=x1+150,y=(y1*3)+20,anchor='w')


myText3=tk.StringVar()
myText4=tk.StringVar()
myText5=tk.StringVar()
myText6=tk.StringVar()
myText7=tk.StringVar()
myText8=tk.StringVar()

tk.Label(root,textvariable=myText3).place(x=x1+150,y=(y1*4.5)+20,anchor='w')
tk.Label(root,textvariable=myText4).place(x=x1+150,y=(y1*5.3)+20,anchor='w')
tk.Label(root,textvariable=myText5).place(x=x1+150,y=(y1*6.1)+20,anchor='w')
tk.Label(root,textvariable=myText6).place(x=x1+150,y=(y1*6.9)+20,anchor='w')
tk.Label(root,textvariable=myText7).place(x=x1+150,y=(y1*7.7)+20,anchor='w')
tk.Label(root,textvariable=myText8).place(x=x1+150,y=(y1*8.5)+20,anchor='w')



#dropdown_to_choose_currency

w1=["ars",
"aud",
"bch",
"bdt",
"bhd",
"bmd",
"bnb",
"brl",
"btc",
"cad",
"chf",
"clp",
"cny",
"czk",
"dkk",
"dot",
"eos",
"eth",
"eur",
"gbp",
"hkd",
"huf",
"idr",
"ils",
"inr",
"jpy",
"krw",
"kwd",
"lkr",
"ltc",
"mmk",
"mxn",
"myr",
"ngn",
"nok",
"nzd",
"php",
"pkr",
"pln",
"rub",
"sar",
"sek",
"sgd",
"thb",
"try",
"twd",
"uah",
"usd",
"vef",
"vnd",
"xag",
"xau",
"xdr",
"xlm",
"xrp",
"yfi",
"zar",
"bits",
"link",
"sats",
]

cmb=ttk.Combobox(root,value=w1,width=10)
cmb.place(x=x1+150,y=(y1*1.5)+20,anchor='w')
cmb.current(1)
#cmb.bind('<<ComboboxSelected>>',sav_info)


tree=ttk.Treeview(root)
tree.place(x=x1,y=(y1*12)+20,anchor='w')

sb=ttk.Scrollbar(root,orient='vertical',command=tree.yview)
sb.place(x=x1*11.1,y=(y1*8)+20,height=230)

tree.configure(yscrollcommand=sb.set)


tree['columns']=('1','2','3','4','5')
tree['show']='headings'
tree.column("1", width=100, anchor='w')
tree.column("2", width=100, anchor='c')
tree.column("3", width=100, anchor='c')
tree.column("4", width=100, anchor='c')
tree.column("5", width=100, anchor='c')

tree.heading("1", text="Date")
tree.heading("2", text="Timestamp")
tree.heading("3", text="HNT Amount")
tree.heading("4", text="HNT Price")
tree.heading("5", text="Daily Earning")

tree.bind('<Button-1>',sav_info)

#columns=['Date','HNT Amount','HNT Price','Daily Earning']
#for col in columns:
    #router_tree_view.column(col, width=100)
    #router_tree_view.heading(col, text=col)

#contacts = []
#for n in range(1, 100):
    #contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# add data to the treeview
#for contact in contacts:
    #tree.insert('', tk.END, values=contact)


#button 
tk.Button(text='Enter', width='10',command=sav_info).place(x=length-150,y=width-325,anchor='w')

root.mainloop()




