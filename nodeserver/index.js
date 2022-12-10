const express = require('express'); 
const cors = require('cors');
const multer = require("multer");
const http = require("http");
const path = require("path");
const fs = require("fs")
const {spawn} = require("child_process");

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
        const summarizePython=spawn("python",["nodeserver/pythonscripts/DSNet/infer.py",tempPath]);

        res.status(200)
          .contentType("text/plain")
          .end("File uploaded and processed!");
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
  console.log("reqss");
  console.log(req.query.path);
  // console.log(req);

  const childPython = spawn("python",["nodeserver/pythonscripts/imagecaption/image_captioning.py",req.query.path])
  childPython.stdout.on("data",(data) =>{
    console.log("stdout :"+ data);
    res.send(data);
  });

  childPython.stderr.on("data",(data) => {
    res.send(data);
  });
  

})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})