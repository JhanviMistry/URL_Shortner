import random
import string

from flask import Flask, render_template, redirect, request

app = Flask(__name__)
shortened_url = {}

def short_url(length=7):
    chars = string.ascii_letters + string.digits
    url = "".join(random.qchoice(chars) for _ in range(length))
    return url

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        url = short_url()
        while url in shortened_url:
            url = short_url()

        shortened_url[url] = long_url
    
        return f"Shortened URL : {request.url_root}{url}"
    return render_template("index.html") #if GET #render_template to render the html page for the long url 

@app.route("/<url>")
def redirect_url(url):
    long_url = shortened_url.get(url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)