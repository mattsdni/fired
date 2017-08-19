import mongoose, { Schema } from 'mongoose';

// Define user schema
var userSchema = new Schema({
  username: {
    type: String,
    unique: true,
  },
  firedCount: Number,
});

// Export Mongoose model
export default mongoose.model('user', userSchema);