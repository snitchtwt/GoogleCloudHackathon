import mongoose from "mongoose";
import dotenv from "dotenv";

dotenv.config();

const USERNAME=process.env.DB_USERNAME;
const PASSWORD=process.env.DB_PASSWORD;

export const connection = () => {
    
    mongoose.set('strictQuery', false);

    const url= `mongodb://${USERNAME}:${PASSWORD}@ac-xd5qgv9-shard-00-00.v0uoffe.mongodb.net:27017,ac-xd5qgv9-shard-00-01.v0uoffe.mongodb.net:27017,ac-xd5qgv9-shard-00-02.v0uoffe.mongodb.net:27017/?ssl=true&replicaSet=atlas-w5gv5q-shard-0&authSource=admin&retryWrites=true&w=majority`;
    mongoose.connect(url ,{ useNewUrlParser: true });
    mongoose.connection.on('connected',()=>{
        console.log('Database connected Sucessfully');
    })

    mongoose.connection.on('disconnected',()=>{
        console.log('Database disconnected');
    })

    mongoose.connection.on('error',()=>{
        console.log('Error while connecting to the database',error.message);
    })
}
export default connection;