import json
from skill_gap_model import calculate_similarity, find_missing_skills, suggest_learning_path


def load_roles(filename="roles.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: roles.json file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: roles.json contains invalid JSON.")
        return {}


def display_roles(roles):
    print("\nAvailable Job Roles:")
    for index, role in enumerate(roles.keys(), start=1):
        print(f"{index}. {role}")


def get_role_choice(roles):
    role_names = list(roles.keys())
    choice = input("\nEnter the target role name: ").strip()

    for role in role_names:
        if choice.lower() == role.lower():
            return role

    print("Invalid role selected.")
    return None


def get_user_skills():
    user_input = input("\nEnter your skills separated by commas: ").strip()

    if not user_input:
        return []

    return [skill.strip() for skill in user_input.split(",") if skill.strip()]


def main():
    print("===== AI-Based Skill Gap Analyzer =====")

    roles = load_roles()
    if not roles:
        return

    display_roles(roles)

    selected_role = get_role_choice(roles)
    if selected_role is None:
        return

    user_skills = get_user_skills()
    if not user_skills:
        print("No skills entered. Please run the program again.")
        return

    role_skills = roles[selected_role]

    match_score = calculate_similarity(user_skills, role_skills)
    missing_skills = find_missing_skills(user_skills, role_skills)
    recommendations = suggest_learning_path(missing_skills)

    print("\n===== ANALYSIS RESULT =====")
    print(f"Target Role: {selected_role}")
    print(f"Your Skills: {', '.join(user_skills)}")
    print(f"Required Skills: {', '.join(role_skills)}")
    print(f"Match Score: {match_score}%")

    if missing_skills:
        print("\nMissing Skills:")
        for skill in missing_skills:
            print(f"- {skill}")
    else:
        print("\nExcellent! You already match all the major skills for this role.")

    if recommendations:
        print("\nRecommended Learning Path:")
        for item in recommendations:
            print(f"- {item}")


if __name__ == "__main__":
    main()
