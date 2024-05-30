#!/usr/bin/python3
# app/views.py
from flask import render_template, flash, request, redirect, url_for
from app import app, db, login_manager
from app.models import User, JobOffer
from flask import Flask
from app.forms import RegistrationForm 
from app.forms import Modifinfo
from app.forms import LoginForm
from sqlalchemy.exc import SQLAlchemyError
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_required, UserMixin
from  flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
@app.route('/', methods=['GET', 'POST'])
def homepage():
    app.logger.info('Accès à la page d\'accueil')
    return render_template('HOME_PAGE.html')

@app.route("/contact")
def contact():
    app.logger.info('utilisateur a accede  à la page de contacte')
    return render_template("contact.html")

@app.route("/prive")
def sctr_prv():
    app.logger.info('utilisateur a accede  à la page du secteur prive')
    return render_template("sctr_prv.html", pp="PRIVé")

#ljadid
@app.route("/modif", methods=['GET', 'POST'])
def modif():
    modif = Modifinfo()
    if modif.validate_on_submit():
        current_user.email = modif.email.data
        current_user.username = modif.username.data
        db.session.commit()
        flash('Vos informations de profil ont été mises à jour avec succès')
        return redirect(url_for('profile'))
    modif.email.data = current_user.email
    modif.username.data = current_user.username
    return render_template('profile.html', modif=modif)

@app.route("/public")
def sctr_pblc():
    app.logger.info('utilisateur a accede  à la page du secteur publique')
    return render_template("sctr_pblc.html", pp="public")


@app.route("/councours")
def councours():
    app.logger.info('utilisateur a accede  à la page des concours')
    return render_template('modls_councours.html',  pp="councours")


@app.route("/stages")
def stages():
    app.logger.info('utilisateur a accede  à la page des stages')
    return render_template('stages.html', pp=" stages")


@app.route("/orientation")
def orientation():
    app.logger.info('utilisateur a accede  à la page des stages')
    return render_template("orientation.html", pp="oriontations")


@app.route("/faq")
def faq():
    app.logger.info('utilisateur a accede  à la page des Faq')
    return render_template("faq_page.html", pp="faq")

#@app.route('/loginn')
#def loginn():
    
 #   form = LoginForm()
  #  return render_template('login.html', form=form)
#@app.route('/login')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #flash('dkhaaal')    
    if request.method == 'POST' and form.validate_on_submit():
        # Logique de connexion ici
        flash('Connectez-vous')
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(':)', 'success')
            print("okkkkkkk") 
            # L'utilisateur existe et le mot de passe est correct
            # Vous pouvez ajouter la logique de connexion ici
            return redirect(url_for('profile'))
        else:
            # L'utilisateur n'existe pas ou le mot de passe est incorrect
            # Vous pouvez ajouter un message d'erreur à afficher dans le formulaire
            print("not okkkkkkk")
            flash('Nom d\'utilisateur ou mot de passe incorrect', 'danger')
    #logique de gestion de la connexion ici
        print("mot okkkkkkk")
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])

#@app.route('/register')
def register():
    form = RegistrationForm()
    app.logger.info('Accès à la page d\'inscription')

    if request.method == 'POST' and form.validate_on_submit():
        try:
        # kan Créew un nouvel utilisateur avec les données du formulaire
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            #kanverifiew ila admin
            is_admin = False
            admin = 'admin@piw.com' 
            if form.email.data == admin:
                id_admin = True
            new_user = User(username=form.username.data, email=form.email.data, password=hashed_password, is_admin=is_admin)

        # anzido l'utilisateur à la base de données
            db.session.add(new_user)
            db.session.commit()
            flash(f'Vous etes bien inscrit  {form.username.data}')
            return redirect(url_for('login'))
        except SQLAlchemyError as e:
            app.logger.error(f"Erreur d'accès à la base de données lors de l'inscription : {e}")
            db.session.rollback()
            flash('Veuillez vous connecter vous etes deja inscrit', 'danger')

    return render_template('register.html', form=form)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # Check if the user is authenticated
    if current_user.is_authenticated:
        if request.method == 'POST':
            # Handle form submission for both admins and non-admins
            username =  request.form.get('username')
            current_user.username = username
            email = request.form.get('email')
            current_user.email = email
            db.session.commit()
            flash('Vos informations de profil ont été mises à jour avec succès')
            return redirect(url_for('profile'))

        # Render the appropriate template based on admin status
        if current_user.is_admin:
            # Admin users will see 'admin_profile.html'
            return render_template('admin_profile.html')
        else:
            # Non-admin users will see 'profile.html'
            return render_template('profile.html')
    else:
        # Redirect to the login page if the user is not authenticated
        flash('Veuillez vous connecter pour accéder à votre profil.', 'warning')
        return redirect(url_for('login'))
        

#@app.route('/profile/<int:user_id>')
#def profile(user_id):
 #   try:
        # Récupérez l'utilisateur de la base de données en utilisant l'ID
  #      user = User.query.get_or_404(user_id)
   #     return render_template('profile.html', user=user)
   # except SQLAlchemyError as e:
    #    app.logger.error(f"Erreur d'accès à la base de données lors de la récupération du profil : {e}")
     #   flash('Erreur d\'accès à la base de données', 'danger')
      #  return redirect(url_for('home'))

@app.route('/logout')
def logout():
    logout_user()
    # Rediriger vers une page après la déconnexion
    return redirect(url_for('home'))

@app.route('/nous_connaitre')
def nous_connaitre():
    app.logger.info('Accès à la nous_connaitre')
    return render_template('nous_connaitre.html')
