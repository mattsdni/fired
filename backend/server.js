import express from 'express';
import morgan from 'morgan';
import mongoose from 'mongoose';
import bodyParser from 'body-parser'
import User from './models/user';
var cors = require('cors');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/users');

// Initialize http server
const app = express();

// Logger that outputs all requests into the console
app.use(morgan('combined'));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors())

app.get('/users', function(req, res) {
  // Find all users and return json response
  User.find().lean().exec((err, users) => res.json(
    { users: users.map(user => ({...user, }))}
  ));
});

app.get('/user', function(req, res) {
  // return user data
  User.find({'username': req.body.username}).exec((err, user) => res.json(user));
});

app.post('/user', function(req, res) {
  // create user
  var data = {
    username: req.body.username,
    firedCount: 0,
  }
  var user = new User(data);
  user.save();
  res.json(user);
});

app.delete('/user', function(req, res) {
  // delete user
  User.find({ username:req.body.username }).remove().exec();
  res.json("OK");
});

app.post('/fire', function(req, res) {
  // Fire the user once
  User.findOneAndUpdate({'username': req.body.username}, {$inc : {'firedCount' : 1}}).exec((err, user) => res.json(user));
});

const server = app.listen(3000, () => {
  const { address, port } = server.address();
  console.log(`Listening at http://${address}:${port}`);
});