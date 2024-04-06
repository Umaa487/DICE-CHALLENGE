from flask import Flask
from pyngrok import ngrok
ngrok.set_auth_token('2eQr6J6ar61hO8QztweySdcRILS_7mHhmmFD75aZyq2DXEpgD')
public_url=ngrok.connect(5000).public_url
port_no = 5000
app = Flask(__name__)
ngrok.set_auth_token("2eQr6J6ar61hO8QztweySdcRILS_7mHhmmFD75aZyq2DXEpgD")
public_url =  ngrok.connect(port_no).public_url
@app.route("/",methods=['GET', 'POST'])
def login():
    # read the HTML file into a string variable
    with open("/content/drive/MyDrive/Dice_Login.html", "r") as f:
        html_content = f.read()

    # return the HTML content as a response
    return html_content
#Main page
@app.route("/home")
def home():
    # read the HTML file into a string variable
    with open("/content/drive/MyDrive/Securin.html", "r") as f:
        html_content = f.read()

    # return the HTML content as a response
    return html_content
@app.route('/tot')
def total_combinations():
     # Assuming user input for number of dice
    total_comb = str(total_Comb(2))

    # read the HTML file into a string variable
    with open("/content/drive/MyDrive/total_combinations.html", "r") as f:
        html_content = f.read()
        html_content = html_content.replace('{{total_comb}}', total_comb)
    # return the HTML content as a response
    return html_content

@app.route('/dist')
def pos_comb():
    result = pos_Comb()
    output_text = generate_output(result)
    # read the HTML file into a string variable
    with open("/content/drive/MyDrive/pos_comb.html", "r") as f:
        html_content = f.read()
        html_content=html_content.replace('{{output_text}}',output_text)
    # return the HTML content as a response
    return html_content

@app.route('/prob')
def prob_sum():
    output_text = generate_output_prob()
    with open("/content/drive/MyDrive/prob_sum.html", "r") as f:
        html_content = f.read()
        html_content=html_content.replace('{{output_text}}',output_text)
    # return the HTML content as a response
    return html_content

@app.route('/undoom')
def undoom_sum():
    output_text=unDoom()
    with open("/content/drive/MyDrive/UnDoom_Dice.html", "r") as f:
        html_content = f.read()
        html_content=html_content.replace('{{output_text}}',output_text)
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
    # Generate the output dynamically based on the result
    output_text = ""
    for sum_value, possibilities in result.items():
        output_text += f"<li>Sum {sum_value}: {possibilities}</li>"
    return output_text

dist={}
def prob_Sum():
    for die_A in range(1, 7):
        for die_B in range(1, 7):
            total_Sum = die_A + die_B
            if total_Sum not in dist:
                dist[total_Sum] = 1
            else:
                dist[total_Sum] += 1

def generate_output_prob():
    prob_Sum()
    output = ""
    Total_Comb = total_Comb(2)
    for Sum in dist:
        Tot = (dist[Sum]) / Total_Comb

        output += f"<li>Sum {str(Sum)}: {Tot:.2f}</li>"  # Assuming 36 possible outcomes
    return output

def unDoom():
    list1 = list(range(1, 5))
    list2 = list(range(1, 12))
    die_comb1 = []
    die_comb2 = []
    old_List = [0.0, 0.0, 0.027777777777777776, 0.05555555555555555, 0.08333333333333333, 0.1111111111111111, 0.1388888888888889, 0.16666666666666666, 0.1388888888888889, 0.1111111111111111, 0.08333333333333333, 0.05555555555555555, 0.027777777777777776]

    def total_comb(dice_A,dice_B):
         return len(dice_A)*len(dice_B)
         
    def comb_A(N,temp):
        if len(temp)==6:
            die_comb1.append(temp)
            return
        if N<0:
            return
        comb_A(N-1,temp+[list1[N]])
        comb_A(N-1,temp)

    def comb_B(N,temp):
        if len(temp)==6:
            die_comb2.append(temp)
            return
        if N<0:
            return
        comb_B(N-1,temp+[list2[N]])
        comb_B(N-1,temp)

    def pos_Dist(dice_A,dice_B):
        ans = [0 for i in range(max(dice_A)+max(dice_B)+1)]
        for i in dice_A:
            for j in dice_B:
                ans[i+j] += 1
        return ans
        
    def prob_Dice(dice_A,dice_B):
        if max(dice_A) + max(dice_B) == 12:
            dist = pos_Dist(dice_A,dice_B)
            ln = total_comb(dice_A,dice_B)
            for i in range(max(dice_A)+max(dice_B)+1):
                if dist[i]:
                    if old_List[i] != dist[i]/ln:
                        return False
            return True

        return False

    comb_A(len(list1) - 1, [])
    comb_B(len(list2) - 1, [])
    
    New_Dices = []

    for dice_A in die_comb1:
        for dice_B in die_comb2:
            if prob_Dice(dice_A, dice_B):
                New_Dices.append((dice_A, dice_B))
                
    return New_Dices

unDoom_Dice=''
range1 = range(1,5)
range2 = range(11,0,-1)
def total_Comb(N_dice):
    N_faces = 6
    Total_Comb = pow(N_faces, N_dice)
    return Total_Comb
def pos_Comb(a,b):
    dist = []
    for dA in a:
        for dB in b:
            total_Comb = dA + dB
            if total_Comb not in dist:
                dist.append(total_Comb)
    return dist
def check(l):
    l=sorted(l)
    a=2
    for i in range(11):
        if l[i]!=a:
            return False
        a+=1
    return True
def prob_Sum():
    dist = {}
    l=[]
    for die_A in range(1, 7):
        for die_B in range(1, 7):
            total_Sum = die_A + die_B
            if total_Sum not in dist:
                dist[total_Sum] = 1
            else:
                dist[total_Sum] += 1
    Total_Comb = total_Comb(2)
    for Sum in dist:
        Tot = (dist[Sum]) / Total_Comb
        Tot=f"{Tot:.2f}"
        l.append(Tot)
    return l

def newSum(a,b):
    dist = {}
    l=[]
    for die_A in a:
        for die_B in b:
            total_Sum = die_A + die_B
            if total_Sum not in dist:
                dist[total_Sum] = 1
            else:
                dist[total_Sum] += 1
    Total_Comb = total_Comb(2)
    d=dict(sorted(dist.items()))
    for Sum in d:
        Tot = (d[Sum]) / 36
        Tot=f"{Tot:.2f}"
        l.append(Tot)
    return l

def unDoom():
  c = itertools.product(range1, repeat=6)
  b=itertools.combinations(range2,6)
  c=list(c)[::-1]
  b=list(b)[::-1]
  for i in c:
    for j in b:
        f=0
        i=list(i)
        j=list(j)
        if max(i)+max(j)==12:
            l=pos_Comb(i,j)
            if check(l):
                new=newSum(i,j)
                old=prob_Sum()
                for k in range(6):
                    if new[k]!=old[k]:
                        break
                    else:
                        f+=1
                if f==6:
                    unDoom_Dice+=f"{[i,j]}"
                    return unDoom_Dice
                    
print(f"To acces the Gloable link please click {public_url}")

app.run(port=port_no)
