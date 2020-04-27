#include "lists.h"

/**
 * check_cycle - checks a cycle in a list
 * @l: pointer to list
 * Return: x
 */
int check_cycle(listint_t *l)
{
	listint_t *c = l;
	int xh = l->n;

	c = c->next;
	while (c)
	{
		if (c->n == xh)
			return (1);
		c = c->next;
	}
	return (0);
}
