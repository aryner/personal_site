function euclidSteps(m,n) {
  var steps = [];
  var r = -1;
  while (r !== 0) {
    var step = {};
    step.m = m;
    step.n = n;
    if (m < n) {
      var temp = m;
      m = n;
      n = temp;
      step.r = -1;
      steps.push(step);
      continue;
    }
    r = m % n;
    step.r = r;
    steps.push(step);
    m = n;
    n = r;
  }

  return steps
}

function displayStep(step) {
  if(step.m < step.n) {
    step.r = step.m;
  }
  var result = '<code>m = '+step.m+', n = '+step.n+', m/n = '+Math.floor(step.m/step.n)+', r = '+step.r+'</code><br>';
  if(step.r === 0) {
    result += '<code>GCD = '+step.n+'</code>';
  }

  return result;
}

const gcd = document.getElementById('gcd')

gcd.onclick = function() {
  var display  = document.getElementById('steps');
  var m = document.getElementById('m').value;
  var n = document.getElementById('n').value;

  if (!n || !m || !Number(n+m)) {
    display.innerHTML = '';
  }
  else {
    var content = '';
    var steps = euclidSteps(Number(m),Number(n));
    steps.forEach(function(step) {
      content += displayStep(step);
    });
    display.innerHTML = content;
  }
};


