#include "lists.h"

/**
 * check_cycle - checks a cycle in a list
 * @l: pointer to list
 * Return: x
 */
int check_cycle(listint_t *l)
{
	listint_t *c = l;
	int xh = l->n, xs = 0, t = 0;

	c = c->next;
	xs = c->n;
	l = l->next;
	while (l)
	{
		if (l->n == xh)
			t++;
		if (t && xs == l->n)
			return (1);
		l = l->next;
	}
	return (0);
}
