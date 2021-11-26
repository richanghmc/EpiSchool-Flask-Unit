from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Hardest Decision"
    
    text = """You walk into your favorite boba shop with an intense craving. You take a look at the 
    menu and was struck with the difficult decision of ordering a milk tea or a fruit tea.
    Which do you pick?"""

    image = "https://www.joshuakennon.com/wp-content/uploads/2019/06/Making-Our-Way-through-the-Line-at-Omomo-Tea-in-Irvine-California.jpeg"

    choices = [
        ('milk_tea',"Milk Tea"),
        ('fruit_tea',"Fruit Tea")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices, image=image)



@app.route("/milktea")
def milk_tea():
    title = "You selected milk tea..."
    
    text = """The cashier asks what sweetness you desire. Another difficult decision you must make.
    Do I want to be healthy today? Do I just want to splurge. Hmmmm, you haven't thought this hard 
    since the start of the pandemic."""

    image = "https://www.honestfoodtalks.com/wp-content/uploads/2021/08/Okinawa-milk-tea-recipe-using-kokuto.jpeg"

    choices = [
        ('half_Sugar',"Half Sugar"),
        ('full_sugar',"Full Sugar")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices, image=image)

@app.route("/fruittea")
def fruit_tea():
    title = "You selected fruit tea..."
    
    text = """Fruit teas are always too sweet so you decide to order it with half sugar.
    The cashier hands you the drink and you feel good that you chose a healthy option. You take the drink and leave."""

    choices = []

    image = "https://www.fodmapeveryday.com/wp-content/uploads/2020/07/Low-FODMAP-Iced-Green-tea-with-Passionfruit-in-a-clear-footed-glass-on-gray-surface-outdoors.jpg"

    return render_template('adventure.html', title=title, text=text, choices=choices, image=image)



@app.route("/fullsugar")
def full_sugar():
    title = "You selected full sugar!"
    
    text = """The amount of guilt you feel is overwhelming. You start to question if you will survive.
    You can feel your own blood sugar levels rise. Just this once you tell yourself. Next time you must exercise control.
    You take your drink and go home feeling bad."""

    image = "https://cdn.diabetesselfmanagement.com/2021/05/dsm-sugar-facts-shutterstock-1564269901.jpg"

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices, image=image)

@app.route("/halfsugar")
def half_Sugar():
    title = "You selected half sugar!"

    text = """ Got job on being healthy. The cashier smiles at you and hands you your drink.
    You feel content and go home.
    """

    image = "https://michelleswordpressyay.files.wordpress.com/2012/06/img_2365-1.jpg"
    
    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices, image = image)