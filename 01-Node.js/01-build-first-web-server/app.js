const http = require('http');

const hostname = '0.0.0.0';
const port = 3000;

const server = http.createServer((req,resp) => {
    /* // ES6 features? -> "{ <properties> } = <object>"
    const { method, url } = req;
    const { headers } = req;
    const userAgent = headers['user-agent'];
    console.log(`request = ${method},${url},${userAgent}`);
    */

    resp.statusCode = 200;
    resp.setHeader('Content-Type','text/plain; charset=utf-8');
    resp.end('hello, world\n');
});

server.listen(
    port, hostname,
    () => {
        console.log(`Server running at http://${hostname}:${port}/`);
    }
);
