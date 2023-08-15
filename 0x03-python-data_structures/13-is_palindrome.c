#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * copy_lists - This function copy a singled link lists
 * @head: Is the pointer to the first elements
 * Return: The new copy list
*/
listint_t *copy_lists(listint_t *head)
{
	listint_t *new_list = NULL;
	listint_t *current = head;

	while (current != NULL)
	{
		add_nodeint_end(&new_list, current->n);
		current = current->next;
	}
	return (new_list);
}
/**
 * rounded_lists - This function rounded the linked list
 * @list: Is the linked lists
 * Return: The rounded lists
*/
listint_t *rounded_lists(listint_t *list)
{
	listint_t *current, *tmp = list, *new_list = NULL;

	current = tmp;
	while (tmp != NULL)
	{
		current = tmp;
		tmp = tmp->next;
		current->next = new_list;
		new_list = current;
	}
	return (new_list);
}
/**
 * is_palindrome - checks if the singly linked lists
 * of integerer is a palindrome
 * @head: Is a pointers to pointers of the singly lists
 * Return: 0 or 1
*/
int is_palindrome(listint_t **head)
{
	listint_t *copy, *rr_lt, *tmp = *head, *tmp2;

	if (*head == NULL)
		return (1);
	copy = copy_lists(tmp);

	rr_lt = rounded_lists(copy);
	tmp2 = rr_lt;
	while (tmp != NULL && tmp2 != NULL)
	{
		if (tmp->n != tmp2->n)
		{
			free_listint(rr_lt);
			return (0);
		}
		tmp = tmp->next;
		tmp2 = tmp2->next;
	}
	free_listint(rr_lt);
	return (1);
}
