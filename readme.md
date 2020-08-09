## Reddit Weather Sidebar

Displays the weather forecast in the sidebar for a chosen city.

### Instructions

-   Install requirements `pip install -r requirements.txt`
-   Create Reddit (script) app at <https://www.reddit.com/prefs/apps/> and get keys
-   Get an API key from <https://openweathermap.org>
-   Edit conf.ini with your details
-   Edit old Reddit stylesheet at <https://old.reddit.com/r/SUBREDDIT/about/stylesheet/> and add this CSS

        .side table {
          width: 100%;
          font-family: IBMPlexSans, Arial, sans-serif;
        }

        .side thead {
          display: none;
        }

        .side h2, .side h3 {
          padding-top: 1rem;
          text-align: center;
        }

-   Add a new custom widget on the new Reddit style at <https://new.reddit.com/r/SUBREDDIT/?styling=true>, name it `Weather` (or whatever you declared it to be in conf.ini) and add this CSS

        .md table {
          width: 100%;
          font-family: IBMPlexSans, Arial, sans-serif;
        }

        .md thead {
          display: none;
        }

        .md h2, .md h3 {
          padding-top: 1rem;
          text-align: center;
          font-family: IBMPlexSans, Arial, sans-serif;
        }

-   Run it `python run.py`

### Settings Info

`reddit_user` - Reddit username  
`reddit_pass` - Reddit password  
`reddit_client_id` - Reddit Client ID  
`reddit_client_secret` - Reddit Client Secret  
`reddit_target_subreddit` - Subreddit to update sidebar  
`reddit_widget_name` - Widget name (new Reddit style)  

`weather_api_key` - API key from openweathermap  
`weather_units` metric  
`weather_city` London,UK  

### Notes

-   The account that you use for the bot has to be a mod of the target subreddit and have the correct permissions to edit things.

### Tip

BTC - 1AYSiE7mhR9XshtS4mU2rRoAGxN8wSo4tK
