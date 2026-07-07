# Study Selector

A web-based platform that helps students connect with peers studying the same subjects and years. Study Selector enables users to register, create profiles, find study partners, and collaborate with other students in their field of study.

![Study Selector Logo](LOGO.png)

**Live Demo:** [https://study-selector.vercel.app](https://study-selector.vercel.app)

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Database Setup](#database-setup)
- [API Routes](#api-routes)
- [Contributing](#contributing)

## ✨ Features

- **User Authentication**: Secure login and registration system
- **User Profiles**: Create and manage personal study profiles
- **Subject & Year Selection**: Choose your field of study and academic year
- **Study Partner Discovery**: Find peers studying the same subject and year
- **Profile Management**: Update and delete profile information
- **Responsive Design**: Mobile-friendly interface
- **Contact & About Pages**: Get in touch and learn more about the platform

## 🛠 Tech Stack

- **Frontend**: HTML5, CSS3
- **Backend**: Python with Flask
- **Database**: MySQL
- **Deployment**: Vercel

### Language Composition
- HTML: 45%
- CSS: 36.8%
- Python: 18.2%

## 📁 Project Structure

```
study_selector/
├── flask1.py                 # Flask backend application
├── Webpage.html             # Main homepage
├── Login.html               # Login page
├── Registration.html        # User registration page
├── profile.html             # User profile page
├── Study.html               # Study partner search page
├── search_result.html       # Search results page
├── about.html               # About page
├── contact.html             # Contact page
├── chatting.html            # Chat feature page
├── style.css                # Main stylesheet
├── style1.css - style9.css   # Additional stylesheets
├── LOGO.png                 # Application logo
└── images/                  # Image assets
```

## 🚀 Installation

### Prerequisites
- Python 3.7+
- MySQL Server
- pip (Python package manager)

### Steps

1. **Clone the repository:**
```bash
git clone https://github.com/Yadavsandeep-stack/study_selector.git
cd study_selector
```

2. **Install Python dependencies:**
```bash
pip install flask mysql-connector-python
```

3. **Set up the database:**
   - Create a MySQL database named `temp3`
   - Import the required tables (see [Database Setup](#database-setup))

4. **Configure database connection:**
   - Open `flask1.py`
   - Update the database credentials:
   ```python
   db = mysql.connector.connect(
       host="localhost",
       user="your_mysql_user",
       password="your_mysql_password",
       database="temp3"
   )
   ```

5. **Run the application:**
```bash
python flask1.py
```

The application will be available at `http://localhost:5000`

## 💾 Database Setup

Create the following tables in your MySQL database:

### student table
```sql
CREATE TABLE student (
    username VARCHAR(50) PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    year VARCHAR(50),
    subject VARCHAR(100)
);
```

### subjects_table
```sql
CREATE TABLE subjects_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject VARCHAR(100)
);
```

### year_table
```sql
CREATE TABLE year_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year VARCHAR(50)
);
```

## 📱 Usage

### For Students

1. **Register**: Create a new account with username, email, and password
2. **Select Academic Details**: Choose your year and subject of study
3. **Find Study Partners**: Use the Study page to search for peers in your subject and year
4. **View Profiles**: See contact information and details of matching students
5. **Manage Profile**: Update or delete your profile information anytime

### Navigation

- **Home**: Access the main landing page
- **About**: Learn more about the Study Selector platform
- **Study**: Search for study partners by subject and year
- **Contact**: Get in touch with the team
- **Profile**: View and manage your personal information

## 🔌 API Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home/Login page |
| `/login` | POST | User login |
| `/register` | GET, POST | User registration |
| `/profile` | GET | View user profile |
| `/update_profile` | GET, POST | Update profile information |
| `/delete_profile` | POST | Delete user account |
| `/logout` | GET | User logout |
| `/homepage` | GET | Main homepage |
| `/study` | GET | Study partner search form |
| `/search_results` | GET | Display search results |
| `/about` | GET | About page |
| `/contact` | GET | Contact page |

## 🔐 Security Notes

- Passwords are stored in the database (consider implementing hashing for production)
- Session management is implemented using Flask sessions
- Input validation should be enhanced for production use

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests to improve the project.

## 📄 License

This project is open source and available under the MIT License.

## 📧 Contact

For questions or suggestions, please reach out through the Contact page on the application or visit the [GitHub repository](https://github.com/Yadavsandeep-stack/study_selector).

---

**Created by**: Sandeep Yadav  
**Last Updated**: April 2026
