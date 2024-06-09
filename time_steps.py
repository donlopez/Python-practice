start_time = int(input())
end_time = int(input())

print('Time steps:', end=' ')

for curr_time in range(start_time, end_time + 1, 4):
    print(curr_time, end=' ')
print()
