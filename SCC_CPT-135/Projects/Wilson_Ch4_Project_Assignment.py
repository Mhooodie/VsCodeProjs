'''Chap 4'''

service_dict1 = {

    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12,

}

service_dict2 = {

    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12,
    
    "oil change": 35,
    "tire rotation": 19,
    "car wash": 7,
    "car wax": 12
}

print("\nDavy's auto shop services")
for service, price in service_dict1.items():
    print (f'{service} -- ${price}')

print("")
service1 = input("Select first service:\n").strip()
service2 = input("Select second service:\n").strip()

print("\nDavy's auot shop invoice\n")
print(f'Service 1: {service1}, ${service_dict2.get(service1)}')
print(f'Service 2: {service2}, ${service_dict2.get(service2)}\n')
total_cost = service_dict2.get(service1) + service_dict2.get(service2)
print(f'Total: {total_cost}$')

















