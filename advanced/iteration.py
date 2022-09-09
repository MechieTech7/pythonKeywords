# Break,Continue,While,Pass,For,In

for count in range(1, 10):
    while count < 3:
        print(f"This is for the count {count}")
        count += count
    if count == 3:
        pass
        print(f"This is pass block for count {count}")
        print(f"This is also the pass block")
    elif count == 4:
        continue
        print("This statement will not be executed")
    else:
        break
        print("This statement will not be executed")
print(count)
