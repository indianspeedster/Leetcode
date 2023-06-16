/**
 * @return {number}
 */
var argumentsLength = function(...args) {
    let total = 0
    for (let number of args){
        total += 1;
    }
 return total
};

/**
 * argumentsLength(1, 2, 3); // 3
 */