import tkinter as tk
from tkinter import ttk
import psycopg2

root = tk.Tk()
root.title("Documentation Database Interface")

photo = tk.PhotoImage(file="/home/ryan/Documents/GitHub/DocumentationDatabase/search.png")
root.iconphoto(False, photo)

frame = ttk.Frame(root, padding=10)
frame.grid()

class Table:   
    def __init__(self,root, data):   
        # code for creating table
        clear_frame()
        ttk.Button(frame, text="<- Search", width=160, command=search_screen).grid(row=0, column=0, columnspan=4)
        ttk.Label(frame, text="Results...").grid(row=1, column=0, columnspan=4)
        for i in range(len(data)):
            for j in range(len(data[i])):          
                self.e = ttk.Entry(root, width=40)
                self.e.grid(row=i+2, column=j)
                self.e.insert(tk.END, data[i][j])
                self.e.configure(state="readonly")

# Connect to postgreSQL database
def sql_connect():
  
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(host="192.168.1.179", database="documentation", user="postgres", password="xm32BAZRP")
          
    # create a cursor
    cur = conn.cursor()
          
    # display database version
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(f"Connected to PostgreSQL database with version {db_version}")
    
    return conn, cur

def get_lang():
    cur.execute("SELECT * FROM languages")
    return cur.fetchall()

def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()

def search(query):
    cur.execute(f"SELECT links.name, link, type, languages.name FROM languages, links WHERE languages.langid = links.langid AND links.name LIKE '%{query}%';")
    #cur.execute("SELECT * FROM links")
    search_screen()
    Table(frame, cur.fetchall())
    
def new_lang(name):
    global languages
    cur.execute("INSERT INTO languages (name) VALUES (%s);", (name,))
    conn.commit()
    languages = get_lang()
    new_screen()

def new_link(name, link, langname, linktype):
    langid = 0
    for lang in languages:
        if lang[1] == langname:
            langid = lang[0]
            break
    cur.execute("INSERT INTO links (name, link, type, langid) VALUES (%s, %s, %s, %s);", (name.strip(), link.strip(), len(linktype) > 0, langid))
    conn.commit()
    new_screen()
    
def search_screen():
    clear_frame()
    
    ttk.Button(frame, text="Add New ->", command=new_screen, width=80).grid(column=0, row=0, columnspan=2)
    ttk.Label(frame, text="Search Entries").grid(column=0, row=1, columnspan=2)
    
    search_query = ttk.Entry(frame, width=60)
    search_query.grid(column=0, row=2)
    
    ttk.Button(frame, text="Search", command=lambda: search(search_query.get()), width=20).grid(column=1, row=2)
    
def new_screen():
    clear_frame()
    
    ttk.Label(frame, text="Add New Language").grid(column=0, row=0, columnspan=2)
    
    lang_name = ttk.Entry(frame, width=40)
    lang_name.grid(column=0, row=1)
    
    ttk.Button(frame, text="Add", width=40, command=lambda: new_lang(lang_name.get())).grid(column=1, row=1)
    
    
    ttk.Label(frame, text="Add New Link").grid(column=0, row=2, columnspan=2)
    
    ttk.Label(frame, text="Name").grid(column=0, row=3)
    name = ttk.Entry(frame, width=40)
    name.grid(column=1, row=3)
    
    ttk.Label(frame, text="Link").grid(column=0, row=4)
    link = ttk.Entry(frame, width=40)
    link.grid(column=1, row=4)
    
    ttk.Label(frame, text="Language").grid(column=0, row=5)
    value_inside = tk.StringVar(frame)
    value_inside.set("Python")
    option = ttk.OptionMenu(frame, value_inside, *[lang[1] for lang in languages])
    option.grid(column=1, row=5)
    
    ttk.Label(frame, text="Docs/Tutorial").grid(column=0, row=6)
    linktype = ttk.Checkbutton(frame)
    linktype.grid(column=1, row=6)
    
    ttk.Button(frame, text="Add", command=lambda: new_link(name.get(), link.get(), value_inside.get(), linktype.state())).grid(column=0, row=7, columnspan=2)

    ttk.Button(frame, text="<- Search", command=search_screen, width=80).grid(column=0, row=8, columnspan=2)

conn, cur = sql_connect()
languages = get_lang()    

search_screen()
root.mainloop()