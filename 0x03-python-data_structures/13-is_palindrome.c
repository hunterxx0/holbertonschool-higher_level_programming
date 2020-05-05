#include "lists.h"

/**
 * revl? (- reverse list)?
 *
 * @h: input head
 * @z: input array
 * Return: n
 */
int revl(listint_t **h, int *z)
{
	listint_t *t = *h;
	int x = 0;

	while (t)
	{
		z[x] = t->n;
		x++;
		t = t->next;
	}
	return (x);
}
/**
 * is_palindrome? (- palind)?
 *
 * @h: input head
 * Return: 1 or 0
 */
int is_palindrome(listint_t **h)
{
	listint_t *t = *h;
	int l = 0, i = 0, x, lis[50], r = 0;

	if (!t)
		return (1);
	l = revl(h, lis);
	x = l;
	while (t && i < x)
	{
		if (t->n != lis[l - 1])
			break;
		i++;
		t = t->next;
		l--;
	}
	if (i == x)
		r = 1;
	return (r);
}
