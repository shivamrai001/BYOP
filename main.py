import json

# ================= LOAD JOB ROLES =================
def load_roles():
    try:
        with open("roles.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: roles.json file not found!")
        return {}

# ================= USER INPUT =================
def get_user_skills():
    skills = input("\nEnter your skills (comma separated): ")
    return [skill.strip().lower() for skill in skills.split(",")]

# ================= SELECT ROLE =================
def select_role(roles):
    print("\nAvailable Job Roles:")
    role_list = list(roles.keys())
    
    for i, role in enumerate(role_list, 1):
        print(f"{i}. {role}")
    
    while True:
        try:
            choice = int(input("Select a role (number): "))
            if 1 <= choice <= len(role_list):
                role_name = role_list[choice - 1]
                return role_name, roles[role_name]
            else:
                print("Invalid choice! Try again.")
        except ValueError:
            print("Please enter a valid number.")

# ================= ANALYSIS =================
def analyze_skills(user_skills, required_skills):
    required_skills = [skill.lower() for skill in required_skills]
    
    matched = list(set(user_skills) & set(required_skills))
    missing = list(set(required_skills) - set(user_skills))
    
    score = (len(matched) / len(required_skills)) * 100
    
    return matched, missing, score

# ================= DISPLAY RESULT =================
def display_result(role, user_skills, matched, missing, score):
    print("\n===== ANALYSIS RESULT =====")
    print(f"Target Role     : {role}")
    print(f"Your Skills     : {', '.join(user_skills)}")
    print(f"Matched Skills  : {', '.join(matched) if matched else 'None'}")
    print(f"Missing Skills  : {', '.join(missing) if missing else 'None'}")
    print(f"Match Score     : {score:.2f}%")
    
    print("\n===== SUGGESTION =====")
    if missing:
        print("You should focus on learning:")
        for skill in missing:
            print(f"- {skill.capitalize()}")
    else:
        print("Excellent! You match all required skills 🎉")

# ================= MAIN =================
def main():
    print("===== SkillGap Analyzer =====")
    
    roles = load_roles()
    if not roles:
        return
    
    user_skills = get_user_skills()
    role_name, required_skills = select_role(roles)
    
    matched, missing, score = analyze_skills(user_skills, required_skills)
    
    display_result(role_name, user_skills, matched, missing, score)

# ================= RUN =================
if __name__ == "__main__":
    main()
import os
import os
print(os.listdir())
