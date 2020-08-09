import praw
import configparser
from requests import get
import time

config = configparser.ConfigParser()
config.read('conf.ini')
reddit_user = config['REDDIT']['reddit_user']
reddit_pass = config['REDDIT']['reddit_pass']
reddit_client_id = config['REDDIT']['reddit_client_id']
reddit_client_secret = config['REDDIT']['reddit_client_secret']
reddit_target_subreddit = config['REDDIT']['reddit_target_subreddit']
reddit_widget_name = config['REDDIT']['reddit_widget_name']
weather_api_key = config['WEATHER']['weather_api_key']
weather_units = config['WEATHER']['weather_units']
weather_city = config['WEATHER']['weather_city']
weather_city_url = weather_city.replace(' ', '%20')
weather_city_pretty = weather_city.replace(',', ', ')

if weather_units == 'metric':
    temp_sign = '°C'
else:
    temp_sign = '°F'

reddit = praw.Reddit(
    username=reddit_user,
    password=reddit_pass,
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent='Reddit Sibebar Weather (by u/impshum)'
)


def main():
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={weather_city_url}&units={weather_units}&appid={weather_api_key}'
    data = get(url).json()

    sidebar_contents = f'## {weather_city_pretty}\n\n'
    current_day = False

    for day in data['list']:
        local = time.localtime(day['dt'])
        weather_day = time.strftime('%d', local)
        weather_time = time.strftime('%H:%M', local)
        dt = time.strftime('%a %d %b %Y', local)
        min_temp = day['main']['temp_min']
        max_temp = day['main']['temp_max']
        temp = int(min_temp) + int(max_temp) / 2
        description = day['weather'][0]['description']
        if weather_day != current_day:
            current_day = weather_day
            sidebar_contents += f'\n\n###{dt}\n\nTime|Temp|Desc  \n:-:|:-:|:-:'
        sidebar_contents += f'  \n{weather_time} | {temp}{temp_sign} | {description}'

    reddit.subreddit(
        reddit_target_subreddit).wiki['config/sidebar'].edit(sidebar_contents)

    for widget in reddit.subreddit(reddit_target_subreddit).widgets.sidebar:
        if widget.shortName.lower() == reddit_widget_name:
            widget.mod.update(text=sidebar_contents)


if __name__ == '__main__':
    main()
