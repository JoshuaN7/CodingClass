import tkinter as tk

class SpreadsheetApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee Spreadsheet")
        self.geometry("400x300")
        
        self.employee_data = [
            {"first_name": "John", "last_name": "Doe", "hours_worked": 40},
            {"first_name": "Jane", "last_name": "Smith", "hours_worked": 35},
            {"first_name": "David", "last_name": "Johnson", "hours_worked": 45}
        ]
        
        self.create_spreadsheet()
    
    def create_spreadsheet(self):
        # Create headers
        headers = ["First Name", "Last Name", "Hours Worked", "Payment"]
        for col, header in enumerate(headers):
            label = tk.Label(self, text=header, relief=tk.RAISED)
            label.grid(row=0, column=col, sticky=tk.NSEW)
            self.grid_columnconfigure(col, weight=1)
        
        # Populate employee data
        for row, employee in enumerate(self.employee_data, start=1):
            first_name = tk.Label(self, text=employee["first_name"])
            last_name = tk.Label(self, text=employee["last_name"])
            hours_worked = tk.Label(self, text=str(employee["hours_worked"]))
            payment = tk.Label(self, text="${:.2f}".format(employee["hours_worked"] * 10))
            
            first_name.grid(row=row, column=0, sticky=tk.NSEW)
            last_name.grid(row=row, column=1, sticky=tk.NSEW)
            hours_worked.grid(row=row, column=2, sticky=tk.NSEW)
            payment.grid(row=row, column=3, sticky=tk.NSEW)
        
        # Adjust row and column weights
        for i in range(row + 1):
            self.grid_rowconfigure(i, weight=1)
        
        self.grid_rowconfigure(0, weight=0)  # Keep the header row fixed
    
if __name__ == "__main__":
    app = SpreadsheetApp()
    app.mainloop()
