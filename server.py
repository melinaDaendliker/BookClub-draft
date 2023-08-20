from flask import Flask, render_template, request
import datetime
import requests
import smtplib


blog_url = "https://api.npoint.io/efe6ae2a5c06d9afb2c9"
response = requests.get(blog_url)
all_posts = response.json()
year = datetime.date.today().year


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", year=year, posts=all_posts)

@app.route('/post/<int:num>')
def posts(num):
    blog_post = all_posts[num - 1]
    return render_template("post.html", year=year, post=blog_post)


@app.route('/about')
def about():
    return render_template("about.html", year=year)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['username']
        email = request.form['email']
        message = request.form['message']
        return render_template("contact.html", year=year, msg_sent=True)
    return render_template("contact.html",  year=year, msg_sent=False)


if __name__ == "__main__" :
    app.run(debug=True)




