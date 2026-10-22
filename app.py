from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():

    if request.method == "POST":

        resume = request.files["resume"]

        resume.save("uploads/" +  resume.filename)

        return f"You uploaded {resume.filename}"

        
        


    return render_template("product.html")




app.run(debug=True)