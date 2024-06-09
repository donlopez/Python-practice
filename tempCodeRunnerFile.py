start_time = int(input())
end_time = int(input())

print('Time steps:', end=' ')

for curr_time in range(start_time, end_time + 1, 4):
    print(curr_time, end=' ')
print()



first_item = int(input())
last_item = int(input())
items_picked = 0

for item in range(first_item, last_item + 1, 4):
    print(f'Checking item: {item}')
    items_picked += 1

print(f'Total items picked: {items_picked}')
