var express = require('express');
var router = express.Router();

res.get('/stations/cheapest/:X/:gasId', function(req, res)) {
	res.json([{stationId: 1}]) //List of X cheapest stations for a given gas type
}

res.get('/stations/cheapest/:X', function(req, res)) {
	res.json([{stationId: 1}]) //List of X cheapest stations on average price
}

res.get('/stations/:id/fuels/:gasId', function(req, res)) {
	res.json({gas93: 983}) //Info about specific fuel
}

router.get('/stations/:id/fuels', function(req, res) {
	res.json({gas93: 983}) //Info about gas/diesel and prices
})

router.get('/stations/:id/payment_methods', function(req, res) {
	res.json({debit: true}) //Info about payment methods for given station
})

router.get('/stations/:id/services', function(req, res) {
	res.json({bathroom: false}) //Info about services in the station
})

router.get('/stations/:id/closest/:X', function(req, res) {
	res.json([{stationId: 1}]) //List of X closest stations
})

router.get('/stations/:id'), function(req, res) { //Detailed info for one station
	res.json({stationId: 1})
}

router.get('/stations', function(req, res) { //Array of all stations with minimal info
  res.json([{stationId: 1}]);
});

router.get('/regions/:id/stations', function(req, res) { //Array of all stations for a given region
	res.json([{stationId: 1}])
})

router.get('/regions/:id', function(req, res) { //Detailed info about a region
	res.json({regionId: 1})
})

router.get('/regions', function(req, res) { //Array of all regions with minimal info
	res.json([{regionId: 1}]) 
})

module.exports = router;
