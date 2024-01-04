#include <stdlib.h>
#include "main.h"

/**
 * check_cycle - checks if a singly linked list contains a cycle
 * @list: A singly linked list
 *
 * Return: if there is no list - 0
 * 	if there is a cycle - 1
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list->next;
	hare = list->next->next;

	while (trutle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);

		turtle = turtle->next;
		hare = hare->next->next;
	}

	return(0);
}
