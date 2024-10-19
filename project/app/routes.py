from flask import blueprints, render_template

main_routes = blueprints.Blueprint('main_routes', __name__)


@main_routes.route('/')
def home():
    return render_template('home.html', title='Home' ,message='THis is home page.')
@main_routes.route('/about')
def about():
    return render_template('about.html', title='About' ,message='This is about page.')
