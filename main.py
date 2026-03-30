from trend import get_trend
from ai import analyze_trend, generate_campaign

def run():
    trend_data = get_trend()
    insight = analyze_trend(trend_data)
    campaign = generate_campaign(insight)

    with open("output.txt", "w") as f:
        f.write(campaign)

if __name__ == "__main__":
    run()
