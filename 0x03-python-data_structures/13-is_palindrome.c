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
int is_palindrome(listint_t **h)
{
	listint_t *t = *h;
	int l = 0, i = 0, r = 0, s = 0;
	if (!t || !t->next)
		return (1);
	l = lenls(h);
	while (t)
	{
		if (i < l / 2)
		s += t->n;
		else
		{
			if (l % 2 != 0 && i == l / 2)
				s += 0;
			else
				s -= t->n;
		}
		t = t->next;
		i++;
	}
	printf("%d\n", s);
	if (s == 0)
		r = 1;
	return (r);
}
