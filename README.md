# You're Fired
"What a great app."
	-Ghandi (probably)

#### Frontend
* nope

#### Backend
* Flask - http://flask.pocoo.org/docs/0.11/
* Jinja2  - http://jinja.pocoo.org/docs/dev/
* SQLAlchemy - http://www.sqlalchemy.org/

## Getting Started
    
Set up your dev environment by running these commands in a terminal:

    brew install nodejs

    cd backend/ && npm install

    brew install mongodb

    sudo mkdir /data/ && sudo mkdir /data/db

    sudo chmod a+w /data/db

To start the database server, in a new terminal window run

    mongod&

To populate the database, in a new terminal window run 
   
    ./node_modules/babel-cli/bin/babel-node.js populate.js 

Start the webserver

    npm start

Open your browser to `http://localhost:3000/v1/users.json` to see the user data.
