# ❤️ Diagnosis Heart Disease using Fuzzy Logic  

![Python](https://img.shields.io/badge/Python-3.8%252B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0%252B-lightgrey?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)

A fuzzy logic-based system for heart disease diagnosis, developed under the supervision of **Prof. Mohammad Mehdi Ebadzadeh** in Spring 2022.  

---

## 📋 Table of Contents  
- [Introduction](#-introduction)  
- [Fuzzy Logic Process](#-fuzzy-logic-process)  
- [Features](#-features)  
- [Installation](#-installation)  
- [Usage](#-usage)  
- [Project Structure](#-project-structure)   
- [License](#-license)  
- [Simulation Results](#-simulation-results)  

---

## 🌟 Introduction  
This project implements a fuzzy logic system to assist in the diagnosis of heart disease. Unlike traditional binary systems, fuzzy logic allows for reasoning with uncertainty and imprecision, making it particularly suitable for medical diagnosis where symptoms and conditions often exist on a spectrum.  

The system takes multiple medical parameters as inputs and provides a risk assessment for heart disease through a three-step fuzzy logic process: **fuzzification, inference, and defuzzification**.  

---

## 🔍 Fuzzy Logic Process  

### 1. 🎯 Fuzzification  
Converts crisp input values into fuzzy values, handling uncertainties in real-world data. Membership functions determine the degree of belonging.  

**Input Parameters and Their Fuzzy Sets:**  
- 👶🧓 Age: Young, Middle-aged, Old
- 💓 Blood Pressure: Low, Normal, High
- 🧪 Cholesterol: Low, Medium, High
- 📊 Heart Rate: Slow, Normal, Fast
- 📈 ECG Results: Normal, Abnormal
- 🏃 Exercise: Sedentary, Moderate, Active
- 🍎 Diet: Poor, Average, Healthy
- 🚬 Smoking: Non-smoker, Light-smoker, Heavy-smoker
- 🍷 Alcohol: Non-drinker, Social-drinker, Heavy-drinker
- 👨‍👩‍👧‍👦 Family History: None, Moderate, Strong

### 2. 🤖 Inference  
The inference engine evaluates fuzzified inputs against a rule base (e.g., *IF age is old AND cholesterol is high THEN risk is high*).  

### 3. 📊 Defuzzification  
Converts fuzzy outputs back to crisp values using the **centroid (center of mass) method**.  

---

## ✨ Features  
- 🖥️ User-friendly web interface built with Flask  
- 📈 Visual representation of fuzzy membership functions  
- ⚡ Real-time risk calculation  
- 🎨 Responsive design for multiple devices  
- 📋 Comprehensive rule base covering various risk factors  
- 🔧 Easily extensible fuzzy system architecture  

---

## 🚀 Installation  

### Prerequisites  
- Python 3.8 or higher  
- pip (Python package manager)  

### Step-by-Step Setup  


**1. Clone the repository**
```bash
git clone https://github.com/Amirbehnam1009/Heart-Disease-Detector-System.git
cd Heart-Disease-Detector-System
```
**2. Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
**3. Install dependencies**
```bash
pip install -r requirements.txt
```
## 💻 Usage
**1. Start the application**

```bash
python app.py
```
**2.Access the web interface**
Open your browser and navigate to http://127.0.0.1:8448

**3.Input medical parameters**
Adjust the sliders to match the patient's metrics:

* Age

* Blood Pressure

* Cholesterol Level

* Heart Rate

* And other relevant factors

**4.Get diagnosis results**
Click "Show Result" to see the fuzzy logic system's assessment of heart disease risk.

## 📁 Project Structure
``` bash
Heart-Disease-Detector-System/
│
├── app.py                 # Main Flask application
├── fuzzy_logic.py         # Core fuzzy logic implementation
├── static/               # Static files (CSS, JS, images)
│   └── css/
│       └── style.css     # Styling for web interface
├── templates/            # HTML templates
│   └── index.html       # Main web page
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```
## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 📸 Simulation Results
**Input Interface**
![Fuzzy1](https://github.com/Amirbehnam1009/Cops-And-Robber/assets/117163007/c1cc9cd3-b5ba-4913-a457-f6138af8c35f)

**Output Result**
![Fuzzy2](https://github.com/Amirbehnam1009/Cops-And-Robber/assets/117163007/f3051a0d-27d3-4938-9b3e-9e9e7c1d256e)
