const https = require('https');
var char = String.fromCharCode;
var report = '';
var data = '';

const getOpts = {
	url : 'https://api.openweathermap.org/data/2.5/weather?id=5375916&appid=92dcc5b18216a951232bc612e25104e0&units=imperial',
	method : 'GET',
};

const getReq = https.request(getOpts, (getRes) => {
	var data = '';
	console.log('statusCode:', getRes.statusCode);
	console.log('headers:', getRes.headers);
	getRes.on('data', (d) => {
		data += d;
	});
});
getReq.on('error', (getErr) => {
	console.error(getErr);
});
console.log(data);
var obj = JSON.parse(data);
console.log(JSON.stringify(obj, null, 4));
var buildstr = obj.main.temp + char(0xB0) + 'F and ' + obj.weather[0].main + '. ' + obj.main.temp_min + char(0xB0) + 'F - ' + obj.main.temp_max + char(0xB0) + 'F, ' + obj.wind.speed + ' mph wind';
console.log(buildstr);
report = encodeURI(buildstr);
console.log(report);





const postOpts= {
	url : 'https://epic-dev/view/api/v1/data-store/write/1?value=' + report + '&api_key=JdDoCVBv4J4dP2u6amTiV9vovFm6rdew',
	rejectUnauthorized : false,
	method : 'POST',
	headers: {
		'Content-Type':'application/json'
	}
};

const postReq = https.request(postOpts, (postRes) => {
	var data = '';
	postRes.on('data', (d) => 		{ data += d; });
	postRes.on('error', (err) => 	{ console.log("Error: " + err.message); });
});
postReq.end();
console.log(data);
