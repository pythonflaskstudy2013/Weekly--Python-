#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import redirect, request, render_template_string, render_template
app = Flask(__name__)

tweets = [
    u"첫 글",
    u"배고파! 밥 먹자",
    u"아! 배불러"
]

@app.route("/v1/tweets")
def home():
    html = ""
    for i in range(len(tweets), 0, -1):
        html += "<li>" + tweets[i-1] + "</li>"

    return """<!doctype html>
<html lang="ko">
<head>
<title>My Tweets v1</title>
</head>
<body>
<form action="/update" method="post">
    <input type="submit" value="Update" /><br />
    <textarea name="status" cols="100" rows="5"></textarea>
</form>
<h1>Tweets</h1>
<ul>""" + html + """
</ul>
</body>
</html>
"""

@app.route("/v2/tweets")
def tweets2():
    return render_template_string("""<!doctype html>
<html lang="ko">
<head>
<title>My Tweets v2</title>
</head>
<body>
<form action="/update" method="post">
    <input type="submit" value="Update" /><br />
    <textarea name="status" cols="100" rows="5"></textarea>
</form>
<h1>Tweets</h1>
<ul>
{% for tweet in tweets %}
  <li>{{ tweet }}</li>
{% endfor %}
</ul>
</body>
</html>
""", tweets=tweets)

@app.route("/v3/tweets")
def tweets3():
    return render_template('tweets.html', tweets=tweets)


@app.route('/update', methods=('POST',))
def update():
    status = request.form.get('status')
    tweets.append(status)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
