#include "lists.h"

/**
 * revl? (- reverse list)?
 *
 * @h: input head
 * Return: n
 */
int *revl(listint_t **h)
{
	listint_t *t = *h;
	int x, *z;

	while (t)
	{
		x++;
		t = t->next;
	}
	z = malloc(sizeof(int) * x);
	if (!z)
		return (NULL);
	t = *h;
	x = 0;
	while (t)
	{
		z[x] = t->n;
		x++;
		t = t->next;
	}
	return (z);
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
	int l = 0, i = 0, x, *lis, r = 0;

	if (!t)
		return (1);
	while (t)
	{
		l++;
		t = t->next;
	}
	x = l;
	t = *h;
	lis = revl(h);
	while (t && i < x)
	{
		if (t->n != lis[l - 1])
			break;
		i++;
		t = t->next;
		l--;
	}
	free(lis);
	if (i == x)
		r = 1;
	return (r);
}
