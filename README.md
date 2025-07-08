# Conglomerate Authentication System

A **Multi-Factor Authentication (MFA)** system built using Python, OpenCV, and Flask to provide layered, secure access to sensitive user credentials. The system incorporates four stages of authentication: text-based login, color pattern verification, image-based puzzle solving, and facial recognition using the **LBPH Face Recognition algorithm**. Designed for maximum usability and minimal infrastructure, the project targets small to medium organizations requiring robust identity protection.

---

## 🔐 Project Overview

Traditional username-password systems are vulnerable to keylogging, shoulder surfing, and password breaches. To mitigate these threats, this system introduces a **4-level authentication** model:

1. **Text Password** – Username & password input
2. **Color Combination** – User-defined RGB color pattern
3. **Image Puzzle** – User selects and sorts image pieces under a time constraint
4. **Face Recognition** – Final authentication via live webcam input

Users must pass all four levels to access their dashboard and manage saved credentials securely.

---

## 🛠️ Technologies Used

- **Programming Language**: Python
- **Framework**: Flask
- **Face Recognition**: OpenCV (LBPH algorithm)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite3
- **Libraries**: NumPy, Pandas, OS, CV2, Flask, Face Recognition

---

## 🧠 Features

- Multi-layered security with increasing complexity at each stage
- **LBPH-based facial recognition** with grayscale image training
- Secure storage of login credentials for multiple social platforms
- User dashboard to **add**, **update**, or **delete** credential records
- **30-second timeout** mechanism for puzzle-solving to prevent brute-force access
- Data encryption and image processing for enhanced privacy

---

## 📷 Face Recognition Workflow

- Captures **200+ face images** during registration
- Converts captured images to grayscale to train a consistent model
- Uses **LBPHFaceRecognizer** from OpenCV to match real-time webcam input with stored features
- If match found → proceed to dashboard  
- If not → revert to login screen

---

## 🧩 Authentication Flow

```mermaid
graph TD
A[User Registration] --> B[Enter Text Credentials]
B --> C[Select Color Pattern]
C --> D[Upload and Sort Image Pieces]
D --> E[Capture Face Image]
E --> F[Train LBPH Model]
F --> G[Login Process Begins]
G --> H{Pass All 4 Levels?}
H -- Yes --> I[Access Dashboard]
H -- No --> J[Redirect to Start]
````

---

## 📁 How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/conglomerate-authentication-system.git
   cd conglomerate-authentication-system
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open your browser and navigate to:

   ```
   http://localhost:5000
   ```

---

## 🧪 Sample Screenshots

* ✅ Registration page with personal details
* 🎨 Color selection interface
* 🧩 Puzzle interaction screen
* 📷 Face capture with webcam
* 🗂️ Dashboard to store and manage social credentials

---

## 👨‍💻 Authors

* **Haasitha Kodali** - [Email](mailto:kodalihaasitha@gmail.com)
* **K. Venkateswara Rao**
* **Y. Hari Chandana**
* **S. Manasa**

---

## 🧾 License

This project is intended for **academic and educational use only**. For commercial deployment, further optimization and regulatory compliance will be required.

---

## 📚 References

* LBPH Face Recognition (OpenCV)
* Research papers on OTP, biometric, and image-based authentication (see project report for full citations)
