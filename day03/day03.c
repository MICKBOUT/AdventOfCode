#include <fcntl.h>
#include <string.h>
#include "get_next_line.h"

long unsigned int	ft_biggg(char *line)
{
	int l = 0;
	while (line[l] && line[l] != '\n') {
		l++;}
	int	prev = -1;
	int	current;
	long unsigned int res = 0;
	for (int place = 0; place < 12; place++){
		current = prev + 1;
		for (int i = current + 1; i < l - (11 - place); i++) {	
			if (line[i] > line[current])
			current = i;
		}
		res *= 10;
		res += line[current] - '0';
		prev = current;
	}
	return (res);
}

int main(int ac, char **av) {
	if (ac != 2) {
		(printf("give the path of the output plz"));
		return (-1);
	}
	int fd = open(av[1], O_RDONLY);
	if (fd < 0)
		printf("fd error");
	char *line;
	long unsigned int res = 0;
	while ((line = get_next_line(fd))) {
		res += ft_biggg(line);
	}
	close(fd);
	printf("res = %lu", res);
}