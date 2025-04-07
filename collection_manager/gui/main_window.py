import tkinter as tk
from tkinter import ttk


class CategoryView(ttk.Frame):
    """Frame which will shows the category view (Cards)"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        label = ttk.Label(self, text="View Categories (Cards)")
        label.pack(padx=20, pady=20)
        
class ItemTableView(ttk.Frame):
    """Frame which will shows the table/list of a category ocjects"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        label = ttk.Label(self, text="View Objects Table (Treeviews)")
        label.pack(padx=20, pady=20)
        
        # Subframes
        # Left panel
        left_panel = ttk.Frame(self, padding="10 10 10 10")
        left_panel.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Right panel
        right_panel = ttk.Frame(self, padding="10 10 10 10")
        right_panel.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # Panels configurations
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)
        
        # Left panel population
        # Labels and Fields
        ttk.Label(left_panel, text="Title:").grid(row=0, column=0, sticky="w", pady=2)
        
        # Memorize entries
        self.title_entry = ttk.Entry(left_panel)
        self.title_entry.grid(row=0, column=1, sticky="ew", pady=2)
        
        ttk.Label(left_panel, text="Author/Director:").grid(row=1, column=0, sticky="w", pady=2)
        self.author_entry = ttk.Entry(left_panel)
        self.author_entry.grid(row=1, column=1, sticky="ew", pady=2)
        
        ttk.Label(left_panel, text="Year:").grid(row=2, column=0, sticky="w", pady=2)
        self.year_entry = ttk.Entry(left_panel)
        self.year_entry.grid(row=2, column=1, sticky="ew", pady=2) 
        
        ttk.Label(left_panel, text="Type:").grid(row=3, column=0, sticky="w", pady=2)
        self.type_entry = ttk.Entry(left_panel)
        self.type_entry.grid(row=3, column=1, sticky="ew", pady=2) 
        
        ttk.Label(left_panel, text="Status:").grid(row=4, column=0, sticky="w", pady=2)
        self.status_entry = ttk.Entry(left_panel)
        self.status_entry.grid(row=4, column=1, sticky="ew", pady=2)
        
        # Configure 1st column in left panel
        left_panel.columnconfigure(1, weight=1)
        
        # Add button ( left_panel )
        # Calling self method inner class
        self.add_button = ttk.Button(left_panel, text="Add", command=self._on_add_item_click)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=15)
        
        # Right panel population
        ttk.Label(right_panel, text="Collection:").grid(row=0, column=0, sticky="w")
        
        # Using Treeview
        columns = ("title", "author", "year", "type", "status")
        self.item_treeview =  ttk.Treeview(right_panel, columns=columns, show="headings")
        
        # Define headings
        self.item_treeview.heading("title", text="Title")
        self.item_treeview.heading("author", text="Author/Director")
        self.item_treeview.heading("year", text="Year")
        self.item_treeview.heading("type", text="Type")
        self.item_treeview.heading("status", text="Status")
        
        # Set columns width (optional)
        self.item_treeview.column("title", width=220)
        self.item_treeview.column("author", width=150)
        self.item_treeview.column("year", width=60, anchor=tk.CENTER)
        self.item_treeview.column("type", width=60, anchor=tk.CENTER)
        self.item_treeview.column("status", width=100)
        
        
        
        
        
         
        
class ItemDetailView(ttk.Frame):
    """Frame which will shows a single object details"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        label = ttk.Label(self, text="Object Detail View")
        label.pack(padx=20, pady=20)
        
class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("My Collections Manager")
        self.root.geometry("800x600")
        
        """Principal structural frames creation"""
        
        # Navbar title Frame
        self.navbar_frame = ttk.Frame(self.root, padding="5 5 5 5")
        self.navbar_frame.grid(row=0, column=0, sticky=tk.EW)
        
        # Main content Frame
        self.main_content_frame = ttk.Frame(self.root, padding="5 5 5 5")
        self.main_content_frame.grid(row=1, column=0, sticky=tk.NSEW)
        
        # Main grid rows/columns config (root)
        self.root.rowconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        # main_content_frame internal grid to expand the view
        self.main_content_frame.rowconfigure(0, weight=1)
        self.main_content_frame.columnconfigure(0, weight=1)
        
        """Creation of Views Istances"""
        
        # Creating views instances passing main_content_frame
        self.category_view = CategoryView(self.main_content_frame)
        self.item_table_view = ItemTableView(self.main_content_frame)
        self.item_detail_view = ItemDetailView(self.main_content_frame)
        
        """Initial Visualization Handling"""
        
        # At the beginning showing only cateogry view
        self.current_view = None
        self.show_category_view()
        
    # def _on_add_click(self):
    #     title = self.title_entry.get()
    #     author = self.author_entry.get()
    #     year = self.year_entry.get()
    #     type = self.type_entry.get()
    #     print(f"Add button clicked!")
    #     print(f" Title: {title}")
    #     print(f" Author: {author}")
    #     print(f" Year: {year}")
    #     print(f" Type: {type}")
        
    #     if title:
    #         display_text = f"{title} - {author} - {year} - {type}"
    #         self.collection_listbox.insert(tk.END, display_text)
    #         self.title_entry.delete(0, tk.END)
    #         self.author_entry.delete(0, tk.END)
    #         self.year_entry.delete(0, tk.END)
    #         self.type_entry.delete(0, tk.END)
    
    """Change View Methods"""
    
    def _switch_view(self, view_to_show):
        """Hide current view and show the new one"""
        if self.current_view:
            self.current_view.grid_remove()
            
        self.current_view = view_to_show
        
        # Show new view in main_content_frame grid
        self.current_view.grid(row=0, column=0, sticky=tk.NSEW)
        
    def show_category_view(self):
        """Show categories view"""
        print("Showing Categories View")
        self._switch_view(self.category_view)
        
    def show_item_table_view(self, category=None):
        """Shows the table objects view (for a certain category)"""
        print(f"Showing Objects Table View (Category: {category})")
        
        # In the future will pass category to load right datas
        # self.item_table_view.load_category(cateogry)
        self._switch_view(self.item_table_view)
        
    def show_item_detail_view(self, item=None):
        """Shows the detail view of an object"""
        print(f"Showing Detail Object View (Item: {item})")
        
        # In the future will pass item to load right datas
        # self.item_detail_view.load_item(item)
        self._switch_view(self.item_detail_view)
        

    