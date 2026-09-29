# INDIVIDUAL VIVA PREPARATION & CONCEPT DEFENSE GUIDE
## ONLINE QUIZ MANAGEMENT SYSTEM
**Department of Information Technology, Army Institute of Technology, Pune**  
**Course:** Skill Development Laboratory using Java (BIT25434A0X)  
**Examiner:** Mrs. Trupti Najan | **Class:** SE IT | **Assessment:** CIE–2 (4 Marks Viva)

---

## 1. PRIMARY QUESTIONS FROM FACULTY CIE-2 RUBRIC

### Q1: Why did you use an abstract class in your application?
**Model Answer:**  
> "In our system, we created the abstract class `Question`. A quiz contains multiple kinds of questions—Multiple Choice Questions (MCQs), True/False questions, and Numeric questions. All of them share core attributes: an integer `id`, `questionText`, `marks`, `topic`, and `difficultyLevel`, along with common logic like `displayHeader()` and getters/setters.
>
> However, an abstract `Question` itself cannot be asked directly because it has no defined format or answer-checking mechanism. Therefore, we declared abstract methods:
> 1. `abstract void displayQuestion()`
> 2. `abstract boolean checkAnswer(String studentAnswer) throws InvalidOptionException`
> 3. `abstract String getCorrectAnswerFormatted()`
>
> By declaring `Question` as abstract, we enforce a strict contract requiring all specialized subclasses (`MultipleChoiceQuestion`, `TrueFalseQuestion`, `NumericQuestion`) to provide their own concrete display and validation behavior, while preventing illegal instantiation of a generic question (`new Question(...)`). We also applied the same design pattern to `User`, which is extended by `Student` and `Instructor`."

---

### Q2: Where is polymorphism used? Explain with the relevant method/class.
**Model Answer:**  
> "Polymorphism is demonstrated in both of its forms in our project:
>
> 1. **Runtime Polymorphism (Method Overriding & Dynamic Method Dispatch):**
>    - In `QuizApplication.java`, we maintain a `Quiz` containing a `List<Question>`. During quiz execution, we iterate through the list using a base class reference:
>      ```java
>      for (Question q : quiz.getQuestions()) {
>          q.displayQuestion();                      // Dynamic dispatch
>          boolean correct = q.checkAnswer(answer);  // Dynamic dispatch
>      }
>      ```
>      At runtime, the JVM determines whether `q` is an instance of `MultipleChoiceQuestion`, `TrueFalseQuestion`, or `NumericQuestion`, invoking the respective overridden methods without any `if-else` or `instanceof` checks.
>    - **Interface-based Strategy Polymorphism:** The `QuizEvaluator` interface has two distinct implementations: `StandardGradingPolicy` and `NegativeMarkingGradingPolicy`. Based on the student's choice, a `QuizEvaluator` reference is bound to either implementation at runtime, calculating the score using the chosen strategy.
>    - In `User.java`, `displayDashboard()` is overridden by `Student` (showing quiz scores and average) and `Instructor` (showing authoring privileges).
>
> 2. **Compile-time Polymorphism (Method Overloading):**
>    - In `QuizOperations` and `QuizManager`:
>      - `searchQuiz(String topic)` — searches quizzes matching a topic keyword.
>      - `searchQuiz(String topic, DifficultyLevel level)` — searches quizzes matching both topic and difficulty.
>    - In `InputValidator`:
>      - `readInteger(Scanner sc, String prompt)`
>      - `readInteger(Scanner sc, String prompt, int min, int max)`
>    - In `QuizEvaluator`:
>      - `evaluateScore(QuizAttempt attempt)`
>      - `evaluateScore(double earnedMarks, int incorrectCount, double penaltyPerIncorrect)`"

---

### Q3: What is the difference between an interface and an abstract class? Why choose one over the other?
**Model Answer:**  
> "The core differences are:
>
> | Dimension | Abstract Class (`Question`, `User`) | Interface (`QuizOperations`, `QuizEvaluator`) |
> |:---|:---|:---|
> | **Inheritance Type** | Single class inheritance (`extends`) | Multiple interface implementation (`implements`) |
> | **State / Fields** | Can hold instance variables with any access modifier (e.g. `private int marks`) | Only `public static final` constants |
> | **Constructors** | Can define constructors to initialize shared state in subclasses | Cannot have constructors |
> | **Relationship** | Represents an **'IS-A'** relationship (e.g., An MCQ *is a* Question) | Represents a **'CAN-DO'** capability or contract (e.g., A class *can evaluate* a quiz) |
> | **Method Types** | Can contain abstract, concrete, protected, and private methods | Until Java 7 only abstract; Java 8+ added `default` and `static` methods |
>
> **Why we chose both in our project:**
> - We used an **abstract class** for `Question` because all questions share actual state (`id`, `marks`, `topic`, `difficulty`) and require constructor initialization.
> - We used an **interface** for `QuizOperations` and `QuizEvaluator` because they represent pure behavioral contracts without requiring shared internal state. For instance, any grading algorithm or persistence mechanism can implement these interfaces independently."

---

### Q4: Why did you create the `QuizEvaluator` interface?
**Model Answer:**  
> "We created `QuizEvaluator` to apply the **Strategy Design Pattern** and achieve loose coupling between the quiz execution engine and the grading rules.
>
> In university exams, regular internal quizzes use standard linear grading (no penalties). However, competitive exams (like GATE or JEE) enforce negative marking penalties (e.g. 25% or 0.25 marks deduction for wrong answers).
>
> By abstracting scoring behind the `QuizEvaluator` interface, `QuizApplication` does not hardcode grading formulas. It calls `evaluator.evaluateScore(attempt)` and `evaluator.generateGrade(percentage)`. If tomorrow the university introduces relative grading or CGPA-based grading, we simply write a new class `RelativeGradingPolicy implements QuizEvaluator` without touching a single line of existing code. This satisfies the Open/Closed Principle."

---

### Q5: What exceptions can occur in your application and how are they handled?
**Model Answer:**  
> "Our application handles both built-in exceptions and a custom exception hierarchy rooted at `QuizException extends Exception`:
>
> 1. `QuizNotFoundException`: Thrown if a user requests, searches, or attempts to delete a quiz ID that does not exist. Caught by displaying a descriptive warning.
> 2. `DuplicateQuizException`: Thrown if an instructor attempts to create a quiz with an ID that is already registered.
> 3. `InvalidQuestionException`: Thrown during question creation if marks are `<= 0`, question text is empty, or an MCQ has fewer than two options.
> 4. `InvalidOptionException`: Thrown during quiz conduction if a student enters an option outside the allowable bounds (e.g. entering `'Z'` for an MCQ with options A–D, or entering arbitrary text for a numeric question). The system catches this, alerts the student, and re-prompts without terminating or crashing the quiz.
> 5. `EmptyQuizException`: Thrown if a student attempts to take a quiz that has zero questions.
> 6. `NumberFormatException` / `InputMismatchException`: Handled defensively inside `InputValidator` to ensure user typographical errors never crash the console application."

---

### Q6: What is the purpose of `try`, `catch`, and `finally` in your code?
**Model Answer:**  
> "In Java:
> - `try`: Encloses code blocks that may trigger exceptional conditions (e.g. accessing `quizManager.getQuiz(quizId)`, parsing student options, or creating new domain objects).
> - `catch`: Intercepts specific exception objects when they are thrown. We follow best practices by catching specific exceptions (such as `InvalidOptionException` or `QuizNotFoundException`) before general `Exception`, allowing customized recovery actions.
> - `finally`: Executes unconditionally, regardless of whether an exception occurred, was caught, or whether a `return` statement was encountered. In `QuizApplication.main`, the `finally` block ensures graceful resource termination and prints audit log confirmations. In our automated test harness, `finally` prints cleanup and diagnostic verification messages after each test case."

---

### Q7: Which part of the program did you implement? (Guide for each group member)

- **Aditya Yadav (Roll No: 8108 - Group Leader):**
  > "I designed the core system architecture, the abstract base class `Question`, and the `User` class hierarchy. I ensured that common attributes (`marks`, `topic`, `difficulty`) were properly encapsulated with validation constructors throwing `InvalidQuestionException`, and defined the abstract methods (`displayQuestion()`, `checkAnswer()`, `getCorrectAnswerFormatted()`) required for dynamic method dispatch. I also designed the aggregation model where `Quiz` contains polymorphic `Question` objects."

- **Abhishekh Singh (Roll No: 8104):**
  > "I implemented the concrete subclasses: `MultipleChoiceQuestion`, `TrueFalseQuestion`, and `NumericQuestion`. I implemented the specialized validation logic for options, single-character conversion for MCQ inputs, boolean evaluation for True/False, and floating-point tolerance delta comparisons in `NumericQuestion`. I also ensured each question type implements `getQuestionType()` polymorphically."

- **Priyam Raj (Roll No: 8134):**
  > "I designed the `QuizOperations` and `QuizEvaluator` interfaces along with their concrete implementations: `StandardGradingPolicy` and `NegativeMarkingGradingPolicy`. I implemented the Strategy Design Pattern allowing runtime selection between standard linear university grading and competitive exam 25% negative marking, as well as automatic letter grade generation (O, A+, A, B, F)."

- **Utkarsh Chauhan (Roll No: 8154):**
  > "I developed the custom checked exception hierarchy (`QuizException`, `QuizNotFoundException`, `DuplicateQuizException`, `InvalidOptionException`, `InvalidQuestionException`, `EmptyQuizException`) and the defensive `InputValidator` class that prevents console crashes on invalid input. I also developed the automated CIE-2 test harness (`run_tests.bat`) that verifies all 5 exception scenarios with structured `try-catch-finally` traces."

---

### Q8: If one requirement changes, which class/method would you modify and why?
**Model Answer:**  
> "Because our application strictly follows Object-Oriented modular design and loose coupling, changes are isolated:
> - **Scenario A: Add a new question type (e.g. Fill-in-the-Blanks):** We simply create `class FillInBlankQuestion extends Question` and implement `displayQuestion()` and `checkAnswer()`. None of the existing question classes or quiz manager logic need modification.
> - **Scenario B: Introduce a new grading scale (e.g. Letter grades A-F with 50% passing cutoff):** We either update `generateGrade()` in `StandardGradingPolicy` or implement a new `RelativeGradingPolicy implements QuizEvaluator`.
> - **Scenario C: Persist quizzes to a MySQL Database or File:** We create `DatabaseQuizManager implements QuizOperations`. The presentation layer (`QuizApplication`) only depends on the `QuizOperations` interface, so the UI code remains completely untouched!"

---

## 2. ADDITIONAL TECHNICAL VIVA QUESTIONS & ANSWERS

### Q9: Can an abstract class have a constructor? If it cannot be instantiated with `new`, what is the constructor's purpose?
**Answer:**  
> "Yes, abstract classes can—and often do—have constructors. While an abstract class cannot be directly instantiated using `new Question()`, its constructor is invoked by subclass constructors via `super(...)`. In our project, `Question` has a parameterized constructor that validates that `questionText` is non-empty and `marks > 0`. This guarantees that no subclass can ever be created in an invalid state."

### Q10: What is the difference between `throw` and `throws`?
**Answer:**  
> "`throw` is an action keyword used inside a method body to explicitly instantiate and raise an exception object (e.g., `throw new InvalidOptionException(opt, format);`).
>
> `throws` is a clause in a method signature that declares to the compiler and calling methods that this method might propagate one or more checked exceptions (e.g., `public void createQuiz(Quiz quiz) throws DuplicateQuizException`)."

### Q11: Why are your custom exceptions checked exceptions (`extends Exception`) instead of unchecked (`extends RuntimeException`)?
**Answer:**  
> "Checked exceptions represent recoverable domain conditions where the calling code is expected to anticipate and handle the error. For example, when a user enters a nonexistent quiz ID or an invalid question choice, the application should catch `QuizNotFoundException` or `InvalidOptionException` and provide a helpful recovery message or prompt for re-entry. Checked exceptions enforce this contract at compile time."

### Q12: How does Dynamic Method Dispatch work in Java at the JVM level?
**Answer:**  
> "Dynamic Method Dispatch is the mechanism by which a call to an overridden method is resolved at runtime rather than compile time. The JVM utilizes a **virtual method table (vtable)** associated with each class. When a method like `q.displayQuestion()` is executed on a reference of type `Question`, the JVM inspects the actual object header in heap memory, identifies its concrete class (e.g. `MultipleChoiceQuestion`), looks up the method address in that class's vtable, and jumps to the subclass implementation."
