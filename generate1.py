import os
import time
import requests
import streamlit as st

BACKEND_V1_API_URL = "https://public-api.beatoven.ai/api/v1"
BACKEND_API_HEADER_KEY = st.secrets("BEATOVEN_API")


def compose_track(request_data):
    try:
        response = requests.post(
            f"{BACKEND_V1_API_URL}/tracks/compose",
            json=request_data,
            headers={"Authorization": f"Bearer {BACKEND_API_HEADER_KEY}"},
        )
        if response.status_code == 200:
            data = response.json()
            if not data.get("task_id"):
                raise Exception(data)
            return data
        else:
            raise Exception({"error": f"HTTP {response.status_code}: {response.text}"})
    except requests.ConnectionError:
        raise Exception({"error": "Could not connect to beatoven.ai"})
    except Exception as e:
        if isinstance(e, Exception) and hasattr(e, 'args') and isinstance(e.args[0], dict):
            raise e
        raise Exception({"error": "Failed to make a request to beatoven.ai"}) from e


def get_track_status(task_id):
    try:
        response = requests.get(
            f"{BACKEND_V1_API_URL}/tasks/{task_id}",
            headers={"Authorization": f"Bearer {BACKEND_API_HEADER_KEY}"},
        )
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception({"error": "Composition failed"})
    except requests.ConnectionError as e:
        raise Exception({"error": "Could not connect"}) from e
    except Exception as e:
        raise Exception({"error": "Failed to make a request"}) from e


def handle_track_file(track_path: str, track_url: str):
    try:
        response = requests.get(track_url)
        if response.status_code == 200:
            with open(track_path, "wb") as f:
                f.write(response.content)
            return {}
        else:
            raise Exception({"error": f"Failed to download file: HTTP {response.status_code}"})
    except requests.ConnectionError as e:
        raise Exception({"error": "Could not download file"}) from e
    except Exception as e:
        raise Exception(
            {"error": "Failed to make a request to get track file"}
        ) from e


def watch_task_status(task_id, interval=10):
    while True:
        track_status = get_track_status(task_id)
        if "error" in track_status:
            raise Exception(track_status)

        print(f"Task status: {track_status}")
        if track_status.get("status") == "composing":
            time.sleep(interval)
            interval = (interval - 2) if interval > 2 else 2
        elif track_status.get("status") == "failed":
            raise Exception({"error": "task failed"})
        else:
            return track_status


def create_and_compose(text_prompt: str):
    # track_meta = {"prompt": {"text": text_prompt}, "format": "wav"}

    # compose_res = compose_track(track_meta)
    # task_id = compose_res["task_id"]
    # # print(f"Started composition task with ID: {task_id}")

    # generation_meta = watch_task_status(task_id)
    # # print(generation_meta)
    # track_url = generation_meta["meta"]["track_url"]
    # # print("Downloading track file")
    # handle_track_file(os.path.join(os.getcwd(), "composed_track.mp3"), track_url)
    # # print("Composed! you can find your track as `composed_track.mp3`")
    time.sleep(30)  # Simulate processing time
    return True