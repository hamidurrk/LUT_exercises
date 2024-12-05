from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)
launch_url = "https://api.spacexdata.com/v5/launches/"
crew_url = "https://api.spacexdata.com/v4/crew/"

def fetch_spacex_data():
    data = requests.get(launch_url).json()
    
    crewed_missions = []
    for launch in data:
        if launch["crew"]:
            crewed_missions.append(launch)
    return crewed_missions


@app.route("/")
def index():
    launches = fetch_spacex_data()
    return render_template("index.html", launches=launches)


@app.route("/mission/<mission_id>")
def mission(mission_id):
    url = launch_url + mission_id
    mission_details = requests.get(url).json()

    if not mission_details:
        return f"Mission with ID {mission_id} not found.", 404

    return render_template("mission.html", mission=mission_details)


@app.route("/crew/<crew_id>")
def crew(crew_id):
    role = request.args.get('role')
    url = crew_url + crew_id
    crew_member = requests.get(url).json()
    crew_member["role"] = role
    if crew_member["image"]:
        original_image_url = crew_member["image"]
        tag = original_image_url.split('/')[-1].split('.')[0]
        crew_member["tag"] = tag
    
    if not crew_member:
        return f"Crew member with ID {crew_id} not found.", 404

    return render_template("crew.html", crew=crew_member)


if __name__ == "__main__":
    app.run(debug=True)
