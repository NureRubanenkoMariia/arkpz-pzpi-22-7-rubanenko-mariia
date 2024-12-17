# Поганий приклад
@staticmethod
def delete(id):
    success = False 
    try:
        member = Member.query.get(id)
        if member:
            db.session.delete(member)
            db.session.commit()
            success = True
            message = 'Member deleted successfully'
        else:
            message = 'Member not found'
    except Exception as e:
        return ErrorHandler.handle_error(str(e))
    
    return {'success': success, 'message': message}, 200 if success else 404

# Гарний приклад
@staticmethod
def delete(id):
    try:
        member = Member.query.get(id)
        if not member:
            return {'success': False, 'message': 'Member not found'}, 404
        
        db.session.delete(member)
        db.session.commit()
        return {'success': True, 'message': 'Member deleted successfully'}, 200
    
    except Exception as e:
        return ErrorHandler.handle_error(str(e))

# Поганий приклад
member = ["John", "Doe", "1990-01-01", 30, "Low"]

def display_member_info(member):
    print(f"First Name: {member[0]}")
    print(f"Last Name: {member[1]}")
    print(f"Date of Birth: {member[2]}")
    print(f"Age: {member[3]}")
    print(f"Threat Level: {member[4]}")

display_member_info(member)

# Гарний приклад
class Member:
    def __init__(self, first_name, last_name, date_of_birth, age, threat_level):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.threat_level = threat_level

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Age: {self.age}")
        print(f"Threat Level: {self.threat_level}")


member = Member("John", "Doe", "1990-01-01", 30, "Low")
member.display_info()


# Поганий приклад
def apply_discount(price, discount):
    if discount > 0.3:
        discount = 0.3 
    price = price * (1 - discount)
    return price

final_price = apply_discount(100, 0.5)
print(f"Final Price: {final_price}")

# Гарний приклад
def apply_discount(price, discount):
    effective_discount = min(discount, 0.3) 
    final_price = price * (1 - effective_discount)
    return final_price

final_price = apply_discount(100, 0.5)
print(f"Final Price: {final_price}")
