import re

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def semantic_similarity_score(
        ideal_answer,
        user_answer
):

    emb1 = model.encode(
        [ideal_answer]
    )

    emb2 = model.encode(
        [user_answer]
    )

    similarity = cosine_similarity(
        emb1,
        emb2
    )[0][0]

    return round(
        similarity * 100,
        2
    )


def extract_keywords(text):

    words = re.findall(
        r"\b[a-zA-Z]{4,}\b",
        text.lower()
    )

    stop_words = {
        "this",
        "that",
        "with",
        "from",
        "have",
        "will",
        "into",
        "their",
        "about",
        "there",
        "would",
        "should",
        "which"
    }

    return list(
        set(
            [
                w
                for w in words
                if w not in stop_words
            ]
        )
    )


def keyword_coverage_score(
        ideal_answer,
        user_answer
):

    keywords = extract_keywords(
        ideal_answer
    )

    if not keywords:
        return 100

    user_text = user_answer.lower()

    matched = 0

    for keyword in keywords:

        if keyword in user_text:
            matched += 1

    return round(
        (matched / len(keywords)) * 100,
        2
    )


def completeness_score(
        ideal_answer,
        user_answer
):

    ideal_words = len(
        ideal_answer.split()
    )

    user_words = len(
        user_answer.split()
    )

    if ideal_words == 0:
        return 100

    return round(
        min(
            (user_words / ideal_words) * 100,
            100
        ),
        2
    )