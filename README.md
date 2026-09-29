Advanced Scientific & Graphing Calculator 🧮📊

<p align="center">
  <img src="screenshots/calculator.png" alt="Advanced Scientific & Graphing Calculator" width="850">
</p><p align="center">
  <strong>A modern desktop scientific calculator with interactive 2D mathematical graphing.</strong>
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-1f6feb">
  <img src="https://img.shields.io/badge/Plotting-Matplotlib-orange">
  <img src="https://img.shields.io/badge/Numerical%20Computing-NumPy-013243">
  <img src="https://img.shields.io/badge/License-MIT-green">
</p>---

📌 Overview

Advanced Scientific & Graphing Calculator is a modern desktop application developed with Python.

The project combines a scientific calculator with an interactive mathematical graphing module, allowing users to perform calculations and visualize mathematical functions within the same application.

The interface uses a dark-themed design built with CustomTkinter, while NumPy and Matplotlib handle numerical processing and graph visualization.

---

✨ Features

🧮 Scientific Calculator

The calculator supports common scientific and mathematical operations, including:

- Basic arithmetic operations
- Trigonometric functions
  - "sin(x)"
  - "cos(x)"
  - "tan(x)"
- Logarithmic and exponential functions
  - "log(x)"
  - "exp(x)"
- Square roots
- Powers
- Mathematical constant "π"
- Mathematical expression evaluation

📊 Interactive Function Graphing

The graphing module allows users to enter a mathematical function and visualize it directly inside the application.

For example:

sin(x)

x^2 - 4

cos(x) + sin(x)

exp(x)

The function is sampled across the selected interval using NumPy and rendered using Matplotlib.

---

🖥️ Application Interface

<p align="center">
  <img src="screenshots/calculator.png" alt="Calculator Interface" width="850">
</p>The application provides two main areas:

Area| Purpose
🧮 Calculator| Enter and evaluate scientific mathematical expressions
📈 Graphing Panel| Enter functions and visualize their curves
🌙 Dark Interface| Provides a modern, consistent desktop experience
📊 Embedded Plot| Displays Matplotlib graphs directly inside the application

---

📈 Graphing Examples

Example 1 — Quadratic Function

x^2 - 4

<p align="center">
  <img src="screenshots/quadratic.png" alt="Quadratic Function Graph" width="750">
</p>Example 2 — Trigonometric Function

sin(x)

<p align="center">
  <img src="screenshots/sine.png" alt="Sine Function Graph" width="750">
</p>«The screenshots above should be placed inside the project's "screenshots/" directory.»

---

🛠️ Built With

Python

The core programming language used to develop the application.

CustomTkinter

Used to create the modern dark-themed graphical user interface.

NumPy

Used for numerical calculations, vectorized operations, and generating data points for function plotting.

Matplotlib

Used to create and embed mathematical graphs directly into the desktop application.

---

🏗️ Application Architecture

The application follows a simple desktop architecture:

                    ┌─────────────────────────┐
                    │   Advanced Calculator   │
                    └────────────┬────────────┘
                                 │
               ┌─────────────────┴─────────────────┐
               │                                   │
        ┌──────▼──────┐                     ┌──────▼──────┐
        │ Scientific  │                     │  Graphing   │
        │ Calculator  │                     │   Module    │
        └──────┬──────┘                     └──────┬──────┘
               │                                   │
        Mathematical                         Function Input
        Expressions                                │
               │                                   ▼
               │                                 NumPy
               │                                   │
               └──────────────┐         ┌──────────┘
                              ▼         ▼
                         Matplotlib
                              │
                              ▼
                       Embedded Graph

---

🚀 Getting Started

Prerequisites

Make sure you have Python 3.10 or newer (64-bit) installed.

Check your Python version:

python --version

Expected output:

Python 3.10.x

or a newer version.

---

📥 Installation

1. Clone the Repository

git clone https://github.com/Abdom7sa/advanced-graphing-calculator.git

2. Navigate to the Project Directory

cd advanced-graphing-calculator

3. Install Dependencies

pip install -r requirements.txt

---

▶️ Running the Application

Start the application with:

python calculator.py

The graphical interface should launch automatically.

---

🧑‍💻 Usage

Scientific Calculations

Use the calculator keypad to enter a mathematical expression.

For example:

25 * 4

or:

sqrt(144)

Press:

=

to calculate the result.

---

Plotting a Function

1. Locate the Function f(x) input field.
2. Enter a mathematical function.
3. Define the desired interval if supported by the application.
4. Click Plot Graph.
5. The function will be rendered inside the embedded Matplotlib canvas.

Example Functions

sin(x)

cos(x)

x^2 - 4

cos(x) + sin(x)

exp(x)

---

📂 Project Structure

advanced-graphing-calculator/
│
├── screenshots/
│   ├── calculator.png
│   ├── quadratic.png
│   └── sine.png
│
├── calculator.py
├── requirements.txt
├── .gitignore
└── README.md

File Description

File / Directory| Description
"calculator.py"| Main application source code
"requirements.txt"| Python package dependencies
"screenshots/"| Application screenshots used in the README
".gitignore"| Files excluded from Git
"README.md"| Project documentation

---

📦 Dependencies

The project relies on the following Python packages:

customtkinter
numpy
matplotlib

They can be installed automatically with:

pip install -r requirements.txt

---

🛡️ Error Handling

The application includes handling for invalid mathematical expressions and calculation errors.

For example, invalid or unsupported expressions can be detected instead of causing the application to terminate unexpectedly.

This provides a more reliable experience when experimenting with mathematical functions.

---

🔮 Future Improvements

Possible future extensions include:

- [ ] Multiple functions on the same graph
- [ ] Custom graph colors and styles
- [ ] Adjustable X/Y ranges
- [ ] Zoom and pan controls
- [ ] Function history
- [ ] Graph export to PNG
- [ ] Save and load calculations
- [ ] More scientific functions
- [ ] Degree/Radian mode
- [ ] Keyboard shortcuts
- [ ] Expression history
- [ ] Improved mathematical expression parser

---

📄 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute the project according to the terms of the license.

---

👨‍💻 Author

Abdom7sa

GitHub:
https://github.com/Abdom7sa

---

<p align="center">
  Made with Python 🐍 · NumPy 🔢 · Matplotlib 📊 · CustomTkinter 🖥️
</p>
