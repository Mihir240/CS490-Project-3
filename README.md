# CS490-Project-3
## Expense Tracker

### Description

Expense tracker is a basic web app that allows users to keep track of their incomes and expenses in one place. 
This app will allow users to login, and create a personal expense profile. Users will be able to add new incomes or expenses, and also access the ones added on the website.

#### Team Members:
 * Abishek Vasudevan
 * Aman Hirpara
 * Mihir Rana
 * Raj Patel
 
### Technologies we used

In this project, we used the Flask framework, as our web server and the React library for client side functionality. In addtion,
we have used Google Authentication for ease of login and React-Bootstrap to streamline our html and css visuals.

#### References
---
- [Flask](https://flask.palletsprojects.com/en/1.1.x/#)
- [React Docs](https://reactjs.org/docs/getting-started.html)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/en/14/)
- [Google Developer Account](https://console.cloud.google.com/apis/dashboard) (For Google Authentication)
- [React-Bootstrap](https://react-bootstrap.github.io/getting-started/introduction)
- [Enzyme-Adapter-React-17](https://github.com/wojtekmaj/enzyme-adapter-react-17)
---

## Flask and create-react-app

### Requirements

1. `pip install flask`
2. `npm install`
3. `pip install -r requirements.txt`

### Setup

1. Run `echo "DANGEROUSLY_DISABLE_HOST_CHECK=true" > .env.development.local` in the project directory
2. Add following to .env file:
   + REACT_APP_GOOGLE_CLIENT_ID = "Your_OAuth_client_ID"
   + DATABASE_URL = "Your_database_url"

## Setting up Google Authentication

<details>
  <summary><b>How to get an OAuth 2.0 client ID</b></summary>
  
  1. Go to the Google [Developers Console](https://console.cloud.google.com/apis/dashboard).
  2. Navigate to the tab "Credentials".
  3. Create a new project.
  4. Navigate to the tab “OAuth consent screen”.
  5. Enter the Application name, Authorized domains, and click the button **Save**.
  6. Click on **Create Credentials** and from the dropdown list select *OAuth client ID*.
  7. From the drop-down menu, select the Web application and click on **Creat**.
  8. Copy your Client ID.
</details>

## React-Bootstrap

#### About


## Enzyme-Adapter-React-17

#### About


## Setting up Our Database (PostgresSql)

#### About
PostgresSql is an open-source relational database management system which is also SQL compliance. We will be using this as our database to store the the expenses of the
respective users.

#### Installation
1) `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql  docs`

#### Setup
1) Once you have installed PostgreSql using the command above we initialize the database.
2) Initialize: `sudo service postgresql initdb`
3) To start the service: `sudo service postgresql start`
4) Now we can make a superuser(if an error says 'could not change directory' that means it worked): `sudo -u postgres createuser --superuser $USER`
5) Now lets make a database: `sudo -u postgres createdb $USER`
6) To ensure that your user shows up follow the commands:
   - `psql`
   - `\du`
   - `\l`
7) Making a new user: 
   - `create user some_username_here superuser password 'some_unique_new_password_here'`
   - `\q` (to quit sql)
8) Now to save your passwords to a `sql.env` file with the following format `SQL_USER=""` and `SQL_PASSWORD=""`.

### SQLAlchemy
---

#### About
To now query and access our database we will use SQLAlchemy.

#### Installation
1) `pip install psycopg2-binary`
2) `pip install Flask-SQLAlchemy==2.1`

#### Creating new database for Heroku and connect our code
1) Login to heroku: `heroku login -i`
2) Create new app: `heroku create`
3) Add a database on our heroku app:`heroku addons:create heroku-postgresql:hobby-dev`
4) To see the config vars that are set by heroku for us: `heroku config`
5) Set the database variable as an environment variable: `export DATABASE_URL='paste config value here'`

## Deploying our App to Heroku 

#### About
Heroku is a cloud platform company which will essentially allow us to host our code on their servers and we can run our game on there.

#### Installation
1. `npm install -g heroku`

#### Setup 
1) First we will need to create a free account on [Heroku](https://www.heroku.com/).
2) Next, we will create a  `requirements.txt` file which will list all the libraries and packages our app uses. This information is needed because Heroku's servers will 
  download said packages and libraries so it can run the app on their servers.
  In your terminal, type the following:
  1. `touch requirements.txt`
  2. `pip freeze > requirements.txt`
3) Once that is done, we will need a `Procfile`, which is a file that will tell Heroku what command to use to run our app.
  1. In your terminal, type: `touch Procfile`
  2. Next, open up the `Procfile` and type your commands needed to run your app. In my case I would write: `web: python main.py`. 
4) Now for the actual deploying part, open your terminal and follow along:
  1. Login to Heroku via terminal: `heroku login -i`
  2. Next go to your project folder and create the heroku app: `heroku create --buildpack heroku/python`
  3. Now we will add the nodejs buildpack: `heroku buildpacks:add --index 1 heroku/nodejs`
  4. Now we will push our code to heroku: `git push heroku main`

## Run Application

1. Run command in terminal (in your project directory): `python app.py`
2. Run command in another terminal, `cd` into the project directory, and run `npm run start`
3. Preview web page in browser '/'
