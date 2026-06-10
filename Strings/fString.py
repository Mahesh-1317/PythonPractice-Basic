name, marks, rank = "Alia", 92.567, 3

print(f'Hello, {name}')

#   Format numbers
print(f'Marks: {marks:.2f}')
print(f'Marks: {marks:.0f}')
print(f'Count: {10000000:,}')

#   Padding and alingment
print(f'{name:<15}|{marks:>8.2f}|{rank:^14}')

#   Expressions inside {}
price, gst = 500, 0.18
print(f'Price:Rs.{price} | GST:Rs.{price*gst:.2f} | Total:Rs.{price*(1+gst):.2f}')