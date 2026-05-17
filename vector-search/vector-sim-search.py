#!/usr/bin/env python

from sentence_transformers import SentenceTransformer

import faiss
import numpy as np


np.set_printoptions(
    edgeitems=2, threshold=1, precision=3, floatmode="fixed", suppress=True
)

MODEL = SentenceTransformer("all-MiniLM-L6-v2")
QUERIES = ["動物"]
TITLES = (
    "ノンアル飲料が…",
    "ニシキヘビが…",
    "大相撲夏場所…",
    "少女守った犬…",
    "2mのオヒョウ…",
)
RANKS = [4, 1, 3, 0, 2]


def get_sample_vectors_of(dimension, by_distance=False):
    random_rotation_matrix = faiss.RandomRotationMatrix(
        MODEL.get_sentence_embedding_dimension(),
        dimension
    )

    for seed in range(1000):
        random_rotation_matrix.init(seed)

        query_vectors, title_vectors = [
            random_rotation_matrix.apply_py(MODEL.encode(strings))
            for strings in [QUERIES, TITLES]
        ]

        if by_distance:
            scores = -np.linalg.norm(title_vectors - query_vectors, axis=1).ravel()
        else:
            scores = (title_vectors @ query_vectors.T).ravel()
        ranks = np.argsort(np.argsort(-scores))
        if np.array_equal(RANKS, ranks):
            return scores, title_vectors, query_vectors

    raise


scores, title_vectors, query_vectors = get_sample_vectors_of(8)
for score, title_vector in zip(scores, title_vectors):
    print(score, title_vector)
for query_vector in query_vectors:
    print(query_vector)


from adjustText import adjust_text

import matplotlib.pyplot as plt
import japanize_matplotlib  # noqa


plt.rcParams["font.size"] = 16
plt.figure()

_, title_vectors, query_vectors = get_sample_vectors_of(2, by_distance=True)
annotations = []
for vectors, marker, strings in [[title_vectors, "k.", TITLES], [query_vectors, "k*", QUERIES]]:
    for vector, string in zip(vectors, strings):
        plt.plot(*vector, marker, markersize=plt.rcParams["font.size"])
        ha = "left" if vector[0] < 0 else "right"
        annotations.append(plt.annotate(string, vector, va="center", ha=ha))
adjust_text(annotations, expand=(1.25, 1.25))

plt.savefig(__file__.replace(".py", ".png"), bbox_inches="tight")
