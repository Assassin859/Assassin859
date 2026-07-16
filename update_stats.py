import re
import urllib.request
import json
import os

def fetch_github_stats(username):
    # Fetch user profile data
    user_url = f"https://api.github.com/users/{username}"
    req = urllib.request.Request(user_url, headers={"User-Agent": "Mozilla/5.0"})
    
    # Try using GITHUB_TOKEN if available to avoid rate limits
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"token {token}")
        
    try:
        with urllib.request.urlopen(req) as response:
            user_data = json.loads(response.read().decode())
            
        # Fetch repos to count stars
        repos_url = f"https://api.github.com/users/{username}/repos?per_page=100"
        req_repos = urllib.request.Request(repos_url, headers={"User-Agent": "Mozilla/5.0"})
        if token:
            req_repos.add_header("Authorization", f"token {token}")
            
        with urllib.request.urlopen(req_repos) as response_repos:
            repos_data = json.loads(response_repos.read().decode())
            
        stars = sum(repo.get("stargazers_count", 0) for repo in repos_data)
        repos_count = user_data.get("public_repos", 0)
        followers = user_data.get("followers", 0)
        
        # Calculate dynamic Web3 metrics
        # Balance = (repos * 100) + (stars * 50) + followers
        wei_balance = (repos_count * 100) + (stars * 50) + followers
        usd_value = float(wei_balance) * 1.25
        
        return {
            "repos": repos_count,
            "stars": stars,
            "followers": followers,
            "wei_balance": f"{wei_balance:,}",
            "usd_value": f"{usd_value:,.2f}"
        }
    except Exception as e:
        print(f"Error fetching stats: {e}")
        # Fallback values
        return {
            "repos": 12,
            "stars": 5,
            "followers": 15,
            "wei_balance": "4,447",
            "usd_value": "3,312.00"
        }

def update_svgs():
    username = "Assassin859"
    stats = fetch_github_stats(username)
    print(f"Fetched stats: {stats}")
    
    # Update metamask.svg
    metamask_path = "metamask.svg"
    if os.path.exists(metamask_path):
        with open(metamask_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace balance
        content = re.sub(r'<text x="180" y="0" [^>]*>[^<]*</text>', f'<text x="180" y="0" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif" font-size="32" fill="#FFFFFF" font-weight="bold" text-anchor="middle">{stats["wei_balance"]} WEI</text>', content)
        # Replace USD value
        content = re.sub(r'<text x="180" y="20" [^>]*>[^<]*</text>', f'<text x="180" y="20" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif" font-size="13" fill="#94A3B8" text-anchor="middle">${stats["usd_value"]} USD (OS Commits)</text>', content)
        
        with open(metamask_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated metamask.svg successfully.")

if __name__ == "__main__":
    update_svgs()
