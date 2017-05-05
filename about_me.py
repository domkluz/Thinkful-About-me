from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def about_me_page():
    return render_template("template.html")

if __name__=="__main__":
    app.run(debug=True,port=8080,host="0.0.0.0")
