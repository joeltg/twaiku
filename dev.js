console.log('hi');

var s = new WebSocket("ws://localhost:5000/api");
s.onopen = function (event) {
	console.log('yay we\'re connected!');
	s.send('{event: "line", length: 7, data: "hello"}');
};
s.onmessage = function (event) {
	console.log('received event!');
	console.log(JSON.parse(event.data));
};

