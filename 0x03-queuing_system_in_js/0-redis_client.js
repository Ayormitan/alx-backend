import { createClient } from 'redis';


//cretae a redis clkient
const client = createClient();


// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});


// Handle connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server: ${err.message}');
});
