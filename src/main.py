import src.entity_fabrics.person_fabric as prsfab
import src.entity_fabrics.client_fabric as clntfab

if __name__ == "__main__":
	persons = prsfab.person_fabric(10)
	clients = clntfab.client_fabric(5, persons)
	client = clients[0]

	print(client.person_reference)
	print(client.person_name)