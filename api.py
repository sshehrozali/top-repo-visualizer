# Program to generate Data visualization for Most starred python projects on Github
# using GitHub API and pygal

# Import libraries
import requests, pygal
from pygal.style import DefaultStyle, NeonStyle

print("-"*100)
print("Program to generate Data Visualization for Top Starred Languages on GitHub")
print("-"*100)

# Keep prompting till valid input
while (True):

    # Ask for language
    ask_lang = input("\nEnter Language (Ex. C, Python, Javascript, etc.):\t")

    # Check for validation, if passed break the loop
    if ask_lang.isalpha() == True:
        break

    # Else, show error
    print("Enter Correct Input!\n")

# Make an API call and store the response.
url = f"https://api.github.com/search/repositories?q=language:{ask_lang}&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code) # Get status code

# Fetch response
response_dict = r.json()

# Print additional information on the screen
print("Total repositories:", response_dict['total_count'])
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# List to store repo names along with star counts, description and HTML URL
names, plot_dicts = [], []

# Store each repo name and stars in list
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    
    # Store each repo stars count, description and HTML URL as bar value, description and clickable link
    plot_dict = {
        "value": repo_dict["stargazers_count"], # Bar's value
        "label": repo_dict["description"] or "", # Bar's description (tooltip)
        "xlink": repo_dict["html_url"] # add clickable link to the bar
    }

    # Store in list
    plot_dicts.append(plot_dict)

# Make visualization
# Generate chart
chart = pygal.StackedLine(x_label_rotation = 90, fill=True, interpolate='cubic', style=DefaultStyle)

chart.title = f"Most Starred {ask_lang.capitalize()} Projects on GitHub" # Generate title for chart
chart.x_labels = names # Make labels for the chart

# Adding bars to the chart
chart.add('', plot_dicts)

# Render chart to .svg format and save in current working directory
chart.render_to_file(f"{ask_lang}_result.svg")  