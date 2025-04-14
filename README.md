# Stitching Unit Defect Prediction - ML Project

This project aims to predict the likelihood of garment defects in each shift of a textile stitching unit using machine learning. The objective is to help the company make proactive adjustments in staffing, machine usage, or employee training to minimize defects and maintain high-quality standards.

## 📂 Data Description

The model uses four integrated datasets:

1. **Production Schedule Data**
   - Includes: Shift ID, date, garment type (T-shirt, dress, jacket), target units, assigned employees.

2. **Machine Assignment Data**
   - Includes: Machine ID, make, model, and assignment details for each shift.

3. **Quality Data**
   - Includes: Number of defects recorded per shift.

4. **Employee Data**
   - Includes: Employee ID, age, experience, education level, training status.

## ⚙️ Project Tasks

- ✅ Data Preprocessing: Cleaned and standardized formats, handled missing values.
- ✅ Data Integration: Merged all datasets on common fields (date and shift).
- ✅ Feature Engineering: Created shift-level features like:
  - Average employee experience
  - Distribution of training status
  - Machine make/model frequencies
- ✅ Model Training: Trained a supervised learning model to predict shift-level defect counts.

## 🛠️ Tools & Technologies

- Python (Pandas, NumPy, Scikit-learn, Matplotlib)
- Jupyter Notebook
- Git/GitHub

## 🚀 Outcome

A predictive model capable of identifying high-risk shifts for defects, helping the company optimize operations and improve quality control.

---

Feel free to contribute or fork the repo!
