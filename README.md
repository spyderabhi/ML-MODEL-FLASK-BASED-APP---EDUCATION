# 🎓 ML Models Flask Based Apps - Education

A Flask web application that predicts educational enrollment totals using a machine learning model. This app lets users input key demographic and educational parameters to get real-time predictions, all wrapped in a clean, responsive UI with educational-themed animations.

---

## ✨ Features

- 📝 **Interactive Form:** Input 15 different features including school counts, population stats, literacy rates, and more.  
- 🤖 **ML-Powered Predictions:** Uses a pre-trained model and scaler for accurate enrollment forecasting.  
- 🎨 **Educational Animations:** Engaging background animations related to education to improve user experience.  
- ⚠️ **Error Handling:** Graceful messages when model/scaler loading or prediction fails.  
- 📱 **Responsive Design:** Works well on desktop and mobile devices.

---

## 🛠 Tech Stack

- Backend: 🐍 Python Flask  
- Frontend: 💻 HTML, CSS, JavaScript  
- ML Libraries: 📊 scikit-learn, XGBoost  
- Styling & Animations: 🎨 Custom CSS with animated SVGs

---

## 🚀 Installation and Setup

### 🔧 Prerequisites

- Python 3.7+  
- pip (Python package manager)


### 🖥 Usage
Fill in the form fields with the relevant educational and demographic data. Click Predict to get the predicted enrollment total. View the prediction on the result page. Use the link to return to the form and make new predictions.

### 📁 File Structure
├── app.py              # Main Flask application  
├── load_model.py       # Module to load trained model and scaler  
├── templates/  
│   ├── index.html      # Input form page with animations  
│   └── result.html     # Prediction results page  
├── static/  
│   └── (optional assets like images, css, js)  
├── best_model.pkl      # Serialized ML model  
├── data_scaler.pkl     # Serialized scaler for preprocessing  
├── requirements.txt    # Python dependencies  
└── README.md           # This documentation  


### 📝 Notes
he ML model was trained using XGBoost and saved as a pickle file. Make sure best_model.pkl and data_scaler.pkl are present in the root directory. The app uses Flask’s built-in development server and is not recommended for production without a production WSGI server like Gunicorn.

### 🔮 Future Enhancements
🔐 Add user authentication and history of predictions

🔗 Provide API endpoints for integration with other apps

📈 Include detailed visualization of results and feature importance

📚 Expand the app to cover more educational prediction models

### 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

### 
📬 Contact
for any questions or suggestions, feel free to open an issue or contact me at theanonymousspyder@gmail.com


