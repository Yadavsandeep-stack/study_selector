from flask import Flask,flash, request, render_template, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session

# DB Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sa@20061129",
    database="temp3"
)

@app.route('/')
def home():
    return render_template('Login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student WHERE username = %s AND password = %s", (username, password))
    student = cursor.fetchone()
    cursor.close()

    if student:
        session['username'] = student['username']
        return redirect(url_for('profile'))
    else:
        return "Login failed. Invalid username or password."

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('home'))

    username = session['username']
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student WHERE username = %s", (username,))
    student = cursor.fetchone()
    cursor.close()

    return render_template('profile.html', student=student)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/homepage')
def homepage():
    return render_template('Webpage.html') 



@app.route('/register', methods=['GET', 'POST'])
def register():
    cursor = db.cursor(dictionary=True)
    
    # Fetch subjects and years from the database
    cursor.execute("SELECT * FROM subjects_table")
    subjects_table = cursor.fetchall()
    
    cursor.execute("SELECT * FROM year_table")
    years_table = cursor.fetchall()

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        selected_year = request.form['year']  # Get the selected year
        selected_subject = request.form['subjects']  # Get the selected subject

        # Password validation
        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for('register'))

        # Check if username or email already exists
        cursor.execute("SELECT * FROM student WHERE username = %s OR email = %s", (username, email))
        existing_user = cursor.fetchone()

        if existing_user:
            flash("Username or email already exists.", "error")
            return redirect(url_for('register'))

        # Insert new user into MySQL
        cursor.execute("INSERT INTO student (username, email, password) VALUES (%s, %s, %s)", 
                    (username, email, password))  
        db.commit()

        # Insert selected year into student table
        cursor.execute("UPDATE student SET year = %s WHERE username = %s", (selected_year, username))
        db.commit()

        # Insert the selected subject into the student table
        if selected_subject:
            cursor.execute("UPDATE student SET subject = %s WHERE username = %s", (selected_subject, username))
            db.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('home'))

    return render_template('Registration.html', subjects_table=subjects_table, years_table=years_table)
@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    if 'username' not in session:
        return redirect(url_for('home'))

    username = session['username']
    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        selected_year = request.form['year']
        selected_subject = request.form['subjects']
        # Password validation
        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for('update_profile'))
        # Update user information in MySQL
        cursor.execute("UPDATE student SET email = %s, password = %s, year = %s, subject = %s WHERE username = %s", 
                    (email, password, selected_year, selected_subject, username))
        db.commit()
        flash("Profile updated successfully!", "success")
        return redirect(url_for('profile'))
    else:
        cursor.execute("SELECT * FROM student WHERE username = %s", (username,))
        student = cursor.fetchone()

        # Fetch subjects and years from the database
        cursor.execute("SELECT * FROM subjects_table")
        subjects_table = cursor.fetchall()
        
        cursor.execute("SELECT * FROM year_table")
        years_table = cursor.fetchall()
        cursor.close()
        return render_template('update_profile.html', student=student, subjects_table=subjects_table, years_table=years_table)
@app.route('/delete_profile', methods=['POST'])
def delete_profile():
    if 'username' not in session:
        return redirect(url_for('home'))

    username = session['username']
    cursor = db.cursor(dictionary=True)

    # Delete user from MySQL
    cursor.execute("DELETE FROM student WHERE username = %s", (username,))
    db.commit()
    cursor.close()

    # Clear the session
    session.pop('username', None)
    flash("Profile deleted successfully!", "success")
    return redirect(url_for('home'))



@app.route('/study')
def study_form():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT DISTINCT subject FROM subjects_table")
    subjects = [row['subject'] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT year FROM year_table")
    years = sorted([row['year'] for row in cursor.fetchall()], reverse=True)

    return render_template('Study.html', subjects=subjects, years=years)


@app.route('/search_results')
def search_results():
    subject = request.args.get('subject')
    year = request.args.get('year')

    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT username, email, year, subject
        FROM student
        WHERE subject = %s AND year = %s
    """, (subject, year))
    
    results = cursor.fetchall()
    cursor.close()

    return render_template('search_result.html', results=results, subject=subject, year=year)

@app.route('/contact')
def contact():

    return render_template('contact.html')
@app.route('/about')
def about():
    return render_template('about.html')






if __name__ == '__main__':
    app.run(debug=True)
