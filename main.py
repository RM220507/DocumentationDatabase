from tkinter import *

# setup window
root = Tk()
root.title("Documentation Database Interface")
root.config(bg="skyblue")

#photo = PhotoImage(file="search.png")
#root.iconphoto(False, photo)


# setup the left and right frames to hold the items
left_frame = Frame(root, width=200, height=400, bg="grey")
left_frame.grid(row=0, column=0, padx=10, pady=10)

right_frame = Frame(root, width=650, height=400, bg="grey")
right_frame.grid(row=0, column=1, padx=10, pady=10)

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
type_options = ["Documentation", "Tutorial", "Datasheet", "Purchase Link"]
search_advanced_type_menu = OptionMenu(search_frame, search_advanced_type, *type_options)
search_advanced_type_menu.grid(row=3, column=1, padx=5, pady=5)
search_advanced_type_menu.config(width=15)

# checkbox and option menu to allow language searching
search_advanced_lang_check = BooleanVar(search_frame)
Checkbutton(search_frame, text="Lang", variable=search_advanced_lang_check, bg="pink").grid(row=4, column=0, padx=5, pady=5)

search_advanced_lang = StringVar(search_frame)
lang_options = ["Python", "CSS", "HTML", "N/A"]
search_advanced_lang_menu = OptionMenu(search_frame, search_advanced_lang, *lang_options)
search_advanced_lang_menu.grid(row=4, column=1, padx=5, pady=5)
search_advanced_lang_menu.config(width=15)

# checkbox and entry to allow LinkID searching
search_advanced_id_check = BooleanVar(search_frame)
Checkbutton(search_frame, text="ID", variable=search_advanced_id_check, bg="pink").grid(row=5, column=0, padx=5, pady=5, sticky="W")

search_advanced_id = Entry(search_frame, width=20)
search_advanced_id.grid(row=5, column=1, padx=5, pady=5, sticky="E")

# search button
Button(search_frame, text="Search", width=25).grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# ADD NEW FRAME
pass

root.mainloop()
