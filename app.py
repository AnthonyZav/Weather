from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from weather import Weather

app = Flask('weather')
bootstrap = Bootstrap5(app)

api_url = 'https://api.weather.gov'
location = '40.5441974,-79.9455194'
    
@app.route('/')
def index():
    wx = Weather(api_url, 'CS0501-SJHS Weather Application V1.0')
    ret = '<p>Welcome to Our Weather App</p>'
    temp = wx.current_temp(location)
    wind = wx.current_wind(location)

    #ret += '\n'
    #ret += f"<p>Your current temparture is : {temp['fahrenheit']}F"
    #ret += '\n'
    #ret += f"</b>Wind is blowing at {wind['speed_mph']}mph from {wind['direction_deg']} degrees"
    #ret += '</p>'

    #return ret

    return render_template('main.html', temp=temp, wind=wind)

