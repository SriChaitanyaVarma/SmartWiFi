def recommend_channel(channel_stats):

    preferred_channels = [1, 6, 11]

    recommendations = []

    for channel in preferred_channels:

        if channel in channel_stats:
            score = channel_stats[channel]["interference_score"]
            count = channel_stats[channel]["count"]
        else:
            score = 0
            count = 0

        recommendations.append({
            "channel": channel,
            "score": score,
            "count": count
        })

    recommendations.sort(key=lambda x: x["score"])

    return {
        "recommendation_reason": (
            f"Channel {recommendations[0]['channel']} "
            f"has the lowest congestion and interference score."
        ),
        "recommended_channel": recommendations[0]["channel"],
        "score": recommendations[0]["score"],
        "all_channels": recommendations
    }