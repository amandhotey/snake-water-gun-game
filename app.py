from flask import Flask , render_template ,request,jsonify,redirect,url_for,send_from_directory
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    yourchoice = data['choice']
    
    computer = random.choice(["s", "w", "g"])
    reverseDict = {"s": "Snake", "w": "Water", "g": "Gun"}

    if yourchoice not in reverseDict:
        return jsonify({"result": "Invalid choice"})

    result = f"You chose {reverseDict[yourchoice]}<br>Computer chose {reverseDict[computer]}<br>"

    if yourchoice == computer:
        result += "It's a draw"
    elif (yourchoice == "s" and computer == "w") or \
         (yourchoice == "w" and computer == "g") or \
         (yourchoice == "g" and computer == "s"):
        result += "You win"
    else:
        result += "Computer wins"

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)