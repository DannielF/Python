counter_out = 0
counter_ins = 0

while counter_out < 11:
    while counter_ins < 11:
        print(counter_out, counter_ins)
        counter_ins += 1
        # if counter_ins >= 6:
        #     break

    counter_out += 1
    counter_ins = 0

# x = 0.0
# for i in range(10):
#     x += 0.1

# if x < 1.0 and x > 0.999999: 
#     print(f'x = {x}')
# else:
#     print(f'x != {x}')