# Project Tasks – Object Storage Assignment

*This repository contains the Object Storage assignment task.*  
*The task is implemented using MinIO and Python, following the assignment requirements.*

---

## Table of Contents

* [Object Storage with MinIO](#1-object-storage-with-minio)

---

## 1. Object Storage with MinIO

**Description:**  
*A practical implementation of Object Storage using MinIO, an S3-compatible storage solution.*

**Key Features:**  
* Create a bucket (if it doesn’t exist)  
* Upload objects with random names and data  
* List all objects in a bucket  
* Read object content  
* Update object content (demonstrates versioning)  
* Delete objects  

---

**Technologies Used:**  
* **Docker** – containerization platform  
* **MinIO** – S3-compatible object storage  
* **Python** – client code using the `minio` library  
* **S3 API** – interaction with object storage  

---

## Setup & Usage

### 1. Run MinIO

*Remove any old container and start a new MinIO container:*

```bash
docker rm -f minio                  # Remove old container (if exists)
docker run -p 9000:9000 -p 9001:9001 --name minio \
-e "MINIO_ROOT_USER=admin" -e "MINIO_ROOT_PASSWORD=admin123" \
minio/minio server /data --console-address ":9001"
```

## MinIO UI and Login

* **MinIO UI:** [http://localhost:9001](http://localhost:9001)  
* **Login Credentials:**  
  * User: `admin`  
  * Password: `admin123`

---

## Run Python Client

*Install dependencies and run the script:*

```bash
pip install minio
python minio_client.py
```

The Python client script performs the following operations:

* Upload a random object  
* List all objects  
* Read object content  
* Update object  
* Delete object  

---
### Updating an Object (Versioning)
* With versioning **enabled**, each update creates a **new version**; previous versions are preserved.
* Without versioning, updates simply overwrite the object.
* Use `list_objects(..., include_version=True)` to see all versions and their Version IDs.

---

## Notes

* Object Storage does not use real folders; all paths are defined via **Keys**  
* Updating an object creates a new version if versioning is enabled  
* MinIO is fully compatible with **S3 API**, allowing easy migration to cloud storage  

