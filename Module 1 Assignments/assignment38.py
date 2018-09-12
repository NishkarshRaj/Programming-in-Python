def check_baggage(baggage_weight):
    if baggage_weight>=0 and baggage_weight<=40:
        return True
    else:
        return False
def check_immigration(expiry_year):
    if expiry_year>=2001 and expiry_year<=2025:
        return True
    else:
        return False
def check_security(noc_status):
    if noc_status=="valid" or noc_status=="VALID":
        return True
    else:
        return False
def traveler():
    try:
        traveler_id=input("Enter the Traveler ID: ")
        traveler_name=input("Enter the Traveler name: ")
        baggage_weight=int(input("Enter the baggage weight: "))
        expiry_year=int(input("Enter the expiry year of immigration: "))
        noc_status=input("Enter the noc status of the traveler: ")
        print(traveler_id)
        print(traveler_name)
        if check_baggage(baggage_weight)==True and check_immigration(expiry_year)==True and check_security(noc_status)==True:
            print("Allow traveler to fly!")
        else:
            print("Detain traveler for re-checking")
    except:
        print("Error encountered")
traveler()
        
