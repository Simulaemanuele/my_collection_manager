import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CategoryCard(ttk.Frame):
    """
    Custom widget which will represents a 'Card' for one category.
    Shows an Image, the category name and the Delete button.
    """
    def __init__(self, parent, category_name="Category Name", image_path=None, delete_callback=None, card_click_callback=None, *args, **kwargs):
        super().__init__(parent, borderwidth=2, relief="groove", padding=5, *args, **kwargs)
        
        self.cateogry_name = category_name
        self.image_path = image_path
        self.delete_callback = delete_callback
        self.card_click_callback = card_click_callback
        
        # Memorize the image to avoid garbage collection
        self._image = None
        self._image_tk = None
        
        # Set inner card's layout (image, text, button)
        self._setup_widgets()
        
        # Add bindings for clicking on card
        self._bind_events()
        
    def _setup_widgets(self):
        """Create and positioning card's inner widgets"""
        
        # --- Image Area (Placeholder) ---
        # Image Label
        self.image_label = ttk.Label(self, text="Image doesn't loaded!")
        self.image_label.pack(pady=(0, 5))
        
        
        # Load Image if path is valid
        self._load_and_display_image()
        
        # --- Text Area ---
        self.name_label = ttk.Label(self, text=self.cateogry_name, anchor="center")
        self.name_label.pack(pady=5, fill=tk.X, expand=True)
        
        # --- Delete Button (Placeholder)
        # NOTE: using simple 'X' and positioned below because according to the design is more difficult and more work is needed
        self.delete_button = ttk.Button(self, text="X", width=3, command=self._on_delete_click)
        self.delete_button.pack(pady=(5, 0), anchor="se")
        
    def _load_and_display_image(self, default_size = (100, 100)):
        """Load image if path exists"""
        if self.image_path:
            try:
                # Using Pillow to open image
                self._image = Image.open(self.image_path)
                
                # Resize image
                self._image = self._image.resize(default_size, Image.Resampling.LANCZOS)
                
                # Convert to Tkinter
                self._image_tk = ImageTk.PhotoImage(self._image)
                
                # Update label
                self.image_label.configure(image=self._image_tk, text="")
            except FileNotFoundError:
                print(f"Error: Image not found to {self.image_path}")
                self.image_label.configure(text=f"Image not found:\n{self.image_path.split('/')[-1]}")
            except Exception as e:
                print(f"Error: loading image {self.image_path}: {e}")
                self.image_label.configure(text="Image error")
        else:
            self.image_label.configure(text="No image")
            
    def _on_delete_click(self):
        """Called when clicked on delete button."""
        print(f"Delete click on: {self.cateogry_name}")
        if self.delete_callback:
            self.delete_callback(self.cateogry_name)
            
    # Method to handle click on the entire card (need to implement)
    def _on_card_click(self, event):
        print(f"Clicked on card: {self.cateogry_name}")
        if self.card_click_callback:
            self.card_click_callback(self.cateogry_name)
    
    # Method to bind events, need to call in (__init__)
    def _bind_events(self):
        # bind click to every widget
        self.bind("<Button-1>", self._on_card_click)
        self.image_label.bind("<Button-1>", self._on_card_click)
        self.name_label.bind("<Button-1>", self._on_card_click)