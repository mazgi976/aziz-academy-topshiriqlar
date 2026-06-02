def rect_area(w, h=1):
    return w * h

input_data = input().split()

if len(input_data) == 1:
    print(rect_area(int(input_data[0])))
else:
    print(rect_area(int(input_data[0]), int(input_data[1])))