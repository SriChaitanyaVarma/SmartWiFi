from collections import defaultdict


def analyze_channels(networks):

    channel_stats = defaultdict(
        lambda: {
            "count": 0,
            "total_signal": 0,
            "interference_score": 0
        }
    )

    for network in networks:

        if "channel" not in network:
            continue

        channel = network["channel"]
        signal = network.get("signal", 0)

        channel_stats[channel]["count"] += 1
        channel_stats[channel]["total_signal"] += signal

    for channel in channel_stats:

        count = channel_stats[channel]["count"]

        signal = channel_stats[channel]["total_signal"]

        channel_stats[channel]["interference_score"] = (
            count * 10 + signal
        )

    return dict(channel_stats)