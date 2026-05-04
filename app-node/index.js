// app-node/index.js
const express = require('express');
const redis = require('redis');
const app = express();

const client = redis.createClient({ url: 'redis://redis:6379' });
client.connect().catch(console.error);

app.get('/texto', (req, res) => res.send("Texto Fixo (Node)"));

app.get('/hora', (req, res) => {
    res.send(`Hora do Servidor: ${new Date().toLocaleTimeString()}`);
});

app.get('/hora-redis', async (req, res) => {
    const cached = await client.get('hora_node');
    if (cached) return res.send(`Hora (via Redis - 60s): ${cached}`);

    const now = new Date().toLocaleTimeString();
    await client.setEx('hora_node', 60, now);
    res.send(`Hora (Novo no Redis): ${now}`);
});

app.listen(5002);
