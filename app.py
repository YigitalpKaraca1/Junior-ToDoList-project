from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", tasks=tasks, toplam_gorev=len(tasks))


@app.route("/add", methods=["POST"])
def add_task():
    new_task = request.form.get("task")

    if new_task:
        tasks.append(new_task)

        return jsonify({
            "success": True,
            "task": new_task,
            "total": len(tasks)
        })

    return jsonify({"success": False})


@app.route("/delete", methods=["POST"])
def delete_task():
    index = request.form.get("index")

    if index is not None:
        index = int(index)

        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)

            return jsonify({
                "success": True,
                "deleted": deleted,
                "total": len(tasks)
            })

    return jsonify({"success": False})


if __name__ == "__main__":
    app.run(debug=True)