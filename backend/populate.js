import mongoose from 'mongoose';
import User from './models/user';

const users = [
  {
    username: 'matt',
    firedCount: 0,
  },
  {
    username: 'melody',
    firedCount: 1,
  },
];

// Connect to MongoDB
mongoose.connect('mongodb://localhost/users');

// Go through each movie
users.map(data => {
  // Initialize a model with movie data
  const user = new User(data);
  // and save it into the database
  user.save();
});