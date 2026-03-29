# Tsuki Line 💫
**Tsuki Line** is a comprehensive Railway Management System built with **Python**. It features a modern GUI, automated email notifications, and real-time route visualization. The project follows a aesthetic anime themes
> ⚠️ Originally developed as a Class 12 Computer Science project, this grew beyond the syllabus scope due to its GUI-based architecture — so it was rebuilt as a passion project instead. Visuals are purely experimental and for fun, so dont take it seriously.

---

## 🚀 Features
* **User Authentication**: Secure Sign-up and Login system integrated with **MySQL**.
* **Ticket Booking**: Supports both **Express** and **Local** train reservations.
* **Dynamic Seat Management**: Real-time availability tracking with support for waiting lists.
* **Automated Ticketing**: Generates a custom-designed digital ticket and emails it to the user using **SMTP**.
* **Live Route Mapping**: Uses **Selenium WebDriver** to fetch and display live Google Maps routes between stations.
* **Multimedia Integration**: Background music and interactive UI elements powered by `pygame` and `customtkinter`.

## 🛠️ Tech Stack
* **Language**: Python 3.x
* **Frontend**: `customtkinter`, `Pillow` (PIL)
* **Backend**: **MySQL** (via `mysql-connector-python`)
* **Automation**: **Selenium** (Chrome Driver)
* **Utilities**: `smtplib` (Email), `pygame` (Audio), `python-dotenv` (Security)

## 📋 Prerequisites
Before running the app, ensure you have the following installed:
* **MySQL Server**
* **Google Chrome** (for Selenium route fetching)
* **Required Python libraries**:
```bash
pip install customtkinter pillow mysql-connector-python tkcalendar pygame selenium python-dotenv
```

## ⚙️ Setup & Configuration

Follow these steps to get the **Tsuki Line** environment running on your local machine.

### 1. Database Setup 🗄️
You must have **MySQL** installed. Create a database named `TSUKI_LINE` and initialize the required tables.
* **Database Name**: `TSUKI_LINE`
* **Core Tables**: `USER`, `TRAIN_SCHEDULE`, `COST`, `EXPRESS_BOOKING`, and `LOCAL_BOOK`.
* Ensure your local MySQL server is running before launching the application.
* You shoud enter data manually through mysql in `TRAIN_SCHEDULE` and `COST` 

#### `USER` Table

| Field | Type | Null | Key | Default | Extra |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **USER_ID** | int | NO | PRI | NULL | auto_increment |
| **Email_ID** | varchar(50) | YES | | NULL | |
| **PASSWORD** | varchar(20) | YES | | NULL | |
| **NAME** | varchar(30) | YES | | NULL | |
| **AGE** | int | YES | | NULL | |
| **GEN** | varchar(1) | YES | | NULL | |

#### `express_booking` Table

| Field        | Type        | Null | Key | Default | Extra          |
|--------------|-------------|------|-----|---------|----------------|
| BOOKING_NO   | int         | NO   | PRI | NULL    | auto_increment |
| USER_ID      | int         | YES  |     | NULL    |                |
| TRAIN        | varchar(30) | YES  |     | NULL    |                |
| DATE         | date        | YES  |     | NULL    |                |
| BOOKING_DATE | date        | YES  |     | NULL    |                |
| PNR          | bigint      | YES  |     | NULL    |                |
| STATUS       | varchar(15) | YES  |     | NULL    |                |
| SEAT         | varchar(5)  | YES  |     | NULL    |                |

#### `local_book` Table

| Field      | Type        | Null | Key | Default | Extra          |
|------------|-------------|------|-----|---------|----------------|
| BOOKING_ID | int         | NO   | PRI | NULL    | auto_increment |
| FROMS      | varchar(20) | YES  |     | NULL    |                |
| TOS        | varchar(20) | YES  |     | NULL    |                |
| USER_ID    | int         | YES  |     | NULL    |                |
| PNR        | bigint      | YES  |     | NULL    |                |

#### `train_schedule` Table

| Field          | Type        | Null | Key | Default | Extra |
|----------------|-------------|------|-----|---------|-------|
| TRAIN_NO       | int         | NO   | PRI | NULL    |       |
| TRAIN_NAME     | varchar(30) | YES  |     | NULL    |       |
| FROM           | varchar(15) | YES  |     | NULL    |       |
| TO             | varchar(15) | YES  |     | NULL    |       |
| DEPARTURE_TIME | time        | YES  |     | NULL    |       |
| ARRIVAL_TIME   | time        | YES  |     | NULL    |       |
| MON            | tinyint(1)  | YES  |     | 1       |       |
| TUE            | tinyint(1)  | YES  |     | 1       |       |
| WED            | tinyint(1)  | YES  |     | 1       |       |
| THU            | tinyint(1)  | YES  |     | 1       |       |
| FRI            | tinyint(1)  | YES  |     | 1       |       |
| SAT            | tinyint(1)  | YES  |     | 1       |       |
| SUN            | tinyint(1)  | YES  |     | 1       |       |

#### `cost` Table

| Field    | Type | Null | Key | Default | Extra |
|----------|------|------|-----|---------|-------|
| TRAIN_NO | int  | NO   | PRI | NULL    |       |
| GN       | int  | YES  |     | NULL    |       |
| SL       | int  | YES  |     | NULL    |       |
| 1A       | int  | YES  |     | NULL    |       |
| 2A       | int  | YES  |     | NULL    |       |
| 3A       | int  | YES  |     | NULL    |       |
| 3E       | int  | YES  |     | NULL    |       |
| CC       | int  | YES  |     | NULL    |       |

### 2. Environment Variables 🔐
To protect your sensitive credentials (like your database password and Gmail App key), this project uses a `.env` file.
1. Create a file named `.env` in the root directory.
2. Add the following lines and replace the placeholders with your actual data:
```env
MYSQL_PASSWORD=your_actual_mysql_password
GMAIL_APP_PASSWORD=your_16_digit_gmail_app_key
```

### 3. Assets & Multimedia 🎨
The GUI relies on specific external assets to render correctly. Ensure your file structure looks like this:
* **`/Holy Grail/`**: This directory must contain all UI images (logos, backgrounds, and buttons).
* **`song.mp3`**: Place your background music file directly in the root directory.
* **`Tsuki line.py`**: The main execution script.

### 4. Installation 🛠️
Install the necessary dependencies using pip:
```bash
pip install customtkinter pillow mysql-connector-python tkcalendar pygame selenium python-dotenv
```

## 📸 Screenshots & UI

The application uses `customtkinter` to achieve a sleek, dark-themed interface.

- **Login / Sign-up:** Features Gaussian blurred backgrounds for a modern look and with anime asthatics.
  <img width="1001" height="661" alt="Screenshot 2025-07-13 192644" src="https://github.com/user-attachments/assets/05aab9f9-22f8-4ee2-ac1f-3b5ebaf2a0ba" />
  <img width="1130" height="727" alt="Screenshot 2025-07-16 213223" src="https://github.com/user-attachments/assets/1698176d-08d1-40d3-801e-bfb5a664cfc3" />

- **Route Visualization:** Integrated Google Maps screenshots via headless Selenium.
  <img width="1245" height="716" alt="Screenshot 2025-10-14 203537" src="https://github.com/user-attachments/assets/870a5970-4996-4f95-a038-4fd51e4164b1" />

- **Express Train Booking:** Features Gaussian blurred backgrounds for a modern look and with anime asthatics.
  <img width="989" height="659" alt="Screenshot 2026-01-29 230044" src="https://github.com/user-attachments/assets/b707f025-c2b6-4546-930d-ea9cd0be69da" />

  
## 🤖 Credits

- **Selenium Integration:** Route fetching and screenshot logic was independently designed and architected, with implementation assistance from [Claude AI](https://claude.ai).
- Additional minor assistance from [ChatGPT](https://chatgpt.com) during development.
-The markdown was made by [Claude AI](https://claude.ai) coz I suck in it 💀
