# ARMY INSTITUTE OF TECHNOLOGY, PUNE
## DEPARTMENT OF INFORMATION TECHNOLOGY
### CONTINUOUS INTERNAL EVALUATION – 2 (CIE–2)
### SKILL DEVELOPMENT LABORATORY USING JAVA (BIT25434A0X)
**Academic Year:** 2026–2027 | **Class:** SE IT (Divisions A & B)  
**Course In-charge / Examiner:** Mrs. Trupti Najan  
**Total Marks:** 20 | **Component:** Group Activity, Demonstration & Individual Viva  

---

## 1. PROJECT TITLE
# ONLINE QUIZ MANAGEMENT SYSTEM

---

## 2. GROUP DETAILS & ALLOCATION SHEET

| Sr. No. | Roll No. | Student Name | Role / Assigned Component | Signature |
|:-------:|:--------:|:-------------|:--------------------------|:---------:|
| 1 | **8108** | **Aditya Yadav** (Group Leader) | Core Architecture, Abstract Base Classes (`Question`, `User`), Aggregation | _________ |
| 2 | **8104** | **Abhishekh Singh** | Specialized Question Archetypes (`MCQ`, `TrueFalse`, `Numeric`), Dynamic Validation | _________ |
| 3 | **8134** | **Priyam Raj** | Interfaces (`QuizOperations`, `QuizEvaluator`), Pluggable Strategy Grading Policies | _________ |
| 4 | **8154** | **Utkarsh Chauhan** | Custom Checked Exception Hierarchy (`QuizException`), Defensive Input, Automated Test Suite | _________ |

**Class:** SE IT B | **Academic Year:** 2026–2027

---

## 3. PROBLEM STATEMENT (1 Short Paragraph)
Educational institutions require automated, reliable, and standardized assessment environments to conduct evaluations, evaluate student responses objectively, and enforce institutional integrity. The **Online Quiz Management System** is a modular Core Java console application that enables faculty to design, administer, and organize multi-format assessments (Multiple Choice, True/False, and Numeric questions) while allowing students to search quizzes by topic and difficulty, undergo time-bounded testing, and receive instant scorecard analytics under interchangeable grading policies (Standard Linear Grading or Negative Marking). Built strictly around **Unit III (Polymorphism, Interfaces, Abstract Classes)** and **Unit IV (Robust Exception Handling)**, the system enforces complete domain validation, zero-crash fault tolerance, and loose coupling between assessment generation and evaluation algorithms.

---

## 4. OBJECTIVES OF THE APPLICATION
1. **Dynamic Question Modeling:** Model diverse question archetypes (Multiple Choice, True/False, Numeric) using an **abstract class** (`Question`) and runtime polymorphism.
2. **Contract-Driven Decoupling:** Decouple quiz lifecycle operations and grading strategies using **interfaces** (`QuizOperations`, `QuizEvaluator`).
3. **Pluggable Evaluation Strategies:** Implement compile-time and runtime **polymorphism** to support interchangeable scoring policies (Standard University Scoring vs. Competitive Exam Negative Marking).
4. **Resilient Domain Validation:** Prevent invalid states, illegal choices, non-numeric entries, and duplicate identifiers through a custom **Exception Hierarchy** (`QuizException`, `QuizNotFoundException`, `DuplicateQuizException`, `InvalidOptionException`, `InvalidQuestionException`, `EmptyQuizException`) with structured `try-catch-finally` handling.
5. **Real-time Feedback & Analytics:** Deliver transparent performance reports, audit trails, letter grades (O, A+, A, B, etc.), and historical performance tracking.

---

## 5. MAPPING OF MANDATORY JAVA CONCEPTS (UNITS III & IV)

| Java Concept | Project Component | Specific Classes & Methods | Practical Purpose / Justification |
|:---|:---|:---|:---|
| **Abstract Class** | Question Archetype Model | `abstract class Question` in `model` | Defines common properties (`id`, `questionText`, `marks`, `topic`, `difficulty`) while forcing specialized subclasses to implement `displayQuestion()`, `checkAnswer()`, and `getCorrectAnswerFormatted()`. Prevents direct instantiation of an undefined question. |
| **Abstract Class** | User Hierarchy | `abstract class User` in `model` | Enforces shared identity (`userId`, `name`, `email`) and declares abstract `displayDashboard()` implemented uniquely by `Student` and `Instructor`. |
| **Interfaces** | Lifecycle Contract | `interface QuizOperations` in `service` | Defines contracts for creating, adding, finding, and removing quizzes without coupling to in-memory, file, or database persistence. |
| **Interfaces** | Grading Strategy Contract | `interface QuizEvaluator` in `service` | Defines common scoring behavior (`evaluateScore`, `generateGrade`, `printDetailedReport`), allowing pluggable evaluation logic. |
| **Runtime Polymorphism (Method Overriding)** | Dynamic Method Dispatch | Subclasses of `Question` (`MultipleChoiceQuestion`, `TrueFalseQuestion`, `NumericQuestion`) | When iterating over `List<Question>`, the JVM dynamically dispatches `displayQuestion()` and `checkAnswer()` according to the runtime type. |
| **Runtime Polymorphism (Interface Strategy)** | Grading Policies | `StandardGradingPolicy` and `NegativeMarkingGradingPolicy` | Both classes implement `QuizEvaluator`. The student selects their preferred mode at runtime, and the system executes the corresponding strategy. |
| **Compile-time Polymorphism (Method Overloading)** | Search & Input Utilities | `QuizOperations.searchQuiz(String topic)` vs `searchQuiz(String topic, DifficultyLevel level)`<br>`InputValidator.readInteger(...)`, `readString(...)` | Provides convenient method overloads for filtering quizzes and reading console inputs. |
| **Custom Exception Hierarchy** | Domain-Specific Error Handling | `QuizException` (Base) -> `QuizNotFoundException`, `DuplicateQuizException`, `InvalidOptionException`, `InvalidQuestionException`, `EmptyQuizException` | Translates raw runtime failures into meaningful domain exceptions, ensuring transparent error handling. |
| **Structured Exception Handling** | Defensive Runtime Protection | `try`, `catch`, `finally`, `throw`, `throws` in `QuizApplication`, `QuizManager`, `InputValidator` | `try` blocks isolate risky user input and domain checks; `catch` handles custom errors without crashing; `finally` guarantees resource release and audit logs; `throw`/`throws` propagate errors up the call stack. |

---

## 6. SYSTEM ARCHITECTURE & COMPONENT OVERVIEW

### Package Hierarchy:
```
com.ait.quiz
├── exception
│   ├── QuizException.java                (Base custom checked exception)
│   ├── QuizNotFoundException.java        (Thrown when Quiz ID is not found)
│   ├── DuplicateQuizException.java       (Thrown on duplicate quiz registration)
│   ├── InvalidQuestionException.java     (Thrown on negative marks or invalid bounds)
│   ├── InvalidOptionException.java       (Thrown on illegal option selection)
│   └── EmptyQuizException.java           (Thrown when attempting empty quiz)
├── model
│   ├── DifficultyLevel.java              (Enum: EASY, MEDIUM, HARD)
│   ├── Question.java                     (Abstract base class)
│   ├── MultipleChoiceQuestion.java       (Concrete Question subclass for MCQs)
│   ├── TrueFalseQuestion.java            (Concrete Question subclass for T/F)
│   ├── NumericQuestion.java              (Concrete Question subclass with tolerance)
│   ├── User.java                         (Abstract base class for system users)
│   ├── Student.java                      (Concrete User subclass with score tracking)
│   ├── Instructor.java                   (Concrete User subclass for faculty actions)
│   ├── Quiz.java                         (Quiz aggregation of Questions)
│   └── QuizAttempt.java                  (Audit record of student performance)
├── service
│   ├── QuizOperations.java               (Interface for CRUD operations)
│   ├── QuizEvaluator.java                (Interface for grading policy strategies)
│   ├── StandardGradingPolicy.java        (Linear scoring implementation)
│   ├── NegativeMarkingGradingPolicy.java (Competitive penalty scoring)
│   └── QuizManager.java                  (Service managing quizzes and attempts)
├── util
│   ├── InputValidator.java               (Overloaded scanner reading utilities)
│   └── ConsoleUI.java                    (ANSI/ASCII box and banner utilities)
└── main
    └── QuizApplication.java             (Menu-driven entry point & automated test suite)
```

---

## 7. FUNCTIONAL REQUIREMENTS & MODULE DESCRIPTION

### Module 1: Student Operations
- **Browse & Search:** View all registered quizzes; search quizzes by topic keyword or by topic + difficulty level (demonstrates compile-time polymorphism).
- **Interactive Quiz Conduction:** Take quizzes question-by-question with dynamic UI prompts.
- **Resilient Input:** Entering illegal options (e.g. 'Z' on MCQ or text in numeric) triggers an `InvalidOptionException` and allows re-entry without terminating the quiz.
- **Scorecard & Detailed Audit:** Instant breakdown of each question, showing chosen answer, correct answer, marks awarded, net percentage, and letter grade.
- **Attempt History:** Persistent in-session history of all past attempts and cumulative average percentage.

### Module 2: Faculty / Instructor Operations
- **Quiz Authoring:** Create new quizzes with custom title, topic, and difficulty. Enforces unique ID validation (`DuplicateQuizException`).
- **Dynamic Question Builder:** Add Multiple Choice Questions (with arbitrary option counts), True/False statements, and Numeric Questions (with floating point tolerance).
- **Quiz Administration:** Inspect questions inside any quiz; delete quizzes safely with `QuizNotFoundException` verification.
- **Student Performance Review:** Overview of all attempts across all students with metrics.

### Module 3: Automated CIE-2 Concept Demonstration Suite
- Non-interactive test harness accessible directly from Option 3 of the main menu.
- Automatically tests and verifies all Unit III and Unit IV concepts in sequence, executing positive tests, negative tests, and printing `try-catch-finally` execution traces.

---

## 8. ONGOING MINI-PROJECT ROADMAP (PHASE 2 & PHASE 3)
In accordance with the CIE-2 guidelines for converting this activity into a continuous project:
- **Phase 1 (Completed for CIE-2):** Core Java prototype demonstrating Abstract classes, Interfaces, Polymorphism, and Exception Handling.
- **Phase 2 (Project Enhancement):** File persistence using Java Serialization (`ObjectInputStream` / `ObjectOutputStream`) or CSV storage; advanced collection filtering using Java Streams.
- **Phase 3 (Full Mini-Project Expansion):** Java Swing / JavaFX Graphical User Interface (GUI), JDBC database integration with MySQL / PostgreSQL, timed questions using multithreading (`Thread` / `ScheduledExecutorService`), and exportable PDF certificates.
