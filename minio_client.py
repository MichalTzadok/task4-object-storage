from minio import Minio
from minio.versioningconfig import VersioningConfig
import random, string, io

client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="admin123",
    secure=False
)

bucket_name = "mybucket"

client.set_bucket_versioning(bucket_name, VersioningConfig(status="Enabled"))

def random_string(n=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

object_name = random_string() + ".txt"

# ---------- 1. Create or update object (new version is created) ----------
data = random_string(50).encode('utf-8')
data_stream = io.BytesIO(data)
client.put_object(bucket_name, object_name, data_stream, len(data))
print(f"Created/Updated object: {object_name}")

# ---------- 2. List all objects in the bucket ----------
print("\nObjects in bucket:")
for obj in client.list_objects(bucket_name):
    print(obj.object_name)

# ---------- 3. Read object data ----------
resp = client.get_object(bucket_name, object_name)
print("\nObject data:", resp.read().decode())

# ---------- 4. Update object (creates a new version) ----------
new_data = random_string(30).encode('utf-8')
new_data_stream = io.BytesIO(new_data)
client.put_object(bucket_name, object_name, new_data_stream, len(new_data))
print("\nObject updated (new version created)")

resp = client.get_object(bucket_name, object_name)
print("Object data after update:", resp.read().decode())

# ---------- 5. List all object versions ----------
print("\nObject versions:")
for obj in client.list_objects(bucket_name, prefix=object_name, include_version=True):
    print(f"Object: {obj.object_name}, Version ID: {obj.version_id}, Is Latest: {obj.is_latest}")

# ---------- 6. Delete object ----------
# client.remove_object(bucket_name, object_name)
print("\nObject deleted")
