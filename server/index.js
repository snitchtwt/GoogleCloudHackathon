import express from "express";
import cors from "cors";
import bodyParser from "body-parser";

import connection from "./databse/db.js";
import routes from "./routes/route.js";

const app = express();

app.use(cors());

app.use(bodyParser.json({ extended: true }));
app.use(bodyParser.urlencoded({ extended: true }));

app.use("/", routes);

const PORT = 8000;

app.listen(PORT, () =>
  console.log(`server started sucessfully on port ${PORT}`)
);
connection();