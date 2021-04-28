function balancedBrackets(input: string): boolean {
  const inputArr = input.split("");
  const leftHandBracket = "(";
  const rightHandBracket = ")";

  let leftHandCount = 0;
  let rightHandCount = 0;

  for (let index = 0; index < inputArr.length; index++) {
    if (inputArr[index] === leftHandBracket) {
      leftHandCount++;
    } else if (inputArr[index] === rightHandBracket) {
      rightHandCount++;
    }

    if (rightHandCount > leftHandCount) {
      return false;
    }
  }

  return leftHandCount === rightHandCount;
}

/*
 *	()								= TRUE
 *	(1 + 2) * 4 			= TRUE
 *	((2 + 4)					= FALSE
 *	)(								= FALSE
 *	(2 / 3) * (2 - 1)	= TRUE
 *  (1 * 3 + (7 - 2)) = TRUE
 *	()(								= FALSE
 */

// [')', '(']

const testString = "(1 + 2) * 4";
const testString2 = "(2 / 3) * (2 - 1)";
const testString3 = ")(";

// balancedBrackets(testString2);
// balancedBrackets(testString3);
console.log("", balancedBrackets(testString3));

function balancedBracketsOptimal(input: string): boolean {
  const inputArr = input.split("");
  const leftHandBracket = "(";
  const rightHandBracket = ")";

  let bracketCount = 0;

  for (let index = 0; index < inputArr.length; index++) {
    if (inputArr[index] === leftHandBracket) {
      bracketCount++;
    } else if (inputArr[index] === rightHandBracket) {
      bracketCount--;
    }

    if (bracketCount < 0) {
      return false;
    }
  }

  return bracketCount === 0;
}
