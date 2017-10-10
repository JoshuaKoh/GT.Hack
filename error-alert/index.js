//var debug = require('debug')('error-alert:server'); 
var express = require('express')
var app = express()
var logger = require('morgan'); 

app.use(logger('dev'));
app.set('view engine', 'jade');
app.get('/', function (req, res) {
  res.send('Hello World')
})

app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});
var port = process.env.PORT || 1337; 
app.listen(port);
console.log("Server running at http://localhost:%d", port);