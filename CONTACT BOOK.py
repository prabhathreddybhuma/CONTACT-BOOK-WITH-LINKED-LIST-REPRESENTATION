import tkinter as tk
from tkinter import ttk, messagebox

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None

class AddressBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.attributes("-fullscreen", True)  # Make the window full screen
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  # Set the window size to the screen size

        self.address_book_head = None

        # Heading
        self.heading_label = tk.Label(self.root, text="Contact Book", font=("Helvetica", 20, "bold"))
        self.heading_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Canvas for visualization
        self.canvas = tk.Canvas(self.root, width=1200, height=400)
        self.canvas.grid(row=1, column=0, columnspan=3, pady=10)

        self.create_ui()

    def create_ui(self):
        # Entry fields for contact information
        self.name_label = tk.Label(self.root, text="Name:", font=("Helvetica", 14))
        self.name_label.grid(row=2, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.root, style="Padded.TEntry", font=("Helvetica", 15))
        self.name_entry.grid(row=2, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.root, text="Phone:", font=("Helvetica", 14))
        self.phone_label.grid(row=3, column=0, padx=5, pady=5)
        self.phone_entry = ttk.Entry(self.root, style="Padded.TEntry", font=("Helvetica", 15))
        self.phone_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for address book management
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.grid(row=4, column=0, columnspan=2, pady=10)

        add_button = ttk.Button(self.button_frame, text="Add Contact", command=self.add_contact, style="TButton")
        add_button.grid(row=0, column=0, padx=10)

        delete_button = ttk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact, style="TButton")
        delete_button.grid(row=0, column=1, padx=10)

        display_button = ttk.Button(self.button_frame, text="Display Contacts", command=self.display_contacts, style="TButton")
        display_button.grid(row=0, column=2, padx=10)

        exit_button = ttk.Button(self.button_frame, text="Exit", command=self.exit_program, style="TButton")
        exit_button.grid(row=0, column=3, padx=10)

        # Text widget for displaying contacts
        self.contacts_text = tk.Text(self.root, height=10, width=40)
        self.contacts_text.grid(row=2, column=2, rowspan=6, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and phone:
            new_contact = Contact(name, phone)
            new_contact.next = self.address_book_head
            self.address_book_head = new_contact
            self.display_contacts()
            self.draw_linked_list()

    def delete_contact(self):
        name = self.name_entry.get()

        if not name:
            messagebox.showerror("Error", "Enter the name of the contact to delete.")
            return

        current = self.address_book_head
        prev = None

        while current:
            if current.name == name:
                if prev:
                    prev.next = current.next
                else:
                    self.address_book_head = current.next
                self.display_contacts()
                self.draw_linked_list()
                return
            prev = current
            current = current.next

        messagebox.showerror("Error", f"Contact with name '{name}' not found in the address book.")

    def display_contacts(self):
        self.contacts_text.delete(1.0, tk.END)  # Clear the text widget
        current = self.address_book_head

        while current:
            contact_info = f"Name: {current.name}\nPhone: {current.phone}\n\n"
            self.contacts_text.insert(tk.END, contact_info)
            current = current.next

    def draw_linked_list(self):
        self.canvas.delete("all")
        current = self.address_book_head
        x = 50
        y = 200
        node_width = 120
        node_height = 40

        while current:
            fill_color = "blue" if current.next else "green"
            self.canvas.create_rectangle(x, y, x + node_width, y + node_height, fill=fill_color)
            name_text = f"Name: {current.name}"
            phone_text = f"Phone: {current.phone}"
            self.canvas.create_text(x + node_width / 2, y + node_height / 4, text=name_text, fill="white", font=("Helvetica", 8, "bold"))
            self.canvas.create_text(x + node_width / 2, y + 3 * node_height / 4, text=phone_text, fill="white", font=("Helvetica", 8, "bold"))

            if current.next:
                self.draw_arrow(x + node_width, y + node_height / 2, x + node_width + 30, y + node_height / 2)

            x += node_width + 10
            current = current.next

    def draw_arrow(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="red", width=2)

    def exit_program(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AddressBookApp(root)
    root.mainloop()