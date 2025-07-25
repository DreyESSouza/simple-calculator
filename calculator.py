from customtkinter import *
import logic

root = CTk()
root.title("Calculator")
root.geometry("280x386")
root.resizable(False, False)

display = CTkLabel(root, text="", fg_color="#4F4F4F", text_color="white", width=270, height=60, anchor="e", font=("Digital-7",25))
display.grid(row=0, column=0, columnspan=4, pady=5, padx=5)

#-----------------------------------------------------------------------------------------------------------------#

buttom_clear_everithing = CTkButton(root, text="CE", width=60, height=55, font=("Arial", 20), fg_color="#8B0000", command= lambda: logic.clear_display(display))
buttom_clear_everithing.grid(row=1 ,column=0, pady=4, columnspan=1)

buttom_clear = CTkButton(root, text="C", width=60, height=55, font=("Arial", 20), fg_color="#8B0000", command= lambda: logic.delete_caractere(display))
buttom_clear.grid(row=1 ,column=1, pady=4, columnspan=1)

buttom_percentage = CTkButton(root, text="%", width=60, height=55, font=("Arial", 20), fg_color="#191970", command= lambda: logic.porcetage(buttom_percentage, display))
buttom_percentage.grid(row=1 ,column=2, pady=4)

buttom_div = CTkButton(root, text="÷", width=60, height=55, font=("Arial", 20),fg_color="#191970", command= lambda: logic.math_signs(buttom_div, display))
buttom_div.grid(row=1, column=3, pady=4)

#-----------------------------------------------------------------------------------------------------------------#

buttom_7 = CTkButton(root, text=7, width=60, height=55, font=("Arial", 20),fg_color="#1C1C1C", command= lambda: logic.write_display(buttom_7, display))
buttom_7.grid(row=2, column=0, pady=4)

buttom_8 = CTkButton(root, text=8, width=60, height=55, font=("Arial", 20),fg_color="#1C1C1C", command= lambda: logic.write_display(buttom_8, display))
buttom_8.grid(row=2, column=1, pady=4)

buttom_9 = CTkButton(root, text=9, width=60, height=55, font=("Arial", 20),fg_color="#1C1C1C", command= lambda: logic.write_display(buttom_9, display))
buttom_9.grid(row=2, column=2, pady=4)

buttom_multip = CTkButton(root, text="×", width=60, height=55, font=("Arial", 20),fg_color="#191970", command= lambda: logic.math_signs(buttom_multip, display))
buttom_multip.grid(row=2, column=3, pady=4)

#-----------------------------------------------------------------------------------------------------------------#

buttom_4 = CTkButton(root, text=4, width=60, height=55, font=("Arial", 20), fg_color="#1C1C1C", command= lambda: logic.write_display(buttom_4, display))
buttom_4.grid(row=3, column=0, pady=4)

buttom_5 = CTkButton(root, text=5, width=60, height=55, font=("Arial", 20), fg_color="#1C1C1C", command= lambda: logic.write_display(buttom_5, display))
buttom_5.grid(row=3, column=1, pady=4)

buttom_6 = CTkButton(root, text=6, width=60, height=55, font=("Arial", 20), fg_color="#1C1C1C", command= lambda: logic.write_display(buttom_6, display))
buttom_6.grid(row=3, column=2, pady=4)

buttom_subtr = CTkButton(root, text="-", width=60, height=55, font=("Arial", 20), fg_color="#191970", command= lambda: logic.math_signs(buttom_subtr, display))
buttom_subtr.grid(row=3, column=3, pady=4)

#-----------------------------------------------------------------------------------------------------------------#

buttom_1 = CTkButton(root, text=1, width=60, height=55, font=("Arial", 20), fg_color="#1C1C1C", command= lambda: logic.write_display(buttom_1, display))
buttom_1.grid(row=4, column=0, pady=4)

buttom_2 = CTkButton(root, text=2, width=60, height=55, font=("Arial", 20), fg_color="#1C1C1C", command= lambda: logic.write_display(buttom_2, display))
buttom_2.grid(row=4, column=1, pady=4)

buttom_3 = CTkButton(root, text=3, width=60, height=55, font=("Arial", 20), fg_color="#1C1C1C", command= lambda: logic.write_display(buttom_3, display))
buttom_3.grid(row=4, column=2, pady=4)

buttom_add = CTkButton(root, text="+", width=60, height=55, font=("Arial", 20), fg_color="#191970", command= lambda: logic.math_signs(buttom_add, display))
buttom_add.grid(row=4, column=3, pady=4)

#-----------------------------------------------------------------------------------------------------------------#

buttom_0 = CTkButton(root, text=0, width=60, height=55, font=("Arial", 20), fg_color="#1C1C1C", command= lambda: logic.write_display(buttom_0, display))
buttom_0.grid(row=5, column=0, pady=4)

buttom_point = CTkButton(root, text=".", width=60, height=55, font=("Arial", 20), fg_color="#191970", command= lambda: logic.math_signs(buttom_point, display))
buttom_point.grid(row=5, column=1, pady=4)

buttom_equal = CTkButton(root, text="=", width=135, height=55, font=("Arial", 20), fg_color="#191970", command = lambda: logic.calculate(display))
buttom_equal.grid(row=5, column=2, pady=4, columnspan=2)

root.mainloop()