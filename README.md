# Online Quiz Management System

[![Java SE](https://img.shields.io/badge/Java-JDK%208--26%20SE-orange.svg)](https://www.oracle.com/java/)
[![AIT Pune](https://img.shields.io/badge/Institution-AIT%20Pune-navy.svg)](https://www.aitpune.com/)
[![Course](https://img.shields.io/badge/Course-BIT25434A0X-blue.svg)](#)
[![Evaluation](https://img.shields.io/badge/Evaluation-CIE--2%20(Continuous%20Internal%20Evaluation)-success.svg)](#)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-brightgreen.svg)](https://abhisheksinghapsb-gif.github.io/Online-Quiz-Management-System/)

### 🎓 Continuous Internal Evaluation 2 (CIE-2)
- **Institution:** Army Institute of Technology (AIT), Pune
- **Department:** Department of Information Technology
- **Course:** Skill Development Laboratory using Java (`BIT25434A0X`)
- **Class:** SE IT B
- **Course In-charge / Examiner:** Mrs. Trupti Najan

---

## 👥 Project Team Members

| Roll Number | Full Name | Academic Role / Contribution |
| :---: | :--- | :--- |
| **8108** | **Aditya Yadav** *(Group Leader)* | Project Architecture, Interface Design (`QuizOperations`, `QuizEvaluator`), System Integration |
| **8104** | **Abhishekh Singh** | Domain Model Hierarchy (`Question`, `User`), Runtime Polymorphism, Custom Exception Tree |
| **8134** | **Priyam Raj** | Embedded Web Server (`QuizWebServer`), REST APIs, Client-Side JavaScript Controller & UI |
| **8154** | **Utkarsh Chauhan** | Automated Test Matrix (`run_tests.bat`), Grading Strategies, Validation & Quality Assurance |

---

## 🌐 Shareable Links & Deliverables

- **GitHub Repository:** [https://github.com/abhisheksinghapsb-gif/Online-Quiz-Management-System](https://github.com/abhisheksinghapsb-gif/Online-Quiz-Management-System)
- **Live Interactive Web Application:** [https://abhisheksinghapsb-gif.github.io/Online-Quiz-Management-System/](https://abhisheksinghapsb-gif.github.io/Online-Quiz-Management-System/)
- **CIE-2 Presentation Deck:** [Online_Quiz_Management_System_Presentation.pptx](Online_Quiz_Management_System_Presentation.pptx) (12 custom visual slides with UML architecture diagrams)
- **Formal Project Report:** [docs/CIE2_PROJECT_SUBMISSION_REPORT.md](docs/CIE2_PROJECT_SUBMISSION_REPORT.md)
- **UML & Architecture Diagrams:** [docs/UML_AND_ARCHITECTURE_DIAGRAMS.md](docs/UML_AND_ARCHITECTURE_DIAGRAMS.md)
- **Viva Preparation & Questions Guide:** [docs/VIVA_PREPARATION_AND_ANSWERS.md](docs/VIVA_PREPARATION_AND_ANSWERS.md)
- **Verified Sample Execution Logs:** [docs/SAMPLE_EXECUTION_AND_TEST_CASES.md](docs/SAMPLE_EXECUTION_AND_TEST_CASES.md)

---

## 📌 Executive Summary

The **Online Quiz Management System** is a modular, high-reliability academic assessment platform developed in Java. It directly addresses the critical requirements of **Unit III (Object-Oriented Programming, Interfaces & Polymorphism)** and **Unit IV (Exception Handling & Defensive Programming)** from the Savitribai Phule Pune University (SPPU) / AIT autonomous syllabus.

### Key Technical Pillars
1. **Abstract Classes (Unit III):**
   - `Question`: Base abstract class encapsulating `id`, `marks`, `topic`, `difficulty`, enforcing polymorphic `displayQuestion()` and `checkAnswer(String)`.
   - `User`: Base abstract class with `userId`, `name`, `role`, enforcing abstract `displayDashboard()`.
2. **Interfaces & Strategy Pattern (Unit III):**
   - `QuizOperations`: Defines behavioral contracts for quiz CRUD, search, and attempt audit management.
   - `QuizEvaluator`: Strategy Pattern interface implemented by:
     - `StandardGradingPolicy` (Linear university grading: full marks for correct, 0 penalty for wrong).
     - `NegativeMarkingGradingPolicy` (Competitive exam grading: 25% negative marking deduction for wrong answers).
3. **Polymorphism (Unit III):**
   - **Runtime Polymorphism (Dynamic Method Dispatch):** `MultipleChoiceQuestion`, `TrueFalseQuestion`, and `NumericQuestion` polymorphically rendered and validated through `Question` references.
   - **Compile-Time Polymorphism (Method Overloading):** Overloaded `searchQuiz(String topic)` and `searchQuiz(String topic, DifficultyLevel level)` in `QuizManager`.
4. **5-Tier Custom Checked Exception Hierarchy (Unit IV):**
   - Root: `QuizException` (extends `java.lang.Exception`)
   - `QuizNotFoundException`: Thrown on invalid quiz lookup.
   - `DuplicateQuizException`: Thrown on duplicate quiz registration.
   - `InvalidQuestionException`: Thrown on domain rule violations (e.g. negative marks, duplicate question ID).
   - `InvalidOptionException`: Thrown when user inputs illegal choices (e.g. typing 'Z' on MCQ), prompting graceful recovery without crashing.
   - `EmptyQuizException`: Thrown when attempting to launch a quiz containing 0 questions.

---

## 📚 Multi-Age Quiz Repositories (9 Built-in Quizzes)

The system features 9 realistic, pre-loaded quizzes organized across 4 target age demographics:

| Target Age Tier | Quiz ID | Quiz Title | Topic & Question Archetypes | Marks |
| :--- | :--- | :--- | :--- | :---: |
| **Kids (8–12 Yrs)** | `KIDS-SCI` | **Junior Science & Space Quest** | Planets, geology, photosynthesis (T/F), Moon light (T/F), solar system count (Numeric) | 25 |
| **Kids (8–12 Yrs)** | `KIDS-MATH` | **Junior Math & Brain Riddles** | Geometry shapes, speed multiplication, triangle right angles (T/F), dozen eggs (Numeric) | 20 |
| **Teens (13–17 Yrs)** | `TEEN-CODE` | **Teen Coder: Python & Logic Basics** | Console output, operator precedence, naming rules (T/F), while loop (T/F), powers of 2 (Numeric) | 25 |
| **Teens (13–17 Yrs)** | `TEEN-STEM` | **High School STEM: Physics & Tech** | Electric current SI unit, CPU architecture, sound wave velocity (T/F), boiling point (Numeric) | 20 |
| **College (18–22 Yrs)** | `JAVA-OOP` | **OOP, Interfaces & Polymorphism** | Interface implementation, abstract class rules, dynamic dispatch (T/F), functional interfaces | 25 |
| **College (18–22 Yrs)** | `JAVA-EXC` | **Exception Handling in Java** | `finally` block guarantees, custom checked exceptions, catch hierarchy (T/F), int byte size | 20 |
| **College (18–22 Yrs)** | `JAVA-GEN` | **Java Collections & Core Concepts** | `HashMap` key uniqueness, `ArrayList` ordering & duplicates (T/F) | 10 |
| **Competitive / Pro (20+)** | `PRO-APT` | **Aptitude & Logical Deduction** | Train platform speed math, sequence progression, formal logic (T/F), polygon angles | 20 |
| **Competitive / Pro (20+)** | `PRO-SE` | **Software Architecture, SOLID & Git** | Liskov substitution, `git checkout -b`, Open/Closed principle (T/F), HTTP status codes | 20 |

---

## 🚀 Execution & Quick Start Guide

### Prerequisites
- **Java SE Development Kit (JDK):** Version 8 or higher (Fully verified on Java 26 SE).
- **Operating System:** Windows, Linux, or macOS.

### 1. Compile the Java Source Code
- **On Windows (1-Click Batch):**
  ```cmd
  compile.bat
  ```
- **Via Standard Command Line:**
  ```bash
  javac -d bin src/com/ait/quiz/exception/*.java src/com/ait/quiz/model/*.java src/com/ait/quiz/service/*.java src/com/ait/quiz/util/*.java src/com/ait/quiz/main/*.java src/com/ait/quiz/web/*.java
  ```

### 2. Launch the Application

#### Option A: Interactive Web Browser Portal (Recommended)
Double-click **`run_web.bat`** (or execute `java -cp bin com.ait.quiz.web.QuizWebServer`) and navigate to:
```
http://localhost:8080
```
- Multi-age category filtering (`Kids`, `Teens`, `College`, `Competitive / Pro`).
- Live 10-minute quiz countdown timer with automatic submission.
- Real-time scoring under Standard Linear or Competitive 25% negative marking.
- Faculty assessment portal for creating quizzes and appending questions.
- Built-in Java Concept Defense Inspector and automated viva test runner.

#### Option B: Terminal Console CLI
Double-click **`run.bat`** (or execute `java -cp bin com.ait.quiz.main.QuizApplication`).
- Interactive student & faculty dashboards with formatted ASCII table views.
- Try entering illegal choices like `'Z'` on question 1 to witness defensive exception catching without fatal crashes.

#### Option C: Automated 60-Second CIE-2 Viva Test Suite
Double-click **`run_tests.bat`**.
- Automatically runs a comprehensive test matrix proving abstract classes, dynamic dispatch, interface strategy swapping, method overloading, and triggers all 5 custom exceptions with `try-catch-finally` traces.

---

## 📂 Repository Directory Layout

```
├── .gitignore                                   # Standard Java, IDE & cache exclusions
├── index.html                                   # Root redirect for GitHub Pages deployment
├── compile.bat                                  # Batch script to compile Java code into bin/
├── run.bat                                      # Batch script to launch Terminal CLI
├── run_web.bat                                  # Batch script to launch embedded Web Server
├── run_tests.bat                                # Batch script for automated viva demonstration
├── build_sih_deck.py                            # Python script that generates the 12-slide PPTX
├── Online_Quiz_Management_System_Presentation.pptx # 12-Slide formal CIE-2 presentation
├── README.md                                    # Main project documentation & guide
│
├── bin/                                         # Compiled bytecode (.class) [Ignored in git]
│
├── ppt_assets/                                  # High-resolution generated presentation graphics
│   ├── ait_badge.jpg                            # AIT Pune Department of IT crest
│   ├── java_abstract_classes.jpg                # UML class hierarchy diagram
│   ├── java_strategy_pattern.jpg                # QuizEvaluator Strategy Pattern diagram
│   ├── java_polymorphism.jpg                    # Dynamic method dispatch workflow
│   ├── java_exception_tree.jpg                  # Custom exception hierarchy tree
│   ├── quiz_core_innovation.jpg                 # System innovation shield graphic
│   ├── quiz_process_workflow.jpg                # 5-step processing pipeline infographic
│   ├── quiz_benefits_wheel.jpg                  # Operational benefits wheel
│   └── quiz_tech_brain.jpg                      # Digital assessment brain graphic
│
├── docs/                                        # Formal CIE-2 submission reports
│   ├── CIE2_PROJECT_SUBMISSION_REPORT.md        # Comprehensive formal submission document
│   ├── UML_AND_ARCHITECTURE_DIAGRAMS.md         # Mermaid & ASCII architectural diagrams
│   ├── VIVA_PREPARATION_AND_ANSWERS.md          # 20+ viva preparation Q&A guide
│   └── SAMPLE_EXECUTION_AND_TEST_CASES.md       # Verified test executions & exception traces
│
├── src/                                         # Java Core Source Code
│   └── com/ait/quiz/
│       ├── exception/                           # Unit IV: Custom 5-tier Exception Hierarchy
│       ├── model/                               # Unit III: Abstract Classes & Question Models
│       ├── service/                             # Unit III: Interfaces, Strategy Policies & Repository
│       ├── util/                                # Input Validation & Console Formatting
│       ├── main/                                # Application Entry Point & Viva Test Harness
│       └── web/                                 # Embedded Lightweight Java HttpServer
│
└── web/                                         # Modern Web Application Frontend
    ├── index.html                               # Responsive Glassmorphism Web Interface
    ├── style.css                                # Design System (AIT Brand Colors & Dark/Light Badges)
    └── app.js                                   # Dual-Mode Client & REST API Controller
```

---

## 🏆 CIE-2 Rubric Evaluation Alignment

| Evaluation Rubric Criterion (Marks) | Requirements Checked | Project Implementation Details |
| :--- | :--- | :--- |
| **Problem Understanding (2 Marks)** | Clarity, scope & educational relevance | Defined in [CIE2_PROJECT_SUBMISSION_REPORT.md](docs/CIE2_PROJECT_SUBMISSION_REPORT.md), eliminating paper exam grading latency and human scoring errors. |
| **Use of Java Concepts (6 Marks)** | Unit III & IV syllabus compliance | Strategy Pattern (`QuizEvaluator`), abstract `Question` & `User`, custom checked exceptions, method overloading, dynamic dispatch. |
| **Program Implementation (4 Marks)** | Correctness, logic, output formatting | Clean compilation, 9 pre-loaded multi-age quizzes, defensive input validation, zero crash guarantee. |
| **Demonstration (2 Marks)** | Live working application & clarity | Automated demonstration suite (`run_tests.bat`) and modern browser UI (`run_web.bat`). |
| **Individual Viva (4 Marks)** | Conceptual depth & student contribution | Prepared viva answers for each team member in [VIVA_PREPARATION_AND_ANSWERS.md](docs/VIVA_PREPARATION_AND_ANSWERS.md). |
| **Code Quality & Documentation (2 Marks)** | Clean structure, readability, diagrams | Strict package separation, Javadoc documentation, UML diagrams in [UML_AND_ARCHITECTURE_DIAGRAMS.md](docs/UML_AND_ARCHITECTURE_DIAGRAMS.md). |

---

## 📄 License & Academic Attribution
Developed for the **Skill Development Laboratory using Java (BIT25434A0X)** at **Army Institute of Technology (AIT), Pune**.  
Academic Year 2026. All rights reserved by team members **Aditya Yadav, Abhishekh Singh, Priyam Raj, and Utkarsh Chauhan**.
