var watson = require('watson-developer-cloud');
var language_translator = watson.language_translator({
  username: '{username}',
  password: '{password}',
  version: 'v2'
});
language_translator.translate({
    text: 'hello',
    source: 'en',
    target: 'es'
  }, function(err, translation) {
    if (err)
      console.log(err)
    else
      console.log(translation);
});