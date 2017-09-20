import express from 'express';
import morgan from 'morgan';
import mongoose from 'mongoose';
import bodyParser from 'body-parser'
import User from './models/user';

// Connect to MongoDB
mongoose.connect('mongodb://localhost/users');

// Initialize http server
const app = express();

// Logger that outputs all requests into the console
app.use(morgan('combined'));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/users', function(req, res) {
  // Find all users and return json response
  User.find().lean().exec((err, users) => res.json(
    { users: users.map(user => ({...user, }))}
  ));
});

app.post('/fireUser', function(req, res) {
  // Fire the user once
  User.findOneAndUpdate({'username': req.body.username}, {$inc : {'firedCount' : 1}}).exec((err, user) => res.json(user));
});

const server = app.listen(3000, () => {
  const { address, port } = server.address();
  console.log(`Listening at http://${address}:${port}`);
});