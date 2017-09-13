# You're Fired
"What a great app."
	-Ghandi (probably)

#### Frontend
* React Native - https://facebook.github.io/react-native/docs/getting-started.html

#### Backend
* Express - http://expressjs.com/en/api.html
* Node.js - https://nodejs.org/dist/latest-v8.x/docs/api/
* MongoDB - https://docs.mongodb.com/manual/

## Getting Started
Install Node.js v8.4.0 and npm v4.6.1

#### Frontend
To start frontend dev run this command
    
    cd frontend/ && npm install
   
    npm start

Then download Expo for your phone and scan the QR code to get started.

#### Backend    
Set up your dev environment by running these commands in a terminal:

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

