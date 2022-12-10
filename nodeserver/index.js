const express = require('express'); 
const cors = require('cors');
const multer = require("multer");
const http = require("http");
const path = require("path");
const fs = require("fs")

const app = express()
app.use(cors())
const port = 3001
const upload = multer({
  dest: path.join(__dirname,"./uploaded/files")
  // you might also want to set some limits: https://github.com/expressjs/multer#limits
});
app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.post("/summarize",
  upload.single("video"),
  (req,res)=>{
    const tempPath = req.file.path;
    console.log(tempPath)
    const targetPath = path.join(__dirname, "./uploaded/files/image"+Date.now()+".mp4");

    if (path.extname(req.file.originalname).toLowerCase() === ".mp4") {
      fs.rename(tempPath, targetPath, err => {
        console.log("Renamed")
        if (err) return console.log(err);
        res
          .status(200)
          .contentType("text/plain")
          .end("File uploaded!");
      });
    } else {
      fs.unlink(tempPath, err => {
        if (err) return console.log(err);

        res
          .status(403)
          .contentType("text/plain")
          .end("Only .mp4 files are allowed!");
      });
    }
  })


app.post("/caption",(req,res)=>{
  res.status(404).send("YET TO IMPLEMENT")
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})