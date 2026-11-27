def reciprocal_rank_fusion(
    result_lists: list[list[dict]],
    k: int = 60
) -> list[dict]:
    if k <= 0:
            raise ValueError("k must be positive")

    fused_scores = {}
    chunk_lookup = {}