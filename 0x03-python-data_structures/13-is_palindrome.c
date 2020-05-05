#include "lists.h"
int lenls(listint_t **h)
{
	int ln = 0;
	listint_t *t = *h;
	while (t)
	{
		ln++; t = t->next;
	}
	return (ln);
}
int *revl(listint_t **h, int *z)
{
	listint_t *t = *h;
	int x = 0;
	while (t)
	{
		z[x] = t->n; x++; t = t->next;
	}
	return (z);
}
int is_palindrome(listint_t **h)
{
	listint_t *t = *h;
	int l = 0, i = 0, x, *lis, r = 0;
	if (!t)
		return (1);
	l = lenls(h); lis = malloc(sizeof(int) * l);
	if (!lis)
		return (0);
	lis = revl(h, lis); x = l;
	while (i < x)
	{
		if (lis[i] != lis[l - 1])
			break;
		i++; l--;
	} free(lis);
	if (i == x)
		r = 1;
	return (r);
}
