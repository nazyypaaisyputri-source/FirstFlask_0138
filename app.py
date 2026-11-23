from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/form-post", methods=["GET", "POST"])
def form_post():
    hasil_nama = None
    pesan_error = None

    if request.method == "POST":
        nama_input = request.form.get("nama_input", "").strip()
        if not nama_input:
            pesan_error = "Kolom nama tidak boleh kosong!"
        else:
            hasil_nama = nama_input

    return render_template(
        "index.html",
        hasil_nama=hasil_nama,
        pesan_error=pesan_error,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)