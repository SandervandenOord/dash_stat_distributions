# Interactive statistical distributions with Dash Plotly (deployed on Heroku)

#### Check it out at: https://binomial.herokuapp.com/

#### Deploying this app on Heroku is easy:
1. Create a Heroku account
2. Create an app on Heroku
3. Connect app to github repo that contains app.
4. put following files on github:
- your app
- requirements.txt (it should also include gunicorn, this is for Heroku) 
- Procfile (this is a special file for Heroku) and only contains line: web: gunicorn binomial3:server

I basically did the installation following parts of this documentation:
https://dash.plot.ly/deployment
