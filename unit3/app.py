from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Hardest Decision"
    
    text = """You walk into your favorite boba shop with an intense craving. You take a look at the 
    menu and was struck with the difficult decision of ordering a milk tea or a fruit tea.
    Which do you pick?"""

    choices = [
        ('milk_tea',"Milk Tea"),
        ('fruit_tea',"Fruit Tea")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/milktea")
def milk_tea():
    title = "You selected milk tea..."
    
    text = """The cashier asks what sweetness you desire. Another difficult decision you must make.
    Do I want to be healthy today? Do I just want to splurge. Hmmmm, you haven't thought this hard 
    since the start of the pandemic."""

    choices = [
        ('half_Sugar',"Half Sugar"),
        ('full_sugar',"Full Sugar")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/fruittea")
def fruit_tea():
    title = "You selected fruit tea..."
    
    text = """Fruit teas are always too sweet so you decide to order it with half sugar.
    The cashier hands you the drink and you feel good that you chose a healthy option. You take the drink and leave."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/fullsugar")
def full_sugar():
    title = "You selected full sugar!"
    
    text = """The amount of guilt you feel is overwhelming. You start to question if you will survive.
    You can feel your own blood sugar levels rise. Just this once you tell yourself. Next time you must exercise control.
    You take your drink and go home feeling bad."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/halfsugar")
def half_Sugar():
    title = "You selected half sugar!"

    text = """ Got job on being healthy. The cashier smiles at you and hands you your drink.
    You feel content and go home.
    """
    
    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)