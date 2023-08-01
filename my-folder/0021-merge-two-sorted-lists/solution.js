/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    if(!list1 && !list2){
        return null
    }
    var head = new ListNode(0);
    var merged = head

    var transverseLists=(list1, list2)=>{
        // if list 2 is empty return list 1
        if(list1 && !list2){
            merged.next = list1
            return
        }
        // if list1 is empty, return list2
        if(list2 && !list1){
            merged.next = list2
            return
        }
        // append least node
        if(list1.val <= list2.val){
            merged.next = list1
            list1 = list1.next
        }else{
            merged.next = list2
            list2 = list2.next
        }
        // move to next node
        merged = merged.next
        // iterate till last list
        return transverseLists(list1, list2)
    }
    // call func
    transverseLists(list1,list2)
    return head.next

};
