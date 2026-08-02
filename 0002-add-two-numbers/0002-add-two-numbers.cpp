/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
   
       ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode;
        ListNode* cur = head;

        int sum = 0;
         while (l1 != nullptr || l2 != nullptr || sum != 0) {
            ListNode* a1 = new ListNode;
            if (l1 != nullptr) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                sum += l2->val;
                l2 = l2->next;
            }
            
            a1->val = sum % 10;
            sum = sum / 10;
            cur->next = a1;
            cur = cur->next;
        }
        return head->next;
    } 
    
};