# UML AND ARCHITECTURE DIAGRAMS
## ONLINE QUIZ MANAGEMENT SYSTEM (CIE-2)
**Department of Information Technology, Army Institute of Technology, Pune**

---

## 1. COMPREHENSIVE CLASS DIAGRAM (MERMAID)

```mermaid
classDiagram
    %% Abstract Question Hierarchy
    class Question {
        <<abstract>>
        -int id
        -String questionText
        -int marks
        -String topic
        -DifficultyLevel difficulty
        +displayHeader() void
        +displayQuestion()* void
        +checkAnswer(String studentAnswer)* boolean
        +getCorrectAnswerFormatted()* String
        +getQuestionType()* String
        +getId() int
        +getMarks() int
        +getTopic() String
        +getDifficulty() DifficultyLevel
    }

    class MultipleChoiceQuestion {
        -List~String~ options
        -int correctOptionIndex
        +displayQuestion() void
        +checkAnswer(String studentAnswer) boolean
        +getCorrectAnswerFormatted() String
        +getQuestionType() String
        +getOptions() List~String~
        +getCorrectOptionIndex() int
    }

    class TrueFalseQuestion {
        -boolean correctAnswer
        +displayQuestion() void
        +checkAnswer(String studentAnswer) boolean
        +getCorrectAnswerFormatted() String
        +getQuestionType() String
        +isCorrectAnswer() boolean
    }

    class NumericQuestion {
        -double correctAnswer
        -double tolerance
        +displayQuestion() void
        +checkAnswer(String studentAnswer) boolean
        +getCorrectAnswerFormatted() String
        +getQuestionType() String
        +getCorrectAnswer() double
        +getTolerance() double
    }

    Question <|-- MultipleChoiceQuestion : Extends
    Question <|-- TrueFalseQuestion : Extends
    Question <|-- NumericQuestion : Extends

    %% User Hierarchy
    class User {
        <<abstract>>
        -String userId
        -String name
        -String email
        +displayDashboard()* void
        +getRole()* String
        +getUserId() String
        +getName() String
        +getEmail() String
    }

    class Student {
        -String rollNumber
        -String division
        -List~QuizAttempt~ attempts
        +displayDashboard() void
        +getRole() String
        +addAttempt(QuizAttempt attempt) void
        +getAveragePercentage() double
    }

    class Instructor {
        -String department
        -String designation
        +displayDashboard() void
        +getRole() String
        +getDepartment() String
        +getDesignation() String
    }

    User <|-- Student : Extends
    User <|-- Instructor : Extends

    %% Interfaces and Implementations
    class QuizOperations {
        <<interface>>
        +createQuiz(Quiz quiz) void
        +addQuestionToQuiz(String quizId, Question question) void
        +getQuiz(String quizId) Quiz
        +getAllQuizzes() List~Quiz~
        +searchQuiz(String topic) List~Quiz~
        +searchQuiz(String topic, DifficultyLevel level) List~Quiz~
        +deleteQuiz(String quizId) boolean
        +recordAttempt(QuizAttempt attempt) void
        +getAllAttempts() List~QuizAttempt~
        +getAttemptsByStudent(String rollNumber) List~QuizAttempt~
    }

    class QuizManager {
        -Map~String, Quiz~ quizMap
        -List~QuizAttempt~ attemptHistory
        +createQuiz(Quiz quiz) void
        +addQuestionToQuiz(String quizId, Question question) void
        +getQuiz(String quizId) Quiz
        +getAllQuizzes() List~Quiz~
        +searchQuiz(String topic) List~Quiz~
        +searchQuiz(String topic, DifficultyLevel level) List~Quiz~
        +deleteQuiz(String quizId) boolean
        +recordAttempt(QuizAttempt attempt) void
        +getAllAttempts() List~QuizAttempt~
        +getAttemptsByStudent(String rollNumber) List~QuizAttempt~
    }

    QuizOperations <|.. QuizManager : Implements

    class QuizEvaluator {
        <<interface>>
        +evaluateScore(QuizAttempt attempt) double
        +evaluateScore(double earnedMarks, int incorrectCount, double penalty) double
        +generateGrade(double percentage) String
        +getPolicyName() String
        +printDetailedReport(QuizAttempt attempt) void
    }

    class StandardGradingPolicy {
        +evaluateScore(QuizAttempt attempt) double
        +evaluateScore(double earnedMarks, int incorrectCount, double penalty) double
        +generateGrade(double percentage) String
        +getPolicyName() String
        +printDetailedReport(QuizAttempt attempt) void
    }

    class NegativeMarkingGradingPolicy {
        -double penaltyRate
        +evaluateScore(QuizAttempt attempt) double
        +evaluateScore(double earnedMarks, int incorrectCount, double penalty) double
        +generateGrade(double percentage) String
        +getPolicyName() String
        +printDetailedReport(QuizAttempt attempt) void
    }

    QuizEvaluator <|.. StandardGradingPolicy : Implements
    QuizEvaluator <|.. NegativeMarkingGradingPolicy : Implements

    %% Domain Aggregations
    class Quiz {
        -String quizId
        -String title
        -String description
        -String topic
        -DifficultyLevel difficulty
        -List~Question~ questions
        +addQuestion(Question question) void
        +removeQuestion(int questionId) boolean
        +getTotalMarks() int
        +getQuestionCount() int
        +validateForConduct() void
    }

    class QuizAttempt {
        -String attemptId
        -String quizId
        -String quizTitle
        -String studentRollNumber
        -String studentName
        -double scoreObtained
        -double percentage
        -String grade
        -List~QuestionResult~ questionResults
        +addQuestionResult(QuestionResult res) void
    }

    Quiz "1" o-- "*" Question : Aggregates
    QuizManager "1" *-- "*" Quiz : Contains
    QuizManager "1" *-- "*" QuizAttempt : Stores
    Student "1" *-- "*" QuizAttempt : Tracks
```

---

## 2. EXCEPTION CLASS HIERARCHY

```mermaid
classDiagram
    class Exception {
        <<built-in>>
    }
    class QuizException {
        +QuizException(String message)
    }
    class QuizNotFoundException {
        -String quizId
    }
    class DuplicateQuizException {
        -String quizId
    }
    class InvalidOptionException {
        -String chosenOption
        -String expectedFormat
    }
    class InvalidQuestionException {
    }
    class EmptyQuizException {
        -String quizId
    }

    Exception <|-- QuizException : Extends
    QuizException <|-- QuizNotFoundException : Extends
    QuizException <|-- DuplicateQuizException : Extends
    QuizException <|-- InvalidOptionException : Extends
    QuizException <|-- InvalidQuestionException : Extends
    QuizException <|-- EmptyQuizException : Extends
```

---

## 3. SEQUENCE DIAGRAM: QUIZ ATTEMPT & EVALUATION FLOW

```mermaid
sequenceDiagram
    autonumber
    actor Student
    participant App as QuizApplication
    participant QMgr as QuizManager
    participant Quiz as Quiz
    participant Q as Question (Polymorphic)
    participant Eval as QuizEvaluator (Polymorphic)

    Student->>App: Select "Take Quiz" and enter Quiz ID
    App->>QMgr: getQuiz(quizId)
    alt Quiz does not exist
        QMgr-->>App: throws QuizNotFoundException
        App-->>Student: Display error & re-prompt
    else Quiz exists
        QMgr-->>App: returns Quiz object
        App->>Quiz: validateForConduct()
        alt Quiz is empty
            Quiz-->>App: throws EmptyQuizException
            App-->>Student: Display empty quiz alert
        else Quiz has questions
            Student->>App: Select Grading Strategy (Standard / Negative Marking)
            App->>Eval: Instantiate chosen QuizEvaluator
            loop For each Question in Quiz
                App->>Q: displayQuestion() [Dynamic Dispatch]
                Q-->>Student: Render prompt & options (MCQ / TF / Numeric)
                Student->>App: Input Answer
                App->>Q: checkAnswer(studentAnswer)
                alt Invalid input format
                    Q-->>App: throws InvalidOptionException
                    App-->>Student: Display format error and re-prompt question
                else Valid input
                    Q-->>App: returns boolean (isCorrect)
                end
            end
            App->>Eval: evaluateScore(QuizAttempt) [Strategy Dispatch]
            Eval-->>App: Net Score & Letter Grade
            App->>Eval: printDetailedReport(QuizAttempt)
            Eval-->>Student: Render complete report & audit
            App->>QMgr: recordAttempt(QuizAttempt)
        end
    end
```

---

## 4. ASCII ARCHITECTURE OVERVIEW

```
+-------------------------------------------------------------------------------+
|                             QuizApplication (Main)                            |
+-------------------------------------------------------------------------------+
         |                                                   |
         v                                                   v
+-----------------------+                         +----------------------+
|    <<interface>>      |                         |    <<interface>>     |
|    QuizOperations     |                         |     QuizEvaluator    |
+-----------------------+                         +----------------------+
         ^                                                   ^
         | implements                                        | implements
+-----------------------+                 +--------------------------+-----------------------+
|      QuizManager      |                 |   StandardGradingPolicy  | NegativeMarkingPolicy |
+-----------------------+                 +--------------------------+-----------------------+
         | contains
         v
+-----------------------+
|         Quiz          |
+-----------------------+
         | aggregates
         v
+-------------------------------------------------------------------------------+
|                              Question (Abstract)                              |
+-------------------------------------------------------------------------------+
         ^                                  ^                                   ^
         |                                  |                                   |
+-----------------------+        +-----------------------+        +--------------------------+
| MultipleChoiceQuestion|        |   TrueFalseQuestion   |        |     NumericQuestion      |
+-----------------------+        +-----------------------+        +--------------------------+
```
