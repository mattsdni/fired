import User from '../models/user';
import moment from 'moment';

export const index = (req, res, next) => {
  // Find all movies and return json response
  User.find().lean().exec((err, users) => res.json(
    // Iterate through each movie
    { users: users.map(user => ({
      ...user,
    }))}
  ));
};