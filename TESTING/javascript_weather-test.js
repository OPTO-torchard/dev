const https = require('https');
var char = String.fromCharCode;
var report = '';
var data = '';

https.get('https://api.openweathermap.org/data/2.5/weather?id=5375916&appid=92dcc5b18216a951232bc612e25104e0&units=imperial', (resp) => {
		let data = '';
		resp.on('data', (chunk) => {
			data += chunk;
		});

		resp.on('end', () => {
			var obj = JSON.parse(data);
			console.log(JSON.stringify(obj, null, 4));
			var report = obj.main.temp + char(0xB0) + 'F and ' + obj.weather[0].main + '. ' + obj.main.temp_min + char(0xB0) + 'F - ' + obj.main.temp_max + char(0xB0) + 'F, ' + obj.wind.speed + ' mph wind';
			console.log(report);
		});

	}).on("error", (err) => {
	console.log("Error: " + err.message);
	console.log('Weather GET request complete.');
});
console.log('Starting POST request.');

//report = report.replace(/ /g, '%20');
report = encodeURI(report);
console.log(report);


const options = {
	url : 'http://epic-dev/view/api/v1/data-store/write/1?value=' + report + '&api_key=JdDoCVBv4J4dP2u6amTiV9vovFm6rdew',
	rejectUnauthorized : false,
	method : 'POST',
	headers: {
		'accept':'application/json'
	}
};

const https2 = require('http');

const req = https2.request(options, (res) => {
	var data = '';
	res.on('data', (d) => 		{ data += d; });
	res.on('error', (err) => 	{ console.log("Error: " + err.message); });
});
req.end();
console.log(data);
