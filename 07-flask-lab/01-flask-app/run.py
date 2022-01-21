from devsynop import create_app

app = create_app()

if __name__ == "__main__":
    # debug true will allow us to update and run our project automatically
    app.run(debug=True) 