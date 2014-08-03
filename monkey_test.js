var monkey_test = function () {
  return {
    
    /*
     * elements will store a cached list of DOM Elements
     * this is used to decrease time it will take to make
     * changes to the DOM (i.e. not traverse to find the
     * element that needs to be changed)
     */
    elements: null,

    init: function () {
      this.elements = []
    },
    
    performTestWithSelector: function (id, newContent) {
      var element = document.getElementById(id);
      element.innerHTML = newContent;
    },

    performDrasticChange: function () {
    
    },

    relocateToTestingPage: function () {
      //document.location -> localhost:8000/result.html
    }
  }
}

monkeyTest = new monkey_test();
monkeyTest.init()
