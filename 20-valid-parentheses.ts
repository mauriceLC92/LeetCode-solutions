function isValid(s: string): boolean {
  let bracketTracker = {
    "(": ")",
    "[": "]",
    "{": "}",
  };

  let stack = [];
  const inputStringArr = s.split("");

  for (let index = 0; index < inputStringArr.length; index++) {
    const currentBracket = inputStringArr[index];

    if (bracketTracker[currentBracket]) {
      stack.push(currentBracket);
    } else {
      if (stack.length === 0) {
        return false;
      }
      const lastElement = stack.pop();
      if (currentBracket !== bracketTracker[lastElement]) {
        return false;
      }
    }
  }

  return stack.length === 0;
}
