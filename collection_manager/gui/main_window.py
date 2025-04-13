import tkinter as tk
from tkinter import ttk
from .widgets import CategoryCard

class CategoryView(ttk.Frame):
    """Frame which will shows the category view (Cards)"""
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        # # --- Static instance of a Card ---
        # placeholder_image_path = "assets/images/placeholder-img.png" 
        
        # # Define placeholder callbacks
        # def placeholder_delete(name):
        #     print(f"Delete callback called for: {name}")
            
        # def placeholder_click(name):
        #     print(f"Click callback called for: {name}")
            
        # # Create the Card
        # test_card = CategoryCard(
        #     parent=self,
        #     category_name="Test Category",
        #     image_path=placeholder_image_path,
        #     delete_callback=placeholder_delete,
        #     card_click_callback=placeholder_click
        # )
        
        # test_card.pack(padx=10, pady=10)
        
        categories_data = [
            {"name": "Books", "image": "assets/images/placeholder-img-1.png"},
            {"name": "Movies", "image": "assets/images/placeholder-img-2.png"},
            {"name": "Videogames", "image": "assets/images/placeholder-img-3.png"},
            {"name": "Music", "image": "assets/images/placeholder-img-4.png"},
            {"name": "Comics/Manga", "image": "assets/images/placeholder-img-5.png"},
            {"name": "Other", "image": "assets/images/placeholder-img-6.png"},
        ]
        
        # --- Configure internal Grid of CategoryView ---
        cards_per_row = 3
        for i in range(cards_per_row):
            # Config columns with same weight but not the rows which will be adaptive
            self.columnconfigure(i, weight=1)
            
        # --- Create and positioning Cards loop ---
        row_num = 0
        col_num = 0
        for category_data in categories_data:
            # Define callback placeholder
            def placeholder_delete(name=category_data["name"]):
                print(f"Delete callback called for: {name}")
                
            card = CategoryCard(
            parent=self,
            category_name=category_data["name"],
            image_path=category_data["image"],
            delete_callback=placeholder_delete,
            card_click_callback=self._on_card_clicked
            )
                        
            # Grid positioning the card
            card.grid(row=row_num, column=col_num, padx=10, pady=10, sticky="nsew")
            
            self.rowconfigure(row_num, weight=1)
            # Update Row and Column for the next card
            col_num += 1
            if col_num >= cards_per_row:
                col_num = 0
                row_num += 1
            
        # Placeholder for the add category button
        # add_new_card = ttk.Button(self, text="+", command=self._on_add_category)
        # add_new_card.grid(row=row_num, column=col_num, padx=10, pady=10, sticky="nsew")
        
    def _on_card_clicked(self, category_name):
        """Called from CategoryCard when a Card is clicked"""
        print(f"Card '{category_name}' clicked on CategoryView. Calling the controller...")
        
        # Using controller in MainWindow to change view
        self.controller.show_item_table_view(category_name)
            
class ItemTableView(ttk.Frame):
    """Frame which will shows the table/list of a category ocjects"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
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
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(right_panel, orient=tk.VERTICAL, command=self.item_treeview.yview)
        self.item_treeview.configure(yscroll=scrollbar.set)
        
        # Positioning Treeview and Scrollbar into right_panel grid
        self.item_treeview.grid(row=1, column=0, sticky="nsew")
        scrollbar.grid(row=1, column=1, sticky="ns")
        
        # Config right_panel rows and columns to expand Treeview
        right_panel.rowconfigure(1, weight=1)
        right_panel.columnconfigure(0, weight=1)
        
        # Set table title cateogry
        self.category_title_label = ttk.Label(right_panel, text="Seleziona una categoria", font=("Arial", 14, "bold"))
        self.category_title_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))
        
    """Method which will handle click on Add button"""
    def _on_add_item_click(self):
        # Read entry values of the class itself
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        item_type = self.type_entry.get()
        status = self.status_entry.get()
        
        # [DEBUG] message
        print("[--- DEBUG MESSAGE ---]")
        print(" Add button clicked!")
        print(f"   Title: {title}")
        print(f"   Author/Director: {author}")
        print(f"   Year: {year}")
        print(f"   Item type: {item_type}")
        print(f"   Status: {status}")
        print(f"[{"-"*21}]")
        
        # TODO: Item save logic
        
        # Add item to the Treeview
        if title:
            values_to_insert = (title, author, year, item_type, status)
            self.item_treeview.insert('', tk.END, values=values_to_insert)
            
            # Clean input fields
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
            self.year_entry.delete(0, tk.END)
            self.type_entry.delete(0, tk.END)
            self.status_entry.delete(0, tk.END)
            
        else:
            print("Title is mandatory!")
            
    def load_category_data(self, category_name):
        """Update tthe view to show data in the specified category"""
        
        # Update title 
        self.category_title_label.config(text=f"Category: {category_name or "N/A"}")
        
        # Clean Tradeview
        # get_children() returns all first level ID's rows
        for item_id in self.item_treeview.get_children():
            self.item_treeview.delete(item_id)
            
        # Emulate datas upload for selected category
        sample_items = []
        if category_name == "Books":
            sample_items = [
                {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'year': '1954'},
                {'title': 'A Song of Ice and Fire', 'author': 'G.R.R. Martin', 'year': '1996'},
                {'title': 'Foundation', 'author': 'Isaac Asimov', 'year': '1951'}
            ]
            
        elif category_name == "Movies":
            sample_items = [
                {'title': 'Blade Runner', 'author': 'Ridley Scott', 'year': '1982'},
                {'title': 'Inception', 'author': 'Christopher Nolan', 'year': '2010'},
            ]
        
        elif category_name == "Videogames":
            sample_items = [
                {'title': 'The Witcher 3', 'author': 'CD Projekt Red', 'year': '2015'},
                {'title': 'Elden Ring', 'author': 'FromSoftware', 'year': '2022'},
                {'title': 'Baldur\'s Gate 3', 'author': 'Larian Studios', 'year': '2023'}
            ]
        elif category_name == "Music":
            sample_items = [
                {'title': 'The horse and the infant', 'author': 'Jorge Rivera-Herrans', 'year': '2024'},
                {'title': 'Odysseus', 'author': 'Jorge Rivera-Herrans', 'year': '2024'}
            ]
        elif category_name == "Comics/Manga":
            sample_items = [
                {'title': 'One Piece', 'author': 'Eichiro Oda', 'year': '1997'},
                {'title': 'Naruto', 'author': 'Masashi Kishimoto', 'year': '1999'}
            ]
        elif category_name == "Other":
            sample_items = [
                {'title': 'Carbonara', 'author': 'Me', 'year': 'n.d.'}
            ]
        
        # Populating Treeview table
        for item in sample_items:
            values_to_insert = (item['title'], item['author'], item['year'])
            self.item_treeview.insert('', tk.END, values=values_to_insert)
            
        print(f"Loaded {len(sample_items)} items for {category_name} category")
            
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
        self.category_view = CategoryView(self.main_content_frame, controller=self)
        self.item_table_view = ItemTableView(self.main_content_frame)
        self.item_detail_view = ItemDetailView(self.main_content_frame)
        
        """Initial Visualization Handling"""
        
        # At the beginning showing only cateogry view
        self.current_view = None
        self.show_category_view()
        
        # TEST BUTTON
        test_button = ttk.Button(self.navbar_frame, text="Go to Item table (Test)", command=self.show_item_table_view)
        test_button.pack(side=tk.LEFT, padx=10)
        
        
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
        self.item_table_view.load_category_data(category)
        self._switch_view(self.item_table_view)
        
    def show_item_detail_view(self, item=None):
        """Shows the detail view of an object"""
        print(f"Showing Detail Object View (Item: {item})")
        
        # In the future will pass item to load right datas
        # self.item_detail_view.load_item(item)
        self._switch_view(self.item_detail_view)
        

    