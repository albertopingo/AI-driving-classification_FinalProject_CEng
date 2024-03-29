import tkinter as tk
import tkinter.filedialog as filedialog

class Window(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("AI Driving Classification")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.frame = tk.Frame(self)
        
        
        # Add your widgets and other GUI elements here
        self.button = tk.Button(self.frame, text="Select File", command=self.select_file)
        self.button.pack()
        
        # Add a dropdown menu to select
        self.model_var = tk.StringVar(self)
        self.model_var.set("LSTM")  # Default
        self.model_dropdown = tk.OptionMenu(self.frame, self.model_var, "LSTM", "Other", command=self.select_model)
        self.model_dropdown.pack()
        
        self.canvas = tk.Canvas(self.frame, bg="white", height=303, width=303)
        self.canvas.pack()
        
        self.panel_buttons = tk.PanedWindow(self.frame)
        self.panel_buttons.pack()
        
        self.btn_run = tk.Button(master=self.panel_buttons, text="Start", command=self.run_button_clicked)
        self.btn_run.pack(side='left')

        self.btn_stop = tk.Button(master=self.panel_buttons, text="Stop", command=self.stop_button_clicked)
        self.btn_stop.pack(side='left')
        self.btn_stop['state'] = tk.DISABLED
        
        self.frame.pack()  

    def on_closing(self):
        # Add any cleanup code or actions to perform before closing the window
        self.destroy()
        
    
    def select_file(self):
        filetypes = [("CSV Files", "*.csv"), ("JSON Files", "*.json")]
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path:
            print("Selected file:", file_path)
            # print("Selected model:", self.model_var.get())
            
    def select_model(self, model):
        print("Selected model:", model)
        
    def run_button_clicked(self):
        print("Run button clicked")
        self.btn_run['state'] = tk.DISABLED
        self.btn_stop['state'] = tk.NORMAL
        
    def stop_button_clicked(self):
        print("Stop button clicked")
        self.btn_run['state'] = tk.NORMAL
        self.btn_stop['state'] = tk.DISABLED
        
            
