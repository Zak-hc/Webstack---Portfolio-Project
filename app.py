from agil import create_app

app = create_app()

if __name__ == '__main__':
    with create_app().app_context():
        db.create_all()  # Crée les tables dans la base de données si elles n'existent pas déjà
    app.run(debug=True)

