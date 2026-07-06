# YouTube Video Trend Analyzer

videos = [
    ["Music", 500000, 50000],
    ["Gaming", 300000, 30000],
    ["Education", 150000, 15000],
    ["Comedy", 250000, 25000],
    ["Music", 700000, 80000],
    ["Gaming", 450000, 45000],
    ["Comedy", 350000, 40000],
    ["Education", 200000, 22000]
]
categories = {}
 # Calculate category views
  for video in videos:
  category = video[0]
   views = video[1]
    if category not in categories:
    categories[category] = []
  categories[category].append(views)
  print("Average Views by Category:")
for category, views in categories.items():
avg = sum(views) / len(views)
 print(category, ":", avg)
print("\nEngagement Rate:")
for video in videos:
category = video[0]
 views = video[1]
  likes = video[2]
 engagement = (likes / views) * 100
 print(category, "=", round(engagement,2), "%")
# Find best category
best = max(categories, key=lambda x: sum(categories[x]))
print("\nTop Performing Category:", best)



 