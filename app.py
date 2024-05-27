from flask import Flask, request, render_template
from src.pipeline.prediction_pipeline import PredictPipeline, CustomData

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def predict():

    if request.method == "POST":
        data = CustomData(
            carat = float(request.form.get("carat")),
            cut = request.form.get("cut"),
            color = request.form.get("color"),
            clarity = request.form.get("clarity"),
            depth = float(request.form.get("depth")),
            table = float(request.form.get("table")),
            x = float(request.form.get("x")),
            y = float(request.form.get("y")),
            z = float(request.form.get("z"))

        )

        final_df = data.data_to_dataframe()

        pred = PredictPipeline()
        prediction = pred.predict(final_df)

        result = round(prediction[0], 2)

        return render_template("result.html", predicted_value = result)







if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)