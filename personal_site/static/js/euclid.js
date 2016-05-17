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

