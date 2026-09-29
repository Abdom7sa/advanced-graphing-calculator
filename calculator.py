import customtkinter as ctk
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Set overall GUI style
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class AdvancedGraphingCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Advanced Scientific & Graphing Calculator")
        self.geometry("1000x650")
        self.resizable(True, True)

        self.expression = ""

        # Main Layout Configuration (Left: Calculator, Right: Graphing)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Left Frame: Calculator Controls
        self.calc_frame = ctk.CTkFrame(self, corner_radius=15)
        self.calc_frame.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        # Display Entry
        self.display = ctk.CTkEntry(
            self.calc_frame,
            height=70,
            font=("Consolas", 24),
            justify="right",
            corner_radius=10
        )
        self.display.pack(fill="x", padx=15, pady=(15, 10))

        # Calculator Keypad Layout
        self.button_frame = ctk.CTkFrame(self.calc_frame, fg_color="transparent")
        self.button_frame.pack(fill="both", expand=True, padx=10, pady=10)

        buttons = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('*', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('-', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('+', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('sqrt', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('^', 5, 2), ('=', 5, 3),
            ('x', 6, 0), ('log', 6, 1), ('exp', 6, 2), ('pi', 6, 3)
        ]

        for col in range(4):
            self.button_frame.grid_columnconfigure(col, weight=1)
        for row in range(7):
            self.button_frame.grid_rowconfigure(row, weight=1)

        for text, r, c in buttons:
            self.create_calc_button(text, r, c)

        # Right Frame: Graphing Engine
        self.graph_frame = ctk.CTkFrame(self, corner_radius=15)
        self.graph_frame.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

        # Plot Controls Panel
        self.plot_control_frame = ctk.CTkFrame(self.graph_frame, fg_color="transparent")
        self.plot_control_frame.pack(fill="x", padx=15, pady=(15, 5))

        self.graph_label = ctk.CTkLabel(
            self.plot_control_frame, 
            text="Function f(x):", 
            font=("Arial", 14, "bold")
        )
        self.graph_label.pack(side="left", padx=(0, 10))

        self.func_entry = ctk.CTkEntry(
            self.plot_control_frame, 
            placeholder_text="e.g. sin(x) or x^2 - 4",
            font=("Consolas", 14)
        )
        self.func_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.plot_btn = ctk.CTkButton(
            self.plot_control_frame, 
            text="Plot Graph", 
            width=100,
            command=self.plot_function
        )
        self.plot_btn.pack(side="right")

        # Embed Matplotlib Figure
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        self.style_plot()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=15, pady=15)

    def create_calc_button(self, text, row, col):
        if text in ['=', '+', '-', '*', '/']:
            bg_color = "#1f538d"
        elif text == 'C':
            bg_color = "#942f2f"
        elif text in ['sin', 'cos', 'tan', 'sqrt', '^', 'log', 'exp', 'pi', 'x']:
            bg_color = "#334252"
        else:
            bg_color = "#2b2b2b"

        btn = ctk.CTkButton(
            self.button_frame,
            text=text,
            font=("Arial", 16, "bold"),
            fg_color=bg_color,
            corner_radius=8,
            command=lambda t=text: self.on_button_click(t)
        )
        btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display.delete(0, 'end')

        elif char == '=':
            try:
                formatted = self.prepare_expression(self.expression)
                result = eval(formatted, {"__builtins__": None}, {"math": math})

                if isinstance(result, float) and result.is_integer():
                    result = int(result)

                self.display.delete(0, 'end')
                self.display.insert(0, str(result))
                self.expression = str(result)

            except Exception:
                self.display.delete(0, 'end')
                self.display.insert(0, "Error")
                self.expression = ""

        else:
            self.expression += str(char)
            self.display.delete(0, 'end')
            self.display.insert(0, self.expression)

    def prepare_expression(self, expr):
        formatted = expr.replace('^', '**')
        formatted = formatted.replace('sqrt', 'math.sqrt')
        formatted = formatted.replace('sin', 'math.sin')
        formatted = formatted.replace('cos', 'math.cos')
        formatted = formatted.replace('tan', 'math.tan')
        formatted = formatted.replace('log', 'math.log10')
        formatted = formatted.replace('exp', 'math.exp')
        formatted = formatted.replace('pi', 'math.pi')
        return formatted

    def style_plot(self):
        self.fig.patch.set_facecolor('#2b2b2b')
        self.ax.set_facecolor('#1a1a1a')
        self.ax.spines['bottom'].set_color('#ffffff')
        self.ax.spines['top'].set_color('#ffffff')
        self.ax.spines['left'].set_color('#ffffff')
        self.ax.spines['right'].set_color('#ffffff')
        self.ax.xaxis.label.set_color('#ffffff')
        self.ax.yaxis.label.set_color('#ffffff')
        self.ax.tick_params(colors='#ffffff', which='both')
        self.ax.grid(True, color='#444444', linestyle='--', linewidth=0.5)

    def plot_function(self):
        raw_func = self.func_entry.get().strip()
        if not raw_func:
            return

        try:
            x = np.linspace(-10, 10, 1000)

            # Safe context mapping vector operations using numpy
            allowed_symbols = {
                'x': x,
                'sin': np.sin,
                'cos': np.cos,
                'tan': np.tan,
                'sqrt': np.sqrt,
                'log': np.log10,
                'exp': np.exp,
                'pi': np.pi
            }

            parsed_func = raw_func.replace('^', '**')
            y = eval(parsed_func, {"__builtins__": None}, allowed_symbols)

            self.ax.clear()
            self.style_plot()

            self.ax.plot(x, y, color='#1f538d', linewidth=2, label=f"f(x) = {raw_func}")
            self.ax.axhline(0, color='#666666', linewidth=0.8)
            self.ax.axvline(0, color='#666666', linewidth=0.8)
            self.ax.set_title(f"Graph of f(x) = {raw_func}", color='#ffffff', fontsize=12)
            self.ax.legend(facecolor='#2b2b2b', edgecolor='none', labelcolor='#ffffff')

            self.canvas.draw()

        except Exception:
            self.ax.clear()
            self.style_plot()
            self.ax.text(
                0.5, 0.5, "Invalid Expression", 
                color='#ff4444', fontsize=14, 
                ha='center', va='center', transform=self.ax.transAxes
            )
            self.canvas.draw()


if __name__ == "__main__":
    app = AdvancedGraphingCalculator()
    app.mainloop()