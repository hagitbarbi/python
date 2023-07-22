
import requests


def login_function(login_url, username, password):
    # יצירת משתנה מטעם ממשתקת כדי לקבל את הפרטים של הטופס התחברות
    payload = {
        'username': username,
        'password': password
    }

    # שליחת בקשת POST לכתובת ה-URL של טופס ההתחברות עם הפרטים של המשתמש
    response =requests.post(login_url, data=payload)

    # בדיקה אם התחברות הצליחה
    if response.status_code == 200:
        print("התחברת בהצלחה!")
        # כאן אפשר להוסיף קוד נוסף שיבצע פעולות בממשק לאחר ההתחברות
    else:
        print("התחברות נכשלה. נסה שוב.")

# דוגמא לשימוש בפונקציה
login_url = "https://example.com/login"  # הקישור לטופס ההתחברות
username = "my_username"  # שם המשתמש
password = "my_password"  # הסיסמה
login_function(login_url, username, password)
