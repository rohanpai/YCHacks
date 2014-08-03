var monkey_test = function () {
  return {

    init: function () {
      var x = document.getElementById('blah');
      x.innerHTML = "sdfsdfsdf"
    },
    
    performTestWithSelector: function () {
    
    }
  }
}

monkeyTest = new monkey_test().init();

/*
function monkey_test (selector) {
  var elem = document.querySelector(selector);
  var tests = [test1, test2, test3];
  for(var i = 0; i < tests.length; i++) {
    tests[i](selector);
  }
}
*/
