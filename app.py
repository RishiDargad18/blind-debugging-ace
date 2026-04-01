from flask import Flask, request, jsonify, render_template
from core.state import get_user
from core.dispatcher import problem_map

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/command', methods=['POST'])
def command():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"output": "Invalid request"})

        user_id = data.get("user")
        cmd = data.get("cmd", "")

        if not user_id or not cmd:
            return jsonify({"output": "Invalid input"})

        # normalize input
        cmd = cmd.strip().lower()
        user = get_user(user_id)

        print("CMD:", repr(cmd))  # debug log

        # =====================
        # HELP
        # =====================
        if cmd == "help":
            if user["problem"] is None:
                return jsonify({"output": "No problem selected. Type: use <1-4>"})
            return jsonify({"output": problem_map[user["problem"]].info})

        # =====================
        # CLEAR
        # =====================
        if cmd == "clear":
            return jsonify({"output": "__CLEAR__"})

        # =====================
        # USE COMMAND
        # =====================
        if cmd.startswith("use"):
            parts = cmd.split()

            if len(parts) != 2:
                return jsonify({"output": "Usage: use <problem_number>"})

            try:
                p = int(parts[1])
            except:
                return jsonify({"output": "Invalid problem number"})

            if p not in problem_map:
                return jsonify({"output": "Problem does not exist"})

            user["problem"] = p
            user["data"] = {}

            return jsonify({
                "output": f"Problem {p} : {problem_map[p].info}"
            })

        # =====================
        # FORCE PROBLEM SELECT
        # =====================
        if user["problem"] is None:
            return jsonify({
                "output": "No problem selected. Type: use <1-4>"
            })

        # =====================
        # RUN PROBLEM
        # =====================
        try:
            p = user["problem"]
            result = problem_map[p].run(user["data"], cmd)

            return jsonify({"output": str(result)})

        except Exception as e:
            print(f"[ERROR] Problem {p} failed:", e)
            return jsonify({"output": "Invalid input. Type 'help'."})

    except Exception as e:
        print("[FATAL ERROR]:", e)
        return jsonify({"output": "Server error. Try again."})


# =====================
# RUN (LOCAL ONLY)
# =====================
if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=5000)
