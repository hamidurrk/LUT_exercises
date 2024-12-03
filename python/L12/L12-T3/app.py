from flask import Flask, render_template
import requests

app = Flask(__name__)


def fetch_spacex_data():
    # TODO: 1. Fetch data from SpaceX API

    # TODO: 2. Filter out the missions where we have crew included
    crewed_missions = []
    return crewed_missions


@app.route("/")
def index():
    launches = fetch_spacex_data()
    return render_template("index.html", launches=launches)


@app.route("/mission/<mission_id>")
def mission(mission_id):
    # TODO: 1. Implement fetching the missions from v5/launches

    # TODO: 2. Implement finding the mission by its ID
    # Find the mission by its ID
    mission_details = None

    if not mission_details:
        return f"Mission with ID {mission_id} not found.", 404

    return render_template("mission.html", mission=mission_details)


@app.route("/crew/<crew_id>")
def crew(crew_id):
    # TODO: 3. Implement the logic for getting crew member details
    crew_member = None

    if not crew_member:
        return f"Crew member with ID {crew_id} not found.", 404

    return render_template("crew.html", crew=crew_member)


if __name__ == "__main__":
    app.run(debug=True)
