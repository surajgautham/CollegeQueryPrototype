#!/usr/bin/env python3

from tkinter import *
import webbrowser

links1 = {"RVCE": "https://www.rvce.edu.in/about-us.",
         "PESU": "https://www.pes.edu/about-us/",
          }
links2= {"PESU":"https://www.pesuacademy.com/Academy/sessionExpired"}
links3= {"RVCE":"https://rvce.edu.in/rvce-scheme-syllabus",
        "PESU" : "https://www.pes.edu/handbook-of-scheme-of-instruction-and-syllabi-2018-19/"}
links4= {"RVCE":"https://www.rvce.edu.in/contact-us",
         "PESU":"https://www.pes.edu/contact/"}
links6= {"RVCE":"https://rvce.edu.in/faqs",
         "PESU":"https://www.pes.edu/faqs/"}
links7={"RVCE":"https://docs.google.com/forms/d/15XZx4jt8ZMeiGWh8iVr4zKteYmg4hdpvOA8z4KU-klw/edit",
         "PESU":"https://docs.google.com/forms/d/15XZx4jt8ZMeiGWh8iVr4zKteYmg4hdpvOA8z4KU-klw/edit"}


# Create new Tkinter instance
root = Tk()

# Creats a new page
page_home = Frame(root)

# Position Page
page_home.grid(row=0, column=0, sticky='news')

# Create new label with required text
l1 = Label(page_home, text="*****Enter college name*****")

# Positioning Label
l1.pack()

# Object to hold the value of selected option
college = StringVar(page_home)

# Sets default value of college
college.set("Default")


def clear_default(evt):
    if college.get() == "Default":
        evt.widget.delete(0, END)


ignore = False
vs = []


def process_input(evt):
    global ignore, vs

    # Ignore keys entered by code
    if ignore:
        ignore = False
        return

    # For each college in colleges, check if college name is in input text
    vs = []
    curr_text = str.lower(college.get())
    college_list.delete(0, END)
    for c in links1.keys():
        if str.lower(c).startswith(curr_text):
            # If yes, then add it to the suggestions box
            college_list.insert(END, c)
            vs.append(c)

    # Dont run if backspace is pressed
    if evt.keycode not in [22, 50, 110]:

        # If any suggestions exist, then auto fill the first suggestion
        if len(vs):
            college_entry.delete(0, END)

            # Ignore keys pressed due to autofill for processing
            ignore = len(vs) != 1
            college_entry.insert(END, vs[0])

            # Select auto fill text
            college_entry.select_range(len(curr_text), END)

    # Enable Feature selection if a valid input is typed
    if len(vs) == 1:
        feature_option.configure(state="normal")
    else:
        feature_option.configure(state="disabled")


def select_item(evt):
    global vs
    if vs:
        # If selection is present, then change entry text to selected value
        sel = evt.widget.curselection()
        if sel:
            college_entry.delete(0, END)
            college_entry.insert(END, vs[sel[0]])
            feature_option.configure(state="normal")


# Creating an option menu in page_home
college_entry = Entry(page_home, textvariable=college)
college_entry.bind("<Button-1>", clear_default)
college_entry.bind("<KeyRelease>", process_input)

# Positioning option menu
college_entry.pack()

college_list = Listbox(page_home)
college_list.bind("<<ListboxSelect>>", select_item)
college_list.pack()

# Object to hold the value of selected option
features = StringVar(page_home)

# Default
features.set("Select Feature")


def enable_second_options(x, options_2):
    # global variable_name
    print("Sel:", x)

    # Enable second options, normal is the value to enabled dropdown
    options_2.configure(state="normal")


def next_callback(*args):
    

    # Get Feature
    if features.get() == "About College":
            # If featuer is show college, the show College link page
            page_linking.tkraise()

            # Set text to college link text
            lbl_link["text"] = "About College " + college.get()

            # Set Hyperlink to Required college link
            lbl_link.bind("<Button-1>", lambda x: webbrowser.open_new(links1[college.get()]))
    elif features.get() == "How to apply":
        links5 = {"CET":
                    {"Register": "https://www.sarvgyan.com/articles/kcet-2020-application-form",
                     "Docs. to be submitted": "https://www.collegedekho.com/exam/kcet/counselling-process",
                      "Fee structure":"http://kea.kar.nic.in/cet2020/R2/fees.pdf"},
                "COMEDK":
                    {"Register":"https://www.comedk.org/about-uget-and-notification/",
                     "Docs. to be submitted":"https://www.comedk.org/",
                     "Fee structure":"https://www.comedk.org"}}
        def hta(evt):
            if exam.get() == "CET" and second_option.get() == "Register":
              
                # Open hyperlink
                webbrowser.open_new(links5[exam.get()][second_option.get()])
            elif exam.get() == "CET" and second_option.get() == "Docs. to be submitted":
              
                # Open hyperlink
                webbrowser.open_new(links5[exam.get()][second_option.get()])
            elif exam.get() == "CET" and second_option.get() == "Fee structure":
              
                # Open hyperlink
                webbrowser.open_new(links5[exam.get()][second_option.get()])
            elif exam.get() == "COMEDK" and second_option.get() == "Register":
              
                # Open hyperlink
                webbrowser.open_new(links5[exam.get()][second_option.get()])
            elif exam.get() == "COMEDK" and second_option.get() == "Docs. to be submitted":
              
                # Open hyperlink
                webbrowser.open_new(links5[exam.get()][second_option.get()])
            elif exam.get() == "COMEDK" and second_option.get() == "Fee structure":
              
                # Open hyperlink
                webbrowser.open_new(links5[exam.get()][second_option.get()])
           
           
        
           
           
        
           
           
        new_page = Frame(root)
        new_page.grid(row=0, column=0, sticky="NEWS")

        # NOTE: Options 2 is declared before first options
        # to use it in first dropdown's command, but packed later to position
        # it after the first dropdown
        second_option_values = ["Register", "Docs. to be submitted", "Fee structure"]
        second_option = StringVar(page_home)
        second_option.set("Select the info. you seek")
        options_2 = OptionMenu(new_page, second_option, *second_option_values,
                               command=hta)

        # Disable options 2 in the start
        options_2.configure(state="disabled")

        # "CET", "COMEDK", "PRIVATE EXAM" -> lists for dropdown
        # All arguments from the 3rd argument (inclusive) is considered as
        # the elements in list for the dropdown
        exam = StringVar(page_home)

        # Set default value
        exam.set("Select Exam")
        exams = OptionMenu(new_page, exam, "CET", "COMEDK", "PRIVATE EXAM",
                           command=lambda x: enable_second_options(x, options_2))

        exams.pack()
        options_2.pack()

        prev_btn = Button(new_page, text="Prev", command=prev_callback)
        prev_btn.pack()

        new_page.tkraise()

      

    elif features.get() == "Syllabi and courses":

        # If featuer is show college, the show College link page
        page_linking.tkraise()

        # Set text to college link text
        lbl_link["text"] = "Syllabi and courses " + college.get()

        # Set Hyperlink to Required college link
        lbl_link.bind("<Button-1>", lambda x: webbrowser.open_new(links3[college.get()]))
    elif features.get() == "Contact the college":

        # If featuer is show college, the show College link page
        page_linking.tkraise()

        # Set text to college link text
        lbl_link["text"] = "Contact the college " + college.get()

        # Set Hyperlink to Required college link
        lbl_link.bind("<Button-1>", lambda x: webbrowser.open_new(links4[college.get()]))
    elif features.get() == "FAQ":

        # If featuer is show college, the show College link page
        page_linking.tkraise()

        # Set text to college link text
        lbl_link["text"] = "FAQ " + college.get()

        # Set Hyperlink to Required college link
        lbl_link.bind("<Button-1>", lambda x: webbrowser.open_new(links6[college.get()]))
    elif features.get() == "Provide feedback regarding this interface":

        # If featuer is show college, the show College link page
        page_linking.tkraise()

        # Set text to college link text
        lbl_link["text"] = "Provide feedback regarding this interface " + college.get()

        # Set Hyperlink to Required college link
        lbl_link.bind("<Button-1>", lambda x: webbrowser.open_new(links7[college.get()]))
    # elif features.get() == "feature 2":
    #   open feature 2 page
    #   customize feature 2 page
    # ...


# Creating an option menu in page_home
feature_option = OptionMenu(page_home, features, "About College", "How to apply", "Syllabi and courses","Contact the college","FAQ","Provide feedback regarding this interface",
                            command=next_callback)
feature_option.configure(state="disabled")

# Positioning option menu
feature_option.pack()



#############################################################################################
def prev_callback():
    """Run when previous button is pressed"""

    # Raise home page
    page_home.tkraise()


# Create linking page
page_linking = Frame(root)
page_linking.grid(row=0, column=0, sticky='news')


lbl_link = Label(page_linking, fg="blue", cursor="hand2")
lbl_link.pack()

linking_prev_btn = Button(page_linking, text="Prev", command=prev_callback)
linking_prev_btn.pack()

# Raise Home Page
page_home.tkraise()

# Run application loop
root.mainloop()

