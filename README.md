# Artificial Pancreas System (APS) 

A simplified simulation of an **Artificial Pancreas System** built with Python.  
The system models how blood glucose levels respond to **meals**, **exercise**, and **insulin delivery**, and automatically predicts the right action to maintain glucose balance.

This project demonstrates:
- Object-Oriented Programming principles  
- Method simulation for physiological processes  
- Decision logic (high/low glucose regulation)  
- Automated testing using `pytest`  

---
##  How It Works

The `ArtificialPancreasSystem` simulates glucose regulation using simple formulas:

### Meal Intake
Increases glucose levels:
```python
glucose_level += carbs * GLUCOSE_PER_CARB
```
### Exercise

Decreases glucose but never below 50:

```python
glucose_level -= duration * GLUCOSE_BURN_PER_MIN
```
### Predict Action

Decides whether to deliver insulin, warn, or maintain:

```python
if glucose > target + tolerance:
    deliver_insulin()
elif glucose < target - tolerance:
    warn_low_glucose()
else:
    maintain()
```

---
## Running the Project

### 1️ Clone the repository
```bash
git clone https://github.com/Praze-hub/de-week2-unittest-Okechukwu_God-spraise.git
```
### Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
### Install dependencies
```bash
pip install requirements.txt
```

### Run demo
```bash
python main.py
```

### Run tests
```bash
python -m pytest test_artificial_pancreas.py
```








