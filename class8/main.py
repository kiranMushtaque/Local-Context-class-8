import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from connection import config  
import asyncio


# --- 1. BANK ACCOUNT CLASS ---
class BankAccount:
    def __init__(self, account_number, customer_name, account_balance, account_type):
        self.account_number = account_number
        self.customer_name = customer_name
        self.account_balance = account_balance
        self.account_type = account_type

    def __str__(self):
        return f"BankAccount({self.account_number}, {self.customer_name}, {self.account_balance}, {self.account_type})"


# --- 2. STUDENT PROFILE CLASS ---
class StudentProfile:
    def __init__(self, student_id, student_name, current_semester, total_courses):
        self.student_id = student_id
        self.student_name = student_name
        self.current_semester = current_semester
        self.total_courses = total_courses

    def __str__(self):
        return f"StudentProfile({self.student_id}, {self.student_name}, Semester: {self.current_semester}, Courses: {self.total_courses})"


# --- 3. LIBRARY BOOK CLASS ---
class LibraryBook:
    def __init__(self, book_id, book_title, author_name, is_available):
        self.book_id = book_id
        self.book_title = book_title
        self.author_name = author_name
        self.is_available = is_available

    def __str__(self):
        return f"LibraryBook({self.book_id}, {self.book_title}, {self.author_name}, Available: {self.is_available})"


# --- OBJECT CREATION ---
bank_account = BankAccount(
    account_number="ACC-789456",
    customer_name="Fatima Khan",
    account_balance=75500.50,
    account_type="savings"
)

student = StudentProfile(
    student_id="STU-456",
    student_name="Hassan Ahmed",
    current_semester=4,
    total_courses=5
)

library_book = LibraryBook(
    book_id="BOOK-123",
    book_title="Python Programming",
    author_name="John Smith",
    is_available=True
)


# --- PRINT OBJECTS ---
print(bank_account)
print(student)
print(library_book)



async def main():
    response = await config.model_provider.chat.completions.create(
        model=config.model.model,
        messages=[
            {"role": "user", "content": f"Summarize these objects:\n{bank_account}\n{student}\n{library_book}"}
        ]
    )
    print("\nAI Summary:", response.choices[0].message.content) 


if __name__ == "__main__":
    asyncio.run(main())
