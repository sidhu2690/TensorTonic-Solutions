def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    topk = recommended[:k]
    precision = sum([1 for item in topk if item in relevant])/k
    recall = sum([1 for item in topk if item in relevant])/len(relevant)
    
    return [precision, recall]
    
    