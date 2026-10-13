from flask import Flask, render_template_string

app = Flask(__name__)

# Басты бет (Home page)
@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="kk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PaaS веб-қосымшасы</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #eef2f7;
                text-align: center;
                padding: 50px 15px;
            }
            .container {
                max-width: 650px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2457a7;
            }
            p {
                font-size: 18px;
                line-height: 1.6;
                color: #333;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #2457a7;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
            a:hover {
                background-color: #1a3e75;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Қош келдіңіз!</h1>
            <p>Бұл PaaS платформасына орналастыруға арналған қарапайым Flask веб-қосымшасы.</p>
            <a href="/info">Қосымша туралы ақпарат</a>
        </div>
    </body>
    </html>
    """)

# Ақпараттық бет (Info page)
@app.route("/info")
def info():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="kk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ақпарат</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #eef2f7;
                text-align: center;
                padding: 50px 15px;
            }
            .container {
                max-width: 650px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2457a7;
            }
            p {
                font-size: 18px;
                line-height: 1.6;
                color: #333;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #6c757d;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
            a:hover {
                background-color: #5a6268;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Қосымша туралы</h1>
            <p>Бұл веб-қосымша Python Flask фреймворгі арқылы жасалды және бұлттық ортада іске қосуға дайын.</p>
            <a href="/">Басты бетке қайту</a>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)