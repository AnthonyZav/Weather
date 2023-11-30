#!/usr/bin/env python 3

import json
import requests


class Weather(object):
    def __init__(self, api_url, user_agent):
        self.api_url = api_url
        self.headers = {
            'User-Agent': user_agent,
            'content-type': 'application/json',
            'Accept': 'application/json'
        }
 
    def current_temp(self, location):
        latest = self._latest_observations(location)
        t = latest['temperature']['value']
        try:
            f = float((9/5 * t) + 32)
        except TypeError:
            t = None
            f = None
        ret = {
            'fahrenheit': f,
            'celsius': t
        }
        return ret
    
    def current_wind(self, location):
        latest = self._latest_observations(location)
        try:
            speed = latest['windSpeed']['value']
            speed_mph = speed * 0.621371
        except TypeError:
            speed = None
            speed_mph = None
        try:
            gust = latest['windGust']['value']
            gust_mph = gust * 0.621371
        except TypeError:
            gust = None
            gust_mph = None
        
        ret = {
            'direction_degrees': dir,
            'speed_kmh': speed,
            'speed_mph': speed_mph,
            'gust_kmh': gust,
            'gust_mph': gust_mph,
        }
        return ret
    
    def current_precipitation(self, location):
        latest = self._latest_observations(location)
        dir = latest['percipitation']['value']

    def current_clouds(self, location):
        latest = self._latest_observations(location)
        dir = latest['cloud population']['value']
        
    def _get_station(self, location=None):
        if not location:
            raise RuntimeError('No location specified for call')
        url = f"{self.api_url}/points/{location}"
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            raise RuntimeError(f"API request failed: {res.reason} ({res.status_code})")
        data = res.json()
        url = data['properties']['observationStations']

        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            raise RuntimeError(f"API request failed for observation stations: {res.reason} ({res.code})")
        data = res.json()
        stations = data['features']
        station_id = stations[0]['properties']['stationIdentifier']
        return station_id
    
    def _latest_observations(self, location=None):
        if not location:
            raise RuntimeError('No location specified for call')
        station = self._get_station(location)
        
        url = f"{self.api_url}/stations/{station}/observations/latest"
        print(url)
        res = requests.get(url, headers=self.headers)
        if res.status_code != 200:
            raise RuntimeError(f"Unable to get latest observation: {res.reason} ({res.status_code})")
        print(res.status_code)
        print(res.text)
        data = res.json()
        return data['properties']




if __name__ == '__main__':
    api_url = 'https://api.weather.gov'
    location = '40.5441974,-79.9455194'
    wx = Weather(api_url, 'CS0501-SJHS Weather Application V1.0')
    temp = wx.current_temp(location)
    print(temp)


    wind = wx.current_wind(location)
    print(wind)
