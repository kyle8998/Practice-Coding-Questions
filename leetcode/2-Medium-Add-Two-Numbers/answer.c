#include <stdio.h>
#include <stdlib.h>

//  Definition for singly-linked list.
struct ListNode {
	int val;
	struct ListNode *next;
};

// Stuff above not needed for leetcode submission
//------------------------------------------------------------------------------

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
	// Carry to carry over when sum is over 9
	int carry = 0, sum = 0;
	struct ListNode *result =
	    (struct ListNode *)calloc(1, sizeof(struct ListNode));
	struct ListNode *p1 = l1, *p2 = l2;
	struct ListNode *p = result;

	// If either linked list is null, just return the other
	if (l1 == NULL)
		return l2;
	if (l2 == NULL)
		return l1;

	// Loop through while both lists still have values
	while (1) {
		// Set sum equal to the values and the carry then gets next node
                // If p1 and p2 are not null
                if (p1 && p2){
		    sum = carry + p1->val + p2->val;
		    p1 = p1->next;
		    p2 = p2->next;
                }
                // If p2 is null
                else if (p1 && (p2 == NULL)){
                    sum = carry + p1->val;
                    p1 = p1->next;
                }
                // If p1 is null
                else if (p2 && (p1 == NULL)){
                    sum = carry + p2->val;
                    p2 = p2->next;
                }
                else {
                    break;
                }

		// Carry if p1 + p2 is over 10
		carry = sum / 10;
		// Sets the result value to the sum % 10
		p->val = sum % 10;
		// If p1 or p2 still have values
                // create a new node in the result linked list
		if (p1 || p2) {
			p->next =
			    (struct ListNode *)calloc(1,
						      sizeof(struct ListNode));
			p = p->next;
		}
                // Special last digit edge case
                // Probably could be improved but I'm too lazy
                else if (carry > 0){
                        p->next =
                            (struct ListNode *)calloc(1,
                                                      sizeof(struct ListNode));
                        p = p->next;
                        p->val = carry;
                }
	}
	return result;
}

//------------------------------------------------------------------------------
// Testing

int main()
{
	struct ListNode *l1 =
	    (struct ListNode *)calloc(3, sizeof(struct ListNode));
	struct ListNode *p1 = l1;
	p1->val = 1;
	p1->next = p1 + 1;
	p1++;

	p1->val = 8;
/*	p1->next = p1 + 1;
	p1++;

	p1->val = 5;
	p1->next = NULL;
*/
	struct ListNode *l2 =
	    (struct ListNode *)calloc(5, sizeof(struct ListNode));
	struct ListNode *p2 = l2;
	p2->val = 0;
/*	p2->next = p2 + 1;
	p2++;

	p2->val = 6;
	p2->next = p2 + 1;
	p2++;

	p2->val = 4;
	p2->next = p2 + 1;
	p2++;

	p2->val = 9;
	p2->next = p2 + 1;
	p2++;

	p2->val = 9;
	p2->next = NULL;
*/
	struct ListNode *p = addTwoNumbers(l1, l2);

	while (p != NULL) {
		printf("%d ", p->val);
		p = p->next;
	}
	printf("\n");

	return 0;
}
