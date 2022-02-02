from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #refreshes page every time a change is made. turned off in production 