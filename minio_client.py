from minio import Minio
import random, string
import io



# Connect to MinIO server

client = Minio(
    "localhost:9000",         
    access_key="admin",      
    secret_key="admin123",    
    secure=False              
)

bucket_name = "mybucket"     


# Function to generate a random string

def random_string(n=10):
    """
    Returns a random string of length n containing letters and digits.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


# 1. Create a new random object

object_name = random_string() + ".txt"   # Random object name with .txt extension
data = random_string(50).encode('utf-8') # Random content as bytes
data_stream = io.BytesIO(data)
client.put_object(bucket_name, object_name, data_stream, len(data)) # Upload object
print(f"Created object: {object_name}")


# 2. List all objects in the bucket
object_name="L4hj66qt4a.txt"

print("Objects in bucket:")
for obj in client.list_objects(bucket_name):
    print(obj.object_name)

# 3. Read data from an existing object

resp = client.get_object(bucket_name, object_name)
print("Object data:", resp.read().decode()) 

# 4. Update an existing object (overwrite)

new_data = random_string(30).encode('utf-8')
new_data_stream = io.BytesIO(new_data)
client.put_object(bucket_name, object_name, new_data_stream, len(new_data))
print("Object updated")

# 5. Delete an existing object

client.remove_object(bucket_name, object_name)
print("Object deleted")
