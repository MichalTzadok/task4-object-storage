# Object Storage – Questions & Answers

---

## 1. Differences Between Object Storage and Other Distributed Storage Types

1. **NAS (Network Attached Storage)** – Traditional file storage connected to a network.  
   * **Advantage:** Simple to use and share files.  
   * **Disadvantage:** Difficult to scale to very large sizes; not suitable for large cloud deployments.  

2. **HDFS (Hadoop Distributed File System)** – A file system that distributes files across multiple machines and keeps replicas.  
   * **Advantage:** Reliable, suitable for large datasets, maintains replication.  
   * **Disadvantage:** Complex, not optimized for modern cloud infrastructure.  

3. **Object Storage (S3, MinIO)** – Stores "objects" with additional metadata. No fixed folder hierarchy.  
   * **Advantage:** Cloud-friendly, flexible, scalable, supports replication and versioning of objects.  
   * **Disadvantage:** Less intuitive for users accustomed to regular folders on a computer.  

**Conclusion:** Object Storage is the modern solution for cloud storage and large datasets.

---

## 2. What is S3?

1. Amazon’s cloud storage service.  
2. Stores data as objects with additional metadata.  
3. Provides access to data via API, software, or web browser.

---

## 3. What is a Bucket?

1. A "bucket" is a container where S3 objects are stored.  
2. Every file must reside in a bucket.  
3. Think of it as a top-level folder, but it can contain millions of objects.

---

## 4. Do Folders Exist in S3?

1. Not really – there are no actual folders like on a computer.  
2. Folders can be simulated using object names with `/`.  
   * **Example:** `images/photo.jpg` – looks like a folder (`images`), but it’s actually part of the object’s name.

---

## 5. Are There Size Limitations?

1. A single object can be up to **5 TB**.  
2. Regular upload requests are limited to **5 GB**; for larger files, use **Multipart Upload**.  
3. Compared to traditional file systems:  
   * NTFS or ext4 have file size limits (usually 4–16 GB).  
   * Object Storage is virtually unlimited and can store massive amounts of cloud data.

---

## 6. What S3 Implementations Exist?

1. **AWS S3** – Official Amazon service.  
2. **MinIO** – Free, can run locally or in the cloud.  
3. **Ceph Object Gateway** – Distributed object storage system.  
4. **Wasabi, Backblaze B2** – External cloud services supporting S3.  

**Common Uses:** Storing images, videos, backups, documents, analytics data, and more.

---
### Updating an Object (Versioning)
* With versioning **enabled**, each update creates a **new version**; previous versions are preserved.
* Without versioning, updates simply overwrite the object.
* Use `list_objects(..., include_version=True)` to see all versions and their Version IDs.

