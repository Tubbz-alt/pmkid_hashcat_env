import docker
import os


BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def exec_in_container(command):
    """Runs a command in the hashcat_container and returns the console output.
    """
    client = docker.from_env()
    with open(os.path.join(BASE_PATH, 'hashcat.docker'), 'rb') as fileobj:
        hashcat_image = client.images.build(fileobj=fileobj)[0]
    std_out = client.containers.run(
        image=hashcat_image,
        command=command)
    return std_out.decode('utf-8')


# Example of how to use the container.
std_out = exec_in_container('ip addr show')
print(std_out)
