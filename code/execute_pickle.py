import pickle
from pathlib import Path


# Controlled execution environment: Windows 10 VM used for the lab.
pickle_path = Path(r"C:\Users\vboxuser\Desktop\malicious_model_vm.pkl")
marker_path = Path(r"C:\Users\vboxuser\Desktop\payload_executed.txt")

print("Before unpickling:")
print("Marker exists:", marker_path.exists())

print("\nLoading pickle...")

with pickle_path.open("rb") as f:
    pickle.load(f)

print("\nAfter unpickling:")
print("Marker exists:", marker_path.exists())

if marker_path.exists():
    print("PAYLOAD EXECUTION CONFIRMED")
    print("Marker contents:")
    print(marker_path.read_text())
else:
    print("Payload execution was not observed.")
