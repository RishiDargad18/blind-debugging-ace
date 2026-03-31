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
            return jsonify({"output": "Invalid request"}), 400

        user_id = data.get("user")
        cmd = data.get("cmd", "").strip()

        if not user_id or not cmd:
            return jsonify({"output": "Invalid input"}), 400

        user = get_user(user_id)
        parts = cmd.split()

        # =====================
        # HELP
        # =====================
        if cmd == "help":
            p = user["problem"]
            return jsonify({"output": problem_map[p].info})

        # =====================
        # CLEAR
        # =====================
        if cmd == "clear":
            return jsonify({"output": "__CLEAR__"})

        # =====================
        # SWITCH PROBLEM
        # =====================
        if parts[0] == "use":
            if len(parts) < 2:
                return jsonify({"output": "Usage: use <problem_number>"})

            try:
                p = int(parts[1])
            except ValueError:
                return jsonify({"output": "Invalid problem number"})

            if p not in problem_map:
                return jsonify({"output": "Problem does not exist"})

            user["problem"] = p
            user["data"] = {}  # reset state

            return jsonify({
                "output": f"{problem_map[p].info}"
            })

        # =====================
        # RUN PROBLEM
        # =====================
        p = user["problem"]

        if p not in problem_map:
            return jsonify({"output": "Invalid problem state"})

        try:
            result = problem_map[p].run(user["data"], cmd)
            return jsonify({"output": str(result)})

        except Exception as e:
            print(f"[ERROR] Problem {p} failed:", e)
            return jsonify({"output": "Invalid input. Type 'help'."})

    except Exception as e:
        # catch ANY unexpected crash
        print("[FATAL ERROR]:", e)
        return jsonify({"output": "Server error. Please try again."})


import os
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)