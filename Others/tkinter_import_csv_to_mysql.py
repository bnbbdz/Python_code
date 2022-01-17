from tkinter.filedialog import askopenfilename
import tkinter as tk
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import time
import re
import yaml
from sqlalchemy.types import NVARCHAR
import urllib

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 800, height = 300)
canvas1.pack()

lable1 = tk.Label(root, text = 'Text table\'s name')
lable1.config(font=('Arial',11))
canvas1.create_window(400,100,window = lable1)

entry1 = tk.Entry (root)
canvas1.create_window(400, 120, window=entry1)

def input_file_location():
    global filename
    filename = askopenfilename()
    text = tk.Label(text=filename)
    text.place(x=300,y=70)

config_file = open(r"D:\03. Learning\01. Coder\00. Git_code_backup\Others\config.yml")
parsed_config_file = yaml.load(config_file, Loader=yaml.FullLoader)
server = parsed_config_file['default']['server']
uid = parsed_config_file['default']['uid']
pwd = parsed_config_file['default']['pwd']
db = 'cuongnm'

#Create function
patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}

def convert(text):
    """
    Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'
    text: input string to be converted
    Return: string converted
    """
    output = text
    for regex, replace in patterns.items():
        output = re.sub('\s|\.|-|\?', '_', output)
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output).upper()      
        
    return output

def sqlcol(dfparam):    
    
    dtypedict = {}
    for i,j in zip(dfparam.columns, dfparam.dtypes):        
        if "object" in str(j):
            dtypedict.update({i: sqlalchemy.types.NVARCHAR(length=255)})
                                 
        if "datetime" in str(j):
            dtypedict.update({i: sqlalchemy.types.DateTime()})

        if "float" in str(j):
            dtypedict.update({i: sqlalchemy.types.Float(precision=3, asdecimal=True)})

        if "int" in str(j):
            dtypedict.update({i: sqlalchemy.types.INT()})
        
    return dtypedict

def import_excel_file ():
    global x1
    x1 = entry1.get()
    #Upload excel file and load into oracle
    df = pd.read_csv(filename) 

    old_columns = df.columns.tolist() 
    new_columns = [convert(x) for x in old_columns]
    df = df.rename(columns=dict(zip(old_columns, new_columns)))
    outputdict = sqlcol(df)

    start_time = time.time()

    conn_str = ('Driver={SQL Server};'
                    'Server=' + server + ';'
                    'Database=' + db + ';'
                    'UID='+uid+';'
                    'PWD='+pwd+';')
    params = urllib.parse.quote_plus(conn_str)

    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

    df.to_sql(name=x1,con=engine ,if_exists = 'append', index=False, dtype=outputdict)
    kq = tk.Label(text="done in --- %s seconds ---" % (time.time() - start_time))
    kq.place(x=300,y=190)      

button1 = tk.Button (root, text='Choose file',command=input_file_location, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 50, window=button1)

button2 = tk.Button (root, text='  Import file to sql server', command=import_excel_file, bg='lightskyblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 170, window=button2)

button3 = tk.Button (root, text='Exit Application', command=root.destroy, bg='lightsteelblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 240, window=button3)
 
root.mainloop()

#https://www.youtube.com/watch?v=293_0BqZAa4