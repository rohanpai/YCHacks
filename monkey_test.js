function monkey_test (selector) {
  var elem = document.querySelector(selector);
  var tests = [test1, test2, test3];
  for(var i = 0; i < tests.length; i++) {
    tests[i](selector);
  }
}