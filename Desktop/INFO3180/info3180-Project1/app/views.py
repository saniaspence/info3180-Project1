"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import ProfileForm
from app.models import UserProfile
from werkzeug.security import check_password_hash
from .data import get_date, format_date


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/profile', methods =["GET", "POST"])
def profile():

	 form = ProfileForm()
	 id = len(UserProfile.query.all())
	 if request.method == "POST" and form.validate_on_submit():
			first_name = form.first_name.data
			last_name = form.last_name.data
			gender = form.gender.data
			email = form.email.data
			location = form.location.data
			biography = form.biography.data
			image = form.image.data
			joined_on = form.joined_on.data
			image_name = first_name + last_name + str(id +1)

			
			NewUser = UserProfile(first_name=first_name, last_name=last_name,
     		gender=gender, email=email, location=location, biography=biography, image=image, joined_on=joined_on)

			db.session.add(NewUser)
			db.session.commit()

			image.save("app/static/profilepictures/" + image_name + ".jpg")
			flash ("New User Profile Created", successfully)
			return redirect(url_for("profiles"))
		
		return render_template('profile.html', form = form)


@app.route('/profile/<userid>')
def userProfile(userid):

	user = UserProfile.query.filter_by(id = userid).first()
	return render_template('userprofile.html',user = user,date = format_date(user.created_on))


@app.route('/profiles')
def profiles():
	"""Render the website's list of profiles"""
	users = UserProfile.query.all()
	return render_template('profiles.html',users = users)


@app.route('/secure-page')
@login_required
def secure_page():
    """Render the website's secure page."""
    return render_template('secure_page.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # change this to actually validate the entire form submission
        # and not just one field
        if form.username.data:
            # Get the username and password values from the form.
            username = form.username.data
            password = form.password.data

            # using your model, query database for a user based on the username
            # and password submitted. Remember you need to compare the password hash.
            # You will need to import the appropriate function to do so.
            # Then store the result of that query to a `user` variable so it can be
            # passed to the login_user() method below.
            user = UserProfile.query.filter_by(username=username).first()

            if user is not None and check_password_hash(user.password, password):
            # get user id, load into session
            	login_user(user)
            	flash('logged in successfully!')

            # remember to flash a message to the user
            return redirect(url_for("home"))  # they should be redirected to a secure-page route instead
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('you have logged out!')
    return redirect(url_for('home'))

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")