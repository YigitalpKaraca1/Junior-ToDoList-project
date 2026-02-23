from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    search = ""
    filtered_tasks = tasks

    if request.method == "POST":
        search = request.form.get("searchbar")
        new_task = request.form.get("task")
        delete_index = request.form.get("delete_index")

        if search:
            filtered_tasks = [t for t in tasks if search.lower() in t.lower()]
        else:
            filtered_tasks = tasks

        if delete_index is not None:
            index = int(delete_index)
            if 0 <= index < len(tasks):
                tasks.pop(index)

        else:
            if new_task:
                tasks.append(new_task)

    toplam = len(tasks)

    return render_template(
        "index.html",
        tasks=filtered_tasks,
        toplam_gorev=toplam,
        search=search
    )

if __name__ == "__main__":
    app.run(debug=True)