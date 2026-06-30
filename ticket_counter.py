
passenger_name = "Abdullah"          
destination = "Reykjavik"            
ticket_price = 2450.75            
number_of_tickets = 2             
is_available = True               

print("\nPassenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price: AED", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Tickets Available?", is_available)

print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))


total_cost = ticket_price * number_of_tickets
discount = 150
final_cost = total_cost - discount

print("\nTotal Cost: AED", total_cost)
print("Discount: AED", discount)
print("Final Cost: AED", final_cost)

print("Double Ticket Price: AED", ticket_price * 2)
print("Ticket Price After AED50 Increase: AED", ticket_price + 50)
print("Half Ticket Price: AED", ticket_price / 2)



print("\nIs ticket price under AED3000?", ticket_price < 3000)
print("Are more than 2 tickets booked?", number_of_tickets > 2)
print("Is destination London?", destination == "London")
print("Is final cost more than AED4000?", final_cost > 4000)


travel_message = passenger_name + " is travelling to " + destination + "."
print("\nTravel Message:", travel_message)

print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("First letter of destination:", destination[0])
print("Length of passenger name:", len(passenger_name))


morning_ticket_price = 1800
evening_ticket_price = 2200

print("\nBefore Swapping:")
print("Morning Ticket Price: AED", morning_ticket_price)
print("Evening Ticket Price: AED", evening_ticket_price)

temp_price = morning_ticket_price
morning_ticket_price = evening_ticket_price
evening_ticket_price = temp_price

print("\nAfter Swapping:")
print("Morning Ticket Price: AED", morning_ticket_price)
print("Evening Ticket Price: AED", evening_ticket_price)

# FINAL SUMMARY

print("\n------------------------------")
print("TRAVEL TICKET SUMMARY")
print("------------------------------")
print("Passenger:", passenger_name)
print("Destination:", destination)
print("Tickets Booked:", number_of_tickets)
print("Final Amount to Pay: AED", final_cost)