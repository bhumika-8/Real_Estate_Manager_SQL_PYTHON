import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime


class App:
    def __init__(self, root):
        self.root = root  
        self.root.geometry('1500x600')
        self.root.title("Real Estate Management System")
        
        self.connection = self.connect_to_db()
        
        self.logged_in = False
        self.user_role = ""
        self.user_id=0

        self.frames = []

        self.create_frames()
        self.create_menu()
        self.show_frame(0)

        self.current_date = datetime.now().date()


    def connect_to_db(self):
        try:
           
            connection = mysql.connector.connect(
                host='localhost',  
                database='PROJECT_2', 
                user='root',  
                password='krishnA!8'  
            )
            if connection.is_connected():
                print("Successfully connected to the database")
                return connection
        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("Database Error", f"Failed to connect to the database: {e}")
            return None

    def create_frames(self):
        self.sign_in_frame = tk.Frame(self.root)
        self.sign_in_frame.configure(width=1500, height=600)
        self.heading_1 = tk.Label(self.sign_in_frame, text="LOGIN",font=("Helvetica", 16))
        self.heading_1.pack(pady=20)
        self.user_name = tk.Label(self.sign_in_frame, text="USERNAME")
        self.user_name.pack()
        self.user_text = tk.Text(self.sign_in_frame, height=1)
        self.user_text.pack(padx=110)
        self.pass_word = tk.Label(self.sign_in_frame, text="PASSWORD")
        self.pass_word.pack()
        self.pass_txt = tk.Entry(self.sign_in_frame, show="*")
        self.pass_txt.pack()
        self.sign_button = tk.Button(self.sign_in_frame, text="Submit",command=self.login)
        self.sign_button.pack(pady=10)
        self.clear_button = tk.Button(self.sign_in_frame, text="Clear", command=self.clear_sign_in_fields)
        self.clear_button.pack()
        self.frames.append(self.sign_in_frame)

        self.register_in = tk.Frame(self.root)
        self.register_in.configure(width=1500, height=600)
        self.heading_2 = tk.Label(self.register_in, text="REGISTER",font=("Helvetica", 16))
        self.heading_2.pack(pady=20)
        self.user_name_reg = tk.Label(self.register_in, text="USERNAME")
        self.user_name_reg.pack()
        self.user_text_reg = tk.Text(self.register_in, height=1)
        self.user_text_reg.pack(padx=110)
        self.email_label = tk.Label(self.register_in, text="Email")
        self.email_label.pack()
        self.email_text = tk.Text(self.register_in, height=1)
        self.email_text.pack(padx=110)
        self.pass_word_reg = tk.Label(self.register_in, text="PASSWORD")
        self.pass_word_reg.pack()
        self.pass_txt_reg = tk.Entry(self.register_in, show="*")
        self.pass_txt_reg.pack()
 
        self.agent_details_frame = tk.Frame(self.register_in)
        self.agent_details_frame.configure(width=1500, height=400)
        tk.Label(self.agent_details_frame, text="License Number").pack()
        self.lic_no = tk.Text(self.agent_details_frame, height=1)
        self.lic_no.pack(padx=110)
        tk.Label(self.agent_details_frame, text="Phone Number").pack()
        self.phone = tk.Text(self.agent_details_frame, height=1)
        self.phone.pack(padx=110)
        tk.Label(self.agent_details_frame, text="Rating").pack()
        self.rat_no = tk.Text(self.agent_details_frame, height=1)
        self.rat_no.pack(padx=180)
        
        self.agent_details_frame.pack_forget()  

        
        tk.Button(self.register_in, text="Are you an agent?", command=self.show_agent_details).pack()
        self.reg_button = tk.Button(self.register_in, text="Submit",command=self.register)
        self.reg_button.pack(pady=10)
        self.clear_button_reg = tk.Button(self.register_in, text="Clear", command=self.clear_register_fields)
        self.clear_button_reg.pack()
        self.frames.append(self.register_in)

        self.insert_property_frame = tk.Frame(self.root)
        self.insert_property_frame.pack_propagate(False)
        self.insert_property_frame.configure(width=1500, height=600)
        tk.Label(self.insert_property_frame, text="Insert Property",font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.insert_property_frame, text="Property ID").pack()
        self.property_id_insert = tk.Text(self.insert_property_frame, height=1, width=30)
        self.property_id_insert.pack()
        tk.Label(self.insert_property_frame, text="Title").pack()
        self.title_insert = tk.Text(self.insert_property_frame, height=1, width=30)
        self.title_insert.pack()
        tk.Label(self.insert_property_frame, text="Description").pack()
        self.desc_insert = tk.Text(self.insert_property_frame, height=3, width=30)
        self.desc_insert.pack()
        tk.Label(self.insert_property_frame, text="Price").pack()
        self.price_insert = tk.Text(self.insert_property_frame, height=1, width=30)
        self.price_insert.pack()
        tk.Label(self.insert_property_frame, text="Location").pack()
        self.location_insert = tk.Text(self.insert_property_frame, height=1, width=30)
        self.location_insert.pack()
        tk.Label(self.insert_property_frame, text="Size").pack()
        self.size_insert = tk.Text(self.insert_property_frame, height=1, width=30)
        self.size_insert.pack()
        self.submit_insert = tk.Button(self.insert_property_frame, text="Submit",command=self.insert_property)
        self.submit_insert.pack(pady=10)
        self.frames.append(self.insert_property_frame)

        self.update_property_frame = tk.Frame(self.root)
        self.update_property_frame.pack_propagate(False)
        self.update_property_frame.configure(width=1500, height=600)
        tk.Label(self.update_property_frame, text="Update Property",font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.update_property_frame, text="Property ID").pack()
        self.property_id_update = tk.Text(self.update_property_frame, height=1, width=30)
        self.property_id_update.pack()
        tk.Label(self.update_property_frame, text="Title").pack()
        self.title_update = tk.Text(self.update_property_frame, height=1, width=30)
        self.title_update.pack()
        tk.Label(self.update_property_frame, text="Description").pack()
        self.desc_update = tk.Text(self.update_property_frame, height=3, width=30)
        self.desc_update.pack()
        tk.Label(self.update_property_frame, text="Price").pack()
        self.price_update = tk.Text(self.update_property_frame, height=1, width=30)
        self.price_update.pack()
        tk.Label(self.update_property_frame, text="Location").pack()
        self.location_update = tk.Text(self.update_property_frame, height=1, width=30)
        self.location_update.pack()
        tk.Label(self.update_property_frame, text="Size").pack()
        self.size_update = tk.Text(self.update_property_frame, height=1, width=30)
        self.size_update.pack()
        self.update_button = tk.Button(self.update_property_frame, text="Update",command=self.update_property)
        self.update_button.pack(pady=10)
        self.frames.append(self.update_property_frame)

        self.delete_property_frame = tk.Frame(self.root)
        self.delete_property_frame.pack_propagate(False)
        self.delete_property_frame.configure(width=1500, height=600)
        tk.Label(self.delete_property_frame, text="Delete Property",font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.delete_property_frame, text="Property ID").pack()
        self.property_id_delete = tk.Text(self.delete_property_frame, height=1, width=30)
        self.property_id_delete.pack()
        self.delete_button = tk.Button(self.delete_property_frame, text="Delete",command=self.delete_property)
        self.delete_button.pack(pady=10)
        self.frames.append(self.delete_property_frame)

        self.add_to_favorite_frame = tk.Frame(self.root)
        self.add_to_favorite_frame.pack_propagate(False)
        self.add_to_favorite_frame.configure(width=1500, height=600)
        tk.Label(self.add_to_favorite_frame, text="Add to Favorite", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.add_to_favorite_frame, text="Property ID").pack()
        self.property_id_fav = tk.Text(self.add_to_favorite_frame, height=1, width=30)
        self.property_id_fav.pack(pady=10)
        self.add_fav_button = tk.Button(self.add_to_favorite_frame, text="Add to Favorite",command=self.add_fav)
        self.add_fav_button.pack(pady=20)
        self.frames.append(self.add_to_favorite_frame)

        self.add_transaction_frame = tk.Frame(self.root)
        self.add_transaction_frame.pack_propagate(False)
        self.add_transaction_frame.configure(width=1500, height=600)
        tk.Label(self.add_transaction_frame, text="Add Transaction", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.add_transaction_frame, text="Transaction ID").pack()
        self.transaction_id_entry = tk.Text(self.add_transaction_frame, height=1, width=30)
        self.transaction_id_entry.pack(pady=5)
        tk.Label(self.add_transaction_frame, text="Property ID").pack()
        self.property_id_trans_entry = tk.Text(self.add_transaction_frame, height=1, width=30)
        self.property_id_trans_entry.pack(pady=5)
        tk.Label(self.add_transaction_frame, text="Buyer Username").pack()
        self.buyer_username_entry = tk.Text(self.add_transaction_frame, height=1, width=30)
        self.buyer_username_entry.pack(pady=5)
        tk.Label(self.add_transaction_frame, text="Transaction Amount").pack()
        self.transaction_amount_entry = tk.Text(self.add_transaction_frame, height=1, width=30)
        self.transaction_amount_entry.pack(pady=5)
        self.add_transaction_button = tk.Button(self.add_transaction_frame, text="Add Transaction",command=self.add_transaction)
        self.add_transaction_button.pack(pady=20)
        self.frames.append(self.add_transaction_frame)

        
        self.find_properties_location_frame = tk.Frame(self.root)
        self.find_properties_location_frame.pack_propagate(False)
        self.find_properties_location_frame.configure(width=1500, height=600)
        tk.Label(self.find_properties_location_frame, text="Find Properties by Location", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.find_properties_location_frame, text="Location").pack()
        self.location_entry = tk.Text(self.find_properties_location_frame, height=1, width=30)
        self.location_entry.pack(pady=5)
        self.find_properties_location_button = tk.Button(self.find_properties_location_frame, text="Find Properties",command=self.view_properties_by_location)
        self.find_properties_location_button.pack(pady=20)
        self.frames.append(self.find_properties_location_frame)


        self.find_properties_price_frame = tk.Frame(self.root)
        self.find_properties_price_frame.pack_propagate(False)
        self.find_properties_price_frame.configure(width=1500, height=600)
        tk.Label(self.find_properties_price_frame, text="Find Properties by Price Range", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.find_properties_price_frame, text="Starting Price").pack()
        self.starting_price_entry = tk.Text(self.find_properties_price_frame, height=1, width=30)
        self.starting_price_entry.pack(pady=5)
        tk.Label(self.find_properties_price_frame, text="Ending Price").pack()
        self.ending_price_entry = tk.Text(self.find_properties_price_frame, height=1, width=30)
        self.ending_price_entry.pack(pady=5)
        self.find_properties_price_button = tk.Button(self.find_properties_price_frame, text="Find Properties",command=self.view_properties_by_price)
        self.find_properties_price_button.pack(pady=20)
        self.frames.append(self.find_properties_price_frame)

        self.view_frame=tk.Frame(self.root)
        self.view_frame.pack_propagate(False)
        self.view_frame.configure(width=1500, height=600)
        self.frames.append(self.view_frame)

        self.view_fav=tk.Frame(self.root)
        self.view_fav.pack_propagate(False)
        self.view_fav.configure(width=1500, height=600)
        self.frames.append(self.view_fav)

        self.view_trans_frame=tk.Frame(self.root)
        self.view_trans_frame.pack_propagate(False)
        self.view_trans_frame.configure(width=1500, height=600)
        self.frames.append(self.view_trans_frame)  

        self.view_my_frame=tk.Frame(self.root)
        self.view_my_frame.pack_propagate(False)
        self.view_my_frame.configure(width=1500, height=600)
        self.frames.append(self.view_my_frame)  #12


    def create_menu(self):
        self.upmenu = tk.Menu(self.root)
        self.in_menu = tk.Menu(self.upmenu, tearoff=0)
        self.in_menu.add_command(label="Login", command=lambda: self.show_frame(0))
        self.in_menu.add_command(label="Register", command=lambda: self.show_frame(1))
        self.upmenu.add_cascade(menu=self.in_menu, label="Entry")
        self.property_menu=tk.Menu(self.upmenu,tearoff=0)
        self.property_menu.add_command(label="Insert Property",command=lambda:self.show_frame(2))
        self.property_menu.add_command(label="Update Property",command=lambda:self.show_frame(3))
        self.property_menu.add_command(label="Delete Property",command=lambda:self.show_frame(4))
        self.upmenu.add_cascade(menu=self.property_menu,label="Property")
        self.view_prop=tk.Menu(self.update_button,tearoff=0)
        self.view_prop.add_command(label="View all properties",command=lambda:self.view_all_properties())
        self.view_prop.add_command(label="Add to favourites",command=lambda:self.show_frame(5))
        self.view_prop.add_command(label="View my favorite",command=lambda:self.view_my_fav())
        self.view_prop.add_command(label="View my properties",command=lambda:self.view_my_prop())
        self.upmenu.add_cascade(menu=self.view_prop,label="View")
        self.trans_menu=tk.Menu(self.upmenu,tearoff=0)
        self.trans_menu.add_command(label="Add transaction",command=lambda:self.show_frame(6))
        self.trans_menu.add_command(label="View my Transactions",command=lambda:self.view_trans())
        self.upmenu.add_cascade(menu=self.trans_menu,label="Transactions")
        self.find_prop=tk.Menu(self.upmenu,tearoff=0)
        self.find_prop.add_command(label="Location",command=lambda:self.show_frame(7))
        self.find_prop.add_command(label="Price Range",command=lambda:self.show_frame(8))
        self.upmenu.add_cascade(menu=self.find_prop,label="Find Properties")
        
        self.root.config(menu=self.upmenu)


    def show_frame(self, frame_index):
        for frame in self.frames:
            frame.pack_forget()
        
        self.frames[frame_index].pack(fill='both', expand=True)

    def show_agent_details(self):
        self.agent_details_frame.pack(fill='both', expand=True)

    def clear_sign_in_fields(self):
        self.user_text.delete('1.0', tk.END)
        self.pass_txt.delete(0, tk.END)

    def clear_register_fields(self):
        self.user_text_reg.delete('1.0', tk.END)
        self.email_text.delete('1.0', tk.END)
        self.pass_txt_reg.delete(0, tk.END)
        self.lic_no.delete('1.0', tk.END)
        self.phone.delete('1.0', tk.END)
        self.rat_no.delete('1.0', tk.END)
    
    def login(self):
        username = self.user_text.get('1.0', tk.END).strip()  
        password = self.pass_txt.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password.")
            return

        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT role, user_id FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                self.user_role = result[0]  
                self.user_id = result[1]    
                self.logged_in = True
                self.view_all_properties()

                messagebox.showinfo("Login Success", f"Welcome {username}!")
                
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            if cursor:
                cursor.close()

    def register(self):
        
        username = self.user_text_reg.get("1.0", tk.END).strip()  
        password = self.pass_txt_reg.get().strip()
        email = self.email_text.get("1.0", tk.END).strip()
        license_number = self.lic_no.get("1.0", tk.END).strip()  
        phone_number = self.phone.get("1.0", tk.END).strip()  
        rating = self.rat_no.get("1.0", tk.END).strip()  

        if not username or not password or not email:
            messagebox.showerror("Error", "All fields are required!")
            return

        role = 'customer'  

        try:
            cursor = self.connection.cursor()
            cursor.callproc('insert_user', [username, password, email, role])
            self.connection.commit()

            cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
            self.user_id = cursor.fetchone()[0]  

            if license_number and phone_number and rating:
                role = 'agent'  
                cursor.execute("UPDATE users SET role='agent' WHERE user_id=%s",(self.user_id,))
                cursor.callproc('insert_agent', [self.user_id, license_number, phone_number, rating])
                self.connection.commit()

            messagebox.showinfo("Success", f"{role.capitalize()} registered successfully!")

        except Exception as e:
            self.connection.rollback()  
            messagebox.showerror("Error", f"Error registering {role}: {e}")

        finally:
            if cursor:
                cursor.close()


    
    def insert_property(self):
        
        if not self.logged_in:  
            messagebox.showerror("Error", "You must log in first!")
            return

        
        if self.user_role != 'agent':  
            messagebox.showerror("Error", "Only agents can insert properties!")
            return
            
        property_id = self.property_id_insert.get("1.0", tk.END)  
        title = self.title_insert.get("1.0", tk.END)  
        description = self.desc_insert.get("1.0", tk.END) 
        price = self.price_insert.get("1.0", tk.END)  
        location = self.location_insert.get("1.0", tk.END) 
        size = self.size_insert.get("1.0", tk.END)  

        if not property_id or not title or not description or not price or not location or not size:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT agent_id FROM agents WHERE user_id = %s", (self.user_id,))
            agent_id = cursor.fetchone()

            if not agent_id:
                messagebox.showerror("Error", "Agent not found in database!")
                return

            agent_id = agent_id[0]  

            cursor.callproc('insert_property', [property_id, agent_id, title, description, location, price, size,self.current_date])

            self.connection.commit()

            messagebox.showinfo("Success", "Property inserted successfully!")
            property_id = self.property_id_insert.delete("1.0", tk.END) 
            title = self.title_insert.delete("1.0", tk.END)  
            description = self.desc_insert.delete("1.0", tk.END)  
            price = self.price_insert.delete("1.0", tk.END)  
            location = self.location_insert.delete("1.0", tk.END)  
            size = self.size_insert.delete("1.0", tk.END)  

        except Exception as e:
            self.connection.rollback()  
            messagebox.showerror("Error", f"Error inserting property: {e}")


    def update_property(self):
        if not self.logged_in: 
            messagebox.showerror("Error", "You must log in first!")
            return

        if self.user_role != 'agent':  
            messagebox.showerror("Error", "Only agents can insert properties!")
            return

        property_id = self.property_id_update.get("1.0", tk.END)  
        title = self.title_update.get("1.0", tk.END)  
        description = self.desc_update.get("1.0", tk.END)  
        price = self.price_update.get("1.0", tk.END)  
        location = self.location_update.get("1.0", tk.END) 
        size = self.size_update.get("1.0", tk.END)  

        if not property_id or not title or not description or not price or not location or not size:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT agent_id FROM agents WHERE user_id = %s", (self.user_id,))
            agent_id = cursor.fetchone()

            if not agent_id:
                messagebox.showerror("Error", "Agent not found in database!")
                return

            agent_id = agent_id[0]  

            
            cursor.callproc('update_property_2', [property_id, agent_id, title, description, location, price, size,self.current_date])

            
            self.connection.commit()

            messagebox.showinfo("Success", "Property updated successfully!")
            property_id = self.property_id_update.delete("1.0", tk.END)  
            title = self.title_update.delete("1.0", tk.END)  
            description = self.desc_update.delete("1.0", tk.END)  
            price = self.price_update.delete("1.0", tk.END)  
            location = self.location_update.delete("1.0", tk.END)  
            size = self.size_update.delete("1.0", tk.END)  

        except Exception as e:
            self.connection.rollback()  
            messagebox.showerror("Error", f"Error updating property: {e}")


    def delete_property(self):
        if not self.logged_in:  
            messagebox.showerror("Error", "You must log in first!")
            return

        if self.user_role != 'agent':  
            messagebox.showerror("Error", "Only agents can delete properties!")
            return

        property_id = self.property_id_delete.get("1.0", tk.END)

        if not property_id:
            messagebox.showerror("Error", "Property ID is required!")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT agent_id FROM agents WHERE user_id = %s", (self.user_id,))
            agent_id = cursor.fetchone()

            if not agent_id:
                messagebox.showerror("Error", "Agent not found in database!")
                return

            agent_id = agent_id[0]  

            cursor.execute("SELECT property_id FROM properties WHERE property_id = %s AND agent_id = %s", (property_id, agent_id))
            property = cursor.fetchone()

            if not property:
                messagebox.showerror("Error", "This property does not belong to you!")
                return

            cursor.callproc('delete_property', [property_id])
            self.connection.commit()

            messagebox.showinfo("Success", "Property deleted successfully!")
            property_id = self.property_id_delete.delete("1.0", tk.END)

        except Exception as e:
            self.connection.rollback() 
            messagebox.showerror("Error", f"Error deleting property: {e}")
    
    
    def view_all_properties(self):
        if not self.logged_in:  
            messagebox.showerror("Error", "You must log in first!")
            return

        cursor = None  

        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM active_properties"  
            cursor.execute(query)
            properties = cursor.fetchall()
            for widget in self.frames[7].winfo_children():
                    widget.destroy()
            self.show_frame(9)

            if properties:
                columns = [desc[0] for desc in cursor.description]  
                tree = ttk.Treeview(self.frames[9], columns=columns, show='headings')

                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=150)

                for row in properties:
                    tree.insert('', 'end', values=row)

                tree.pack(fill=tk.BOTH, expand=True)
            else:
                tk.Label(self.frames[9], text="No properties found.", fg="blue").pack()

        except Exception as e:
            tk.Label(self.frames[9], text=f"Error fetching properties: {str(e)}", fg="red").pack()
        finally:
            if cursor:
                cursor.close()


    def view_my_fav(self):
       
        if not self.logged_in:  
            messagebox.showerror("Error", "You must log in first!")
            return

        cursor = None 

        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM favorites WHERE user_id=%s"
            cursor.execute(query, (self.user_id,))  

            properties = cursor.fetchall()
            for widget in self.frames[7].winfo_children():
                    widget.destroy()
            self.show_frame(10)

            if properties:
                columns = [desc[0] for desc in cursor.description]  
                tree = ttk.Treeview(self.frames[10], columns=columns, show='headings')
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=150)
                for row in properties:
                    tree.insert('', 'end', values=row)

                tree.pack(fill=tk.BOTH, expand=True)
                cursor.execute("SELECT MIN(p.price) FROM properties as p INNER JOIN favorites as f on f.property_id=p.property_id WHERE f.user_id=%s ;", (self.user_id,))
                text_display = cursor.fetchone()
                if text_display  is not None:
                    tk.Label(self.frames[10], text=f"Price: {text_display[0]} ", fg="red").pack()
                else:
                    tk.Label(self.frames[10], text="No properties found or no price data available.", fg="blue").pack()

            else:
                tk.Label(self.frames[10], text="No properties found.", fg="blue").pack()

        except Exception as e:
            tk.Label(self.frames[10], text=f"Error fetching properties: {str(e)}", fg="red").pack()
        finally:
            if cursor:
                cursor.close()

    def view_trans(self):
        
        if not self.logged_in:  
            messagebox.showerror("Error", "You must log in first!")
            return

        if self.user_role != 'agent':  
            messagebox.showerror("Error", "Only agents can delete properties!")
            return

        cursor = None  

        try:
            cursor = self.connection.cursor()

            
            query = ("SELECT * FROM transactions WHERE property_id IN ( SELECT property_id FROM properties WHERE agent_id = (SELECT agent_id FROM agents WHERE user_id = %s))")


            cursor.execute(query, (self.user_id,))  
            properties = cursor.fetchall()
            for widget in self.frames[7].winfo_children():
                    widget.destroy()
            self.show_frame(11)

            if properties:
    
                columns = [desc[0] for desc in cursor.description]  
                tree = ttk.Treeview(self.frames[11], columns=columns, show='headings')
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=150)

                for row in properties:
                    tree.insert('', 'end', values=row)

                tree.pack(fill=tk.BOTH, expand=True)
            else:
                tk.Label(self.frames[11], text="No properties found.", fg="blue").pack()

        except Exception as e:
            tk.Label(self.frames[11], text=f"Error fetching properties: {str(e)}", fg="red").pack()
        finally:
            if cursor:
                cursor.close()

    def view_properties_by_location(self):
        if not self.logged_in:  
            messagebox.showerror("Error", "You must log in first!")
            return
        
        loc=self.location_entry.get("1.0",tk.END).strip()

        if not loc:
            messagebox.showerror("Error", "Location cannot be empty!")
            return

        cursor = None
        try:
            cursor = self.connection.cursor()
            
            query = "SELECT * FROM properties WHERE location=%s"

            cursor.execute(query, (loc,))  

            properties = cursor.fetchall()
            self.show_frame(7)

            if properties:
                columns = [desc[0] for desc in cursor.description]  
                tree = ttk.Treeview(self.frames[7], columns=columns, show='headings')
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=150)

                for row in properties:
                    tree.insert('', 'end', values=row)

                tree.pack(fill=tk.BOTH, expand=True)
            else:
                tk.Label(self.frames[7], text="No properties found in this location!", fg="blue").pack()

        except Exception as e:
            tk.Label(self.frames[7], text=f"Error fetching properties: {str(e)}", fg="red").pack()
        finally:
            if cursor:
                cursor.close()


    def view_properties_by_price(self):
        if not self.logged_in:  
            messagebox.showerror("Error", "You must log in first!")
            return
        
        s_price = self.starting_price_entry.get("1.0", tk.END)
        e_price= self.ending_price_entry.get("1.0",tk.END)  

        if not s_price and e_price:
            messagebox.showerror("Error", "Location cannot be empty!")
            return

        cursor = None
        try:
            cursor = self.connection.cursor()
            
            query = "SELECT * FROM active_properties WHERE price BETWEEN %s AND %s ORDER BY price"

            cursor.execute(query, (s_price,e_price,))  

            properties = cursor.fetchall()
            self.show_frame(8)

            if properties:
                columns = [desc[0] for desc in cursor.description]  
                tree = ttk.Treeview(self.frames[8], columns=columns, show='headings')
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=150)

                for row in properties:
                    tree.insert('', 'end', values=row)

                tree.pack(fill=tk.BOTH, expand=True)
            else:
                tk.Label(self.frames[8], text="No properties found for this price range.", fg="blue").pack()

        except Exception as e:
            tk.Label(self.frames[8], text=f"Error fetching properties: {str(e)}", fg="red").pack()
        finally:
            if cursor:
                cursor.close()


    def view_my_prop(self):
        if not self.logged_in:  
            messagebox.showerror("Error", "You must log in first!")
            return
        

        cursor = None
        try:
            cursor = self.connection.cursor()
            
            query = "SELECT * FROM properties WHERE agent_id =(SELECT agent_id FROM agents WHERE user_id=%s)"

            cursor.execute(query, (self.user_id,))  

            properties = cursor.fetchall()
            for widget in self.frames[7].winfo_children():
                if isinstance(widget, ttk.Treeview):
                    widget.destroy()

            
            self.show_frame(12)

            if properties:
                columns = [desc[0] for desc in cursor.description]  
                tree = ttk.Treeview(self.frames[12], columns=columns, show='headings')
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=150)

                for row in properties:
                    tree.insert('', 'end', values=row)

                tree.pack(fill=tk.BOTH, expand=True)
            else:
                tk.Label(self.frames[12], text="No properties found for this location.", fg="blue").pack()

        except Exception as e:
            tk.Label(self.frames[12], text=f"Error fetching properties: {str(e)}", fg="red").pack()
        finally:
            if cursor:
                cursor.close()


    def add_fav(self):
        if not self.logged_in:  
            messagebox.showerror("Error", "You must log in first!")
            return

        property_id = self.property_id_fav.get("1.0", tk.END)

       
        if not property_id:
            messagebox.showerror("Error", "Property ID is required!")
            return

        try:
            cursor = self.connection.cursor()
            
           
            cursor.callproc('add_to_favorites', [self.user_id,property_id])
            self.connection.commit()

            messagebox.showinfo("Success", "Property added to favourites successfully successfully!")

        except Exception as e:
            self.connection.rollback()  
            messagebox.showerror("Error", f"Error adding property to favourites: {e}")


    def add_transaction(self):
        
        if not self.logged_in:  
            messagebox.showerror("Error", "You must log in first!")
            return
        
        if self.user_role != 'agent':  
            messagebox.showerror("Error", "You must be an agent to add transactions!")
            return

        cursor = None
        try:
            cursor = self.connection.cursor()
            # cursor.execute("SELECT agent_id FROM agents WHERE user_id = %s", (self.user_id,))
            # agent = cursor.fetchone()

            # if not agent:
            #     messagebox.showerror("Error", "No agent found for this user!")
            #     return

            # agent_id = agent[0]  

            transaction_id = self.transaction_id_entry.get("1.0", tk.END).strip() 
            property_id = self.property_id_trans_entry.get("1.0", tk.END).strip()
            buyer_username = self.buyer_username_entry.get("1.0", tk.END).strip()
            transaction_amount = self.transaction_amount_entry.get("1.0", tk.END).strip()

            if not transaction_id or not property_id or not buyer_username or not transaction_amount:
                messagebox.showerror("Error", "All fields must be filled out!")
                return

            cursor.callproc("add_transaction", (
                int(transaction_id), int(property_id), buyer_username, float(transaction_amount)))

            self.connection.commit()

           
            messagebox.showinfo("Success", "Transaction added successfully!")

            self.transaction_id_entry.delete("1.0", "end")
            self.property_id_trans_entry.delete("1.0", "end")
            self.buyer_username_entry.delete("1.0", "end")
            self.transaction_amount_entry.delete("1.0", "end")

        except Exception as e:
            messagebox.showerror("Error", f"Error adding transaction: {str(e)}")
        finally:
            if cursor:
                cursor.close()




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

