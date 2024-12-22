# Homework

---

## **Pre-requisites**

Before running the test, ensure the following are installed and configured:

- **Python 3.10.6**
- **requests**, **Pytest**, **python-dotenv** Python libraries

To install the required Python libraries, use the following command:
```bash
pip install -r requirements.txt
```

---

## **Setup Instructions**

1. Clone this repository.
2. Navigate to the project directory.

---

## **How to Run the Test**

To execute the test, use the following command:
```bash
pytest
```

To debug with requests/responses log:
```bash
pytest --log-cli-level=DEBUG
```
---

## **Test Case**

| Test Case ID | Description | API URL | Expected Status Code | Expected Keys | Additional Validation |
|-|-|-|-|-|-|
| TC01 | Verify API response format. | `/breeds/list/all`, `/breeds/image/random` | 200 | `message`, `status`| N/A                                                        |
| TC02 | Verify API response contains a valid image URL. | `/breeds/image/random`| 200 | `message` | `message` must be a valid image URL. |

### TC01: Verify API response format

1. **Setup**: Initialize the test environment and create a session.
2. **Execution**: 
   - Call the `/breeds/list/all` API.
   - Call the `/breeds/image/random` API.
3. **Validation**:
   - Verify that the status code of the response is 200.
   - Verify that the response contains the keys `message` and `status`.

### TC02: Verify API response contains a valid image URL

1. **Setup**: Initialize the test environment and create a session.
2. **Execution**: 
   - Call the `/breeds/image/random` API.
3. **Validation**:
   - Verify that the status code of the response is 200.
   - Verify that the `message` key in the response contains a valid image URL (ending with `.jpg`, `.jpeg`, or `.png`).

---

## **Framework Structure**

```plaintext
tino_hw_3/
├── apis/                           # API objects for dog.ceo
├── tests/
│   ├── test_dog_ceo.py             # Test case implementation
├── libs/
│   ├── base_session.py             # Handles requests.Session in one place
│   ├── share_function.py           # Utility functions
├── conftest.py                     # Entry point for pytest
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
└── .env                            # Environment configuration files
```

