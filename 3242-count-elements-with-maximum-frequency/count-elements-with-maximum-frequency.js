/**
 * @param {number[]} nums
 * @return {number}
 */
var maxFrequencyElements = function(nums) {
    var myMap = new Map();
    for (const num of nums) {
        myMap.set(num, 0);
    }
    let maxi = 0
    for (const num of nums) {
        var x = myMap.get(num)
        maxi = Math.max(maxi, x+1)
        myMap.set(num, x+1);
    }

    

    let count = 0
    for (var [key, value] of myMap) {
    if (value === maxi){
        count += 1
    }
}
    return maxi * count
};