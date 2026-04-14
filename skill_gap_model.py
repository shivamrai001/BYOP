from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def normalize_skills(skill_list):
    return [skill.strip().lower() for skill in skill_list if skill.strip()]


def skills_to_text(skill_list):
    return " ".join(normalize_skills(skill_list))


def calculate_similarity(user_skills, role_skills):
    user_text = skills_to_text(user_skills)
    role_text = skills_to_text(role_skills)

    documents = [user_text, role_text]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(similarity_score * 100, 2)


def find_missing_skills(user_skills, role_skills):
    user_set = set(normalize_skills(user_skills))
    role_set = normalize_skills(role_skills)

    missing = [skill for skill in role_set if skill not in user_set]
    return missing


def suggest_learning_path(missing_skills):
    recommendations = []
    for skill in missing_skills:
        recommendations.append(f"Learn {skill}")
    return recommendations
