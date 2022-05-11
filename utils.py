import json

__data = []


def load_candidates_from_json(path):
    global __data
    with open(path, "r", encoding="utf-8") as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):
    for candidate in __data:
        if candidate["id"] == candidate_id:
            return {
                "name": candidate["name"],
                "position": candidate["position"],
                "picture": candidate["picture"],
                "skills": candidate["skills"]
            }
    return {"not_found": "Кандидат не обнаружен"}


def get_candidates_by_name(candidate_name):
    return [candidate for candidate in __data if candidate_name.lower() in candidate['name'].lower()]


def get_candidates_by_skill(skill_name):
    candidates = []
    for candidate in __data:
        skill = candidate["skills"].lower().split(", ")
        if skill_name.lower() in skill:
            candidates.append(candidate)
    return candidates
