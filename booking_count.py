# Theatre Booking System


TOTAL_SEATS = 350
remaining_seats = TOTAL_SEATS


total_bookings = 0
t

ickets_sold = 0
rejected_bookings = 0


while True:
    print(f"\nAvailable Seats: {remaining_seats}")
    tickets = int(input("Enter number of tickets (0 to exit): "))


    # Exit condition
    if tickets == 0:
        break


    # Validate ticket count
    if tickets < 1 or tickets > 15:
        print("BOOKING REJECTED - You can book between 1 and 15 tickets only")
        rejected_bookings += 1
        continue


    # Check seat availability
    if tickets > remaining_seats:
        print("BOOKING REJECTED - Not enough seats available")
        rejected_bookings += 1
        continue


    ages = []
    invalid_age = False


    # Get ages
    for i in range(tickets):
        age = int(input(f"Enter age of person {i+1}: "))
        
        # Age validation
        if age < 12:
            invalid_age = True
        ages.append(age)


    # If any age invalid → reject booking
    if invalid_age:
        print("BOOKING REJECTED - Age restriction")
        rejected_bookings += 1
        continue


    # Booking confirmed
    print(f"BOOKING CONFIRMED - {tickets} tickets")
    total_bookings += 1
    tickets_sold += tickets
    remaining_seats -= tickets


    # Stop if theatre full
    if remaining_seats == 0:
        print("\nTheatre is now FULL")
        break


# Final Report
print("\n----- FINAL REPORT -----")
print(f"Total Bookings: {total_bookings}")
print(f"Total Tickets Sold: {tickets_sold}")
print(f"Rejected Bookings: {rejected_bookings}")
print(f"Remaining Seats: {remaining_seats}")
