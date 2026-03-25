- commands
```bash
    uvicorn main:app --reload
```
# Bank Application Project
1. Objective
Build a simple banking system where users can:
- Create an account
- View account details
- Deposit money
- Withdraw money
- View transaction history

# 2. Tech Stack
 Backend: Python/FASTAPI, REST API, CRUD
 Frontend: React with basic HTML, CSS, JavaScript
 Database: MongoDB
 Tools: VS Code, Postman, Swagger

# . High-Level Architecture
Frontend (UI) Routes REST API Controller Model Database→ → → →

# 4. Database Design ✓
4.1 Collections
USERS Collection
{
"_id": ObjectId(), // MongoDB unique ID, replaces user_id
"name": "John Doe",
"email": "john@example.com",
"created_at": "2026-03-23T18:00:00Z"
}
ACCOUNTS Collection
{
"_id": ObjectId(), // replaces account_id
"user_id": ObjectId("..."), // reference to USERS._id
"balance": 0.00,
"account_type": "Checking",
"created_at": "2026-03-23T18:00:00Z"
}

TRANSACTIONS Collection
{
"_id": ObjectId(), // replaces txn_id
"account_id": ObjectId("..."), // reference to ACCOUNTS._id
"txn_type": "deposit", // or "withdrawal"
"amount": 100.50,
"created_at": "2026-03-23T18:05:00Z"
}


# 5. Backend Design (MVC)
### 5.1 Model (Entities)
✓ User
✓ Account
✓ Transaction

### 5.2 Controller Layer (Business Logic)
AccountController Methods:
 createAccount(userId, accountType)
 getAccount(accountId)
 deposit(accountId, amount)
 withdraw(accountId, amount)
 getTransactions(accountId)

### 5.4 Router (REST APIs)
Create Account
POST /api/accounts
{
"userId": 1,
"accountType": "SAVINGS"
}
Get Account Details
GET /api/accounts/{id}
Deposit Money
POST /api/accounts/{id}/deposit
{
"amount": 500
}
Withdraw Money
POST /api/accounts/{id}/withdraw
{
"amount": 200
}

Transaction History
GET /api/accounts/{id}/transactions

# 6. Additionally
 Add User registration & login
 Password hashing
 JWT token generation
 Protected routes
 Admin vs user roles
 Add transfer between accounts
 Add pagination for transactions
 Add validation messages on UI
### 6.1. Business Rules
 Cannot withdraw more than balance
 Deposit amount must be positive