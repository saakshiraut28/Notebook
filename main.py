from website import create_app

app = create_app()

if __name__=='__main__': # Only if we run this file our server will start
    app.run(debug=True) # debug == true becoz we don't want to keep the flask webserver manually running
