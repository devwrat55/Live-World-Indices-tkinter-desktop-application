import tkinter
import tkinter as tk
root=tkinter.Tk()
root.title('World Live Indices')
root.state('zoomed')
root.configure(background='white')
global update_mat
update_mat=[]
global update_mat_old
update_mat_old=[]

global ct
ct=0
from time import strftime
def update_csv_of_indices():
    
    import requests 
    from bs4 import BeautifulSoup 
    import pandas as pd
    prices=[]
    names=[]
    changes=[]
    percentChanges=[]
    
    r= requests.get("https://in.finance.yahoo.com/world-indices")
    data=r.text
    soup=BeautifulSoup(data, 'html.parser')
    
    for row in soup.find_all('tbody'):
        for srow in row.find_all('tr'):
            for name in srow.find_all('td', attrs={'class':'data-col1'}):
                names.append(name.text)
            for price in srow.find_all('td', attrs={'class':'data-col2'}):
                prices.append(price.text)
            for change in srow.find_all('td', attrs={'class':'data-col3'}):
                changes.append(change.text)
            for percentChange in srow.find_all('td', attrs={'class':'data-col4'}):
                percentChanges.append(percentChange.text)
    
    df = pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})
    df.to_csv('stock_world_indices_data.csv', index = False, header=True)
    
    global ct
    ct = 0
    
    
def counter_label(label):
    global ct
    global update_mat
    global update_mat_old
    #print("ct = " ,ct)
    #print("update_mat = ",update_mat)
    #print("update_mat_old  =",update_mat_old)
    if(float(update_mat[ct].replace(',', '').replace('%','')) == float(update_mat_old[ct].replace(',', '').replace('%',''))):
        mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
        label.config(text=update_mat[ct], background = mycolorbg)
    elif(float(update_mat[ct].replace(',', '').replace('%','')) < float(update_mat_old[ct].replace(',', '').replace('%',''))):
        mycolorbg = '#%02x%02x%02x' % (255, 0, 0)
        label.config(text=update_mat[ct], background = mycolorbg)
    elif(float(update_mat[ct].replace(',', '').replace('%','')) > float(update_mat_old[ct].replace(',', '').replace('%',''))):
        mycolorbg = '#%02x%02x%02x' % (0, 255, 0)
        label.config(text=update_mat[ct], background = mycolorbg)
  
  
def time1(): 
    string = strftime(' %d/%m/%Y %I:%M:%S %p ')    
	 #string = strftime('%d/%m/%Y; %H:%M:%S %p; %I%p')     
    lbl.config(text = string) 
    lbl.after(1000, time1) 

# Styling the label widget so that clock 
# will look more attractive 
mycolorbg = '#%02x%02x%02x' % (248, 0, 0)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)
lbl = tk.Label(root, font = ('Consolas', 20, 'bold'), 
			background = mycolorbg, 
			foreground = mycolorfg) 
# Placing clock at the centre 
# of the tkinter window 
#anchor "right": must be n, ne, e, se, s, sw, w, nw, or center
lbl.grid(row = 0, column = 20, sticky = "nesw")
time1()

lab=tkinter.Label( root, text = "              ")
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
lab.config(font=("Consolas", 21), 
            background = mycolorbg, 
            foreground = mycolorfg) 
lab.grid(row = 0, column = 18, sticky = "e")




for i in range(25):
    if(1):
        space00 = tk.Label( root, text = "      |  ")
        mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
        mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
        space00.config(font=("Consolas", 11), 
        			background = mycolorbg, 
        			foreground = mycolorfg) 
        space00.grid(row = i+1, column = 0, sticky = "nesw")
    else:
        space00 = tk.Label( root, text = "         ")
        mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
        mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
        space00.config(font=("Consolas", 11), 
        			background = mycolorbg, 
        			foreground = mycolorfg) 
        space00.grid(row = i+1, column = 0, sticky = "nesw")

headings = ["    INDEX    ", " | ", "    LAST    ", " | ", "    CHANGE    ", " | ", "    CHANGE %    ", " | "]
for i in range(len(headings)):
    index01 = tk.Label( root, text = headings[i])
    mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
    mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
    index01.config(font=("Consolas", 11), 
    			background = mycolorbg, 
    			foreground = mycolorfg) 
    index01.grid(row = 1, column = i+1, sticky = "nesw")

import csv
i=0
ii=2
j=0
k=0
for ii in range(25):   
    for j in range(2,9,2):
        data = tkinter.Label( root, text = " | ")
        mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
        mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
        data.config(font=("Consolas", 11), 
        			background = mycolorbg, 
        			foreground = mycolorfg) 
        data.grid(row = ii+1, column = j, sticky = "e")
    ii=ii+1



update_csv_of_indices() 
mat1=[]
row1=[]
column1=[]       
with open('stock_world_indices_data.csv', 'r') as file:
    reader = csv.reader(file)
    i=0
    ii=2
    j=0
    k=0
    
    for row in reader:
        if(i>0 and i<36 and i != 11 and i != 14 and i != 16 and i != 17 and i != 24 and i != 26 and i <30):
            k=0
            for j in range(1,8,2):
                if(j==1):
                    data = tkinter.Label( root, text = row[k])
                    mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
                    mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
                    data.config(font=("Consolas", 11), 
                    			background = mycolorbg, 
                    			foreground = mycolorfg) 
                    data.grid(row = ii+1, column = j, sticky = "e")
                else:
                    mat1.append(row[k])
                    row1.append(ii+1)
                    column1.append(j)
                k=k+1 
            ii=ii+1
        i=i+1
        
#print(mat1)
#print(row1)
#print(column1)


update_mat=mat1
update_mat_old=mat1

counter1 = 0



#i used this to generate below code

#str1="""
#or i in range(0,24):
#    for j in range(0,3):
#        str1 += """
#        label"""+str(i)+str(j)+"""=tkinter.Label( root, text = mat1[counter1])
#        mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
#        mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
#        label"""+str(i)+str(j)+""".config(font=("Consolas", 11), 
#                    background = mycolorbg, 
#                    foreground = mycolorfg) 
#        label"""+str(i)+str(j)+""".grid(row = row1[counter1], column = column1[counter1], sticky = "e")
#        counter1+=1
#        """

#print(str1)


label00=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label00.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label00.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label01=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label01.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label01.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label02=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label02.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label02.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label10=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label10.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label10.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label11=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label11.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label11.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label12=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label12.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label12.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label20=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label20.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label20.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label21=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label21.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label21.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label22=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label22.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label22.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label30=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label30.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label30.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label31=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label31.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label31.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label32=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label32.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label32.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label40=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label40.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label40.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label41=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label41.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label41.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1


label42=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label42.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label42.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label50=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label50.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label50.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label51=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label51.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label51.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label52=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label52.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label52.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label60=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label60.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label60.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label61=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label61.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label61.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label62=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label62.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label62.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label70=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label70.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label70.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label71=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label71.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label71.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label72=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label72.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label72.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label80=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label80.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label80.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label81=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label81.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label81.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label82=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label82.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label82.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label90=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label90.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label90.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label91=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label91.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label91.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label92=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label92.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label92.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label100=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label100.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label100.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label101=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label101.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label101.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label102=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label102.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label102.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label110=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label110.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label110.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label111=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label111.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label111.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label112=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label112.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label112.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label120=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label120.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label120.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label121=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label121.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label121.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label122=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label122.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label122.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label130=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label130.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label130.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label131=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label131.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label131.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label132=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label132.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label132.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label140=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label140.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label140.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label141=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label141.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label141.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label142=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label142.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label142.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label150=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label150.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label150.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label151=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label151.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label151.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label152=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label152.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label152.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label160=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label160.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label160.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label161=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label161.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label161.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label162=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label162.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label162.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label170=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label170.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label170.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label171=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label171.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label171.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label172=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label172.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label172.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label180=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label180.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label180.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label181=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label181.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label181.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label182=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label182.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label182.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label190=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label190.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label190.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label191=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label191.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label191.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label192=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label192.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label192.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label200=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label200.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label200.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label201=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label201.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label201.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label202=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label202.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label202.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label210=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label210.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label210.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label211=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label211.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label211.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label212=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label212.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label212.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label220=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label220.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label220.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label221=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label221.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label221.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1

label222=tkinter.Label( root, text = mat1[counter1])
mycolorbg = '#%02x%02x%02x' % (255, 255, 255)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)  # set your favourite rgb color
label222.config(font=("Consolas", 11), 
            background = mycolorbg, 
            foreground = mycolorfg) 
label222.grid(row = row1[counter1], column = column1[counter1], sticky = "e")
counter1+=1    


from threading import Thread

global stop_threads




def function2():
    while True:
        
        
        
        update_csv_of_indices()
        
        mat1=[]
        with open('stock_world_indices_data.csv', 'r') as file:
            reader = csv.reader(file)
            i=0
            ii=2
            j=0
            k=0
            
            for row in reader:
                if(i>0 and i<36 and i != 11 and i != 14 and i != 16 and i != 17 and i != 24 and i != 26 and i <30):
                    k=0
                    for j in range(1,8,2):
                        if(j!=1):
                            mat1.append(row[k])
                                
                        k=k+1 
                    ii=ii+1
                i=i+1
      
        global update_mat
        global update_mat_old
        update_mat_old = update_mat       
        update_mat = mat1
        global ct        
        counter_label(label00)
        ct=ct+1
        counter_label(label01)
        ct=ct+1
        counter_label(label02)
        ct=ct+1
        counter_label(label10)
        ct=ct+1
        counter_label(label11)
        ct=ct+1
        counter_label(label12)
        ct=ct+1
        counter_label(label20)
        ct=ct+1
        counter_label(label21)
        ct=ct+1
        counter_label(label22)
        ct=ct+1
        counter_label(label30)
        ct=ct+1
        counter_label(label31)
        ct=ct+1
        counter_label(label32)
        ct=ct+1
        counter_label(label40)
        ct=ct+1
        counter_label(label41)
        ct=ct+1
        counter_label(label42)
        ct=ct+1
        counter_label(label50)
        ct=ct+1
        counter_label(label51)
        ct=ct+1
        counter_label(label52)
        ct=ct+1
        counter_label(label60)
        ct=ct+1
        counter_label(label61)
        ct=ct+1
        counter_label(label62)
        ct=ct+1
        counter_label(label70)
        ct=ct+1
        counter_label(label71)
        ct=ct+1
        counter_label(label72)
        ct=ct+1
        counter_label(label80)
        ct=ct+1
        counter_label(label81)
        ct=ct+1
        counter_label(label82)
        ct=ct+1
        counter_label(label90)
        ct=ct+1
        counter_label(label91)
        ct=ct+1
        counter_label(label92)
        ct=ct+1
        counter_label(label100)
        ct=ct+1
        counter_label(label101)
        ct=ct+1
        counter_label(label102)
        ct=ct+1
        counter_label(label110)
        ct=ct+1
        counter_label(label111)
        ct=ct+1
        counter_label(label112)
        ct=ct+1
        counter_label(label120)
        ct=ct+1
        counter_label(label121)
        ct=ct+1
        counter_label(label122)
        ct=ct+1
        counter_label(label130)
        ct=ct+1
        counter_label(label131)
        ct=ct+1
        counter_label(label132)
        ct=ct+1
        counter_label(label140)
        ct=ct+1
        counter_label(label141)
        ct=ct+1
        counter_label(label142)
        ct=ct+1
        counter_label(label150)
        ct=ct+1
        counter_label(label151)
        ct=ct+1
        counter_label(label152)
        ct=ct+1
        counter_label(label160)
        ct=ct+1
        counter_label(label161)
        ct=ct+1
        counter_label(label162)
        ct=ct+1
        counter_label(label170)
        ct=ct+1
        counter_label(label171)
        ct=ct+1
        counter_label(label172)
        ct=ct+1
        counter_label(label180)
        ct=ct+1
        counter_label(label181)
        ct=ct+1
        counter_label(label182)
        ct=ct+1
        counter_label(label190)
        ct=ct+1
        counter_label(label191)
        ct=ct+1
        counter_label(label192)
        ct=ct+1
        counter_label(label200)
        ct=ct+1
        counter_label(label201)
        ct=ct+1
        counter_label(label202)
        ct=ct+1
        counter_label(label210)
        ct=ct+1
        counter_label(label211)
        ct=ct+1
        counter_label(label212)
        ct=ct+1
        counter_label(label220)
        ct=ct+1
        counter_label(label221)
        ct=ct+1
        counter_label(label222)
        
        ct=0
        #print("here")

try:
    Thread(target = function2).start()
    
except:
    pass


root.mainloop()





