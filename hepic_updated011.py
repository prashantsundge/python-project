import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import *

# Function to perform search in MySQL database
def search_records():
    number = search_entry.get()
    connection = None  # Define connection variable
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='connx_db',
                                             user='root',
                                             password='root')
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT * FROM nutreco_final_db WHERE telephone = %s"
            cursor.execute(query, (number,))
            records = cursor.fetchall()
            
            if records:
                # results_listbox.delete(0, tk.END)
                # for record in records:
                #     results_listbox.insert(tk.END, record)
                results_text.delete("1.0", tk.END)  # Clear previous results
                # Display column names
                column_names = [i[0] for i in cursor.description]
                results_text.insert(tk.END, " | ".join(column_names) + "\n")
                # Display records
                for record in records:
                    results_text.insert(tk.END, " | ".join(map(str, record)) + "\n")
                    
               
            else:
                messagebox.showinfo("Info", "No records found for the given number.")
                    
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
        messagebox.showerror("Error", "Error while connecting to MySQL database.")
    finally:
        if connection and connection.is_connected():  # Check if connection is not None
            cursor.close()
            connection.close()

# Create main window
root = tk.Tk()
root.title("Search Records")
root.geometry("1366x768+0+0")

lbtitle=Label(root, bd=20,relief=RIDGE,text="HEPIC DID FINDER", fg='Blue',bg='White',font=('Times new Roman',50,'bold'))
lbtitle.pack(side=TOP,fill=X)

#=======================Dataframe======================================

Dataframe=Frame(root,bd=20,relief=RIDGE)
Dataframe.place(x=0,y=130,width=1530,height=100)

# ===========================Button Frame===============================

# # Create frame for search bar
# search_frame = tk.Frame(root,highlightbackground="blue", highlightthickness=2)
# search_frame.pack(padx=30,pady=30)

# Create search label
search_label = tk.Label(Dataframe, bd=10,relief=RIDGE, text="Enter telephone Number to Search:",fg='black',bg='White',font=('Times new Roman',28,'bold'))
search_label.pack(side=tk.LEFT)


# Create search entry
search_entry = tk.Entry(Dataframe,fg='black',bg='White',font=("Helvetica", 14), bd=2, relief=tk.SOLID)
search_entry.pack(side=tk.LEFT, padx=10, pady=10)


# Create search button
search_button = tk.Button(Dataframe, text="Search",bd=4, fg='Black',bg='Grey',font=('Times new Roman',18,'bold'),command=search_records)
search_button.pack(side=tk.LEFT, padx=10)

#==================================Result pane======================================

# Create frame for results
# results_frame = tk.Frame(root)
# results_frame.pack(pady=10)
results_frame=Frame(root,bd=20,relief=RIDGE)
results_frame.place(x=0,y=250,width=1530,height=400)

# # # Create scrollbar for results
# scrollbar = tk.Scrollbar(results_frame)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# Create listbox to display results
# results_text = tk.Listbox(results_frame, width=1530)
# results_text.pack()



# Create text widget to display results
results_text = tk.Text(results_frame, font=("Helvetica", 12), wrap=tk.WORD)
results_text.pack(fill=tk.BOTH, expand=True)

# # # Configure scrollbar
# scrollbar.config(command=results_listbox.yview)

root.mainloop()
