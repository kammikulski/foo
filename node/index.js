const express = require('express');
const app = express();
const port = 3000;

const replication = process.env.replication 

//app.get('/', async (req, res) => {
//	await new Promise(resolve => setTimeout(resolve, 60000)); // 60s
	//
app.get('/', (req, res) => {
  console.log(`request received on ${replication}`);

  const timer = setTimeout(() => {
    if (!res.headersSent) {
      console.log(`sending late response from ${replication}`);
      res.send(`response from ${replication}`);
    }
  }, 7000);

  req.on('close', () => {
    console.log(`client disconnected from ${replication}`);
    clearTimeout(timer);
  });
  
});

app.listen(port, '0.0.0.0', () => {
  console.log(`server ${replication} listening on port ${port}`);
});
