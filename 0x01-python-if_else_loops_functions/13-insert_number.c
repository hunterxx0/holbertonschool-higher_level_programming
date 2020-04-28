#include "lists.h"
/**
 * insert_node? (- add node at the beginning)?
 *
 * @h: input head
 * @n: input node
 * Return: n
 */
listint_t *insert_node(listint_t **h, const int n)
{
	listint_t *t, *x = *h, *z = (listint_t *)malloc(sizeof(listint_t));

	if (z == NULL)
		return (NULL);
	z->n = n;
	z->next = NULL;
	if ((*h)->n > n)
	{
		z->next = *h;
		*h = z;
	}
	else
	{
		while (x)
		{
			if (x->n > n)
				break;
			t = x;
			x = x->next;

		}
		z->next = t->next;
		t->next = z;
	}
	return (z);
}
