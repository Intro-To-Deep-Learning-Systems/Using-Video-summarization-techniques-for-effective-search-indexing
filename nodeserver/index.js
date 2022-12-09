const express = require('express'); 
const cors = require('cors');

const app = express()
app.use(cors())
const port = 3001

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.post("/summarize",(req,res)=>{
  res.status(404).send("YET TO IMPLEMENT")
})


app.post("/caption",(req,res)=>{
  res.status(404).send("YET TO IMPLEMENT")
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})