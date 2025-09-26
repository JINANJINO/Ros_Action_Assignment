# Ros Action Assignment(Make Calculator)
This is the content of the assignment given in the robot operating system practice class.

> **Action File**
- Goal : Two numbers and one string
```CMake
# Goal
int8 num_a
int8 num_b
string op
```
- Result : calculation result
```CMake
# Result
float32 answer
```
- Feedback : loading Count
```CMake
# Feedback
int8 loading_count
```

---

> **Tasks to be performed on the Action Server and Action Client**
- Action Server : When a request comes in, count to 10 and perform the corresponding operation.
```python
for i in range(1, 10):
  # Send Feedback
  time.sleep(1)
# Perform operations
# Send Result
```

- Action Client : output the results(**Verify that the four operators work properly**)

---

> Outcomes achieved

**Plus**
<img width="1415" height="837" alt="Screenshot from 2025-09-26 20-25-42" src="https://github.com/user-attachments/assets/a666cf8a-5a32-48e8-b4bc-a398fe492120" />

**Minus**
<img width="1415" height="837" alt="Screenshot from 2025-09-26 20-27-04" src="https://github.com/user-attachments/assets/4a9e44d4-4e77-4e45-ad38-67369212ba94" />

**Multiplication**
<img width="1415" height="837" alt="Screenshot from 2025-09-26 20-30-22" src="https://github.com/user-attachments/assets/a299bbbe-b699-4db7-b1f9-2b46ecfb2b5f" />

> ⚠️**Note:** ```*``` is recognized as a wildcard, so you must use it in the command line with ```'*'```.

**Divide**
<img width="1415" height="837" alt="Screenshot from 2025-09-26 20-35-34" src="https://github.com/user-attachments/assets/dea9efb0-16d4-4f55-9c40-bff0195ef302" />

---

> **RQT Graph**
<img width="1649" height="848" alt="Screenshot from 2025-09-26 19-53-30" src="https://github.com/user-attachments/assets/65ee9437-ae9d-4648-8744-9b40be79b2c9" />

You can check out the code in ```calculate_server.py``` and ```claculate_client.py``` in my repo.
