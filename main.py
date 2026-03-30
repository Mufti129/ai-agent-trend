import subprocess
from trend import get_trend
from ai import analyze_trend, generate_campaign

def run():
    # Ambil data tren
    trend_data = get_trend()

    # Analisa AI
    insight = analyze_trend(trend_data)

    # Generate campaign
    campaign = generate_campaign(insight)

    # Tampilkan di log GitHub Actions
    print("=== HASIL CAMPAIGN ===")
    print(campaign)

    # Simpan ke file
    with open("output.txt", "w") as f:
        f.write(campaign)

    # Setup git config
    subprocess.run(["git", "config", "--global", "user.email", "action@github.com"])
    subprocess.run(["git", "config", "--global", "user.name", "github-actions"])

    # Tambahkan file output
    subprocess.run(["git", "add", "output.txt"])

    # Commit (biar tidak error kalau tidak ada perubahan)
    subprocess.run(["git", "commit", "-m", "update output"], check=False)

    # Push ke repo
    subprocess.run(["git", "push"], check=False)


if __name__ == "__main__":
    run()
