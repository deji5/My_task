available_seat = set(range(1, 51))
while True:
    print("\n availableseat:", available_seat)
    seat = int(input("Enter seat num: "))
    if seat == 0:
     print("Booking system closed. ")
     break
    if seat in available_seat:
       available_seat.remove(seat)
       print(f"seak as been reserved successfully.")
    else:
       print(f"seat as already been reserved .Try again.")
