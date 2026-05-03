const express = require('express');
const app = express();

app.get('/texto', (req, res) => {
    res.send("Aplicação Node.js: Texto Fixo via Express");
});

app.get('/hora', (req, res) => {
    res.send(`Hora atual (Node): ${new Date().toLocaleTimeString()}`);
});

app.listen(5002, () => console.log('Node App rodando na porta 5002'));