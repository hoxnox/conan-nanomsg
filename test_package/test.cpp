#include <nanomsg/nn.h>
#include <nanomsg/reqrep.h>

int main(int argc, char* argv[])
{
	int fd = nn_socket (AF_SP, NN_REP);
	if (fd < 0)
		return -1;
	return 0;
}

