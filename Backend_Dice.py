from flask import Flask, render_template, request, url_for
from flask_ngrok import run_with_ngrok
from flask import Flask
from pyngrok import ngrok

app = Flask(__name__)
run_with_ngrok(app)

#Main page
@app.route("/")
def home():
    # read the HTML file into a string variable
    with open("/content/drive/MyDrive/Securin.html", "r") as f:
        html_content = f.read()

    # return the HTML content as a response
    return html_content

@app.route('/tot')
def total_combinations():
    n_dice = int(input("Enter the number of dice: "))  # Assuming user input for number of dice
    total_comb = total_Comb(n_dice)

    # read the HTML file into a string variable
    with open("/content/drive/MyDrive/total_combinations.html", "r") as f:
        html_content = f.read()
        html1 = html1.replace('{{total_comb}}', total_comb)
    # return the HTML content as a response
    return html_content

@app.route('/dist')
def pos_comb():
    result = pos_Comb()
    output_text = generate_output(result)
    # read the HTML file into a string variable
    with open("/content/drive/MyDrive/pos_comb.html", "r") as f:
        html_content = f.read()
        html_content.replace('{{output}}',output_text)
    # return the HTML content as a response
    return html_content

@app.route('/prob')
def prob_sum():
    result = prob_Sum()
    output_text = generate_output_prob(result)
    # read the HTML file into a string variable
    with open("/content/drive/MyDrive/prob_sum.html", "r") as f:
        html_content = f.read()
        html_content.replace('{{out_prob}}',output_text)
    # return the HTML content as a response
    return html_content

def total_Comb(N_dice):
    N_faces = 6
    Total_Comb = pow(N_faces, N_dice)
    return Total_Comb

def pos_Comb():
    dist = {}
    for dA in range(1, 7):
        for dB in range(1, 7):
            total_Comb = dA + dB
            if total_Comb not in dist:
                dist[total_Comb] = []
            dist[total_Comb].append((dA, dB))
    return dist

def generate_output(result):
    output = ""
    for key, value in result.items():
        output += f"Sum {key}: {value}\n"
    return output

def total_Comb(N_dice):
    N_faces = 6
    Total_Comb = pow(N_faces, N_dice)
    return Total_Comb

def prob_Sum():
    dist = {}
    for die_A in range(1, 7):
        for die_B in range(1, 7):
            total_Sum = die_A + die_B
            if total_Sum not in dist:
                dist[total_Sum] = 1
            else:
                dist[total_Sum] += 1
    return dist

def generate_output_prob(result):
    output = ""
    for key, value in result.items():
        output += f"Sum {key}: Probability {value/36:.2f}\n"  # Assuming 36 possible outcomes
    return output

if __name__ == "__main__":
    app.run()
