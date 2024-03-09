/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var getCommon = function(nums1, nums2) {
    let ptr1 = 0
    let ptr2 = 0

    while (ptr1 <= nums1.length-1 && ptr2 <= nums2.length-1){
        if (nums1[ptr1] === nums2[ptr2]){
            return nums1[ptr1]
        }
        if (nums1[ptr1] > nums2[ptr2]){
            ptr2 += 1
        }
        else{
            ptr1 += 1
        }
    }
    return -1

    
};