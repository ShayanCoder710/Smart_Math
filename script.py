import customtkinter as ctk
from tkinter import messagebox
import webbrowser
import math





app = ctk.CTk()
app.geometry("700x370")
app.title("Smart math 8")
app.resizable(False , False)



ctk.set_appearance_mode("Dark")
app.configure(fg_color = "gray")



frame = ctk.CTkFrame(app , corner_radius = 6 , border_color = 'white' , border_width = 3)
frame.pack(pady = 10)
frame.configure(fg_color = "#dadada")



label = ctk.CTkLabel(frame , text = "Smart math" , text_color = "#161616" , font = ("ubuntu" , 30))
label.grid(row = 0 , column = 0 , pady = 17 , padx = 269)



frame2 = ctk.CTkFrame(app , corner_radius = 10 , border_color = 'white' , border_width = 3)
frame2.pack(fill = "both" , expand = True)
frame2.configure(fg_color = "gray")



def open_square_root():
    

    window = ctk.CTkToplevel(app)
    window.geometry("265x300")
    window.title("Square Root")
    window.resizable(False , False)
    window.configure(fg_color = "gray")


    frame = ctk.CTkFrame(window , corner_radius = 10 , border_color = 'white' , border_width = 3)
    frame.pack(fill = "both" , expand = True , padx = 14 , pady = 10)
    frame.configure(fg_color = "#dadada")


    label = ctk.CTkLabel(frame , text = "Square Root Calculator" , text_color = "#161616" , font = ("ubuntu" , 20))
    label.grid(row = 0 , column = 0 , pady = 15 , padx = 10 , sticky = "ew")


    e1 = ctk.CTkEntry(frame , placeholder_text = "Enter A Number" , font = ("ubuntu" , 16) , height = 40 , justify = "center")
    e1.grid(row = 1 , column = 0 , pady = 10 , padx = 20 , sticky = "ew")


    resultl = ctk.CTkLabel(frame , text = "" , height = 37 , font = ("ubuntu" , 18) , fg_color = "#727272" , text_color = "white" , corner_radius = 8)
    resultl.grid(row = 2 , column = 0 , pady = 15 , padx = 20 , sticky = "ew")


    def calculate_sqrt():
        num_str = e1.get().strip()


        if not num_str:
            messagebox.showerror("Error" , "Please enter a number.")

        elif not num_str.replace('.' , '' , 1).isdigit():
            messagebox.showerror("Error" , "Please enter a valid number.")

        else:
            num = float(num_str)
            
            if num < 0:
                messagebox.showerror("Error" , "Cannot calculate square root of negative number.")
            else:
                res = math.sqrt(num)
                resultl.configure(text = f"Result = {res:.3f}")


    btn = ctk.CTkButton(frame , text = "Calculate" , font = ("ubuntu" , 18) , command = calculate_sqrt , height = 45 , fg_color = "#2D6EAF" , hover_color = "#1a4a80")
    btn.grid(row = 3 , column = 0 , pady = 20 , padx = 20 , sticky = "ew")


btn = ctk.CTkButton(frame2 , width = 213 , height = 40 , text = "Square Root" , font = ("ubuntu" , 23) , text_color = "#1D1D1D" , fg_color = "#e6e6e6", hover_color = "#c5c5c5" , command = open_square_root) 
btn.grid(row = 0 , column = 0 , pady = 10 , padx = 10)



def open_power():

    window = ctk.CTkToplevel(app)
    window.geometry("480x340")
    window.title("Power")
    window.resizable(True , False)
    window.configure(fg_color = "gray")


    frame = ctk.CTkFrame(window , corner_radius = 10 , border_color = 'white' , border_width = 3)
    frame.pack(fill = "both" , expand = True , padx = 15 , pady = 10)
    frame.configure(fg_color = "#dadada")


    label = ctk.CTkLabel(frame , text = "Power Calculator" , text_color = "#161616" , font = ("ubuntu" , 20))
    label.grid(row = 0 , column = 0 , pady = 15 , padx = 10 , sticky = "ew")


    e1 = ctk.CTkEntry(frame , placeholder_text = "Base Number" , font = ("ubuntu" , 16) , height = 40 , width = 420 , justify = "center")
    e1.grid(row = 1 , column = 0 , pady = 10 , padx = 15 , sticky = "ew")


    e2 = ctk.CTkEntry(frame , placeholder_text = "Exponent" , font = ("ubuntu" , 16) , height = 40 , justify = "center")
    e2.grid(row = 2 , column = 0 , pady = 10 , padx = 15 , sticky = "ew")


    resultl = ctk.CTkLabel(frame , text = "" , font = ("ubuntu" , 18) , height = 36 , fg_color = "#727272" , text_color = "white" , corner_radius = 8)
    resultl.grid(row = 3 , column = 0 , pady = 15 , padx = 15 , sticky = "ew")


    def calculate_power():
        base_str = e1.get().strip()
        exp_str = e2.get().strip()


        if not base_str or not exp_str:
            messagebox.showerror("Error" , "Please enter both values.")

        elif not base_str.replace('.' , '' , 1).isdigit() or not exp_str.isdigit():
            messagebox.showerror("Error" , "Please enter valid numbers.")

        else:
            base = int(base_str)
            exp = int(exp_str)
            res = base ** exp
            resultl.configure(text = f"Result = {res}")


    btn = ctk.CTkButton(frame , text = "Calculate" , font = ("ubuntu" , 18) , command = calculate_power , height = 45 , fg_color = "#2D6EAF" , hover_color = "#1a4a80")
    btn.grid(row = 4 , column = 0 , pady = 20 , padx = 15 , sticky = "ew")


btn = ctk.CTkButton(frame2 , width = 213 , height = 40 , text = "Power" , font = ("ubuntu" , 23) , text_color = "#1D1D1D" , fg_color = "#e6e6e6", hover_color = "#c5c5c5" , command = open_power) 
btn.grid(row = 0 , column = 1 , pady = 10 , padx = 10)



def open_prime():


    window = ctk.CTkToplevel(app)
    window.geometry("340x300")
    window.title("Prime Number")
    window.resizable(False , False)
    window.configure(fg_color = "gray")


    frame = ctk.CTkFrame(window , corner_radius = 10 , border_color = 'white' , border_width = 3)
    frame.pack(fill = "both" , expand = True , padx = 15 , pady = 10)
    frame.configure(fg_color = "#dadada")


    label = ctk.CTkLabel(frame , text = "Prime Checker" , text_color = "#161616" , font = ("ubuntu" , 20))
    label.grid(row = 0 , column = 0 , pady = 15 , padx = 10 , sticky = "ew")


    e1 = ctk.CTkEntry(frame , placeholder_text = "Enter A Number" , font = ("ubuntu" , 16) , height = 40 , width = 270 , justify = "center")
    e1.grid(row = 1 , column = 0 , pady = 10 , padx = 20 , sticky = "ew")


    resultl = ctk.CTkLabel(frame , height = 45 , text = "" , font = ("ubuntu" , 18) , fg_color = "#727272" , text_color = "white" , corner_radius = 8)
    resultl.grid(row = 2 , column = 0 , pady = 15 , padx = 20 , sticky = "ew")


    def check_prime():
        
        num_str = e1.get().strip()


        if not num_str or not num_str.isdigit():
            messagebox.showerror("Error" , "Please enter a positive integer.")
            return
        
        num = int(num_str)


        if num < 2:
            resultl.configure(text = "No, It is Not Prime")
            return


        for i in range(2 , int(math.sqrt(num)) + 1):
            if num % i == 0:
                resultl.configure(text = "No, It is Not Prime")
                return
        
        resultl.configure(text = "Yes, It is Prime")


    btn = ctk.CTkButton(frame , text = "Check" , font = ("ubuntu" , 18) , command = check_prime , height = 45 , fg_color = "#2D6EAF" , hover_color = "#1a4a80")
    btn.grid(row = 3 , column = 0 , pady = 20 , padx = 20 , sticky = "ew")


btn = ctk.CTkButton(frame2 , width = 213 , height = 40 , text = "Prime Number" , font = ("ubuntu" , 23) , text_color = "#1D1D1D" , fg_color = "#e6e6e6", hover_color = "#c5c5c5" , command = open_prime) 
btn.grid(row = 0 , column = 2 , pady = 10 , padx = 10)



def open_soea():
    window = ctk.CTkToplevel(app)
    window.geometry("390x300")
    window.title("Size of each angle")
    window.resizable(False , False)
    window.configure(fg_color = "gray")


    frame = ctk.CTkFrame(window , corner_radius = 10 , border_color = 'white' , border_width = 3)
    frame.pack(fill = "both" , expand = True , padx = 15 , pady = 10)
    frame.configure(fg_color = "#dadada")


    label = ctk.CTkLabel(frame , text = "Find the size of each angle" , text_color = "#161616" , font = ("ubuntu" , 20))
    label.grid(row = 0 , column = 0 , pady = 15 , padx = 10 , sticky = "ew")


    e1 = ctk.CTkEntry(frame , placeholder_text = "Number of sides" , font = ("ubuntu" , 16) , height = 40 , width = 320 , justify = "center")
    e1.grid(row = 1 , column = 0 , pady = 10 , padx = 20 , sticky = "ew")


    resultl = ctk.CTkLabel(frame , text = "" , height = 45 , font = ("ubuntu" , 18) , fg_color = "#727272" , text_color = "white" , corner_radius = 8)
    resultl.grid(row = 2 , column = 0 , pady = 15 , padx = 20 , sticky = "ew")


    def calculate():
        side = e1.get().strip()

        if not side:
            messagebox.showerror("Error" , "Please enter values.")

        elif not side.replace('.' , '' , 1).isdigit():
            messagebox.showerror("Error" , "Please enter valid numbers.")

        else:
            side = float(side)
            res = (side-2)*180/side
            resultl.configure(text = f"Size of each angle = {res:.2f}")


    btn = ctk.CTkButton(frame , text = "Calculate" , font = ("ubuntu" , 18) , command = calculate , height = 45 , fg_color = "#2D6EAF" , hover_color = "#1a4a80")
    btn.grid(row = 4 , column = 0 , pady = 20 , padx = 20 , sticky = "ew")


btn = ctk.CTkButton(frame2 , width = 213 , height = 40 , text = "Size of each angle" , font = ("ubuntu" , 23) , text_color = "#1D1D1D" , fg_color = "#e6e6e6", hover_color = "#c5c5c5" , command = open_soea) 
btn.grid(row = 1 , column = 0 , pady = 10 , padx = 10)



def open_circle():

    window = ctk.CTkToplevel(app)
    window.geometry("390x300")
    window.title("perimeter and area of the circle")
    window.resizable(False , False)
    window.configure(fg_color = "gray")


    frame = ctk.CTkFrame(window , corner_radius = 10 , border_color = 'white' , border_width = 3)
    frame.pack(fill = "both" , expand = True , padx = 15 , pady = 10)
    frame.configure(fg_color = "#dadada")


    label = ctk.CTkLabel(frame , text = "Perimeter and area of the circle" , text_color = "#161616" , font = ("ubuntu" , 20))
    label.grid(row = 0 , column = 0 , pady = 15 , padx = 10 , sticky = "ew")


    e1 = ctk.CTkEntry(frame , placeholder_text = "Circle radius" , font = ("ubuntu" , 16) , height = 40 , width = 320 , justify = "center")
    e1.grid(row = 1 , column = 0 , pady = 10 , padx = 20 , sticky = "ew")


    resultl = ctk.CTkLabel(frame , text = "" , height = 52 , font = ("ubuntu" , 18) , fg_color = "#727272" , text_color = "white" , corner_radius = 8)
    resultl.grid(row = 2 , column = 0 , pady = 15 , padx = 20 , sticky = "ew")


    def calculate():

        radius = e1.get().strip()

        if not radius:
            messagebox.showerror("Error" , "Please enter values.")

        elif not radius.replace('.' , '' , 1).isdigit():
            messagebox.showerror("Error" , "Please enter valid numbers.")

        else:
            
            radius = float(radius)

            perimeter = radius*3.14*2
            area = radius*radius*3.14

            resultl.configure(text = f"Circle area = {area:.3f}\nCircle perimeter = {perimeter:.3f}")


    btn = ctk.CTkButton(frame , text = "Calculate" , font = ("ubuntu" , 18) , command = calculate , height = 45 , fg_color = "#2D6EAF" , hover_color = "#1a4a80")
    btn.grid(row = 4 , column = 0 , pady = 20 , padx = 20 , sticky = "ew")

    
btn = ctk.CTkButton(frame2 , width = 213 , height = 40 , text = "Circle" , font = ("ubuntu" , 23) , text_color = "#1D1D1D" , fg_color = "#e6e6e6", hover_color = "#c5c5c5" , command = open_circle) 
btn.grid(row = 1 , column = 1 , pady = 10 , padx = 10)



def open_pythagoras():


    window = ctk.CTkToplevel(app)
    window.geometry("390x346")
    window.title("Pythagoras")
    window.resizable(False , False)
    window.configure(fg_color = "gray")


    frame = ctk.CTkFrame(window , corner_radius = 10 , border_color = 'white' , border_width = 3)
    frame.pack(fill = "both" , expand = True , padx = 15 , pady = 10)
    frame.configure(fg_color = "#dadada")


    label = ctk.CTkLabel(frame , text = "Pythagoras Theorem" , text_color = "#161616" , font = ("ubuntu" , 20))
    label.grid(row = 0 , column = 0 , pady = 15 , padx = 10 , sticky = "ew")


    e1 = ctk.CTkEntry(frame , placeholder_text = "Side A" , font = ("ubuntu" , 16) , height = 40 , width = 320 , justify = "center")
    e1.grid(row = 1 , column = 0 , pady = 10 , padx = 20 , sticky = "ew")


    e2 = ctk.CTkEntry(frame , placeholder_text = "Side B" , font = ("ubuntu" , 16) , height = 40 , justify = "center")
    e2.grid(row = 2 , column = 0 , pady = 10 , padx = 20 , sticky = "ew")


    resultl = ctk.CTkLabel(frame , text = "" , height = 45 , font = ("ubuntu" , 18) , fg_color = "#727272" , text_color = "white" , corner_radius = 8)
    resultl.grid(row = 3 , column = 0 , pady = 15 , padx = 20 , sticky = "ew")


    def calculate_pythagoras():
        a_str = e1.get().strip()
        b_str = e2.get().strip()


        if not a_str or not b_str:
            messagebox.showerror("Error" , "Please enter both sides.")


        elif not a_str.replace('.' , '' , 1).isdigit() or not b_str.replace('.' , '' , 1).isdigit():
            messagebox.showerror("Error" , "Please enter valid numbers.")


        else:
            a = float(a_str)
            b = float(b_str)
            

            if a < 0 or b < 0:
                messagebox.showerror("Error" , "Sides cannot be negative.")

            else:
                c = math.sqrt(a**2 + b**2)
                resultl.configure(text = f"Hypotenuse = {c:.3f}")


    btn = ctk.CTkButton(frame , text = "Calculate" , font = ("ubuntu" , 18) , command = calculate_pythagoras , height = 45 , fg_color = "#2D6EAF" , hover_color = "#1a4a80")
    btn.grid(row = 4 , column = 0 , pady = 20 , padx = 20 , sticky = "ew")


btn = ctk.CTkButton(frame2 , width = 213 , height = 40 , text = "Pythagoras" , font = ("ubuntu" , 23) , text_color = "#1D1D1D" , fg_color = "#e6e6e6", hover_color = "#c5c5c5" , command = open_pythagoras) 
btn.grid(row = 1 , column = 2 , pady = 10 , padx = 10)



def open_percentage():
   

    window = ctk.CTkToplevel(app)
    window.geometry("440x355")
    window.title("Percentage")
    window.resizable(False , False)
    window.configure(fg_color = "gray")


    frame = ctk.CTkFrame(window , corner_radius = 10 , border_color = 'white' , border_width = 3)
    frame.pack(fill = "both" , expand = True , padx = 15 , pady = 10)
    frame.configure(fg_color = "#dadada")


    label = ctk.CTkLabel(frame , text = "Percentage Calculator" , text_color = "#161616" , font = ("ubuntu" , 20))
    label.grid(row = 0 , column = 0 , pady = 15 , padx = 10 , sticky = "ew")


    e1 = ctk.CTkEntry(frame , placeholder_text = "Total Number" , font = ("ubuntu" , 16) , height = 40 , width = 370 , justify = "center")
    e1.grid(row = 1 , column = 0 , pady = 10 , padx = 20 , sticky = "ew")


    e2 = ctk.CTkEntry(frame , placeholder_text = "Percent Value" , font = ("ubuntu" , 16) , height = 40 , justify = "center")
    e2.grid(row = 2 , column = 0 , pady = 10 , padx = 20 , sticky = "ew")


    resultl = ctk.CTkLabel(frame , text = "" , height = 45 , font = ("ubuntu" , 18) , fg_color = "#727272" , text_color = "white" , corner_radius = 8)
    resultl.grid(row = 3 , column = 0 , pady = 15 , padx = 20 , sticky = "ew")


    def calculate_percentage():
        total_str = e1.get().strip()
        percent_str = e2.get().strip()


        if not total_str or not percent_str:
            messagebox.showerror("Error" , "Please enter both values.")


        elif not total_str.replace('.' , '' , 1).isdigit() or not percent_str.replace('.' , '' , 1).isdigit():
            messagebox.showerror("Error" , "Please enter valid numbers.")


        else:
            total = float(total_str)
            percent = float(percent_str)
            res = (total * percent) / 100
            resultl.configure(text = f"Result = {res:.3f}")


    btn = ctk.CTkButton(frame , text = "Calculate" , font = ("ubuntu" , 18) , command = calculate_percentage , height = 45 , fg_color = "#2D6EAF" , hover_color = "#1a4a80")
    btn.grid(row = 4 , column = 0 , pady = 20 , padx = 20 , sticky = "ew")


btn = ctk.CTkButton(frame2 , width = 213 , height = 40 , text = "Percentage" , font = ("ubuntu" , 23) , text_color = "#1D1D1D" , fg_color = "#e6e6e6", hover_color = "#c5c5c5" , command = open_percentage) 
btn.grid(row = 2 , column = 0 , pady = 10 , padx = 10)



def open_gcd_lcm():


    window = ctk.CTkToplevel(app)
    window.geometry("370x350")
    window.title("GCD & LCM")
    window.resizable(False , False)
    window.configure(fg_color = "gray")


    frame = ctk.CTkFrame(window , corner_radius = 10 , border_color = 'white' , border_width = 3)
    frame.pack(fill = "both" , expand = True , padx = 15 , pady = 10)
    frame.configure(fg_color = "#dadada")


    label = ctk.CTkLabel(frame , text = "GCD & LCM Calculator" , text_color = "#161616" , font = ("ubuntu" , 20))
    label.grid(row = 0 , column = 0 , pady = 15 , padx = 10 , sticky = "ew")


    e1 = ctk.CTkEntry(frame , placeholder_text = "Enter First Number" , font = ("ubuntu" , 16) , height = 40 , width = 302 , justify = "center")
    e1.grid(row = 1 , column = 0 , pady = 10 , padx = 20 , sticky = "ew")


    e2 = ctk.CTkEntry(frame , placeholder_text = "Enter Second Number" , justify = "center" , font = ("ubuntu" , 16) , height = 40)
    e2.grid(row = 2 , column = 0 , pady = 10 , padx = 20 , sticky = "ew")


    resultl = ctk.CTkLabel(frame , text = "" , height = 50 , font = ("ubuntu" , 18) , fg_color = "#727272" , text_color = "white" , corner_radius = 8)
    resultl.grid(row = 3 , column = 0 , pady = 15 , padx = 20 , sticky = "ew")


    def calculate_gcd_lcm():
        num1_str = e1.get().strip()
        num2_str = e2.get().strip()


        if not num1_str or not num2_str:
            messagebox.showerror("Error" , "Please enter both numbers.")

        elif not num1_str.isdigit() or not num2_str.isdigit():
            messagebox.showerror("Error" , "Please enter positive integers only.")

        else:
            num1 = int(num1_str)
            num2 = int(num2_str)

            gcd = math.gcd(num1 , num2)
            lcm = math.lcm(num1 , num2)

            resultl.configure(text = f"GCD = {gcd}\nLCM = {lcm}")


    btngl = ctk.CTkButton(frame , text = "Calculate" , font = ("ubuntu" , 18) , command = calculate_gcd_lcm , height = 45 , fg_color = "#2D6EAF" , hover_color = "#1a4a80")
    btngl.grid(row = 4 , column = 0 , pady = 20 , padx = 20 , sticky = "ew")


btn = ctk.CTkButton(frame2 , width = 213 , height = 40 , text = "GCD & LCM" , font = ("ubuntu" , 23) , text_color = "#1D1D1D" , fg_color = "#e6e6e6", hover_color = "#c5c5c5" , command = open_gcd_lcm) 
btn.grid(row = 2 , column = 1 , pady = 10 , padx = 10)



def open_calculator():

    window = ctk.CTkToplevel(app)
    window.geometry("630x470")
    window.title("Calculator")
    window.resizable(False , False)
    window.configure(fg_color = "gray")

    frame = ctk.CTkFrame(window , corner_radius = 10 , border_color = 'white' , border_width = 3)
    frame.pack(fill = "both" , expand = True , padx = 15 , pady = 10)
    frame.configure(fg_color = "#dadada")

    label = ctk.CTkLabel(frame , text = "Calculator" , text_color = "#161616" , font = ("ubuntu" , 20))
    label.grid(row = 0 , column = 0 , pady = 10 , padx = 10 , columnspan = 4 , sticky = "ew")

    display = ctk.CTkEntry(frame , placeholder_text = "0" , font = ("ubuntu" , 24) , height = 40 , justify = "center")
    display.grid(row = 1 , column = 0 , pady = 10 , padx = 10 , columnspan = 4 , sticky = "ew")

    resultl = ctk.CTkLabel(frame , text = "" , font = ("ubuntu" , 18) , fg_color = "#727272" , height = 38 , text_color = "white" , corner_radius = 8)
    resultl.grid(row = 2 , column = 0 , pady = 10 , padx = 10 , columnspan = 4 , sticky = "ew")

    def add_number(num):
        current = display.get()
        if current == "0":
            display.delete(0 , len(current))
        display.insert(len(display.get()) , str(num))

    def add_operator(op):
        current = display.get()
        if current and current[-1] not in "+-*/":
            display.insert(len(current) , op)

    def clear_display():
        display.delete(0 , len(display.get()))
        display.insert(0 , "0")
        resultl.configure(text = "")

    def calculate():
        expr = display.get()
        c = "0123456789.+-*/ ()"         

        if not expr:
            messagebox.showerror("Error", "Please enter an expression.")


        elif not all(char in c for char in expr):
            messagebox.showerror("Error", "Invalid characters in expression.")

        
        else:
            e = eval(expr)
            resultl.configure(text = f"Result = {e:.3f}")


    btn_7 = ctk.CTkButton(frame , text = "7" , font = ("ubuntu" , 18) , command = lambda : add_number(7) , height = 60 , fg_color = "#e6e6e6" , hover_color = "#c5c5c5" , text_color = "#1D1D1D")
    btn_7.grid(row = 3 , column = 0 , pady = 5 , padx = 5)

    btn_8 = ctk.CTkButton(frame , text = "8" , font = ("ubuntu" , 18) , command = lambda : add_number(8) , height = 60 , fg_color = "#e6e6e6" , hover_color = "#c5c5c5" , text_color = "#1D1D1D")
    btn_8.grid(row = 3 , column = 1 , pady = 5 , padx = 5)

    btn_9 = ctk.CTkButton(frame , text = "9" , font = ("ubuntu" , 18) , command = lambda : add_number(9) , height = 60 , fg_color = "#e6e6e6" , hover_color = "#c5c5c5" , text_color = "#1D1D1D")
    btn_9.grid(row = 3 , column = 2 , pady = 5 , padx = 5)

    btn_div = ctk.CTkButton(frame , text = "/" , font = ("ubuntu" , 18) , command = lambda : add_operator("/") , height = 60 , fg_color = "#2D6EAF" , hover_color = "#1a4a80" , text_color = "white")
    btn_div.grid(row = 3 , column = 3 , pady = 5 , padx = 5)

    btn_4 = ctk.CTkButton(frame , text = "4" , font = ("ubuntu" , 18) , command = lambda : add_number(4) , height = 60 , fg_color = "#e6e6e6" , hover_color = "#c5c5c5" , text_color = "#1D1D1D")
    btn_4.grid(row = 4 , column = 0 , pady = 5 , padx = 5)

    btn_5 = ctk.CTkButton(frame , text = "5" , font = ("ubuntu" , 18) , command = lambda : add_number(5) , height = 60 , fg_color = "#e6e6e6" , hover_color = "#c5c5c5" , text_color = "#1D1D1D")
    btn_5.grid(row = 4 , column = 1 , pady = 5 , padx = 5)

    btn_6 = ctk.CTkButton(frame , text = "6" , font = ("ubuntu" , 18) , command = lambda : add_number(6) , height = 60 , fg_color = "#e6e6e6" , hover_color = "#c5c5c5" , text_color = "#1D1D1D")
    btn_6.grid(row = 4 , column = 2 , pady = 5 , padx = 5)

    btn_mul = ctk.CTkButton(frame , text = "*" , font = ("ubuntu" , 18) , command = lambda : add_operator("*") , height = 60 , fg_color = "#2D6EAF" , hover_color = "#1a4a80" , text_color = "white")
    btn_mul.grid(row = 4 , column = 3 , pady = 5 , padx = 5)

    btn_1 = ctk.CTkButton(frame , text = "1" , font = ("ubuntu" , 18) , command = lambda : add_number(1) , height = 60 , fg_color = "#e6e6e6" , hover_color = "#c5c5c5" , text_color = "#1D1D1D")
    btn_1.grid(row = 5 , column = 0 , pady = 5 , padx = 5)

    btn_2 = ctk.CTkButton(frame , text = "2" , font = ("ubuntu" , 18) , command = lambda : add_number(2) , height = 60 , fg_color = "#e6e6e6" , hover_color = "#c5c5c5" , text_color = "#1D1D1D")
    btn_2.grid(row = 5 , column = 1 , pady = 5 , padx = 5)

    btn_3 = ctk.CTkButton(frame , text = "3" , font = ("ubuntu" , 18) , command = lambda : add_number(3) , height = 60 , fg_color = "#e6e6e6" , hover_color = "#c5c5c5" , text_color = "#1D1D1D")
    btn_3.grid(row = 5 , column = 2 , pady = 5 , padx = 5)

    btn_sub = ctk.CTkButton(frame , text = "-" , font = ("ubuntu" , 18) , command = lambda : add_operator("-") , height = 60 , fg_color = "#2D6EAF" , hover_color = "#1a4a80" , text_color = "white")
    btn_sub.grid(row = 5 , column = 3 , pady = 5 , padx = 5)

    btn_0 = ctk.CTkButton(frame , text = "0" , font = ("ubuntu" , 18) , command = lambda : add_number(0) , height = 60 , fg_color = "#e6e6e6" , hover_color = "#c5c5c5" , text_color = "#1D1D1D")
    btn_0.grid(row = 6 , column = 0 , pady = 5 , padx = 5)

    btn_clear = ctk.CTkButton(frame , text = "C" , font = ("ubuntu" , 18) , command = clear_display , height = 60 , fg_color = "#CE0000" , hover_color = "#990000" , text_color = "white")
    btn_clear.grid(row = 6 , column = 1 , pady = 5 , padx = 5)

    btn_eq = ctk.CTkButton(frame , text = "=" , font = ("ubuntu" , 18) , command = calculate , height = 60 , fg_color = "#1B9300" , hover_color = "#115C00" , text_color = "white")
    btn_eq.grid(row = 6 , column = 2 , pady = 5 , padx = 5)

    btn_add = ctk.CTkButton(frame , text = "+" , font = ("ubuntu" , 18) , command = lambda : add_operator("+") , height = 60 , fg_color = "#2D6EAF" , hover_color = "#1a4a80" , text_color = "white")
    btn_add.grid(row = 6 , column = 3 , pady = 5 , padx = 5)




btn = ctk.CTkButton(frame2 , width = 213 , height = 40 , text = "Calculator" , font = ("ubuntu" , 23) , text_color = "#1D1D1D" , fg_color = "#e6e6e6", hover_color = "#c5c5c5" , command = open_calculator) 
btn.grid(row = 2 , column = 2 , pady = 10 , padx = 10)




frame3 = ctk.CTkFrame(app , corner_radius = 6 , border_color = 'white' , border_width = 3)
frame3.pack(pady = 10 , fill = "both")
frame3.configure(fg_color = "#dadada")



def github():
    webbrowser.open('https://github.com/ShayanCoder710/')
open = ctk.CTkButton(frame3 , width = 213 , height = 45 , text = "GitHub of this app" , font = ("ubuntu" , 23) , fg_color = "#01A5CE", hover_color = "#004F99" , command = github) 
open.grid(row = 0 , column = 0 , pady = 17 , padx = 10)



def show_about():

    window = ctk.CTkToplevel(app)
    window.geometry("439x180")
    window.title("About the program")
    window.resizable(False , False)
    window.configure(fg_color = "gray")


    frame = ctk.CTkFrame(window , corner_radius = 10 , border_color = 'white' , border_width = 3)
    frame.pack(fill = "both" , expand = True , padx = 15 , pady = 10)
    frame.configure(fg_color = "#dadada")


    texta = """
Developer : Seyyed Shayan Seyyedi
Program language : Python
Program work : Calculating various mathematical tasks.
"""

    about_label = ctk.CTkLabel(frame , text = texta , text_color = "black" , font = ("ubuntu" , 16) , anchor = "center" , justify = "center")
    about_label.grid(row = 0 , column = 0 , pady = 2 , padx = 5 , sticky = "nsew")

    close_button = ctk.CTkButton(frame , text = "Close" , font = ("ubuntu" , 20) , hover_color = "#990000" , command = window.destroy , width = 50 , fg_color = "#CE0000" , anchor = "center" , height = 40)
    close_button.grid(row = 1 , column = 0 , pady = 2 , padx = 9 , columnspan = 10 , sticky = "nsew")


about_button = ctk.CTkButton(frame3 , width = 213 , text = "About the program" , font = ("ubuntu" , 23) , fg_color = "#1B9300" , hover_color = "#115C00" , command = show_about , height = 45)
about_button.grid(row = 0 , column = 1 , pady = 17 , padx = 10)



def out():
    app.quit()
out = ctk.CTkButton(frame3 , width = 213 , height = 45 , text = "Exit" , font = ("ubuntu" , 23) , fg_color = "#CE0000", hover_color = "#990000" , command = out)
out.grid(row = 0 , column = 2 , pady = 17 , padx = 10)




app.mainloop()
