import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("My Collections Manager")
        
        # Main frame
        self.input_frame = tk.Frame(self.root, padx=10, pady=10)
        self.input_frame.grid(row=0, column=0, sticky=tk.NSEW)
        
        # Input button frame
        self.button_frame = tk.Frame(self.root, pady=10)
        self.button_frame.grid(row=1, column=0, sticky=tk.EW)
        
        # Right list Frame
        self.list_frame = tk.Frame(self.root, padx=10, pady=10)
        self.list_frame.grid(row=0, column=1, rowspan=2, sticky=tk.NSEW)
        
        # Main grid expansion columns config
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=0)
        
        # Input Frame popolating
        tk.Label(self.input_frame, text="Title:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.title_entry = tk.Entry(self.input_frame)
        self.title_entry.grid(row=0, column=1, sticky=tk.EW, pady=2)
        
        tk.Label(self.input_frame, text="Author/Director:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.author_entry = tk.Entry(self.input_frame)
        self.author_entry.grid(row=1, column=1, sticky=tk.EW, pady=2)
        
        tk.Label(self.input_frame, text="Year:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.year_entry = tk.Entry(self.input_frame)
        self.year_entry.grid(row=2, column=1, sticky=tk.EW, pady=2)
        
        tk.Label(self.input_frame, text="Type").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.type_entry = tk.Entry(self.input_frame)
        self.type_entry.grid(row=3, column=1, sticky=tk.EW, pady=2)
        
        # Config the 1st input Frame column to expand
        self.input_frame.columnconfigure(1, weight=1)
        
        # Button Frame popolating
        self.add_button = tk.Button(self.button_frame, text="Add", command=self._on_add_click)
        self.add_button.pack(pady=5)
        
        # List Frame popolating
        tk.Label(self.list_frame, text="Collection:").pack(anchor=tk.W)
        self.collection_listbox = tk.Listbox(self.list_frame)
        self.collection_listbox.pack(fill=tk.BOTH, expand=True)
        
    def _on_add_click(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        type = self.type_entry.get()
        print(f"Add button clicked!")
        print(f" Title: {title}")
        print(f" Author: {author}")
        print(f" Year: {year}")
        print(f" Type: {type}")
        
        if title:
            display_text = f"{title} - {author} - {year} - {type}"
            self.collection_listbox.insert(tk.END, display_text)
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
            self.year_entry.delete(0, tk.END)
            self.type_entry.delete(0, tk.END)
        
        

    