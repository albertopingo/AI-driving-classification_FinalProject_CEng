import tkinter as tk

import tkinter.filedialog as filedialog
import lstm as lstm

class Window(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("AI Driving Classification")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.frame = tk.Frame(self)
        
        # Options Menu
        ## Labels
        self.label_dataset = tk.Label(self.frame, text="Select Dataset:")
        self.label_model = tk.Label(self.frame, text="Select Model:")
        ## Grid with buttons
        self.label_dataset.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.label_model.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        
        ## Buttons
        ### Select File
        self.button_selectFile = tk.Button(self.frame, text="Select File", command=self.select_file)                
        ### Select Model
        self.model_var = tk.StringVar(self)
        self.model_var.set("LSTM")  # Default
        self.button_optionMenu = tk.OptionMenu(self.frame, self.model_var, "LSTM", "Other", command=self.select_model)
        ### Grid with labels
        self.button_selectFile.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.button_optionMenu.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Canvas
        self.canvas = tk.Canvas(self.frame, bg="white", height=303, width=303)
        self.canvas.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        # Start and Stop Buttons
        self.btn_start = tk.Button(master=self.frame, text="Start", command=self.run_button_clicked)
        self.btn_start.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)

        self.btn_stop = tk.Button(master=self.frame, text="Stop", command=self.stop_button_clicked)
        self.btn_stop['state'] = tk.DISABLED
        self.btn_stop.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        
        self.frame.pack()

    def on_closing(self):
        # Add any cleanup code or actions to perform before closing the window
        self.destroy()
        
    def select_file(self):
        filetypes = [("CSV Files", "*.csv"), ("JSON Files", "*.json")]
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path:
            print("Selected file:", file_path)
            print("Selected Model: ", self.model_var.get())
            if self.model_var.get() == "LSTM":
                print("Running LSTM model")
                lstm_model = lstm.LSTM()
                lstm_model.run(file_path)
            
    def select_model(self, model):
        print("Selected model:", model)
        
    def run_button_clicked(self):
        print("Run button clicked")
        self.btn_start['state'] = tk.DISABLED
        self.btn_stop['state'] = tk.NORMAL
        
    def stop_button_clicked(self):
        print("Stop button clicked")
        self.btn_start['state'] = tk.NORMAL
        self.btn_stop['state'] = tk.DISABLED
