const operators = {
    plus: (a, b) => (a + b),
    minus: (a, b) => (a - b),
    times: (a, b) => (a * b),
    divide: (a, b) => (a / b)
};
 
const solve = (sum) => {
    if (typeof sum === 'number') {
        return sum;
    } else if (Array.isArray(sum)) {
        if (sum.length === 3 && operators[sum[1].toLowerCase()]) {
            return operators[sum[1].toLowerCase()](
                solve(sum[0]),
                solve(sum[2])
            );
        } else {
            throw new Error('invalid operator');
            return null;
        }
    } else {
        throw new Error('invalid arguments');
        return null;
    }
}
console.log(solve([3, 'times', [3, 'plus', [9, 'Divide', 9]]]));