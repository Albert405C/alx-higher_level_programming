#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
*add_nodeint - adds a new node at the beginning of a listint_t list
*@head: head of listint_t
*@n: int to add in listint_t list
*Return: address of the new element, or NULL if it failed
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
*is_palindrome - identify if a syngle linked list is palindrome
*@head: head of listint_t
*Return: 1 if it is palindrome else 0
*/



int is_palindrome(listint_t **head) {
    if (*head == NULL || (*head)->next == NULL) {
        /* An empty list or a list with a single node is considered a palindrome */
        return 1;
    }

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp;

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;

        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    if (fast != NULL) {
        slow = slow->next;
    }
    while (prev != NULL && slow != NULL) {
        if (prev->n != slow->n) {
            return 0; 
        }
        prev = prev->next;
        slow = slow->next;
    }

    return 1; 
}
