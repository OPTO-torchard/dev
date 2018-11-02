const https = require('https');
var char = String.fromCharCode;
var report = '';
var data = '';


report = "Opto22";
const postOpts= {
	url : 'http://localhost/view/api/v1/data-store/write/1?value=' + report + '&api_key=JdDoCVBv4J4dP2u6amTiV9vovFm6rdew',
	rejectUnauthorized : false,
	method : 'POST',
	headers: 'accept: application/json'
};

const postReq = https.request(postOpts, (postRes) => {
	var data = '';
	postRes.on('data', (d) => {
		data += d;
	});
});

postReq.on('error', (postErr) => {
	console.error(postErr);
});

console.log(data);

postReq.end();
