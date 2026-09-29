# SAMPLE EXECUTION RUNS & TEST CASE SPECIFICATION
## ONLINE QUIZ MANAGEMENT SYSTEM (CIE-2)
**Department of Information Technology, Army Institute of Technology, Pune**

---

## TEST SUITE OVERVIEW

| Test ID | Category | Objective | Status |
|:-------:|:---------|:----------|:------:|
| **TC-01** | Student Execution | Complete quiz attempt with Standard Linear Grading | **PASS** |
| **TC-02** | Student Execution | Complete quiz attempt with Negative Marking (25% penalty) | **PASS** |
| **TC-03** | Exception Handling | Student enters invalid option `'Z'` on MCQ (Catches `InvalidOptionException`) | **PASS** |
| **TC-04** | Exception Handling | Student inputs non-numeric value for numeric question | **PASS** |
| **TC-05** | Search & Overloading | Topic keyword search (`searchQuiz(String)`) | **PASS** |
| **TC-06** | Search & Overloading | Topic and difficulty search (`searchQuiz(String, DifficultyLevel)`) | **PASS** |
| **TC-07** | Faculty Management | Create new quiz with custom attributes | **PASS** |
| **TC-08** | Exception Handling | Duplicate Quiz ID rejection (`DuplicateQuizException`) | **PASS** |
| **TC-09** | Exception Handling | Non-existent Quiz ID lookup (`QuizNotFoundException`) | **PASS** |
| **TC-10** | Exception Handling | Creation of question with negative marks (`InvalidQuestionException`) | **PASS** |
| **TC-11** | Exception Handling | Conduction of empty quiz (`EmptyQuizException`) | **PASS** |

---

## 1. TEST RUN 1: VALID QUIZ CONDUCTION & STANDARD EVALUATION (TC-01)

### Execution Trace:
```text
================================================================================
                    STUDENT PORTAL - Abhishekh Kumar (3101)
================================================================================
 1. View All Available Quizzes
 2. Search Quizzes by Topic (Method Overloading - 1 param)
 3. Search Quizzes by Topic & Difficulty (Method Overloading - 2 params)
 4. Take a Quiz (Interactive Conduct & Evaluation)
 5. View My Attempt History & Scorecards
 6. View My Student Dashboard (Polymorphic displayDashboard)
 7. Back to Main Menu
--------------------------------------------------------------------------------
 >> Select Student Action
--------------------------------------------------------------------------------
Enter choice (1-7): 4

--------------------------------------------------------------------------------
 >> LIST OF AVAILABLE QUIZZES
--------------------------------------------------------------------------------
Quiz ID      | Title                            | Topic                  | Level    | Que    | Total Marks
--------------------------------------------------------------------------------
JAVA-OOP     | OOP, Interfaces & Polymorphism   | Object-Oriented Pro... | Medium   | 5      | 25 marks
JAVA-EXC     | Exception Handling in Java       | Exception Handling     | Hard     | 4      | 20 marks
JAVA-GEN     | Java Collections & Core Concepts | Collections Framework  | Easy     | 2      | 10 marks

Enter Quiz ID to attempt: JAVA-OOP

--------------------------------------------------------------------------------
 >> SELECT EVALUATION POLICY FOR THIS QUIZ ATTEMPT
--------------------------------------------------------------------------------
 1. Standard Linear Grading (Full marks for correct, zero penalty for wrong)
 2. Competitive Exam Grading (25% negative marking penalty for wrong answers)
Select grading policy (1-2): 1
 [INFO] Selected Evaluator Strategy: Standard Linear Evaluation (No Negative Marking)

================================================================================
          STARTING QUIZ: OOP, Interfaces & Polymorphism (Attempt ID: ATT-142608)
================================================================================
Read each question carefully. Type your answer and press Enter.

--------------------------------------------------------------------------------
[Q1] [Multiple Choice (MCQ) | Easy | Marks: 5]
Topic: Interfaces
Prompt: Which Java keyword is used to implement an interface in a class?
   [A] extends
   [B] implements
   [C] inherits
   [D] interface
   (Enter choice A-D)
>> Your Answer: B
   [✓] Recorded.
--------------------------------------------------------------------------------
[Q2] [Multiple Choice (MCQ) | Medium | Marks: 5]
Topic: Abstract Classes
Prompt: Which of the following statements about an abstract class in Java is TRUE?
   [A] An abstract class can be instantiated directly using 'new'
   [B] An abstract class can contain both abstract methods and concrete methods
   [C] An abstract class cannot contain constructors
   [D] All methods in an abstract class must be abstract
   (Enter choice A-D)
>> Your Answer: B
   [✓] Recorded.
--------------------------------------------------------------------------------
[Q3] [True / False | Easy | Marks: 5]
Topic: Polymorphism
Prompt: In Java, method overloading is resolved at compile time, whereas method overriding is resolved at runtime (dynamic method dispatch).
   [T] True
   [F] False
   (Enter choice T or F)
>> Your Answer: T
   [✓] Recorded.
--------------------------------------------------------------------------------
[Q4] [True / False | Medium | Marks: 5]
Topic: Multiple Inheritance
Prompt: A class in Java can implement multiple interfaces and simultaneously extend multiple concrete classes.
   [T] True
   [F] False
   (Enter choice T or F)
>> Your Answer: F
   [✓] Recorded.
--------------------------------------------------------------------------------
[Q5] [Numeric / Direct Answer | Easy | Marks: 5]
Topic: Interfaces
Prompt: In Java SE 8 and above, what is the minimum number of abstract methods a Functional Interface must have?
   (Enter exact numeric answer)
>> Your Answer: 1
   [✓] Recorded.

================================================================================
                         DETAILED QUIZ PERFORMANCE REPORT                       
================================================================================
Attempt ID   : ATT-142608
Student Name : Abhishekh Kumar (Roll No: 3101)
Quiz Title   : OOP, Interfaces & Polymorphism (ID: JAVA-OOP)
Grading Rule : Standard Linear Evaluation (No Negative Marking)
Date & Time  : 27-Sept-2026 11:34:55
--------------------------------------------------------------------------------
Total Questions: 5 | Correct: 5 | Incorrect: 0
Final Score    : 25.00 / 25 marks
Percentage     : 100.00%
Awarded Grade  : O (Outstanding)
--------------------------------------------------------------------------------
QUESTION BREAKDOWN:
  1. [PASS / CORRECT] Which Java keyword is used to implement an interface in a class?
     Your Answer   : B
     Correct Answer: [B] implements
     Marks Earned  : 5.00
  2. [PASS / CORRECT] Which of the following statements about an abstract class in Java is TRUE?
     Your Answer   : B
     Correct Answer: [B] An abstract class can contain both abstract methods and concrete methods
     Marks Earned  : 5.00
  3. [PASS / CORRECT] In Java, method overloading is resolved at compile time, whereas method overriding is resolved at runtime (dynamic method dispatch).
     Your Answer   : T
     Correct Answer: True
     Marks Earned  : 5.00
  4. [PASS / CORRECT] A class in Java can implement multiple interfaces and simultaneously extend multiple concrete classes.
     Your Answer   : F
     Correct Answer: False
     Marks Earned  : 5.00
  5. [PASS / CORRECT] In Java SE 8 and above, what is the minimum number of abstract methods a Functional Interface must have?
     Your Answer   : 1
     Correct Answer: 1
     Marks Earned  : 5.00
================================================================================
```

---

## 2. TEST RUN 2: INVALID INPUT EXCEPTION HANDLING & RECOVERY (TC-03 & TC-04)

### Execution Trace:
```text
--------------------------------------------------------------------------------
[Q1] [Multiple Choice (MCQ) | Easy | Marks: 5]
Topic: Interfaces
Prompt: Which Java keyword is used to implement an interface in a class?
   [A] extends
   [B] implements
   [C] inherits
   [D] interface
   (Enter choice A-D)
>> Your Answer: Z
 [ERROR] Invalid option selected: 'Z'. Expected format/range: [A to D]
   Please re-enter your answer conforming to the format.
>> Your Answer: 99
 [ERROR] Invalid option selected: '99'. Expected format/range: [Single character A to D]
   Please re-enter your answer conforming to the format.
>> Your Answer: B
   [✓] Recorded.
```
> **Examiner Note:** The application does **NOT** crash. It catches `InvalidOptionException`, explains the expected format, and gracefully re-prompts the student.

---

## 3. TEST RUN 3: NEGATIVE MARKING EVALUATION (TC-02)

### Execution Trace:
```text
--------------------------------------------------------------------------------
 >> SELECT EVALUATION POLICY FOR THIS QUIZ ATTEMPT
--------------------------------------------------------------------------------
 1. Standard Linear Grading (Full marks for correct, zero penalty for wrong)
 2. Competitive Exam Grading (25% negative marking penalty for wrong answers)
Select grading policy (1-2): 2
 [INFO] Selected Evaluator Strategy: Competitive Evaluation (25% Negative Penalty for wrong answers)

================================================================================
                 COMPETITIVE EXAM DETAILED SCORECARD WITH PENALTY               
================================================================================
Attempt ID   : ATT-879A21
Student Name : Abhishekh Kumar (Roll No: 3101)
Quiz Title   : OOP, Interfaces & Polymorphism (ID: JAVA-OOP)
Grading Rule : Competitive Evaluation (25% Negative Penalty for wrong answers)
Date & Time  : 27-Sept-2026 11:35:10
--------------------------------------------------------------------------------
Total Questions : 5
Correct Answers : 4
Wrong Answers   : 1 (-25% marks penalized per wrong answer)
Net Score       : 18.75 / 25 marks
Net Percentage  : 75.00%
Result Status   : A+ (Excellent - Advanced Proficiency)
--------------------------------------------------------------------------------
ITEM-BY-ITEM AUDIT:
  1. [+5.00 marks] Which Java keyword is used to implement an interface in a class?
     Your Answer   : B
     Correct Answer: [B] implements
  2. [+5.00 marks] Which of the following statements about an abstract class in Java is TRUE?
     Your Answer   : B
     Correct Answer: [B] An abstract class can contain both abstract methods and concrete methods
  3. [+5.00 marks] In Java, method overloading is resolved at compile time, whereas method overriding is resolved at runtime (dynamic method dispatch).
     Your Answer   : T
     Correct Answer: True
  4. [-1.25 PENALTY] A class in Java can implement multiple interfaces and simultaneously extend multiple concrete classes.
     Your Answer   : T
     Correct Answer: False
  5. [+5.00 marks] In Java SE 8 and above, what is the minimum number of abstract methods a Functional Interface must have?
     Your Answer   : 1
     Correct Answer: 1
================================================================================
```

---

## 4. TEST RUN 4: AUTOMATED CIE-2 DEMONSTRATION SUITE (TC-05 to TC-11)
When Option 3 is selected from the Main Menu:
```text
================================================================================
              CIE-2 MANDATORY CONCEPTS DEMONSTRATION & TEST SUITE
================================================================================
Target: Army Institute of Technology, Pune | Skill Development Lab
Evaluates Unit III (Polymorphism, Interfaces, Abstract Classes) & Unit IV (Exception Handling)

--------------------------------------------------------------------------------
 >> 1. ABSTRACT CLASS & RUNTIME POLYMORPHISM (Dynamic Method Dispatch)
--------------------------------------------------------------------------------
Base Class: 'Question' (abstract)
Concrete Subclasses: MultipleChoiceQuestion, TrueFalseQuestion, NumericQuestion

Iterating through List<Question> polymorphically:
   Calling q.getQuestionType(): Multiple Choice (MCQ)
   Calling q.displayQuestion():
[Q101] [Multiple Choice (MCQ) | Easy | Marks: 2]
Topic: Geography
Prompt: What is the capital of Maharashtra?
   [A] Pune
   [B] Mumbai
   [C] Nagpur
   [D] Nashik
   (Enter choice A-D)
   Correct Answer: [B] Mumbai

   Calling q.getQuestionType(): True / False
   Calling q.displayQuestion():
[Q102] [True / False | Easy | Marks: 2]
Topic: Java OOP
Prompt: Abstract classes can have constructors in Java.
   [T] True
   [F] False
   (Enter choice T or F)
   Correct Answer: True

   Calling q.getQuestionType(): Numeric / Direct Answer
   Calling q.displayQuestion():
[Q103] [Numeric / Direct Answer | Easy | Marks: 2]
Topic: Architecture
Prompt: How many bits are in a single standard Java byte?
   (Enter exact numeric answer)
   Correct Answer: 8

--------------------------------------------------------------------------------
 >> 2. INTERFACES & STRATEGY POLYMORPHISM (QuizEvaluator)
--------------------------------------------------------------------------------
Interface: QuizEvaluator
Implementations: StandardGradingPolicy vs NegativeMarkingGradingPolicy

   Scenario: 3 Correct (15 marks), 1 Wrong (out of 20 marks)
   [Policy 1] Standard Linear Evaluation (No Negative Marking) -> Final Score: 15.00 / 20.0 | Grade: A (Very Good)
   [Policy 2] Competitive Evaluation (25% Negative Penalty for wrong answers) -> Final Score: 13.75 / 20.0 (15 - 1.25) | Grade: A (Very Good - High Proficiency)

--------------------------------------------------------------------------------
 >> 3. COMPILE-TIME POLYMORPHISM (Method Overloading)
--------------------------------------------------------------------------------
Demonstrating QuizManager.searchQuiz():
   Method 1: searchQuiz(String topic)
      searchQuiz("Java") returned: 2 quizzes.
   Method 2: searchQuiz(String topic, DifficultyLevel level)
      searchQuiz("Java", DifficultyLevel.HARD) returned: 1 quizzes.

--------------------------------------------------------------------------------
 >> 4. EXCEPTION HANDLING TEST MATRIX (try, catch, finally, throw/throws)
--------------------------------------------------------------------------------

[Test A] Triggering QuizNotFoundException for non-existent ID 'GHOST-404':
   [CAUGHT EXPECTED EXCEPTION] Class: QuizNotFoundException
   Message: Quiz not found with ID: 'GHOST-404'. Please check the Quiz ID and try again.
   [FINALLY BLOCK EXECUTED] Cleanup for Test A completed.

[Test B] Triggering DuplicateQuizException by adding existing quiz 'JAVA-OOP':
   [CAUGHT EXPECTED EXCEPTION] Class: DuplicateQuizException
   Message: A quiz with ID 'JAVA-OOP' already exists! Please use a unique identifier.
   [FINALLY BLOCK EXECUTED] Cleanup for Test B completed.

[Test C] Triggering InvalidQuestionException with negative marks (-10):
   [CAUGHT EXPECTED EXCEPTION] Class: InvalidQuestionException
   Message: Question marks must be strictly positive! Provided: -10
   [FINALLY BLOCK EXECUTED] Cleanup for Test C completed.

[Test D] Triggering InvalidOptionException with invalid option 'Z' on MCQ:
   [CAUGHT EXPECTED EXCEPTION] Class: InvalidOptionException
   Message: Invalid option selected: 'Z'. Expected format/range: [A to D]
   [FINALLY BLOCK EXECUTED] Cleanup for Test D completed.

[Test E] Triggering EmptyQuizException by validating an empty quiz:
   [CAUGHT EXPECTED EXCEPTION] Class: EmptyQuizException
   Message: Quiz 'EMPTY-01' contains no questions! Please add questions before conducting.
   [FINALLY BLOCK EXECUTED] Cleanup for Test E completed.

================================================================================
 [SUCCESS] ALL 5 EXCEPTION AND POLYMORPHISM TEST SCENARIOS PASSED WITH FULL SPEC COMPLIANCE!
================================================================================
```
