from flask import Flask, render_template

from scanner.wifi_scanner import scan_wifi
from scanner.parser import parse_wifi_data

from analytics.channel_analyzer import analyze_channels
from analytics.recommendation_engine import recommend_channel

app = Flask(__name__)


@app.route("/")
def dashboard():

    raw = scan_wifi()

    networks = parse_wifi_data(raw)
    
    print("\nNETWORKS:")
    for network in networks:
      print(network)

    analysis = analyze_channels(networks)

    recommendation = recommend_channel(analysis)
    
    best_score = recommendation["score"]

    if best_score < 20:
        network_health = "Excellent"
    elif best_score < 50:
        network_health = "Good"
    else:
        network_health = "Poor"

    recommendation_reason = (
        f"Channel {recommendation['recommended_channel']} "
        f"has the lowest congestion and interference score."
    )

    return render_template(
        "dashboard.html",
        networks=networks,
        analysis=analysis,
        recommendation=recommendation,
        network_health=network_health,
        recommendation_reason=recommendation_reason,
    )


if __name__ == "__main__":
    app.run(debug=True)