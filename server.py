# Assignment: Registration Form
# Create a simple registration page with the following fields:

# email
# first_name
# last_name
# password
# confirm_password
# Here are the validations you must include:

# All fields are required and must not be blank
# First and Last Name cannot contain any numbers
# Password should be more than 8 characters
# Email should be a valid email
# Password and Password Confirmation should match 

# When the form is submitted, make sure the user submits appropriate information. 
# If the user did not submit appropriate information, 
# return the error(s) above the form that asks the user to correct the information. 

# Message Flashing with Categories
# For this, you will need to use flash messages at the very least. 
# You may have to take this one step further and add categories to the flash messages. 
# You can learn that from the flask doc: flash messages with categories

# If the form with all the information is submitted properly, 
# simply have it say a message "Thanks for submitting your information."

# Ninja Version:
# Add the validation that requires a password to have at least 1 uppercase letter and 1 numeric value.

# Hacker Version:
# Add a birth-date field that must be validated as a valid date and must be from the past


from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
import re
from datetime import datetime

# our index route will handle rendering our form

#1
@app.route('/')
def index():
  session['date'] =  datetime.now().strftime("%m/%d/%Y")
  return render_template("form.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
# WE ARE WAITING FOR A POST REQUEST
@app.route('/process', methods=['POST'])
def data():
  print "Got Post Info"
  myemail = request.form['email']
  fname = request.form['firstname']
  lname = request.form['lastname']
  session['pw'] = request.form['password']
  confPw = request.form['confpassword']
  bady = request.form['bday']
  print "*" * 80, myemail
  print "*", fname
  print "*", lname
  print "*", session['pw']
  print "*", confPw

   #do validation
   
#setup the regex to check for just letters in the first and last names.
  ALPHA_REGEX = re.compile(r'^[a-zA-Z]+$')
  EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
  #some test values
  #A23456789
  #23456789A
  #ABCDEFGh9
  #9ABCDEFGh
  PW_U_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]*[A-Z]+[a-zA-Z0-9.+_-]*$')
  PW_NUM_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]*[0-9]+[a-zA-Z0-9.+_-]*$')
  BDAY_VALID_REGEX = re.compile(r'^[0-9]{2}\/{1}[0-9]{2}\/[0-9]{4}$')
  
  if len(request.form['email']) < 1 or len(fname) < 1 or len(lname) < 1 or len (session['pw']) < 1 or len(confPw) < 1 :
    flash(u"Please enter all data",'flashErrorMessages')
    return redirect('/') 
  elif not ALPHA_REGEX .match(request.form['firstname']) and not ALPHA_REGEX .match(request.form['lastname']):
    flash(u"First name must only contain letters",'flashErrorMessages')
    flash(u"Last name must only contain letters",'flashErrorMessages')
    return redirect('/') 
  elif not ALPHA_REGEX.match(request.form['lastname']):
    flash(u"Last name must only contain letters",'flashErrorMessages')
    return redirect('/') 
  elif not ALPHA_REGEX.match(request.form['firstname']):
    flash(u"First name must only contain letters",'flashErrorMessages')
    return redirect('/')
  elif len (request.form['password']) < 9:
     flash(u"Password must be at least 9 characters",'flashErrorMessages')
     return redirect('/')
  elif not PW_U_REGEX.match(request.form['password']):
     flash(u"Password must contain at least 1 uppercase letter",'flashErrorMessages')
     return redirect('/')
  elif not PW_NUM_REGEX.match(request.form['password']):
    flash(u"Password must contain at least 1 number",'flashErrorMessages')
    return redirect('/')
  elif request.form['password'] != confPw:
    flash(u"Passwords do NOT match",'flashErrorMessages')
    return redirect('/')  
  elif not BDAY_VALID_REGEX.match(request.form['bday']):
    flash(u"please enter a valid bady",'flashErrorMessages')
    return redirect('/')
  else:
    flash(u'Thanks for submitting your information', 'flashNoErrorMessages')
    return redirect('/')


   
   
app.run(debug=True) # run our server

