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
        
        # # Main frame
        # self.input_frame = tk.Frame(self.root, padx=10, pady=10)
        # self.input_frame.grid(row=0, column=0, sticky=tk.NSEW)
        
        # # Input button frame
        # self.button_frame = tk.Frame(self.root, pady=10)
        # self.button_frame.grid(row=1, column=0, sticky=tk.EW)
        
        # # Right list Frame
        # self.list_frame = tk.Frame(self.root, padx=10, pady=10)
        # self.list_frame.grid(row=0, column=1, rowspan=2, sticky=tk.NSEW)
        
        # # Main grid expansion columns config
        # self.root.columnconfigure(0, weight=1)
        # self.root.columnconfigure(1, weight=3)
        # self.root.rowconfigure(0, weight=1)
        # self.root.rowconfigure(1, weight=0)
        
        # # Input Frame popolating
        # tk.Label(self.input_frame, text="Title:").grid(row=0, column=0, sticky=tk.W, pady=2)
        # self.title_entry = tk.Entry(self.input_frame)
        # self.title_entry.grid(row=0, column=1, sticky=tk.EW, pady=2)
        
        # tk.Label(self.input_frame, text="Author/Director:").grid(row=1, column=0, sticky=tk.W, pady=2)
        # self.author_entry = tk.Entry(self.input_frame)
        # self.author_entry.grid(row=1, column=1, sticky=tk.EW, pady=2)
        
        # tk.Label(self.input_frame, text="Year:").grid(row=2, column=0, sticky=tk.W, pady=2)
        # self.year_entry = tk.Entry(self.input_frame)
        # self.year_entry.grid(row=2, column=1, sticky=tk.EW, pady=2)
        
        # tk.Label(self.input_frame, text="Type").grid(row=3, column=0, sticky=tk.W, pady=2)
        # self.type_entry = tk.Entry(self.input_frame)
        # self.type_entry.grid(row=3, column=1, sticky=tk.EW, pady=2)
        
        # # Config the 1st input Frame column to expand
        # self.input_frame.columnconfigure(1, weight=1)
        
        # # Button Frame popolating
        # self.add_button = tk.Button(self.button_frame, text="Add", command=self._on_add_click)
        # self.add_button.pack(pady=5)
        
        # # List Frame popolating
        # tk.Label(self.list_frame, text="Collection:").pack(anchor=tk.W)
        # self.collection_listbox = tk.Listbox(self.list_frame)
        # self.collection_listbox.pack(fill=tk.BOTH, expand=True)
        
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
        

    