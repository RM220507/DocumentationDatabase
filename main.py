from tkinter import *
from tkinter import ttk
import mysql.connector
import json
from betteroptionmenu import BetterOptionMenu
from table import Table
from pymysql.converters import escape_string

def search(name, advanced_check, type_check, type, lang_check, lang):
    cursor.execute(f"""SELECT LinkID, LinkName, URL, TypeName, LangName 
                      FROM Links, Types, Languages
                      WHERE Links.TypeID = Types.TypeID
                      AND Links.LangID = Languages.LangID
                      AND LinkName LIKE '%{escape_string(name)}%';""")
    
    if advanced_check:
        results = []
        for result in cursor.fetchall():
            if type_check and type != result[3]:
                continue
            if lang_check and lang != result[4]:
                continue
            results.append(result)
    else:
        results = cursor.fetchall()

    results_table.delete_data()
    results_table.add_data(results)  

def add_new_type(name):
    if type_exists(name):
        return
    
    cursor.execute("INSERT INTO Types (TypeName) VALUES (%s)", (name,))
    db.commit()

    refresh_menus()

def add_new_lang(name):
    if lang_exists(name):
        return
    
    cursor.execute("INSERT INTO Languages (LangName) VALUES (%s)", (name,))
    db.commit()

    refresh_menus()

def add_new_link(name, url, type, lang):
    typeID = type_exists(type)
    if not typeID:
        return
    
    langID = lang_exists(lang)
    if not langID:
        return
    
    cursor.execute("INSERT INTO Links (LinkName, URL, TypeID, LangID) VALUES (%s, %s, %s, %s)", (name, url, typeID, langID))
    db.commit()
    
def type_exists(name):
    cursor.execute("SELECT TypeID FROM Types WHERE TypeName = %s", (name,))
    result = cursor.fetchone()
    if not result:
        return
    return result[0]

def lang_exists(name):
    cursor.execute("SELECT LangID FROM Languages WHERE LangName = %s", (name,))
    result = cursor.fetchone()
    if not result:
        return
    return result[0]

def refresh_menus():
    cursor.execute("SELECT TypeName FROM Types")
    result = cursor.fetchall()
    types = [val[0] for val in result]

    search_advanced_type_menu.DeleteOptions()
    search_advanced_type_menu.AddOptions(types)

    add_type_menu.DeleteOptions()
    add_type_menu.AddOptions(types)

    cursor.execute("SELECT LangName FROM Languages")
    result = cursor.fetchall()
    languages = [val[0] for val in result]

    search_advanced_lang_menu.DeleteOptions()
    search_advanced_lang_menu.AddOptions(languages)

    add_lang_menu.DeleteOptions()
    add_lang_menu.AddOptions(languages)

# setup window
root = Tk()
root.title("Documentation Database Interface")
root.config(bg="skyblue")

photo = PhotoImage(file="/home/ryan/Documents/GitHub/DocumentationDatabase/search.png")
root.iconphoto(False, photo)

root.resizable(False, False)

with open("/home/ryan/Documents/GitHub/DocumentationDatabase/connection_data.json") as f:
    connection_data = json.load(f)
db = mysql.connector.connect(**connection_data)
cursor = db.cursor()

# setup the left and right frames to hold the items
left_frame = Frame(root, width=200, height=400, bg="grey")
left_frame.grid(row=0, column=0, padx=10, pady=10)

right_frame = Frame(root, width=650, height=400, bg="grey", relief=RAISED)
right_frame.grid(row=0, column=1, padx=10, pady=10)

# placeholder options for the BetterOptionsMenu objects until they get refreshed
placeholder_options = ["Wating for Connection"]

# add the items in the left frame - SEARCH and ADD NEW
# SEARCH FRAME
search_frame = Frame(left_frame, width=175, height=200, bg="pink")
search_frame.grid(row=0, column=0, padx=5, pady=5)

#search label
Label(search_frame, text="Search", bg="pink").grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# entry to search NAME
search_query = Entry(search_frame, width=30)
search_query.grid(row=1, column=0, columnspan=2)

# checkbox to enable/disable advanced searching
search_advanced_check = BooleanVar(search_frame)
Checkbutton(search_frame, text="Advanced Search?", variable=search_advanced_check, bg="pink").grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# checkbox and option menu to allow type searching
search_advanced_type_check = BooleanVar(search_frame)
Checkbutton(search_frame, text="Type", variable=search_advanced_type_check, bg="pink").grid(row=3, column=0, padx=5, pady=5)

search_advanced_type = StringVar(search_frame)
search_advanced_type_menu = BetterOptionMenu(search_frame, search_advanced_type, LstOptions=placeholder_options)
search_advanced_type_menu.grid(row=3, column=1, padx=5, pady=5)
search_advanced_type_menu.config(width=15)

# checkbox and option menu to allow language searching
search_advanced_lang_check = BooleanVar(search_frame)
Checkbutton(search_frame, text="Lang", variable=search_advanced_lang_check, bg="pink").grid(row=4, column=0, padx=5, pady=5)

search_advanced_lang = StringVar(search_frame)
search_advanced_lang_menu = BetterOptionMenu(search_frame, search_advanced_lang, LstOptions=placeholder_options)
search_advanced_lang_menu.grid(row=4, column=1, padx=5, pady=5)
search_advanced_lang_menu.config(width=15)

# search button
Button(search_frame, text="Search", width=25, command=lambda: search(search_query.get(), search_advanced_check.get(), search_advanced_type_check.get(), search_advanced_type.get(), search_advanced_lang_check.get(), search_advanced_lang.get())).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# ADD NEW FRAME
add_frame = Frame(left_frame, width=175, height=200, bg="pink")
add_frame.grid(row=1, column=0, padx=5, pady=5)

#add new label
Label(add_frame, text="Add New", bg="pink").grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# data entry frame
add_data_entry_frame = Frame(add_frame, bg="pink")
add_data_entry_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# name entry
Label(add_data_entry_frame, text="Name", bg="pink").grid(row=0, column=0, padx=5, pady=5, sticky="W")
add_name = Entry(add_data_entry_frame, width=22)
add_name.grid(row=0, column=1)

# link entry
Label(add_data_entry_frame, text="Link", bg="pink").grid(row=1, column=0, padx=5, pady=5, sticky="W")
add_link = Entry(add_data_entry_frame, width=22)
add_link.grid(row=1, column=1)

# type option menu
Label(add_data_entry_frame, text="Type", bg="pink").grid(row=2, column=0, padx=5, pady=5, sticky="W")
add_type = StringVar(search_frame)
add_type_menu = BetterOptionMenu(add_data_entry_frame, add_type, LstOptions=placeholder_options)
add_type_menu.grid(row=2, column=1, padx=5, pady=5, sticky="E")
add_type_menu.config(width=15)

# language option menu
Label(add_data_entry_frame, text="Lang", bg="pink").grid(row=3, column=0, padx=5, pady=5, sticky="W")
add_lang = StringVar(search_frame)
add_lang_menu = BetterOptionMenu(add_data_entry_frame, add_lang, LstOptions=placeholder_options)
add_lang_menu.grid(row=3, column=1, padx=5, pady=5, sticky="E")
add_lang_menu.config(width=15)

Button(add_frame, text="Add Lang", width=10, command=lambda: add_new_lang(add_name.get())).grid(row=2, column=0, padx=4, pady=4)
Button(add_frame, text="Add Type", width=10, command=lambda: add_new_type(add_name.get())).grid(row=2, column=1, padx=4, pady=4)

Button(add_frame, text="Add Link", width=25, command=lambda: add_new_link(add_name.get(), add_link.get(), add_type.get(), add_lang.get())).grid(row=3, column=0, columnspan=2, padx=4, pady=4)

results_table = Table(right_frame, ["ID", "Link Name", "URL", "Type", "Language"])

refresh_menus()
root.mainloop()