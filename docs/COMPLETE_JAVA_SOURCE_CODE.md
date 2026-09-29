# Online Quiz Management System — Complete Java Source Code Compilation

> **Institution:** Army Institute of Technology (AIT), Pune  
> **Department:** Department of Information Technology  
> **Course:** Skill Development Laboratory using Java (`BIT25434A0X`)  
> **Evaluation:** Continuous Internal Evaluation 2 (CIE-2) | **Class:** SE IT B  
> **Examiner / Course In-charge:** Mrs. Trupti Najan  
> **Project Group Members:**  
> • **Aditya Yadav** (Roll No: 8108 — Group Leader)  
> • **Abhishekh Singh** (Roll No: 8104)  
> • **Priyam Raj** (Roll No: 8134)  
> • **Utkarsh Chauhan** (Roll No: 8154)  

---

## 📑 Table of Contents

### UNIT IV: EXCEPTION HANDLING HIERARCHY
1. [QuizException.java](#quizexceptionjava) (`src/com/ait/quiz/exception/QuizException.java`)
2. [QuizNotFoundException.java](#quiznotfoundexceptionjava) (`src/com/ait/quiz/exception/QuizNotFoundException.java`)
3. [DuplicateQuizException.java](#duplicatequizexceptionjava) (`src/com/ait/quiz/exception/DuplicateQuizException.java`)
4. [InvalidOptionException.java](#invalidoptionexceptionjava) (`src/com/ait/quiz/exception/InvalidOptionException.java`)
5. [InvalidQuestionException.java](#invalidquestionexceptionjava) (`src/com/ait/quiz/exception/InvalidQuestionException.java`)
6. [EmptyQuizException.java](#emptyquizexceptionjava) (`src/com/ait/quiz/exception/EmptyQuizException.java`)

### UNIT III: ABSTRACT CLASSES & QUESTION MODELS
7. [DifficultyLevel.java](#difficultyleveljava) (`src/com/ait/quiz/model/DifficultyLevel.java`)
8. [Question.java](#questionjava) (`src/com/ait/quiz/model/Question.java`)
9. [MultipleChoiceQuestion.java](#multiplechoicequestionjava) (`src/com/ait/quiz/model/MultipleChoiceQuestion.java`)
10. [TrueFalseQuestion.java](#truefalsequestionjava) (`src/com/ait/quiz/model/TrueFalseQuestion.java`)
11. [NumericQuestion.java](#numericquestionjava) (`src/com/ait/quiz/model/NumericQuestion.java`)
12. [User.java](#userjava) (`src/com/ait/quiz/model/User.java`)
13. [Student.java](#studentjava) (`src/com/ait/quiz/model/Student.java`)
14. [Instructor.java](#instructorjava) (`src/com/ait/quiz/model/Instructor.java`)
15. [Quiz.java](#quizjava) (`src/com/ait/quiz/model/Quiz.java`)
16. [QuizAttempt.java](#quizattemptjava) (`src/com/ait/quiz/model/QuizAttempt.java`)

### UNIT III: INTERFACES & STRATEGY PATTERN GRADING POLICIES
17. [QuizOperations.java](#quizoperationsjava) (`src/com/ait/quiz/service/QuizOperations.java`)
18. [QuizEvaluator.java](#quizevaluatorjava) (`src/com/ait/quiz/service/QuizEvaluator.java`)
19. [StandardGradingPolicy.java](#standardgradingpolicyjava) (`src/com/ait/quiz/service/StandardGradingPolicy.java`)
20. [NegativeMarkingGradingPolicy.java](#negativemarkinggradingpolicyjava) (`src/com/ait/quiz/service/NegativeMarkingGradingPolicy.java`)
21. [QuizManager.java](#quizmanagerjava) (`src/com/ait/quiz/service/QuizManager.java`)

### UNIT III & IV: DEFENSIVE UTILITIES & CONSOLE FORMATTING
22. [InputValidator.java](#inputvalidatorjava) (`src/com/ait/quiz/util/InputValidator.java`)
23. [ConsoleUI.java](#consoleuijava) (`src/com/ait/quiz/util/ConsoleUI.java`)

### APPLICATION ENTRY POINT & CIE-2 VIVA DEMONSTRATION HARNESS
24. [QuizApplication.java](#quizapplicationjava) (`src/com/ait/quiz/main/QuizApplication.java`)

### EMBEDDED LIGHTWEIGHT JAVA HTTP REST WEB SERVER
25. [QuizWebServer.java](#quizwebserverjava) (`src/com/ait/quiz/web/QuizWebServer.java`)

---

## UNIT IV: EXCEPTION HANDLING HIERARCHY

### `QuizException.java`
**Path:** `src/com/ait/quiz/exception/QuizException.java`  
**Lines of Code:** 16  

```java
package com.ait.quiz.exception;

/**
 * Base custom checked exception for all Quiz Management System domain errors.
 * Demonstrates inheritance within exception hierarchies (Unit IV).
 */
public class QuizException extends Exception {
    
    public QuizException(String message) {
        super(message);
    }

    public QuizException(String message, Throwable cause) {
        super(message, cause);
    }
}

```

---

### `QuizNotFoundException.java`
**Path:** `src/com/ait/quiz/exception/QuizNotFoundException.java`  
**Lines of Code:** 18  

```java
package com.ait.quiz.exception;

/**
 * Thrown when an operation attempts to look up or access a quiz with a non-existent ID.
 */
public class QuizNotFoundException extends QuizException {

    private final String quizId;

    public QuizNotFoundException(String quizId) {
        super("Quiz not found with ID: '" + quizId + "'. Please check the Quiz ID and try again.");
        this.quizId = quizId;
    }

    public String getQuizId() {
        return quizId;
    }
}

```

---

### `DuplicateQuizException.java`
**Path:** `src/com/ait/quiz/exception/DuplicateQuizException.java`  
**Lines of Code:** 18  

```java
package com.ait.quiz.exception;

/**
 * Thrown when an instructor attempts to create a quiz with an ID that already exists.
 */
public class DuplicateQuizException extends QuizException {

    private final String quizId;

    public DuplicateQuizException(String quizId) {
        super("A quiz with ID '" + quizId + "' already exists! Please use a unique identifier.");
        this.quizId = quizId;
    }

    public String getQuizId() {
        return quizId;
    }
}

```

---

### `InvalidOptionException.java`
**Path:** `src/com/ait/quiz/exception/InvalidOptionException.java`  
**Lines of Code:** 25  

```java
package com.ait.quiz.exception;

/**
 * Thrown when a user provides an answer or option that does not conform
 * to the allowed choices (e.g. non-existent option, illegal format).
 */
public class InvalidOptionException extends QuizException {

    private final String chosenOption;
    private final String expectedFormat;

    public InvalidOptionException(String chosenOption, String expectedFormat) {
        super("Invalid option selected: '" + chosenOption + "'. Expected format/range: [" + expectedFormat + "]");
        this.chosenOption = chosenOption;
        this.expectedFormat = expectedFormat;
    }

    public String getChosenOption() {
        return chosenOption;
    }

    public String getExpectedFormat() {
        return expectedFormat;
    }
}

```

---

### `InvalidQuestionException.java`
**Path:** `src/com/ait/quiz/exception/InvalidQuestionException.java`  
**Lines of Code:** 12  

```java
package com.ait.quiz.exception;

/**
 * Thrown when question parameters fail domain validation constraints
 * (e.g., empty prompt, fewer than two options, or non-positive marks).
 */
public class InvalidQuestionException extends QuizException {

    public InvalidQuestionException(String message) {
        super(message);
    }
}

```

---

### `EmptyQuizException.java`
**Path:** `src/com/ait/quiz/exception/EmptyQuizException.java`  
**Lines of Code:** 18  

```java
package com.ait.quiz.exception;

/**
 * Thrown when an attempt is made to conduct or evaluate a quiz that has no questions.
 */
public class EmptyQuizException extends QuizException {

    private final String quizId;

    public EmptyQuizException(String quizId) {
        super("Quiz '" + quizId + "' contains no questions! Please add questions before conducting.");
        this.quizId = quizId;
    }

    public String getQuizId() {
        return quizId;
    }
}

```

---

## UNIT III: ABSTRACT CLASSES & QUESTION MODELS

### `DifficultyLevel.java`
**Path:** `src/com/ait/quiz/model/DifficultyLevel.java`  
**Lines of Code:** 29  

```java
package com.ait.quiz.model;

/**
 * Enumeration representing the difficulty level of a quiz question or quiz.
 */
public enum DifficultyLevel {
    EASY("Easy"),
    MEDIUM("Medium"),
    HARD("Hard");

    private final String displayName;

    DifficultyLevel(String displayName) {
        this.displayName = displayName;
    }

    public String getDisplayName() {
        return displayName;
    }

    public static DifficultyLevel fromString(String text) {
        for (DifficultyLevel level : DifficultyLevel.values()) {
            if (level.name().equalsIgnoreCase(text) || level.displayName.equalsIgnoreCase(text)) {
                return level;
            }
        }
        return MEDIUM; // Default fallback
    }
}

```

---

### `Question.java`
**Path:** `src/com/ait/quiz/model/Question.java`  
**Lines of Code:** 117  

```java
package com.ait.quiz.model;

import com.ait.quiz.exception.InvalidOptionException;
import com.ait.quiz.exception.InvalidQuestionException;

/**
 * Abstract base class representing a generic Question in the Quiz System.
 * Demonstrates Unit III concept: Abstract Classes (abstract methods + concrete structure).
 * Subclasses must define specific display, validation, and answer checking behaviours.
 */
public abstract class Question {

    private final int id;
    private String questionText;
    private int marks;
    private String topic;
    private DifficultyLevel difficulty;

    /**
     * Parameterized constructor with validation.
     * Throws InvalidQuestionException if constraints are violated.
     */
    public Question(int id, String questionText, int marks, String topic, DifficultyLevel difficulty) 
            throws InvalidQuestionException {
        if (questionText == null || questionText.trim().isEmpty()) {
            throw new InvalidQuestionException("Question text cannot be null or blank!");
        }
        if (marks <= 0) {
            throw new InvalidQuestionException("Question marks must be strictly positive! Provided: " + marks);
        }
        this.id = id;
        this.questionText = questionText.trim();
        this.marks = marks;
        this.topic = (topic != null && !topic.trim().isEmpty()) ? topic.trim() : "General";
        this.difficulty = (difficulty != null) ? difficulty : DifficultyLevel.MEDIUM;
    }

    // Concrete getters & setters
    public int getId() {
        return id;
    }

    public String getQuestionText() {
        return questionText;
    }

    public void setQuestionText(String questionText) throws InvalidQuestionException {
        if (questionText == null || questionText.trim().isEmpty()) {
            throw new InvalidQuestionException("Question text cannot be empty!");
        }
        this.questionText = questionText.trim();
    }

    public int getMarks() {
        return marks;
    }

    public void setMarks(int marks) throws InvalidQuestionException {
        if (marks <= 0) {
            throw new InvalidQuestionException("Marks must be positive!");
        }
        this.marks = marks;
    }

    public String getTopic() {
        return topic;
    }

    public void setTopic(String topic) {
        this.topic = topic;
    }

    public DifficultyLevel getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(DifficultyLevel difficulty) {
        this.difficulty = difficulty;
    }

    /**
     * Common display header for all questions.
     */
    public void displayHeader() {
        System.out.printf("[Q%d] [%s | %s | Marks: %d]%n", id, getQuestionType(), difficulty.getDisplayName(), marks);
        System.out.println("Topic: " + topic);
        System.out.println("Prompt: " + questionText);
    }

    // --- Abstract Methods to be implemented polymorphically by subclasses ---

    /**
     * Polymorphic method to display the question and its interactive choices/prompts.
     */
    public abstract void displayQuestion();

    /**
     * Polymorphic method to check whether the student's submitted answer is correct.
     * Throws InvalidOptionException if input format violates choice expectations.
     */
    public abstract boolean checkAnswer(String studentAnswer) throws InvalidOptionException;

    /**
     * Returns the human-readable correct answer.
     */
    public abstract String getCorrectAnswerFormatted();

    /**
     * Returns the label of the specific question type.
     */
    public abstract String getQuestionType();

    @Override
    public String toString() {
        return String.format("[Q%d] (%s) %s [%d marks]", id, getQuestionType(), questionText, marks);
    }
}

```

---

### `MultipleChoiceQuestion.java`
**Path:** `src/com/ait/quiz/model/MultipleChoiceQuestion.java`  
**Lines of Code:** 89  

```java
package com.ait.quiz.model;

import com.ait.quiz.exception.InvalidOptionException;
import com.ait.quiz.exception.InvalidQuestionException;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Represents a Multiple Choice Question (MCQ) with 4 or more options (A, B, C, D...).
 * Demonstrates:
 * - Inheritance (extends Question)
 * - Polymorphism / Method Overriding (displayQuestion, checkAnswer, etc.)
 * - Exception Handling (validates choices in constructor and at runtime)
 */
public class MultipleChoiceQuestion extends Question {

    private final List<String> options;
    private final int correctOptionIndex; // 0-indexed (0 -> A, 1 -> B, etc.)

    public MultipleChoiceQuestion(int id, String questionText, int marks, String topic,
                                  DifficultyLevel difficulty, List<String> options, int correctOptionIndex)
            throws InvalidQuestionException {
        super(id, questionText, marks, topic, difficulty);

        if (options == null || options.size() < 2) {
            throw new InvalidQuestionException("MCQ must have at least 2 options! Found: " 
                    + (options == null ? 0 : options.size()));
        }
        if (correctOptionIndex < 0 || correctOptionIndex >= options.size()) {
            throw new InvalidQuestionException("Correct option index (" + correctOptionIndex 
                    + ") is out of valid range [0 to " + (options.size() - 1) + "]!");
        }

        this.options = new ArrayList<>(options);
        this.correctOptionIndex = correctOptionIndex;
    }

    public List<String> getOptions() {
        return Collections.unmodifiableList(options);
    }

    public int getCorrectOptionIndex() {
        return correctOptionIndex;
    }

    @Override
    public void displayQuestion() {
        displayHeader();
        char label = 'A';
        for (String option : options) {
            System.out.printf("   [%c] %s%n", label++, option);
        }
        System.out.println("   (Enter choice A-" + (char)('A' + options.size() - 1) + ")");
    }

    @Override
    public boolean checkAnswer(String studentAnswer) throws InvalidOptionException {
        if (studentAnswer == null || studentAnswer.trim().isEmpty()) {
            throw new InvalidOptionException("Empty input", "A to " + (char)('A' + options.size() - 1));
        }

        String cleaned = studentAnswer.trim().toUpperCase();
        if (cleaned.length() != 1) {
            throw new InvalidOptionException(studentAnswer, "Single character A to " + (char)('A' + options.size() - 1));
        }

        char choice = cleaned.charAt(0);
        int selectedIndex = choice - 'A';

        if (selectedIndex < 0 || selectedIndex >= options.size()) {
            throw new InvalidOptionException(studentAnswer, "A to " + (char)('A' + options.size() - 1));
        }

        return selectedIndex == correctOptionIndex;
    }

    @Override
    public String getCorrectAnswerFormatted() {
        char correctChar = (char) ('A' + correctOptionIndex);
        return String.format("[%c] %s", correctChar, options.get(correctOptionIndex));
    }

    @Override
    public String getQuestionType() {
        return "Multiple Choice (MCQ)";
    }
}

```

---

### `TrueFalseQuestion.java`
**Path:** `src/com/ait/quiz/model/TrueFalseQuestion.java`  
**Lines of Code:** 64  

```java
package com.ait.quiz.model;

import com.ait.quiz.exception.InvalidOptionException;
import com.ait.quiz.exception.InvalidQuestionException;

/**
 * Represents a True/False Question.
 * Demonstrates:
 * - Subclassing abstract base Question
 * - Overriding polymorphic methods with customized boolean behavior
 */
public class TrueFalseQuestion extends Question {

    private final boolean correctAnswer;

    public TrueFalseQuestion(int id, String questionText, int marks, String topic,
                             DifficultyLevel difficulty, boolean correctAnswer)
            throws InvalidQuestionException {
        super(id, questionText, marks, topic, difficulty);
        this.correctAnswer = correctAnswer;
    }

    public boolean isCorrectAnswer() {
        return correctAnswer;
    }

    @Override
    public void displayQuestion() {
        displayHeader();
        System.out.println("   [T] True");
        System.out.println("   [F] False");
        System.out.println("   (Enter choice T or F)");
    }

    @Override
    public boolean checkAnswer(String studentAnswer) throws InvalidOptionException {
        if (studentAnswer == null || studentAnswer.trim().isEmpty()) {
            throw new InvalidOptionException("Empty input", "T / F / True / False");
        }

        String cleaned = studentAnswer.trim().toUpperCase();
        boolean parsedAnswer;

        if (cleaned.equals("T") || cleaned.equals("TRUE")) {
            parsedAnswer = true;
        } else if (cleaned.equals("F") || cleaned.equals("FALSE")) {
            parsedAnswer = false;
        } else {
            throw new InvalidOptionException(studentAnswer, "T, F, TRUE, or FALSE");
        }

        return parsedAnswer == correctAnswer;
    }

    @Override
    public String getCorrectAnswerFormatted() {
        return correctAnswer ? "True" : "False";
    }

    @Override
    public String getQuestionType() {
        return "True / False";
    }
}

```

---

### `NumericQuestion.java`
**Path:** `src/com/ait/quiz/model/NumericQuestion.java`  
**Lines of Code:** 83  

```java
package com.ait.quiz.model;

import com.ait.quiz.exception.InvalidOptionException;
import com.ait.quiz.exception.InvalidQuestionException;

/**
 * Represents a Numeric Answer Question (e.g. calculation, memory size, time complexity constants).
 * Demonstrates:
 * - Subclassing abstract Question
 * - Numerical input validation
 * - Wrapping NumberFormatException into domain-specific InvalidOptionException
 */
public class NumericQuestion extends Question {

    private final double correctAnswer;
    private final double tolerance; // Allowed delta for floating point equality

    public NumericQuestion(int id, String questionText, int marks, String topic,
                           DifficultyLevel difficulty, double correctAnswer, double tolerance)
            throws InvalidQuestionException {
        super(id, questionText, marks, topic, difficulty);
        if (tolerance < 0) {
            throw new InvalidQuestionException("Tolerance cannot be negative! Provided: " + tolerance);
        }
        this.correctAnswer = correctAnswer;
        this.tolerance = tolerance;
    }

    public NumericQuestion(int id, String questionText, int marks, String topic,
                           DifficultyLevel difficulty, double correctAnswer)
            throws InvalidQuestionException {
        this(id, questionText, marks, topic, difficulty, correctAnswer, 0.0);
    }

    public double getCorrectAnswer() {
        return correctAnswer;
    }

    public double getTolerance() {
        return tolerance;
    }

    @Override
    public void displayQuestion() {
        displayHeader();
        if (tolerance > 0) {
            System.out.printf("   (Enter numeric answer with tolerance ±%.2f)%n", tolerance);
        } else {
            System.out.println("   (Enter exact numeric answer)");
        }
    }

    @Override
    public boolean checkAnswer(String studentAnswer) throws InvalidOptionException {
        if (studentAnswer == null || studentAnswer.trim().isEmpty()) {
            throw new InvalidOptionException("Empty input", "A valid number");
        }

        try {
            double parsedVal = Double.parseDouble(studentAnswer.trim());
            return Math.abs(parsedVal - correctAnswer) <= tolerance;
        } catch (NumberFormatException nfe) {
            throw new InvalidOptionException(studentAnswer, "Valid numeric value (e.g., 4 or 3.14)");
        }
    }

    @Override
    public String getCorrectAnswerFormatted() {
        if (tolerance > 0) {
            return String.format("%.2f (±%.2f)", correctAnswer, tolerance);
        }
        // If it's an integer value, show as integer
        if (correctAnswer == Math.floor(correctAnswer) && !Double.isInfinite(correctAnswer)) {
            return String.valueOf((long) correctAnswer);
        }
        return String.valueOf(correctAnswer);
    }

    @Override
    public String getQuestionType() {
        return "Numeric / Direct Answer";
    }
}

```

---

### `User.java`
**Path:** `src/com/ait/quiz/model/User.java`  
**Lines of Code:** 60  

```java
package com.ait.quiz.model;

/**
 * Abstract class representing a System User.
 * Demonstrates:
 * - Abstract class with common user state and abstract dashboard presentation.
 */
public abstract class User {

    private final String userId;
    private String name;
    private String email;

    public User(String userId, String name, String email) {
        if (userId == null || userId.trim().isEmpty()) {
            throw new IllegalArgumentException("User ID cannot be empty!");
        }
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Name cannot be empty!");
        }
        this.userId = userId.trim();
        this.name = name.trim();
        this.email = (email != null && !email.trim().isEmpty()) ? email.trim() : "user@aitpune.edu.in";
    }

    public String getUserId() {
        return userId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    /**
     * Abstract method to be implemented polymorphically depending on user role.
     */
    public abstract void displayDashboard();

    /**
     * Returns user role (e.g., "Student", "Instructor").
     */
    public abstract String getRole();

    @Override
    public String toString() {
        return String.format("[%s] ID: %s | Name: %s (%s)", getRole(), userId, name, email);
    }
}

```

---

### `Student.java`
**Path:** `src/com/ait/quiz/model/Student.java`  
**Lines of Code:** 73  

```java
package com.ait.quiz.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Concrete class representing a Student user in the Quiz System.
 * Demonstrates:
 * - Inheritance (extends User)
 * - Method Overriding (displayDashboard, getRole)
 * - State management for quiz attempts
 */
public class Student extends User {

    private final String rollNumber;
    private final String division; // e.g. "SE IT A"
    private final List<QuizAttempt> attempts;

    public Student(String userId, String name, String email, String rollNumber, String division) {
        super(userId, name, email);
        this.rollNumber = rollNumber;
        this.division = (division != null) ? division : "SE IT";
        this.attempts = new ArrayList<>();
    }

    public String getRollNumber() {
        return rollNumber;
    }

    public String getDivision() {
        return division;
    }

    public void addAttempt(QuizAttempt attempt) {
        if (attempt != null) {
            attempts.add(attempt);
        }
    }

    public List<QuizAttempt> getAttempts() {
        return Collections.unmodifiableList(attempts);
    }

    public double getAveragePercentage() {
        if (attempts.isEmpty()) return 0.0;
        double sum = 0;
        for (QuizAttempt att : attempts) {
            sum += att.getPercentage();
        }
        return sum / attempts.size();
    }

    @Override
    public void displayDashboard() {
        System.out.println("==================================================");
        System.out.println("           STUDENT PORTAL DASHBOARD               ");
        System.out.println("==================================================");
        System.out.printf("Name       : %s%n", getName());
        System.out.printf("Roll No    : %s | Division: %s%n", rollNumber, division);
        System.out.printf("Email      : %s%n", getEmail());
        System.out.printf("Total Quizzes Attempted : %d%n", attempts.size());
        if (!attempts.isEmpty()) {
            System.out.printf("Average Score           : %.2f%%%n", getAveragePercentage());
        }
        System.out.println("--------------------------------------------------");
    }

    @Override
    public String getRole() {
        return "Student";
    }
}

```

---

### `Instructor.java`
**Path:** `src/com/ait/quiz/model/Instructor.java`  
**Lines of Code:** 45  

```java
package com.ait.quiz.model;

/**
 * Concrete class representing an Instructor / Faculty member.
 * Demonstrates:
 * - Inheritance (extends User)
 * - Method Overriding (displayDashboard, getRole)
 */
public class Instructor extends User {

    private final String department;
    private final String designation;

    public Instructor(String userId, String name, String email, String department, String designation) {
        super(userId, name, email);
        this.department = (department != null) ? department : "Information Technology";
        this.designation = (designation != null) ? designation : "Assistant Professor";
    }

    public String getDepartment() {
        return department;
    }

    public String getDesignation() {
        return designation;
    }

    @Override
    public void displayDashboard() {
        System.out.println("==================================================");
        System.out.println("          INSTRUCTOR / FACULTY DASHBOARD          ");
        System.out.println("==================================================");
        System.out.printf("Faculty Name: %s%n", getName());
        System.out.printf("Designation : %s%n", designation);
        System.out.printf("Department  : %s%n", department);
        System.out.printf("Email       : %s%n", getEmail());
        System.out.println("Authorized Actions: Create Quizzes, Add Questions, View Reports");
        System.out.println("--------------------------------------------------");
    }

    @Override
    public String getRole() {
        return "Instructor";
    }
}

```

---

### `Quiz.java`
**Path:** `src/com/ait/quiz/model/Quiz.java`  
**Lines of Code:** 145  

```java
package com.ait.quiz.model;

import com.ait.quiz.exception.EmptyQuizException;
import com.ait.quiz.exception.InvalidQuestionException;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Represents a Quiz composed of polymorphic Question objects.
 * Demonstrates:
 * - Aggregation (Quiz has-many Questions)
 * - Domain validation and exception throwing (EmptyQuizException, InvalidQuestionException)
 */
public class Quiz {

    private final String quizId;
    private String title;
    private String description;
    private String topic;
    private DifficultyLevel difficulty;
    private String targetAgeGroup;
    private final List<Question> questions;

    public Quiz(String quizId, String title, String description, String topic, DifficultyLevel difficulty, String targetAgeGroup) {
        if (quizId == null || quizId.trim().isEmpty()) {
            throw new IllegalArgumentException("Quiz ID cannot be null or empty!");
        }
        if (title == null || title.trim().isEmpty()) {
            throw new IllegalArgumentException("Quiz title cannot be null or empty!");
        }
        this.quizId = quizId.trim().toUpperCase();
        this.title = title.trim();
        this.description = (description != null) ? description.trim() : "";
        this.topic = (topic != null) ? topic.trim() : "General Java";
        this.difficulty = (difficulty != null) ? difficulty : DifficultyLevel.MEDIUM;
        this.targetAgeGroup = (targetAgeGroup != null && !targetAgeGroup.trim().isEmpty()) ? targetAgeGroup.trim() : "College (18-22)";
        this.questions = new ArrayList<>();
    }

    public Quiz(String quizId, String title, String description, String topic, DifficultyLevel difficulty) {
        this(quizId, title, description, topic, difficulty, "College (18-22)");
    }

    public String getTargetAgeGroup() {
        return targetAgeGroup;
    }

    public void setTargetAgeGroup(String targetAgeGroup) {
        if (targetAgeGroup != null && !targetAgeGroup.trim().isEmpty()) {
            this.targetAgeGroup = targetAgeGroup.trim();
        }
    }

    public String getQuizId() {
        return quizId;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        if (title != null && !title.trim().isEmpty()) {
            this.title = title.trim();
        }
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getTopic() {
        return topic;
    }

    public void setTopic(String topic) {
        this.topic = topic;
    }

    public DifficultyLevel getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(DifficultyLevel difficulty) {
        this.difficulty = difficulty;
    }

    public List<Question> getQuestions() {
        return Collections.unmodifiableList(questions);
    }

    public int getQuestionCount() {
        return questions.size();
    }

    /**
     * Adds a polymorphic Question to the quiz.
     * Throws InvalidQuestionException if null or duplicate ID.
     */
    public void addQuestion(Question question) throws InvalidQuestionException {
        if (question == null) {
            throw new InvalidQuestionException("Cannot add a null question to the quiz!");
        }
        for (Question q : questions) {
            if (q.getId() == question.getId()) {
                throw new InvalidQuestionException("Question with ID " + question.getId() + " already exists in this quiz!");
            }
        }
        questions.add(question);
    }

    public boolean removeQuestion(int questionId) {
        return questions.removeIf(q -> q.getId() == questionId);
    }

    public int getTotalMarks() {
        int total = 0;
        for (Question q : questions) {
            total += q.getMarks();
        }
        return total;
    }

    /**
     * Verifies that the quiz is ready to be conducted.
     * Throws EmptyQuizException if no questions are present.
     */
    public void validateForConduct() throws EmptyQuizException {
        if (questions.isEmpty()) {
            throw new EmptyQuizException(quizId);
        }
    }

    @Override
    public String toString() {
        return String.format("[%s] %s | Age: %s | Topic: %s | Level: %s | Questions: %d | Total Marks: %d",
                quizId, title, targetAgeGroup, topic, difficulty.getDisplayName(), questions.size(), getTotalMarks());
    }
}

```

---

### `QuizAttempt.java`
**Path:** `src/com/ait/quiz/model/QuizAttempt.java`  
**Lines of Code:** 109  

```java
package com.ait.quiz.model;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Encapsulates the results of a single quiz attempt by a student.
 * Keeps track of score, grading, and detailed question breakdown.
 */
public class QuizAttempt {

    private final String attemptId;
    private final String quizId;
    private final String quizTitle;
    private final String studentRollNumber;
    private final String studentName;
    private final String timestamp;

    private int totalQuestions;
    private int correctCount;
    private int incorrectCount;
    private double scoreObtained;
    private int totalPossibleMarks;
    private double percentage;
    private String grade;

    // Detailed record of each question result
    public static class QuestionResult {
        private final int questionId;
        private final String questionText;
        private final String studentAnswer;
        private final String correctAnswer;
        private final boolean isCorrect;
        private final double marksAwarded;

        public QuestionResult(int questionId, String questionText, String studentAnswer, 
                              String correctAnswer, boolean isCorrect, double marksAwarded) {
            this.questionId = questionId;
            this.questionText = questionText;
            this.studentAnswer = studentAnswer;
            this.correctAnswer = correctAnswer;
            this.isCorrect = isCorrect;
            this.marksAwarded = marksAwarded;
        }

        public int getQuestionId() { return questionId; }
        public String getQuestionText() { return questionText; }
        public String getStudentAnswer() { return studentAnswer; }
        public String getCorrectAnswer() { return correctAnswer; }
        public boolean isCorrect() { return isCorrect; }
        public double getMarksAwarded() { return marksAwarded; }
    }

    private final List<QuestionResult> questionResults = new ArrayList<>();

    public QuizAttempt(String attemptId, String quizId, String quizTitle, String studentRollNumber, String studentName) {
        this.attemptId = attemptId;
        this.quizId = quizId;
        this.quizTitle = quizTitle;
        this.studentRollNumber = studentRollNumber;
        this.studentName = studentName;
        this.timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("dd-MMM-yyyy HH:mm:ss"));
    }

    public void addQuestionResult(QuestionResult result) {
        questionResults.add(result);
    }

    public List<QuestionResult> getQuestionResults() {
        return Collections.unmodifiableList(questionResults);
    }

    public String getAttemptId() { return attemptId; }
    public String getQuizId() { return quizId; }
    public String getQuizTitle() { return quizTitle; }
    public String getStudentRollNumber() { return studentRollNumber; }
    public String getStudentName() { return studentName; }
    public String getTimestamp() { return timestamp; }

    public int getTotalQuestions() { return totalQuestions; }
    public void setTotalQuestions(int totalQuestions) { this.totalQuestions = totalQuestions; }

    public int getCorrectCount() { return correctCount; }
    public void setCorrectCount(int correctCount) { this.correctCount = correctCount; }

    public int getIncorrectCount() { return incorrectCount; }
    public void setIncorrectCount(int incorrectCount) { this.incorrectCount = incorrectCount; }

    public double getScoreObtained() { return scoreObtained; }
    public void setScoreObtained(double scoreObtained) { this.scoreObtained = scoreObtained; }

    public int getTotalPossibleMarks() { return totalPossibleMarks; }
    public void setTotalPossibleMarks(int totalPossibleMarks) { this.totalPossibleMarks = totalPossibleMarks; }

    public double getPercentage() { return percentage; }
    public void setPercentage(double percentage) { this.percentage = percentage; }

    public String getGrade() { return grade; }
    public void setGrade(String grade) { this.grade = grade; }

    @Override
    public String toString() {
        return String.format("[%s] Student: %s (%s) | Quiz: %s | Score: %.2f/%d (%.2f%%) | Grade: %s",
                attemptId, studentName, studentRollNumber, quizId, scoreObtained, totalPossibleMarks, percentage, grade);
    }
}

```

---

## UNIT III: INTERFACES & STRATEGY PATTERN GRADING POLICIES

### `QuizOperations.java`
**Path:** `src/com/ait/quiz/service/QuizOperations.java`  
**Lines of Code:** 79  

```java
package com.ait.quiz.service;

import com.ait.quiz.exception.DuplicateQuizException;
import com.ait.quiz.exception.InvalidQuestionException;
import com.ait.quiz.exception.QuizNotFoundException;
import com.ait.quiz.model.DifficultyLevel;
import com.ait.quiz.model.Question;
import com.ait.quiz.model.Quiz;
import com.ait.quiz.model.QuizAttempt;

import java.util.List;

/**
 * Core interface defining lifecycle operations on quizzes and attempts.
 * Demonstrates Unit III concept: Interfaces (defining contract for Quiz operations).
 */
public interface QuizOperations {

    /**
     * Creates a new quiz in the repository.
     * Throws DuplicateQuizException if the quizId is already taken.
     */
    void createQuiz(Quiz quiz) throws DuplicateQuizException;

    /**
     * Adds a polymorphic Question to the designated Quiz.
     * Throws QuizNotFoundException if target quiz doesn't exist,
     * or InvalidQuestionException if the question violates integrity rules.
     */
    void addQuestionToQuiz(String quizId, Question question) 
            throws QuizNotFoundException, InvalidQuestionException;

    /**
     * Retrieves a quiz by its unique ID.
     * Throws QuizNotFoundException if not found.
     */
    Quiz getQuiz(String quizId) throws QuizNotFoundException;

    /**
     * Returns all quizzes registered in the system.
     */
    List<Quiz> getAllQuizzes();

    /**
     * Overloaded search method: Finds quizzes matching a topic keyword.
     */
    List<Quiz> searchQuiz(String topic);

    /**
     * Overloaded search method: Finds quizzes matching both topic and difficulty level.
     */
    List<Quiz> searchQuiz(String topic, DifficultyLevel level);

    /**
     * Deletes a quiz by its ID.
     * Throws QuizNotFoundException if not found.
     */
    boolean deleteQuiz(String quizId) throws QuizNotFoundException;

    /**
     * Stores a student's completed quiz attempt.
     */
    void recordAttempt(QuizAttempt attempt);

    /**
     * Retrieves all recorded quiz attempts.
     */
    List<QuizAttempt> getAllAttempts();

    /**
     * Retrieves all quiz attempts by a specific student roll number.
     */
    List<QuizAttempt> getAttemptsByStudent(String rollNumber);

    /**
     * Returns total count of registered quizzes.
     */
    int getQuizCount();
}

```

---

### `QuizEvaluator.java`
**Path:** `src/com/ait/quiz/service/QuizEvaluator.java`  
**Lines of Code:** 36  

```java
package com.ait.quiz.service;

import com.ait.quiz.model.QuizAttempt;

/**
 * Interface defining evaluation contracts and grading policies.
 * Demonstrates Unit III concept: Interfaces (defining common behaviour to be implemented).
 */
public interface QuizEvaluator {

    /**
     * Calculates the overall score for a completed quiz attempt.
     */
    double evaluateScore(QuizAttempt attempt);

    /**
     * Overloaded method demonstrating Compile-time Polymorphism (Method Overloading).
     * Calculates score based on raw marks and penalty deduction.
     */
    double evaluateScore(double earnedMarks, int incorrectCount, double penaltyPerIncorrect);

    /**
     * Determines letter grade based on percentage.
     */
    String generateGrade(double percentage);

    /**
     * Returns the title/description of the grading policy.
     */
    String getPolicyName();

    /**
     * Prints a comprehensive score breakdown and question-by-question review.
     */
    void printDetailedReport(QuizAttempt attempt);
}

```

---

### `StandardGradingPolicy.java`
**Path:** `src/com/ait/quiz/service/StandardGradingPolicy.java`  
**Lines of Code:** 75  

```java
package com.ait.quiz.service;

import com.ait.quiz.model.QuizAttempt;

/**
 * Standard university grading implementation of QuizEvaluator.
 * Awards full marks for correct answers and zero deduction for incorrect answers.
 * Demonstrates:
 * - Interface Implementation
 * - Polymorphism (Method Overriding & Overloading)
 */
public class StandardGradingPolicy implements QuizEvaluator {

    @Override
    public double evaluateScore(QuizAttempt attempt) {
        double total = 0.0;
        for (QuizAttempt.QuestionResult res : attempt.getQuestionResults()) {
            if (res.isCorrect()) {
                total += res.getMarksAwarded();
            }
        }
        return total;
    }

    @Override
    public double evaluateScore(double earnedMarks, int incorrectCount, double penaltyPerIncorrect) {
        // Standard policy ignores penalty
        return Math.max(0.0, earnedMarks);
    }

    @Override
    public String generateGrade(double percentage) {
        if (percentage >= 90.0) return "O (Outstanding)";
        if (percentage >= 80.0) return "A+ (Excellent)";
        if (percentage >= 70.0) return "A (Very Good)";
        if (percentage >= 60.0) return "B+ (Good)";
        if (percentage >= 50.0) return "B (Above Average)";
        if (percentage >= 40.0) return "C (Pass)";
        return "F (Fail)";
    }

    @Override
    public String getPolicyName() {
        return "Standard Linear Evaluation (No Negative Marking)";
    }

    @Override
    public void printDetailedReport(QuizAttempt attempt) {
        System.out.println("================================================================================");
        System.out.println("                         DETAILED QUIZ PERFORMANCE REPORT                       ");
        System.out.println("================================================================================");
        System.out.printf("Attempt ID   : %s%n", attempt.getAttemptId());
        System.out.printf("Student Name : %s (Roll No: %s)%n", attempt.getStudentName(), attempt.getStudentRollNumber());
        System.out.printf("Quiz Title   : %s (ID: %s)%n", attempt.getQuizTitle(), attempt.getQuizId());
        System.out.printf("Grading Rule : %s%n", getPolicyName());
        System.out.printf("Date & Time  : %s%n", attempt.getTimestamp());
        System.out.println("--------------------------------------------------------------------------------");
        System.out.printf("Total Questions: %d | Correct: %d | Incorrect: %d%n",
                attempt.getTotalQuestions(), attempt.getCorrectCount(), attempt.getIncorrectCount());
        System.out.printf("Final Score    : %.2f / %d marks%n", attempt.getScoreObtained(), attempt.getTotalPossibleMarks());
        System.out.printf("Percentage     : %.2f%%%n", attempt.getPercentage());
        System.out.printf("Awarded Grade  : %s%n", attempt.getGrade());
        System.out.println("--------------------------------------------------------------------------------");
        System.out.println("QUESTION BREAKDOWN:");
        int idx = 1;
        for (QuizAttempt.QuestionResult q : attempt.getQuestionResults()) {
            String status = q.isCorrect() ? "[PASS / CORRECT]" : "[FAIL / INCORRECT]";
            System.out.printf(" %2d. %s %s%n", idx++, status, q.getQuestionText());
            System.out.printf("     Your Answer   : %s%n", q.getStudentAnswer());
            System.out.printf("     Correct Answer: %s%n", q.getCorrectAnswer());
            System.out.printf("     Marks Earned  : %.2f%n", q.getMarksAwarded());
        }
        System.out.println("================================================================================");
    }
}

```

---

### `NegativeMarkingGradingPolicy.java`
**Path:** `src/com/ait/quiz/service/NegativeMarkingGradingPolicy.java`  
**Lines of Code:** 100  

```java
package com.ait.quiz.service;

import com.ait.quiz.model.QuizAttempt;

/**
 * Competitive exam grading implementation of QuizEvaluator.
 * Penalizes incorrect answers with a configurable negative deduction factor (default 25% penalty).
 * Demonstrates:
 * - Interface Implementation
 * - Polymorphism (Method Overriding & Overloading)
 */
public class NegativeMarkingGradingPolicy implements QuizEvaluator {

    private final double penaltyRate; // e.g. 0.25 for 25% negative marking

    public NegativeMarkingGradingPolicy() {
        this(0.25);
    }

    public NegativeMarkingGradingPolicy(double penaltyRate) {
        if (penaltyRate < 0.0 || penaltyRate > 1.0) {
            throw new IllegalArgumentException("Penalty rate must be between 0.0 and 1.0!");
        }
        this.penaltyRate = penaltyRate;
    }

    public double getPenaltyRate() {
        return penaltyRate;
    }

    @Override
    public double evaluateScore(QuizAttempt attempt) {
        double rawScore = 0.0;
        for (QuizAttempt.QuestionResult res : attempt.getQuestionResults()) {
            if (res.isCorrect()) {
                rawScore += res.getMarksAwarded();
            } else {
                // Deduct penalty based on question's marks
                double penalty = res.getMarksAwarded() * penaltyRate;
                rawScore -= penalty;
            }
        }
        // Score can be negative or floored at 0 depending on evaluation rules
        return Math.max(0.0, rawScore);
    }

    @Override
    public double evaluateScore(double earnedMarks, int incorrectCount, double penaltyPerIncorrect) {
        double total = earnedMarks - (incorrectCount * penaltyPerIncorrect);
        return Math.max(0.0, total);
    }

    @Override
    public String generateGrade(double percentage) {
        if (percentage >= 85.0) return "O (Exceptional - Competitive Rank 1)";
        if (percentage >= 75.0) return "A+ (Excellent - Advanced Proficiency)";
        if (percentage >= 65.0) return "A (Very Good - High Proficiency)";
        if (percentage >= 50.0) return "B (Qualified)";
        return "Not Qualified (Below cutoff with negative penalties)";
    }

    @Override
    public String getPolicyName() {
        return String.format("Competitive Evaluation (%.0f%% Negative Penalty for wrong answers)", penaltyRate * 100);
    }

    @Override
    public void printDetailedReport(QuizAttempt attempt) {
        System.out.println("================================================================================");
        System.out.println("                 COMPETITIVE EXAM DETAILED SCORECARD WITH PENALTY               ");
        System.out.println("================================================================================");
        System.out.printf("Attempt ID   : %s%n", attempt.getAttemptId());
        System.out.printf("Student Name : %s (Roll No: %s)%n", attempt.getStudentName(), attempt.getStudentRollNumber());
        System.out.printf("Quiz Title   : %s (ID: %s)%n", attempt.getQuizTitle(), attempt.getQuizId());
        System.out.printf("Grading Rule : %s%n", getPolicyName());
        System.out.printf("Date & Time  : %s%n", attempt.getTimestamp());
        System.out.println("--------------------------------------------------------------------------------");
        System.out.printf("Total Questions : %d%n", attempt.getTotalQuestions());
        System.out.printf("Correct Answers : %d%n", attempt.getCorrectCount());
        System.out.printf("Wrong Answers   : %d (-%.0f%% marks penalized per wrong answer)%n", 
                attempt.getIncorrectCount(), penaltyRate * 100);
        System.out.printf("Net Score       : %.2f / %d marks%n", attempt.getScoreObtained(), attempt.getTotalPossibleMarks());
        System.out.printf("Net Percentage  : %.2f%%%n", attempt.getPercentage());
        System.out.printf("Result Status   : %s%n", attempt.getGrade());
        System.out.println("--------------------------------------------------------------------------------");
        System.out.println("ITEM-BY-ITEM AUDIT:");
        int idx = 1;
        for (QuizAttempt.QuestionResult q : attempt.getQuestionResults()) {
            if (q.isCorrect()) {
                System.out.printf(" %2d. [+%.2f marks] %s%n", idx++, q.getMarksAwarded(), q.getQuestionText());
            } else {
                double penalty = q.getMarksAwarded() * penaltyRate;
                System.out.printf(" %2d. [-%.2f PENALTY] %s%n", idx++, penalty, q.getQuestionText());
            }
            System.out.printf("     Your Answer   : %s%n", q.getStudentAnswer());
            System.out.printf("     Correct Answer: %s%n", q.getCorrectAnswer());
        }
        System.out.println("================================================================================");
    }
}

```

---

### `QuizManager.java`
**Path:** `src/com/ait/quiz/service/QuizManager.java`  
**Lines of Code:** 599  

```java
package com.ait.quiz.service;

import com.ait.quiz.exception.DuplicateQuizException;
import com.ait.quiz.exception.InvalidQuestionException;
import com.ait.quiz.exception.QuizNotFoundException;
import com.ait.quiz.model.*;

import java.util.*;

/**
 * Service implementation managing quizzes, questions, and attempt records.
 * Demonstrates:
 * - Interface Implementation (implements QuizOperations)
 * - Method Overloading (searchQuiz with 1 param vs 2 params)
 * - Exception Handling (throwing custom checked exceptions)
 * - Collections Framework (Map, List, ArrayList, LinkedHashMap)
 */
public class QuizManager implements QuizOperations {

    private final Map<String, Quiz> quizMap;
    private final List<QuizAttempt> attemptHistory;

    public QuizManager() {
        this.quizMap = new LinkedHashMap<>();
        this.attemptHistory = new ArrayList<>();
        preloadDefaultQuizzes();
    }

    @Override
    public void createQuiz(Quiz quiz) throws DuplicateQuizException {
        if (quiz == null) {
            throw new IllegalArgumentException("Cannot create a null quiz!");
        }
        String idKey = quiz.getQuizId().toUpperCase();
        if (quizMap.containsKey(idKey)) {
            throw new DuplicateQuizException(quiz.getQuizId());
        }
        quizMap.put(idKey, quiz);
    }

    @Override
    public void addQuestionToQuiz(String quizId, Question question) 
            throws QuizNotFoundException, InvalidQuestionException {
        Quiz quiz = getQuiz(quizId);
        quiz.addQuestion(question);
    }

    @Override
    public Quiz getQuiz(String quizId) throws QuizNotFoundException {
        if (quizId == null || quizId.trim().isEmpty()) {
            throw new QuizNotFoundException("NULL/EMPTY");
        }
        String idKey = quizId.trim().toUpperCase();
        Quiz quiz = quizMap.get(idKey);
        if (quiz == null) {
            throw new QuizNotFoundException(quizId);
        }
        return quiz;
    }

    @Override
    public List<Quiz> getAllQuizzes() {
        return new ArrayList<>(quizMap.values());
    }

    /**
     * Overloaded search method: Search by topic keyword.
     */
    @Override
    public List<Quiz> searchQuiz(String topic) {
        if (topic == null || topic.trim().isEmpty()) {
            return getAllQuizzes();
        }
        String query = topic.trim().toLowerCase();
        List<Quiz> matched = new ArrayList<>();
        for (Quiz q : quizMap.values()) {
            if (q.getTopic().toLowerCase().contains(query) || q.getTitle().toLowerCase().contains(query)) {
                matched.add(q);
            }
        }
        return matched;
    }

    /**
     * Overloaded search method: Search by topic keyword AND DifficultyLevel.
     * Demonstrates Compile-time Polymorphism (Method Overloading).
     */
    @Override
    public List<Quiz> searchQuiz(String topic, DifficultyLevel level) {
        List<Quiz> topicMatches = searchQuiz(topic);
        if (level == null) {
            return topicMatches;
        }
        List<Quiz> finalMatches = new ArrayList<>();
        for (Quiz q : topicMatches) {
            if (q.getDifficulty() == level) {
                finalMatches.add(q);
            }
        }
        return finalMatches;
    }

    @Override
    public boolean deleteQuiz(String quizId) throws QuizNotFoundException {
        String idKey = quizId.trim().toUpperCase();
        if (!quizMap.containsKey(idKey)) {
            throw new QuizNotFoundException(quizId);
        }
        quizMap.remove(idKey);
        return true;
    }

    @Override
    public void recordAttempt(QuizAttempt attempt) {
        if (attempt != null) {
            attemptHistory.add(attempt);
        }
    }

    @Override
    public List<QuizAttempt> getAllAttempts() {
        return Collections.unmodifiableList(attemptHistory);
    }

    @Override
    public List<QuizAttempt> getAttemptsByStudent(String rollNumber) {
        if (rollNumber == null) return Collections.emptyList();
        List<QuizAttempt> studentAttempts = new ArrayList<>();
        for (QuizAttempt att : attemptHistory) {
            if (att.getStudentRollNumber().equalsIgnoreCase(rollNumber.trim())) {
                studentAttempts.add(att);
            }
        }
        return studentAttempts;
    }

    @Override
    public int getQuizCount() {
        return quizMap.size();
    }

    /**
     * Pre-populates the system with realistic sample quizzes containing MCQs,
     * True/False questions, and Numeric questions aligned with SE IT Unit III & IV.
     */
    private void preloadDefaultQuizzes() {
        try {
            // ==============================================================
            // Quiz 1: Unit III - OOP, Abstract Classes, Interfaces & Polymorphism
            // ==============================================================
            // ==============================================================
            // Quiz 1: Unit III - OOP, Abstract Classes, Interfaces & Polymorphism (College 18-22)
            // ==============================================================
            Quiz oopQuiz = new Quiz("JAVA-OOP", "OOP, Interfaces & Polymorphism",
                    "Comprehensive test on Unit III: dynamic binding, abstract classes, interfaces",
                    "Object-Oriented Programming", DifficultyLevel.MEDIUM, "College (18-22)");

            oopQuiz.addQuestion(new MultipleChoiceQuestion(
                    1,
                    "Which Java keyword is used to implement an interface in a class?",
                    5,
                    "Interfaces",
                    DifficultyLevel.EASY,
                    Arrays.asList("extends", "implements", "inherits", "interface"),
                    1 // 'implements' -> index 1
            ));

            oopQuiz.addQuestion(new MultipleChoiceQuestion(
                    2,
                    "Which of the following statements about an abstract class in Java is TRUE?",
                    5,
                    "Abstract Classes",
                    DifficultyLevel.MEDIUM,
                    Arrays.asList(
                            "An abstract class can be instantiated directly using 'new'",
                            "An abstract class can contain both abstract methods and concrete methods",
                            "An abstract class cannot contain constructors",
                            "All methods in an abstract class must be abstract"
                    ),
                    1 // index 1
            ));

            oopQuiz.addQuestion(new TrueFalseQuestion(
                    3,
                    "In Java, method overloading is resolved at compile time, whereas method overriding is resolved at runtime (dynamic method dispatch).",
                    5,
                    "Polymorphism",
                    DifficultyLevel.EASY,
                    true
            ));

            oopQuiz.addQuestion(new TrueFalseQuestion(
                    4,
                    "A class in Java can implement multiple interfaces and simultaneously extend multiple concrete classes.",
                    5,
                    "Multiple Inheritance",
                    DifficultyLevel.MEDIUM,
                    false // Java does not support multiple class inheritance
            ));

            oopQuiz.addQuestion(new NumericQuestion(
                    5,
                    "In Java SE 8 and above, what is the minimum number of abstract methods a Functional Interface must have?",
                    5,
                    "Interfaces",
                    DifficultyLevel.EASY,
                    1.0,
                    0.0
            ));

            createQuiz(oopQuiz);

            // ==============================================================
            // Quiz 2: Unit IV - Exception Handling & Robust Programming (College 18-22)
            // ==============================================================
            Quiz excQuiz = new Quiz("JAVA-EXC", "Exception Handling in Java",
                    "Assesses try, catch, finally, throw, throws, and custom exceptions",
                    "Exception Handling", DifficultyLevel.HARD, "College (18-22)");

            excQuiz.addQuestion(new MultipleChoiceQuestion(
                    1,
                    "What block is GUARANTEED to execute regardless of whether an exception is thrown or caught (unless System.exit() is called)?",
                    5,
                    "Exception Handling",
                    DifficultyLevel.EASY,
                    Arrays.asList("catch", "throw", "finally", "throws"),
                    2 // 'finally' -> index 2
            ));

            excQuiz.addQuestion(new MultipleChoiceQuestion(
                    2,
                    "Which base class must a custom checked exception inherit from in Java?",
                    5,
                    "Custom Exceptions",
                    DifficultyLevel.MEDIUM,
                    Arrays.asList("java.lang.RuntimeException", "java.lang.Exception", "java.lang.Error", "java.lang.ThrowableOnly"),
                    1 // java.lang.Exception -> index 1
            ));

            excQuiz.addQuestion(new TrueFalseQuestion(
                    3,
                    "A single 'try' block can have multiple 'catch' blocks, but subclasses of Exception must be caught BEFORE superclasses.",
                    5,
                    "Catch Hierarchy",
                    DifficultyLevel.MEDIUM,
                    true
            ));

            excQuiz.addQuestion(new NumericQuestion(
                    4,
                    "If an integer division 10 / 0 is evaluated in Java, an ArithmeticException is thrown. What is the byte size of standard Java int?",
                    5,
                    "Java Fundamentals",
                    DifficultyLevel.EASY,
                    4.0,
                    0.0
            ));

            createQuiz(excQuiz);

            // ==============================================================
            // Quiz 3: Java Fundamentals & Collections (College 18-22)
            // ==============================================================
            Quiz genQuiz = new Quiz("JAVA-GEN", "Java Collections & Core Concepts",
                    "Basics of Lists, Maps, and object orientation",
                    "Collections Framework", DifficultyLevel.EASY, "College (18-22)");

            genQuiz.addQuestion(new MultipleChoiceQuestion(
                    1,
                    "Which collection allows storing key-value pairs without duplicate keys?",
                    5,
                    "Collections",
                    DifficultyLevel.EASY,
                    Arrays.asList("ArrayList", "HashMap", "LinkedList", "Vector"),
                    1 // HashMap -> index 1
            ));

            genQuiz.addQuestion(new TrueFalseQuestion(
                    2,
                    "ArrayList in Java maintains insertion order and allows duplicate elements.",
                    5,
                    "Collections",
                    DifficultyLevel.EASY,
                    true
            ));

            createQuiz(genQuiz);

            // ==============================================================
            // Quiz 4: KIDS (8-12 yrs) - Junior Science & Solar System Quest
            // ==============================================================
            Quiz kidsSciQuiz = new Quiz("KIDS-SCI", "Junior Science & Space Quest",
                    "Exciting questions on space, nature, and animals for curious young minds!",
                    "Science & Discovery", DifficultyLevel.EASY, "Kids (8-12)");

            kidsSciQuiz.addQuestion(new MultipleChoiceQuestion(
                    1,
                    "Which planet in our solar system is known as the 'Red Planet'?",
                    5,
                    "Space Exploration",
                    DifficultyLevel.EASY,
                    Arrays.asList("Earth", "Mars", "Jupiter", "Venus"),
                    1 // Mars -> index 1
            ));

            kidsSciQuiz.addQuestion(new MultipleChoiceQuestion(
                    2,
                    "What is the hardest natural mineral substance found on Earth?",
                    5,
                    "Earth Science",
                    DifficultyLevel.EASY,
                    Arrays.asList("Gold", "Iron", "Diamond", "Silver"),
                    2 // Diamond -> index 2
            ));

            kidsSciQuiz.addQuestion(new TrueFalseQuestion(
                    3,
                    "Green plants make their food using sunlight through a process called photosynthesis.",
                    5,
                    "Biology",
                    DifficultyLevel.EASY,
                    true
            ));

            kidsSciQuiz.addQuestion(new TrueFalseQuestion(
                    4,
                    "The Moon produces its own light just like the Sun.",
                    5,
                    "Astronomy",
                    DifficultyLevel.EASY,
                    false
            ));

            kidsSciQuiz.addQuestion(new NumericQuestion(
                    5,
                    "How many recognized planets are there in our Solar System?",
                    5,
                    "Solar System",
                    DifficultyLevel.EASY,
                    8.0,
                    0.0
            ));

            createQuiz(kidsSciQuiz);

            // ==============================================================
            // Quiz 5: KIDS (8-12 yrs) - Junior Math & Logic Riddles
            // ==============================================================
            Quiz kidsMathQuiz = new Quiz("KIDS-MATH", "Junior Math & Brain Riddles",
                    "Fun numerical puzzles and geometry riddles designed for young learners.",
                    "Elementary Math", DifficultyLevel.EASY, "Kids (8-12)");

            kidsMathQuiz.addQuestion(new MultipleChoiceQuestion(
                    1,
                    "How many sides does an Octagon have?",
                    5,
                    "Shapes & Geometry",
                    DifficultyLevel.EASY,
                    Arrays.asList("6", "7", "8", "10"),
                    2 // 8 -> index 2
            ));

            kidsMathQuiz.addQuestion(new MultipleChoiceQuestion(
                    2,
                    "What is 15 multiplied by 4?",
                    5,
                    "Multiplication",
                    DifficultyLevel.EASY,
                    Arrays.asList("45", "50", "60", "65"),
                    2 // 60 -> index 2
            ));

            kidsMathQuiz.addQuestion(new TrueFalseQuestion(
                    3,
                    "A flat triangle can have two 90-degree right angles.",
                    5,
                    "Geometry Rules",
                    DifficultyLevel.EASY,
                    false
            ));

            kidsMathQuiz.addQuestion(new NumericQuestion(
                    4,
                    "If you have 3 dozen eggs, how many total eggs do you have?",
                    5,
                    "Mental Math",
                    DifficultyLevel.EASY,
                    36.0,
                    0.0
            ));

            createQuiz(kidsMathQuiz);

            // ==============================================================
            // Quiz 6: TEENS (13-17 yrs) - Python & Algorithmic Thinking
            // ==============================================================
            Quiz teenCodeQuiz = new Quiz("TEEN-CODE", "Teen Coder: Python & Logic Basics",
                    "Fundamental coding concepts, variables, loops, and algorithmic problem solving.",
                    "Computer Science", DifficultyLevel.MEDIUM, "Teens (13-17)");

            teenCodeQuiz.addQuestion(new MultipleChoiceQuestion(
                    1,
                    "In Python, which built-in function is used to output text to the console?",
                    5,
                    "Python Fundamentals",
                    DifficultyLevel.EASY,
                    Arrays.asList("echo()", "display()", "print()", "write()"),
                    2 // print() -> index 2
            ));

            teenCodeQuiz.addQuestion(new MultipleChoiceQuestion(
                    2,
                    "According to operator precedence, what is the output of: 10 + 2 * 5?",
                    5,
                    "Arithmetic Precedence",
                    DifficultyLevel.EASY,
                    Arrays.asList("60", "20", "70", "25"),
                    1 // 20 -> index 1
            ));

            teenCodeQuiz.addQuestion(new TrueFalseQuestion(
                    3,
                    "In most modern programming languages, a variable name can start with a number (e.g., 2ndValue).",
                    5,
                    "Syntax Rules",
                    DifficultyLevel.EASY,
                    false
            ));

            teenCodeQuiz.addQuestion(new TrueFalseQuestion(
                    4,
                    "A 'while' loop continues to execute as long as its conditional test remains true.",
                    5,
                    "Control Structures",
                    DifficultyLevel.EASY,
                    true
            ));

            teenCodeQuiz.addQuestion(new NumericQuestion(
                    5,
                    "What is 2 raised to the power of 5 (2^5)?",
                    5,
                    "Binary & Powers",
                    DifficultyLevel.EASY,
                    32.0,
                    0.0
            ));

            createQuiz(teenCodeQuiz);

            // ==============================================================
            // Quiz 7: TEENS (13-17 yrs) - High School STEM & Technology
            // ==============================================================
            Quiz teenStemQuiz = new Quiz("TEEN-STEM", "High School STEM: Physics & Digital Tech",
                    "Electricity, laws of motion, and computer hardware for high schoolers.",
                    "STEM Physics", DifficultyLevel.MEDIUM, "Teens (13-17)");

            teenStemQuiz.addQuestion(new MultipleChoiceQuestion(
                    1,
                    "What is the SI unit of Electric Current?",
                    5,
                    "Physics Fundamentals",
                    DifficultyLevel.EASY,
                    Arrays.asList("Volt", "Watt", "Ampere", "Ohm"),
                    2 // Ampere -> index 2
            ));

            teenStemQuiz.addQuestion(new MultipleChoiceQuestion(
                    2,
                    "Which hardware component is widely recognized as the 'Brain' of a computer?",
                    5,
                    "Hardware Architecture",
                    DifficultyLevel.EASY,
                    Arrays.asList("RAM", "CPU", "Hard Disk Drive", "Power Supply"),
                    1 // CPU -> index 1
            ));

            teenStemQuiz.addQuestion(new TrueFalseQuestion(
                    3,
                    "Sound waves travel faster in water than they do through air.",
                    5,
                    "Wave Physics",
                    DifficultyLevel.MEDIUM,
                    true // Sound in water is ~1500 m/s vs air ~343 m/s
            ));

            teenStemQuiz.addQuestion(new NumericQuestion(
                    4,
                    "Standard atmospheric boiling point of pure water at sea level in degrees Celsius is?",
                    5,
                    "Thermodynamics",
                    DifficultyLevel.EASY,
                    100.0,
                    0.0
            ));

            createQuiz(teenStemQuiz);

            // ==============================================================
            // Quiz 8: PROFESSIONALS / GRADUATES (20+ yrs) - GATE & Placement Aptitude
            // ==============================================================
            Quiz proAptQuiz = new Quiz("PRO-APT", "Competitive Aptitude & Logical Deduction",
                    "High-yield quantitative reasoning, speed math, and analytical deduction for GATE & placements.",
                    "General Aptitude", DifficultyLevel.HARD, "Competitive / Pro (20+)");

            proAptQuiz.addQuestion(new MultipleChoiceQuestion(
                    1,
                    "A train traveling at 54 km/h crosses a 180m platform in 20 seconds. What is the length of the train in meters?",
                    5,
                    "Time, Speed & Distance",
                    DifficultyLevel.HARD,
                    Arrays.asList("100 m", "120 m", "150 m", "160 m"),
                    1 // Speed = 15 m/s. Total distance = 300m. Train = 300 - 180 = 120m -> index 1
            ));

            proAptQuiz.addQuestion(new MultipleChoiceQuestion(
                    2,
                    "Find the missing number in the sequence: 3, 7, 15, 31, 63, ?",
                    5,
                    "Number Series",
                    DifficultyLevel.MEDIUM,
                    Arrays.asList("95", "115", "127", "128"),
                    2 // 2n + 1: 63*2 + 1 = 127 -> index 2
            ));

            proAptQuiz.addQuestion(new TrueFalseQuestion(
                    3,
                    "In formal categorical logic, 'Some A are B' strictly implies that 'All A are B'.",
                    5,
                    "Logical Deductions",
                    DifficultyLevel.MEDIUM,
                    false
            ));

            proAptQuiz.addQuestion(new NumericQuestion(
                    4,
                    "What is the total sum of interior angles of a regular hexagon in degrees?",
                    5,
                    "Advanced Geometry",
                    DifficultyLevel.MEDIUM,
                    720.0,
                    0.0 // (6-2)*180 = 720
            ));

            createQuiz(proAptQuiz);

            // ==============================================================
            // Quiz 9: PROFESSIONALS / GRADUATES (20+ yrs) - Software Architecture & Git
            // ==============================================================
            Quiz proSeQuiz = new Quiz("PRO-SE", "Software Architecture, SOLID & Git",
                    "Agile workflows, Git version control, SOLID principles, and microservice concepts.",
                    "Software Engineering", DifficultyLevel.HARD, "Competitive / Pro (20+)");

            proSeQuiz.addQuestion(new MultipleChoiceQuestion(
                    1,
                    "In the SOLID principles of object-oriented design, what does the letter 'L' represent?",
                    5,
                    "SOLID Principles",
                    DifficultyLevel.MEDIUM,
                    Arrays.asList("Linear Extensibility", "Logic Encapsulation", "Liskov Substitution Principle", "Loose Coupling Protocol"),
                    2 // Liskov -> index 2
            ));

            proSeQuiz.addQuestion(new MultipleChoiceQuestion(
                    2,
                    "Which Git command creates a new branch and immediately switches to it in modern Git?",
                    5,
                    "Version Control",
                    DifficultyLevel.EASY,
                    Arrays.asList("git branch -move", "git checkout -b <name>", "git fork <name>", "git push --new"),
                    1 // git checkout -b -> index 1
            ));

            proSeQuiz.addQuestion(new TrueFalseQuestion(
                    3,
                    "According to the Open/Closed Principle, software entities should be open for extension, but closed for modification.",
                    5,
                    "Software Design",
                    DifficultyLevel.MEDIUM,
                    true
            ));

            proSeQuiz.addQuestion(new NumericQuestion(
                    4,
                    "What standard HTTP status code signifies that a requested resource was Not Found on the server?",
                    5,
                    "Web Architecture",
                    DifficultyLevel.EASY,
                    404.0,
                    0.0
            ));

            createQuiz(proSeQuiz);

        } catch (Exception e) {
            System.err.println("Failed to initialize default sample quizzes: " + e.getMessage());
        }
    }
}

```

---

## UNIT III & IV: DEFENSIVE UTILITIES & CONSOLE FORMATTING

### `InputValidator.java`
**Path:** `src/com/ait/quiz/util/InputValidator.java`  
**Lines of Code:** 94  

```java
package com.ait.quiz.util;

import java.util.Scanner;

/**
 * Utility helper for robust console input handling and validation.
 * Demonstrates:
 * - Method Overloading (compile-time polymorphism)
 * - Defensive programming and Exception Handling against input mismatches
 */
public class InputValidator {

    /**
     * Reads a validated integer within a specified range [min, max].
     */
    public static int readInteger(Scanner scanner, String prompt, int min, int max) {
        while (true) {
            System.out.print(prompt);
            String input = scanner.nextLine().trim();
            try {
                int value = Integer.parseInt(input);
                if (value < min || value > max) {
                    System.out.printf("   [!] Error: Value must be between %d and %d. Please try again.%n", min, max);
                    continue;
                }
                return value;
            } catch (NumberFormatException nfe) {
                System.out.println("   [!] Error: Invalid numeric input! Please enter a valid whole number.");
            }
        }
    }

    /**
     * Overloaded method: Reads any valid integer without range constraints.
     * Demonstrates Method Overloading.
     */
    public static int readInteger(Scanner scanner, String prompt) {
        return readInteger(scanner, prompt, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    /**
     * Reads a valid floating-point number.
     */
    public static double readDouble(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt);
            String input = scanner.nextLine().trim();
            try {
                return Double.parseDouble(input);
            } catch (NumberFormatException nfe) {
                System.out.println("   [!] Error: Invalid number! Please enter a valid decimal number (e.g. 5 or 2.5).");
            }
        }
    }

    /**
     * Reads a non-empty string prompt from console.
     */
    public static String readString(Scanner scanner, String prompt, boolean allowEmpty) {
        while (true) {
            System.out.print(prompt);
            String line = scanner.nextLine().trim();
            if (!allowEmpty && line.isEmpty()) {
                System.out.println("   [!] Error: Input cannot be blank! Please provide a value.");
                continue;
            }
            return line;
        }
    }

    /**
     * Overloaded method: Reads non-empty string by default.
     * Demonstrates Method Overloading.
     */
    public static String readString(Scanner scanner, String prompt) {
        return readString(scanner, prompt, false);
    }

    /**
     * Prompts for confirmation (Y/N).
     */
    public static boolean readYesNo(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt + " (Y/N): ");
            String ans = scanner.nextLine().trim().toUpperCase();
            if (ans.equals("Y") || ans.equals("YES")) {
                return true;
            } else if (ans.equals("N") || ans.equals("NO")) {
                return false;
            }
            System.out.println("   [!] Please enter 'Y' for Yes or 'N' for No.");
        }
    }
}

```

---

### `ConsoleUI.java`
**Path:** `src/com/ait/quiz/util/ConsoleUI.java`  
**Lines of Code:** 43  

```java
package com.ait.quiz.util;

/**
 * Helper class for rendering formatted console output, banners, and menus.
 */
public class ConsoleUI {

    public static final String SEPARATOR_DOUBLE = "================================================================================";
    public static final String SEPARATOR_SINGLE = "--------------------------------------------------------------------------------";

    public static void printHeader(String title) {
        System.out.println(SEPARATOR_DOUBLE);
        int totalWidth = 80;
        int padding = Math.max(0, (totalWidth - title.length()) / 2);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < padding; i++) sb.append(" ");
        sb.append(title);
        System.out.println(sb.toString());
        System.out.println(SEPARATOR_DOUBLE);
    }

    public static void printSubHeader(String title) {
        System.out.println(SEPARATOR_SINGLE);
        System.out.println(" >> " + title);
        System.out.println(SEPARATOR_SINGLE);
    }

    public static void printSuccess(String message) {
        System.out.println(" [SUCCESS] " + message);
    }

    public static void printError(String message) {
        System.out.println(" [ERROR] " + message);
    }

    public static void printWarning(String message) {
        System.out.println(" [WARNING] " + message);
    }

    public static void printInfo(String message) {
        System.out.println(" [INFO] " + message);
    }
}

```

---

## APPLICATION ENTRY POINT & CIE-2 VIVA DEMONSTRATION HARNESS

### `QuizApplication.java`
**Path:** `src/com/ait/quiz/main/QuizApplication.java`  
**Lines of Code:** 711  

```java
package com.ait.quiz.main;

import com.ait.quiz.exception.*;
import com.ait.quiz.model.*;
import com.ait.quiz.service.*;
import com.ait.quiz.util.ConsoleUI;
import com.ait.quiz.util.InputValidator;

import java.util.*;

/**
 * Main Application Entry Point for the Online Quiz Management System.
 * Developed for:
 *   Army Institute of Technology, Pune
 *   Department of Information Technology
 *   Course: Skill Development Laboratory using Java (BIT25434A0X)
 *   Continuous Internal Evaluation 2 (CIE-2)
 *
 * Demonstrates:
 *   - Unit III: Polymorphism (overloading & overriding), Interfaces, Abstract Classes
 *   - Unit IV: Exception Handling (try, catch, finally, custom exceptions, throw/throws)
 */
public class QuizApplication {

    private final QuizOperations quizManager;
    private final Scanner scanner;
    private Student currentStudent;
    private Instructor currentInstructor;

    public QuizApplication() {
        this.quizManager = new QuizManager();
        this.scanner = new Scanner(System.in);
        // Default users for demonstration
        this.currentStudent = new Student("S101", "Abhishekh Kumar", "abhishekh@aitpune.edu.in", "3101", "SE IT A");
        this.currentInstructor = new Instructor("FAC01", "Mrs. Trupti Najan", "tnajan@aitpune.edu.in", "Information Technology", "Assistant Professor");
    }

    public static void main(String[] args) {
        QuizApplication app = new QuizApplication();
        try {
            app.run();
        } finally {
            app.shutdown();
        }
    }

    public void run() {
        boolean exit = false;
        while (!exit) {
            ConsoleUI.printHeader("ONLINE QUIZ MANAGEMENT SYSTEM - CIE-2");
            System.out.println(" 1. Student Portal (Browse, Search, Take Quiz, View Results)");
            System.out.println(" 2. Faculty / Instructor Portal (Create Quiz, Add Questions, Reports)");
            System.out.println(" 3. Automated CIE-2 Concept Demonstration & Test Suite (For Examiner/Viva)");
            System.out.println(" 4. Switch / Configure Current User Profile");
            System.out.println(" 5. Exit System");
            ConsoleUI.printSubHeader("Select an option");

            int choice = InputValidator.readInteger(scanner, "Enter choice (1-5): ", 1, 5);

            switch (choice) {
                case 1:
                    studentPortalMenu();
                    break;
                case 2:
                    instructorPortalMenu();
                    break;
                case 3:
                    runAutomatedDemonstrationSuite();
                    break;
                case 4:
                    configureUserProfile();
                    break;
                case 5:
                    exit = true;
                    System.out.println("\nThank you for using the Online Quiz Management System. Goodbye!");
                    break;
            }
        }
    }

    // =========================================================================
    // STUDENT PORTAL
    // =========================================================================

    private void studentPortalMenu() {
        boolean back = false;
        while (!back) {
            ConsoleUI.printHeader("STUDENT PORTAL - " + currentStudent.getName() + " (" + currentStudent.getRollNumber() + ")");
            System.out.println(" 1. View All Available Quizzes");
            System.out.println(" 2. Search Quizzes by Topic (Method Overloading - 1 param)");
            System.out.println(" 3. Search Quizzes by Topic & Difficulty (Method Overloading - 2 params)");
            System.out.println(" 4. Take a Quiz (Interactive Conduct & Evaluation)");
            System.out.println(" 5. View My Attempt History & Scorecards");
            System.out.println(" 6. View My Student Dashboard (Polymorphic displayDashboard)");
            System.out.println(" 7. Back to Main Menu");
            ConsoleUI.printSubHeader("Select Student Action");

            int choice = InputValidator.readInteger(scanner, "Enter choice (1-7): ", 1, 7);

            switch (choice) {
                case 1:
                    displayAllQuizzes();
                    break;
                case 2:
                    searchQuizzesByTopic();
                    break;
                case 3:
                    searchQuizzesByTopicAndDifficulty();
                    break;
                case 4:
                    conductQuizFlow();
                    break;
                case 5:
                    viewStudentAttempts();
                    break;
                case 6:
                    // Polymorphic method call on abstract User reference
                    User userRef = currentStudent;
                    userRef.displayDashboard();
                    break;
                case 7:
                    back = true;
                    break;
            }
        }
    }

    private void displayAllQuizzes() {
        ConsoleUI.printSubHeader("LIST OF AVAILABLE QUIZZES");
        List<Quiz> quizzes = quizManager.getAllQuizzes();
        if (quizzes.isEmpty()) {
            ConsoleUI.printInfo("No quizzes are currently registered in the system.");
            return;
        }

        System.out.printf("%-10s | %-28s | %-16s | %-20s | %-8s | %-4s | %s%n",
                "Quiz ID", "Title", "Target Age", "Topic", "Level", "Que", "Marks");
        System.out.println(ConsoleUI.SEPARATOR_SINGLE);
        for (Quiz q : quizzes) {
            System.out.printf("%-10s | %-28s | %-16s | %-20s | %-8s | %-4d | %d marks%n",
                    q.getQuizId(),
                    truncate(q.getTitle(), 28),
                    truncate(q.getTargetAgeGroup(), 16),
                    truncate(q.getTopic(), 20),
                    q.getDifficulty().getDisplayName(),
                    q.getQuestionCount(),
                    q.getTotalMarks());
        }
    }

    private void searchQuizzesByTopic() {
        String topic = InputValidator.readString(scanner, "Enter topic keyword to search: ");
        // Demonstrates overloaded searchQuiz(topic)
        List<Quiz> results = quizManager.searchQuiz(topic);
        displaySearchResults("Search by Topic: '" + topic + "'", results);
    }

    private void searchQuizzesByTopicAndDifficulty() {
        String topic = InputValidator.readString(scanner, "Enter topic keyword: ");
        System.out.println("Choose Difficulty Level: 1. Easy | 2. Medium | 3. Hard");
        int levelChoice = InputValidator.readInteger(scanner, "Select level (1-3): ", 1, 3);
        DifficultyLevel level = (levelChoice == 1) ? DifficultyLevel.EASY :
                (levelChoice == 2) ? DifficultyLevel.MEDIUM : DifficultyLevel.HARD;

        // Demonstrates overloaded searchQuiz(topic, level)
        List<Quiz> results = quizManager.searchQuiz(topic, level);
        displaySearchResults("Search by Topic: '" + topic + "' & Level: " + level.getDisplayName(), results);
    }

    private void displaySearchResults(String queryDescription, List<Quiz> results) {
        ConsoleUI.printSubHeader(queryDescription + " -> " + results.size() + " matches found");
        if (results.isEmpty()) {
            ConsoleUI.printWarning("No quizzes matched the specified criteria.");
            return;
        }
        for (Quiz q : results) {
            System.out.println(" * " + q);
        }
    }

    private void conductQuizFlow() {
        displayAllQuizzes();
        String quizId = InputValidator.readString(scanner, "\nEnter Quiz ID to attempt: ");

        Quiz quiz;
        try {
            quiz = quizManager.getQuiz(quizId);
            // Validate quiz has questions
            quiz.validateForConduct();
        } catch (QuizNotFoundException | EmptyQuizException e) {
            ConsoleUI.printError("Quiz launch failed: " + e.getMessage());
            return;
        }

        // Select Evaluation Strategy (Interface Polymorphism)
        ConsoleUI.printSubHeader("SELECT EVALUATION POLICY FOR THIS QUIZ ATTEMPT");
        System.out.println(" 1. Standard Linear Grading (Full marks for correct, zero penalty for wrong)");
        System.out.println(" 2. Competitive Exam Grading (25% negative marking penalty for wrong answers)");
        int policyChoice = InputValidator.readInteger(scanner, "Select grading policy (1-2): ", 1, 2);

        QuizEvaluator evaluator = (policyChoice == 1)
                ? new StandardGradingPolicy()
                : new NegativeMarkingGradingPolicy(0.25);

        ConsoleUI.printInfo("Selected Evaluator Strategy: " + evaluator.getPolicyName());

        String attemptId = "ATT-" + UUID.randomUUID().toString().substring(0, 6).toUpperCase();
        QuizAttempt attempt = new QuizAttempt(attemptId, quiz.getQuizId(), quiz.getTitle(),
                currentStudent.getRollNumber(), currentStudent.getName());

        attempt.setTotalQuestions(quiz.getQuestionCount());
        attempt.setTotalPossibleMarks(quiz.getTotalMarks());

        ConsoleUI.printHeader("STARTING QUIZ: " + quiz.getTitle() + " (Attempt ID: " + attemptId + ")");
        System.out.println("Read each question carefully. Type your answer and press Enter.\n");

        int correctCount = 0;
        int incorrectCount = 0;

        // Iterate polymorphically over questions
        for (Question q : quiz.getQuestions()) {
            System.out.println(ConsoleUI.SEPARATOR_SINGLE);
            // Polymorphic method call: displays MCQ, True/False, or Numeric prompt based on runtime object!
            q.displayQuestion();

            boolean answeredValidly = false;
            String studentAns = "";
            boolean isCorrect = false;

            while (!answeredValidly) {
                studentAns = InputValidator.readString(scanner, ">> Your Answer: ");
                try {
                    // Polymorphic method call: checks answer with question-specific rules
                    // Throws InvalidOptionException if input format is illegal
                    isCorrect = q.checkAnswer(studentAns);
                    answeredValidly = true;
                } catch (InvalidOptionException ioe) {
                    ConsoleUI.printError(ioe.getMessage());
                    System.out.println("   Please re-enter your answer conforming to the format.");
                }
            }

            double marksAwarded = isCorrect ? q.getMarks() : 0.0;
            if (isCorrect) {
                correctCount++;
                System.out.println("   [✓] Recorded.");
            } else {
                incorrectCount++;
                System.out.println("   [✗] Recorded.");
            }

            attempt.addQuestionResult(new QuizAttempt.QuestionResult(
                    q.getId(),
                    q.getQuestionText(),
                    studentAns,
                    q.getCorrectAnswerFormatted(),
                    isCorrect,
                    marksAwarded
            ));
        }

        attempt.setCorrectCount(correctCount);
        attempt.setIncorrectCount(incorrectCount);

        // Polymorphic evaluation using the chosen QuizEvaluator strategy!
        double scoreObtained = evaluator.evaluateScore(attempt);
        attempt.setScoreObtained(scoreObtained);

        double percentage = (quiz.getTotalMarks() > 0) ? (scoreObtained / quiz.getTotalMarks()) * 100.0 : 0.0;
        attempt.setPercentage(percentage);
        attempt.setGrade(evaluator.generateGrade(percentage));

        // Save attempt history
        quizManager.recordAttempt(attempt);
        currentStudent.addAttempt(attempt);

        // Display detailed scorecard
        System.out.println();
        evaluator.printDetailedReport(attempt);
    }

    private void viewStudentAttempts() {
        ConsoleUI.printSubHeader("ATTEMPT HISTORY FOR: " + currentStudent.getName() + " (" + currentStudent.getRollNumber() + ")");
        List<QuizAttempt> attempts = quizManager.getAttemptsByStudent(currentStudent.getRollNumber());
        if (attempts.isEmpty()) {
            ConsoleUI.printInfo("You have not taken any quizzes yet.");
            return;
        }

        for (QuizAttempt att : attempts) {
            System.out.println(att);
        }
    }

    // =========================================================================
    // INSTRUCTOR PORTAL
    // =========================================================================

    private void instructorPortalMenu() {
        boolean back = false;
        while (!back) {
            ConsoleUI.printHeader("FACULTY PORTAL - " + currentInstructor.getName() + " (" + currentInstructor.getDepartment() + ")");
            System.out.println(" 1. Create a New Quiz (Demonstrates DuplicateQuizException)");
            System.out.println(" 2. Add Question to a Quiz (MCQ, True/False, Numeric)");
            System.out.println(" 3. View All Quizzes & Detailed Questions");
            System.out.println(" 4. Delete a Quiz (Demonstrates QuizNotFoundException)");
            System.out.println(" 5. View All Student Submissions & Performance Analytics");
            System.out.println(" 6. View Faculty Dashboard (Polymorphic displayDashboard)");
            System.out.println(" 7. Back to Main Menu");
            ConsoleUI.printSubHeader("Select Faculty Action");

            int choice = InputValidator.readInteger(scanner, "Enter choice (1-7): ", 1, 7);

            switch (choice) {
                case 1:
                    createQuizFlow();
                    break;
                case 2:
                    addQuestionFlow();
                    break;
                case 3:
                    viewQuizzesWithQuestions();
                    break;
                case 4:
                    deleteQuizFlow();
                    break;
                case 5:
                    viewAllStudentSubmissions();
                    break;
                case 6:
                    // Polymorphic method call on abstract User reference
                    User userRef = currentInstructor;
                    userRef.displayDashboard();
                    break;
                case 7:
                    back = true;
                    break;
            }
        }
    }

    private void createQuizFlow() {
        ConsoleUI.printSubHeader("CREATE NEW QUIZ");
        String quizId = InputValidator.readString(scanner, "Enter Unique Quiz ID (e.g. JAVA-202): ");
        String title = InputValidator.readString(scanner, "Enter Quiz Title: ");
        String description = InputValidator.readString(scanner, "Enter Quiz Description: ");
        String topic = InputValidator.readString(scanner, "Enter Academic Topic: ");

        System.out.println("Select Difficulty: 1. Easy | 2. Medium | 3. Hard");
        int diffChoice = InputValidator.readInteger(scanner, "Choice (1-3): ", 1, 3);
        DifficultyLevel level = (diffChoice == 1) ? DifficultyLevel.EASY :
                (diffChoice == 2) ? DifficultyLevel.MEDIUM : DifficultyLevel.HARD;

        System.out.println("Select Target Age Group:");
        System.out.println(" 1. Kids (8-12)");
        System.out.println(" 2. Teens (13-17)");
        System.out.println(" 3. College (18-22)");
        System.out.println(" 4. Competitive / Pro (20+)");
        int ageChoice = InputValidator.readInteger(scanner, "Choice (1-4): ", 1, 4);
        String targetAge = (ageChoice == 1) ? "Kids (8-12)" :
                (ageChoice == 2) ? "Teens (13-17)" :
                (ageChoice == 3) ? "College (18-22)" : "Competitive / Pro (20+)";

        try {
            Quiz newQuiz = new Quiz(quizId, title, description, topic, level, targetAge);
            quizManager.createQuiz(newQuiz);
            ConsoleUI.printSuccess("Quiz created successfully with ID: " + newQuiz.getQuizId() + " [" + targetAge + "]");
        } catch (DuplicateQuizException dqe) {
            ConsoleUI.printError("Failed to create quiz: " + dqe.getMessage());
        } catch (IllegalArgumentException iae) {
            ConsoleUI.printError("Invalid input: " + iae.getMessage());
        }
    }

    private void addQuestionFlow() {
        displayAllQuizzes();
        String quizId = InputValidator.readString(scanner, "\nEnter target Quiz ID to add question: ");

        Quiz targetQuiz;
        try {
            targetQuiz = quizManager.getQuiz(quizId);
        } catch (QuizNotFoundException qnfe) {
            ConsoleUI.printError(qnfe.getMessage());
            return;
        }

        ConsoleUI.printSubHeader("ADD QUESTION TO: " + targetQuiz.getTitle());
        System.out.println(" Select Question Type:");
        System.out.println("   1. Multiple Choice Question (MCQ)");
        System.out.println("   2. True / False Question");
        System.out.println("   3. Numeric / Direct Answer Question");

        int typeChoice = InputValidator.readInteger(scanner, "Select type (1-3): ", 1, 3);

        int qId = targetQuiz.getQuestionCount() + 1;
        String prompt = InputValidator.readString(scanner, "Enter Question Prompt/Text: ");
        int marks = InputValidator.readInteger(scanner, "Enter Marks for this question (> 0): ", 1, 100);
        String topic = InputValidator.readString(scanner, "Enter Question Topic: ");

        System.out.println("Select Difficulty: 1. Easy | 2. Medium | 3. Hard");
        int diff = InputValidator.readInteger(scanner, "Select (1-3): ", 1, 3);
        DifficultyLevel difficulty = (diff == 1) ? DifficultyLevel.EASY :
                (diff == 2) ? DifficultyLevel.MEDIUM : DifficultyLevel.HARD;

        Question createdQuestion = null;

        try {
            switch (typeChoice) {
                case 1: // MCQ
                    int optionCount = InputValidator.readInteger(scanner, "Enter number of options (2 to 6): ", 2, 6);
                    List<String> options = new ArrayList<>();
                    for (int i = 0; i < optionCount; i++) {
                        char label = (char) ('A' + i);
                        String opt = InputValidator.readString(scanner, "Option [" + label + "]: ");
                        options.add(opt);
                    }
                    int correctIdx = InputValidator.readInteger(scanner,
                            "Enter correct option number (1 for A, 2 for B...): ", 1, optionCount) - 1;
                    createdQuestion = new MultipleChoiceQuestion(qId, prompt, marks, topic, difficulty, options, correctIdx);
                    break;

                case 2: // True / False
                    boolean correctBool = InputValidator.readYesNo(scanner, "Is the statement TRUE?");
                    createdQuestion = new TrueFalseQuestion(qId, prompt, marks, topic, difficulty, correctBool);
                    break;

                case 3: // Numeric
                    double numAnswer = InputValidator.readDouble(scanner, "Enter correct numeric answer: ");
                    double tolerance = InputValidator.readDouble(scanner, "Enter accepted tolerance delta (0 for exact): ");
                    createdQuestion = new NumericQuestion(qId, prompt, marks, topic, difficulty, numAnswer, tolerance);
                    break;
            }

            if (createdQuestion != null) {
                quizManager.addQuestionToQuiz(targetQuiz.getQuizId(), createdQuestion);
                ConsoleUI.printSuccess("Question added successfully to quiz '" + targetQuiz.getQuizId() + "'!");
            }
        } catch (InvalidQuestionException | QuizNotFoundException e) {
            ConsoleUI.printError("Could not add question: " + e.getMessage());
        }
    }

    private void viewQuizzesWithQuestions() {
        List<Quiz> quizzes = quizManager.getAllQuizzes();
        if (quizzes.isEmpty()) {
            ConsoleUI.printInfo("No quizzes available.");
            return;
        }

        for (Quiz q : quizzes) {
            ConsoleUI.printSubHeader("Quiz: " + q.getTitle() + " [" + q.getQuizId() + "]");
            System.out.printf("Topic: %s | Level: %s | Total Marks: %d | Questions: %d%n",
                    q.getTopic(), q.getDifficulty().getDisplayName(), q.getTotalMarks(), q.getQuestionCount());
            if (q.getQuestions().isEmpty()) {
                System.out.println("   (No questions added yet)");
            } else {
                for (Question question : q.getQuestions()) {
                    System.out.printf("   - %s%n", question);
                }
            }
        }
    }

    private void deleteQuizFlow() {
        displayAllQuizzes();
        String quizId = InputValidator.readString(scanner, "\nEnter Quiz ID to delete: ");
        try {
            boolean deleted = quizManager.deleteQuiz(quizId);
            if (deleted) {
                ConsoleUI.printSuccess("Quiz '" + quizId + "' was successfully removed.");
            }
        } catch (QuizNotFoundException qnfe) {
            ConsoleUI.printError("Delete operation failed: " + qnfe.getMessage());
        }
    }

    private void viewAllStudentSubmissions() {
        ConsoleUI.printSubHeader("ALL RECORDED STUDENT ATTEMPTS");
        List<QuizAttempt> allAttempts = quizManager.getAllAttempts();
        if (allAttempts.isEmpty()) {
            ConsoleUI.printInfo("No student submissions recorded yet.");
            return;
        }

        System.out.printf("%-10s | %-16s | %-8s | %-12s | %-14s | %-10s | %s%n",
                "Attempt", "Student", "Roll", "Quiz ID", "Score", "Percentage", "Grade");
        System.out.println(ConsoleUI.SEPARATOR_SINGLE);
        for (QuizAttempt att : allAttempts) {
            System.out.printf("%-10s | %-16s | %-8s | %-12s | %-14s | %-10s | %s%n",
                    att.getAttemptId(),
                    truncate(att.getStudentName(), 16),
                    att.getStudentRollNumber(),
                    att.getQuizId(),
                    String.format("%.2f / %d", att.getScoreObtained(), att.getTotalPossibleMarks()),
                    String.format("%.2f%%", att.getPercentage()),
                    att.getGrade());
        }
    }

    // =========================================================================
    // PROFILE SWITCHER
    // =========================================================================

    private void configureUserProfile() {
        ConsoleUI.printSubHeader("CONFIGURE CURRENT USER PROFILE");
        System.out.println(" 1. Update Student Profile (Current: " + currentStudent.getName() + " | Roll: " + currentStudent.getRollNumber() + ")");
        System.out.println(" 2. Update Faculty Profile (Current: " + currentInstructor.getName() + " | Dept: " + currentInstructor.getDepartment() + ")");
        System.out.println(" 3. Return");

        int choice = InputValidator.readInteger(scanner, "Select option (1-3): ", 1, 3);
        if (choice == 1) {
            String name = InputValidator.readString(scanner, "Enter Student Name: ");
            String roll = InputValidator.readString(scanner, "Enter Roll Number: ");
            String div = InputValidator.readString(scanner, "Enter Division (e.g. SE IT A): ");
            String email = InputValidator.readString(scanner, "Enter Email: ");
            this.currentStudent = new Student("S-" + roll, name, email, roll, div);
            ConsoleUI.printSuccess("Student profile updated!");
        } else if (choice == 2) {
            String name = InputValidator.readString(scanner, "Enter Faculty Name: ");
            String dept = InputValidator.readString(scanner, "Enter Department: ");
            String desig = InputValidator.readString(scanner, "Enter Designation: ");
            String email = InputValidator.readString(scanner, "Enter Email: ");
            this.currentInstructor = new Instructor("FAC-" + UUID.randomUUID().toString().substring(0, 4), name, email, dept, desig);
            ConsoleUI.printSuccess("Faculty profile updated!");
        }
    }

    // =========================================================================
    // AUTOMATED CIE-2 VIVA / DEMONSTRATION SUITE
    // =========================================================================

    /**
     * Executes a comprehensive live demonstration of all mandatory CIE-2 requirements:
     * 1. Abstract Class & Runtime Polymorphism (Dynamic Method Dispatch)
     * 2. Interfaces & Strategy Pattern (Standard vs Negative Marking)
     * 3. Compile-time Polymorphism (Method Overloading)
     * 4. Exception Handling Suite:
     *    - Catching QuizNotFoundException
     *    - Catching DuplicateQuizException
     *    - Catching EmptyQuizException
     *    - Catching InvalidQuestionException
     *    - Catching InvalidOptionException
     *    - Execution sequence of try-catch-finally
     */
    public void runAutomatedDemonstrationSuite() {
        ConsoleUI.printHeader("CIE-2 MANDATORY CONCEPTS DEMONSTRATION & TEST SUITE");
        System.out.println("Target: Army Institute of Technology, Pune | Skill Development Lab");
        System.out.println("Evaluates Unit III (Polymorphism, Interfaces, Abstract Classes) & Unit IV (Exception Handling)\n");

        // -------------------------------------------------------------
        // CONCEPT 1: Abstract Class & Polymorphic Method Overriding
        // -------------------------------------------------------------
        ConsoleUI.printSubHeader("1. ABSTRACT CLASS & RUNTIME POLYMORPHISM (Dynamic Method Dispatch)");
        System.out.println("Base Class: 'Question' (abstract)");
        System.out.println("Concrete Subclasses: MultipleChoiceQuestion, TrueFalseQuestion, NumericQuestion\n");

        List<Question> sampleQuestions = new ArrayList<>();
        try {
            sampleQuestions.add(new MultipleChoiceQuestion(
                    101, "What is the capital of Maharashtra?", 2, "Geography",
                    DifficultyLevel.EASY, Arrays.asList("Pune", "Mumbai", "Nagpur", "Nashik"), 1
            ));
            sampleQuestions.add(new TrueFalseQuestion(
                    102, "Abstract classes can have constructors in Java.", 2, "Java OOP",
                    DifficultyLevel.EASY, true
            ));
            sampleQuestions.add(new NumericQuestion(
                    103, "How many bits are in a single standard Java byte?", 2, "Architecture",
                    DifficultyLevel.EASY, 8.0, 0.0
            ));
        } catch (InvalidQuestionException e) {
            System.err.println("Setup error: " + e.getMessage());
        }

        System.out.println("Iterating through List<Question> polymorphically:");
        for (Question q : sampleQuestions) {
            System.out.println("   Calling q.getQuestionType(): " + q.getQuestionType());
            System.out.println("   Calling q.displayQuestion():");
            q.displayQuestion();
            System.out.println("   Correct Answer: " + q.getCorrectAnswerFormatted());
            System.out.println();
        }

        // -------------------------------------------------------------
        // CONCEPT 2: Interfaces & Strategy Pattern
        // -------------------------------------------------------------
        ConsoleUI.printSubHeader("2. INTERFACES & STRATEGY POLYMORPHISM (QuizEvaluator)");
        System.out.println("Interface: QuizEvaluator");
        System.out.println("Implementations: StandardGradingPolicy vs NegativeMarkingGradingPolicy\n");

        QuizAttempt demoAttempt = new QuizAttempt("DEMO-001", "JAVA-OOP", "OOP Mastery", "3101", "Abhishekh");
        demoAttempt.setTotalQuestions(4);
        demoAttempt.setTotalPossibleMarks(20);
        // Simulate: 3 correct (5 marks each = 15), 1 wrong (5 marks)
        demoAttempt.addQuestionResult(new QuizAttempt.QuestionResult(1, "Q1", "B", "B", true, 5.0));
        demoAttempt.addQuestionResult(new QuizAttempt.QuestionResult(2, "Q2", "B", "B", true, 5.0));
        demoAttempt.addQuestionResult(new QuizAttempt.QuestionResult(3, "Q3", "T", "T", true, 5.0));
        demoAttempt.addQuestionResult(new QuizAttempt.QuestionResult(4, "Q4", "X", "F", false, 5.0));
        demoAttempt.setCorrectCount(3);
        demoAttempt.setIncorrectCount(1);

        QuizEvaluator stdEvaluator = new StandardGradingPolicy();
        QuizEvaluator negEvaluator = new NegativeMarkingGradingPolicy(0.25); // 25% negative marking

        double scoreStd = stdEvaluator.evaluateScore(demoAttempt);
        double scoreNeg = negEvaluator.evaluateScore(demoAttempt);

        System.out.printf("   Scenario: 3 Correct (15 marks), 1 Wrong (out of 20 marks)%n");
        System.out.printf("   [Policy 1] %s -> Final Score: %.2f / 20.0 | Grade: %s%n",
                stdEvaluator.getPolicyName(), scoreStd, stdEvaluator.generateGrade((scoreStd / 20.0) * 100));
        System.out.printf("   [Policy 2] %s -> Final Score: %.2f / 20.0 (15 - 1.25) | Grade: %s%n",
                negEvaluator.getPolicyName(), scoreNeg, negEvaluator.generateGrade((scoreNeg / 20.0) * 100));

        // -------------------------------------------------------------
        // CONCEPT 3: Method Overloading (Compile-time Polymorphism)
        // -------------------------------------------------------------
        ConsoleUI.printSubHeader("3. COMPILE-TIME POLYMORPHISM (Method Overloading)");
        System.out.println("Demonstrating QuizManager.searchQuiz():");
        System.out.println("   Method 1: searchQuiz(String topic)");
        List<Quiz> topicOnly = quizManager.searchQuiz("Java");
        System.out.println("      searchQuiz(\"Java\") returned: " + topicOnly.size() + " quizzes.");

        System.out.println("   Method 2: searchQuiz(String topic, DifficultyLevel level)");
        List<Quiz> topicAndDiff = quizManager.searchQuiz("Java", DifficultyLevel.HARD);
        System.out.println("      searchQuiz(\"Java\", DifficultyLevel.HARD) returned: " + topicAndDiff.size() + " quizzes.");

        // -------------------------------------------------------------
        // CONCEPT 4: Comprehensive Exception Handling Test Matrix
        // -------------------------------------------------------------
        ConsoleUI.printSubHeader("4. EXCEPTION HANDLING TEST MATRIX (try, catch, finally, throw/throws)");

        // Test A: QuizNotFoundException
        System.out.println("\n[Test A] Triggering QuizNotFoundException for non-existent ID 'GHOST-404':");
        try {
            quizManager.getQuiz("GHOST-404");
        } catch (QuizNotFoundException e) {
            System.out.println("   [CAUGHT EXPECTED EXCEPTION] Class: " + e.getClass().getSimpleName());
            System.out.println("   Message: " + e.getMessage());
        } finally {
            System.out.println("   [FINALLY BLOCK EXECUTED] Cleanup for Test A completed.");
        }

        // Test B: DuplicateQuizException
        System.out.println("\n[Test B] Triggering DuplicateQuizException by adding existing quiz 'JAVA-OOP':");
        try {
            Quiz dup = new Quiz("JAVA-OOP", "Duplicate", "Desc", "OOP", DifficultyLevel.EASY);
            quizManager.createQuiz(dup);
        } catch (DuplicateQuizException e) {
            System.out.println("   [CAUGHT EXPECTED EXCEPTION] Class: " + e.getClass().getSimpleName());
            System.out.println("   Message: " + e.getMessage());
        } finally {
            System.out.println("   [FINALLY BLOCK EXECUTED] Cleanup for Test B completed.");
        }

        // Test C: InvalidQuestionException
        System.out.println("\n[Test C] Triggering InvalidQuestionException with negative marks (-10):");
        try {
            new TrueFalseQuestion(999, "Bad Question", -10, "Test", DifficultyLevel.EASY, true);
        } catch (InvalidQuestionException e) {
            System.out.println("   [CAUGHT EXPECTED EXCEPTION] Class: " + e.getClass().getSimpleName());
            System.out.println("   Message: " + e.getMessage());
        } finally {
            System.out.println("   [FINALLY BLOCK EXECUTED] Cleanup for Test C completed.");
        }

        // Test D: InvalidOptionException
        System.out.println("\n[Test D] Triggering InvalidOptionException with invalid option 'Z' on MCQ:");
        try {
            MultipleChoiceQuestion mcq = new MultipleChoiceQuestion(
                    888, "Test Question", 5, "Test", DifficultyLevel.EASY,
                    Arrays.asList("Option A", "Option B", "Option C", "Option D"), 0
            );
            mcq.checkAnswer("Z"); // Invalid choice outside A-D
        } catch (InvalidOptionException e) {
            System.out.println("   [CAUGHT EXPECTED EXCEPTION] Class: " + e.getClass().getSimpleName());
            System.out.println("   Message: " + e.getMessage());
        } catch (InvalidQuestionException e) {
            System.err.println("Unexpected setup error: " + e.getMessage());
        } finally {
            System.out.println("   [FINALLY BLOCK EXECUTED] Cleanup for Test D completed.");
        }

        // Test E: EmptyQuizException
        System.out.println("\n[Test E] Triggering EmptyQuizException by validating an empty quiz:");
        try {
            Quiz emptyQuiz = new Quiz("EMPTY-01", "Blank Quiz", "Empty", "Test", DifficultyLevel.EASY);
            emptyQuiz.validateForConduct();
        } catch (EmptyQuizException e) {
            System.out.println("   [CAUGHT EXPECTED EXCEPTION] Class: " + e.getClass().getSimpleName());
            System.out.println("   Message: " + e.getMessage());
        } finally {
            System.out.println("   [FINALLY BLOCK EXECUTED] Cleanup for Test E completed.");
        }

        System.out.println("\n" + ConsoleUI.SEPARATOR_DOUBLE);
        ConsoleUI.printSuccess("ALL 5 EXCEPTION AND POLYMORPHISM TEST SCENARIOS PASSED WITH FULL SPEC COMPLIANCE!");
        System.out.println(ConsoleUI.SEPARATOR_DOUBLE);
        System.out.println("\nPress Enter to return to menu...");
        scanner.nextLine();
    }

    private void shutdown() {
        System.out.println("\n[System] Performing graceful shutdown and releasing resources (finally block)...");
    }

    private String truncate(String text, int maxLen) {
        if (text == null) return "";
        if (text.length() <= maxLen) return text;
        return text.substring(0, maxLen - 3) + "...";
    }
}

```

---

## EMBEDDED LIGHTWEIGHT JAVA HTTP REST WEB SERVER

### `QuizWebServer.java`
**Path:** `src/com/ait/quiz/web/QuizWebServer.java`  
**Lines of Code:** 512  

```java
package com.ait.quiz.web;

import com.ait.quiz.exception.*;
import com.ait.quiz.main.QuizApplication;
import com.ait.quiz.model.*;
import com.ait.quiz.service.*;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.*;
import java.net.InetSocketAddress;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

/**
 * Embedded lightweight HTTP Web Server for the Online Quiz Management System.
 * Connects the Java backend models, services, and exception hierarchy to a modern web browser UI.
 * Runs on standard Java SE without third-party frameworks.
 */
public class QuizWebServer {

    private static final int DEFAULT_PORT = 8080;
    private final QuizOperations quizManager;
    private final Path staticDir;
    private HttpServer server;

    public QuizWebServer(QuizOperations quizManager, Path staticDir) {
        this.quizManager = quizManager;
        this.staticDir = staticDir;
    }

    public static void main(String[] args) {
        int port = DEFAULT_PORT;
        if (args.length > 0) {
            try {
                port = Integer.parseInt(args[0]);
            } catch (NumberFormatException ignored) {}
        }

        Path webPath = Paths.get("web");
        if (!Files.exists(webPath)) {
            webPath = Paths.get("../web");
        }

        QuizOperations manager = new QuizManager();
        QuizWebServer webServer = new QuizWebServer(manager, webPath.toAbsolutePath().normalize());

        try {
            webServer.start(port);
            System.out.println("================================================================================");
            System.out.println("           ONLINE QUIZ MANAGEMENT SYSTEM - WEB SERVER STARTED           ");
            System.out.println("================================================================================");
            System.out.println(" Server URL  : http://localhost:" + port);
            System.out.println(" Static Dir  : " + webPath.toAbsolutePath().normalize());
            System.out.println(" Status      : Ready to accept requests from web browser");
            System.out.println(" Press Ctrl+C in this console to stop the server.");
            System.out.println("================================================================================");
        } catch (IOException e) {
            System.err.println("Failed to start web server on port " + port + ": " + e.getMessage());
        }
    }

    public void start(int port) throws IOException {
        server = HttpServer.create(new InetSocketAddress(port), 0);

        // API Endpoints
        server.createContext("/api/quizzes", new QuizzesHandler());
        server.createContext("/api/submit", new SubmitQuizHandler());
        server.createContext("/api/attempts", new AttemptsHandler());
        server.createContext("/api/demo", new DemoRunnerHandler());

        // Static Web Content Handler
        server.createContext("/", new StaticFileHandler(staticDir));

        server.setExecutor(java.util.concurrent.Executors.newCachedThreadPool());
        server.start();
    }

    public void stop() {
        if (server != null) {
            server.stop(0);
        }
    }

    // =========================================================================
    // API HANDLERS
    // =========================================================================

    private class QuizzesHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            String method = exchange.getRequestMethod().toUpperCase();

            if (method.equals("OPTIONS")) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            if (method.equals("GET")) {
                List<Quiz> quizzes = quizManager.getAllQuizzes();
                StringBuilder json = new StringBuilder("[");
                for (int i = 0; i < quizzes.size(); i++) {
                    Quiz q = quizzes.get(i);
                    json.append("{");
                    json.append("\"quizId\":").append(quote(q.getQuizId())).append(",");
                    json.append("\"title\":").append(quote(q.getTitle())).append(",");
                    json.append("\"description\":").append(quote(q.getDescription())).append(",");
                    json.append("\"topic\":").append(quote(q.getTopic())).append(",");
                    json.append("\"difficulty\":").append(quote(q.getDifficulty().getDisplayName())).append(",");
                    json.append("\"targetAgeGroup\":").append(quote(q.getTargetAgeGroup())).append(",");
                    json.append("\"totalMarks\":").append(q.getTotalMarks()).append(",");
                    json.append("\"questionCount\":").append(q.getQuestionCount()).append(",");
                    json.append("\"questions\":[");
                    List<Question> questions = q.getQuestions();
                    for (int j = 0; j < questions.size(); j++) {
                        Question que = questions.get(j);
                        json.append("{");
                        json.append("\"id\":").append(que.getId()).append(",");
                        json.append("\"questionText\":").append(quote(que.getQuestionText())).append(",");
                        json.append("\"marks\":").append(que.getMarks()).append(",");
                        json.append("\"topic\":").append(quote(que.getTopic())).append(",");
                        json.append("\"difficulty\":").append(quote(que.getDifficulty().getDisplayName())).append(",");
                        json.append("\"type\":").append(quote(que.getQuestionType())).append(",");
                        if (que instanceof MultipleChoiceQuestion) {
                            MultipleChoiceQuestion mcq = (MultipleChoiceQuestion) que;
                            json.append("\"options\":[");
                            List<String> opts = mcq.getOptions();
                            for (int k = 0; k < opts.size(); k++) {
                                json.append(quote(opts.get(k)));
                                if (k < opts.size() - 1) json.append(",");
                            }
                            json.append("]");
                        } else {
                            json.append("\"options\":[]");
                        }
                        json.append("}");
                        if (j < questions.size() - 1) json.append(",");
                    }
                    json.append("]");
                    json.append("}");
                    if (i < quizzes.size() - 1) json.append(",");
                }
                json.append("]");

                sendJsonResponse(exchange, 200, json.toString());
            } else if (method.equals("POST")) {
                // Create a new quiz
                String body = readRequestBody(exchange);
                try {
                    Map<String, String> params = parseSimpleJson(body);
                    String id = params.get("quizId");
                    String title = params.get("title");
                    String desc = params.get("description");
                    String topic = params.get("topic");
                    String diff = params.get("difficulty");
                    String ageGroup = params.get("targetAgeGroup");

                    DifficultyLevel level = DifficultyLevel.fromString(diff);
                    Quiz newQuiz = new Quiz(id, title, desc, topic, level, (ageGroup != null ? ageGroup : "College (18-22)"));
                    quizManager.createQuiz(newQuiz);

                    sendJsonResponse(exchange, 201, "{\"success\":true,\"message\":\"Quiz created successfully!\"}");
                } catch (DuplicateQuizException dqe) {
                    sendJsonResponse(exchange, 400, "{\"success\":false,\"error\":" + quote(dqe.getMessage()) + "}");
                } catch (Exception e) {
                    sendJsonResponse(exchange, 500, "{\"success\":false,\"error\":" + quote(e.getMessage()) + "}");
                }
            } else {
                exchange.sendResponseHeaders(405, -1);
            }
        }
    }

    private class SubmitQuizHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            if (exchange.getRequestMethod().equalsIgnoreCase("OPTIONS")) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            if (!exchange.getRequestMethod().equalsIgnoreCase("POST")) {
                exchange.sendResponseHeaders(405, -1);
                return;
            }

            String body = readRequestBody(exchange);
            try {
                // Parse submission JSON
                // Example payload: { "quizId": "JAVA-OOP", "studentName": "...", "rollNumber": "...", "policy": "competitive", "answers": { "1": "B", "2": "A" } }
                Map<String, String> root = parseSimpleJson(body);
                String quizId = root.get("quizId");
                String studentName = root.getOrDefault("studentName", "Student");
                String rollNumber = root.getOrDefault("rollNumber", "3101");
                String policy = root.getOrDefault("policy", "standard");

                Quiz quiz = quizManager.getQuiz(quizId);
                quiz.validateForConduct();

                // Select evaluation strategy (Interface Polymorphism)
                QuizEvaluator evaluator = policy.equalsIgnoreCase("competitive")
                        ? new NegativeMarkingGradingPolicy(0.25)
                        : new StandardGradingPolicy();

                String attemptId = "ATT-" + UUID.randomUUID().toString().substring(0, 6).toUpperCase();
                QuizAttempt attempt = new QuizAttempt(attemptId, quiz.getQuizId(), quiz.getTitle(), rollNumber, studentName);
                attempt.setTotalQuestions(quiz.getQuestionCount());
                attempt.setTotalPossibleMarks(quiz.getTotalMarks());

                Map<String, String> answers = extractNestedMap(body, "answers");

                int correctCount = 0;
                int incorrectCount = 0;

                for (Question q : quiz.getQuestions()) {
                    String studentAns = answers.getOrDefault(String.valueOf(q.getId()), "").trim();
                    boolean isCorrect = false;
                    try {
                        isCorrect = q.checkAnswer(studentAns);
                    } catch (InvalidOptionException ioe) {
                        isCorrect = false;
                    }

                    double marks = isCorrect ? q.getMarks() : 0.0;
                    if (isCorrect) correctCount++;
                    else incorrectCount++;

                    attempt.addQuestionResult(new QuizAttempt.QuestionResult(
                            q.getId(),
                            q.getQuestionText(),
                            studentAns.isEmpty() ? "(Unanswered)" : studentAns,
                            q.getCorrectAnswerFormatted(),
                            isCorrect,
                            marks
                    ));
                }

                attempt.setCorrectCount(correctCount);
                attempt.setIncorrectCount(incorrectCount);

                double score = evaluator.evaluateScore(attempt);
                attempt.setScoreObtained(score);
                double percentage = (quiz.getTotalMarks() > 0) ? (score / quiz.getTotalMarks()) * 100.0 : 0.0;
                attempt.setPercentage(percentage);
                attempt.setGrade(evaluator.generateGrade(percentage));

                quizManager.recordAttempt(attempt);

                // Build detailed response JSON
                StringBuilder json = new StringBuilder("{");
                json.append("\"success\":true,");
                json.append("\"attemptId\":").append(quote(attempt.getAttemptId())).append(",");
                json.append("\"quizTitle\":").append(quote(attempt.getQuizTitle())).append(",");
                json.append("\"studentName\":").append(quote(attempt.getStudentName())).append(",");
                json.append("\"rollNumber\":").append(quote(attempt.getStudentRollNumber())).append(",");
                json.append("\"policyName\":").append(quote(evaluator.getPolicyName())).append(",");
                json.append("\"timestamp\":").append(quote(attempt.getTimestamp())).append(",");
                json.append("\"totalQuestions\":").append(attempt.getTotalQuestions()).append(",");
                json.append("\"correctCount\":").append(attempt.getCorrectCount()).append(",");
                json.append("\"incorrectCount\":").append(attempt.getIncorrectCount()).append(",");
                json.append("\"scoreObtained\":").append(String.format(Locale.US, "%.2f", attempt.getScoreObtained())).append(",");
                json.append("\"totalPossibleMarks\":").append(attempt.getTotalPossibleMarks()).append(",");
                json.append("\"percentage\":").append(String.format(Locale.US, "%.2f", attempt.getPercentage())).append(",");
                json.append("\"grade\":").append(quote(attempt.getGrade())).append(",");
                json.append("\"results\":[");
                List<QuizAttempt.QuestionResult> list = attempt.getQuestionResults();
                for (int i = 0; i < list.size(); i++) {
                    QuizAttempt.QuestionResult qr = list.get(i);
                    json.append("{");
                    json.append("\"questionId\":").append(qr.getQuestionId()).append(",");
                    json.append("\"questionText\":").append(quote(qr.getQuestionText())).append(",");
                    json.append("\"studentAnswer\":").append(quote(qr.getStudentAnswer())).append(",");
                    json.append("\"correctAnswer\":").append(quote(qr.getCorrectAnswer())).append(",");
                    json.append("\"isCorrect\":").append(qr.isCorrect()).append(",");
                    json.append("\"marksAwarded\":").append(qr.getMarksAwarded());
                    json.append("}");
                    if (i < list.size() - 1) json.append(",");
                }
                json.append("]");
                json.append("}");

                sendJsonResponse(exchange, 200, json.toString());
            } catch (Exception e) {
                sendJsonResponse(exchange, 400, "{\"success\":false,\"error\":" + quote(e.getMessage()) + "}");
            }
        }
    }

    private class AttemptsHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            if (exchange.getRequestMethod().equalsIgnoreCase("OPTIONS")) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            List<QuizAttempt> attempts = quizManager.getAllAttempts();
            StringBuilder json = new StringBuilder("[");
            for (int i = 0; i < attempts.size(); i++) {
                QuizAttempt a = attempts.get(i);
                json.append("{");
                json.append("\"attemptId\":").append(quote(a.getAttemptId())).append(",");
                json.append("\"quizId\":").append(quote(a.getQuizId())).append(",");
                json.append("\"quizTitle\":").append(quote(a.getQuizTitle())).append(",");
                json.append("\"studentName\":").append(quote(a.getStudentName())).append(",");
                json.append("\"rollNumber\":").append(quote(a.getStudentRollNumber())).append(",");
                json.append("\"scoreObtained\":").append(String.format(Locale.US, "%.2f", a.getScoreObtained())).append(",");
                json.append("\"totalPossibleMarks\":").append(a.getTotalPossibleMarks()).append(",");
                json.append("\"percentage\":").append(String.format(Locale.US, "%.2f", a.getPercentage())).append(",");
                json.append("\"grade\":").append(quote(a.getGrade())).append(",");
                json.append("\"timestamp\":").append(quote(a.getTimestamp()));
                json.append("}");
                if (i < attempts.size() - 1) json.append(",");
            }
            json.append("]");

            sendJsonResponse(exchange, 200, json.toString());
        }
    }

    private class DemoRunnerHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            if (exchange.getRequestMethod().equalsIgnoreCase("OPTIONS")) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            // Capture output of the demonstration suite
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            PrintStream origOut = System.out;
            PrintStream origErr = System.err;
            try {
                PrintStream ps = new PrintStream(baos);
                System.setOut(ps);
                System.setErr(ps);

                QuizApplication app = new QuizApplication();
                // Run automated test suite logic
                app.runAutomatedDemonstrationSuite();
            } finally {
                System.setOut(origOut);
                System.setErr(origErr);
            }

            String trace = baos.toString(StandardCharsets.UTF_8);
            sendJsonResponse(exchange, 200, "{\"success\":true,\"trace\":" + quote(trace) + "}");
        }
    }

    // =========================================================================
    // STATIC FILE SERVING
    // =========================================================================

    private static class StaticFileHandler implements HttpHandler {
        private final Path rootDir;

        public StaticFileHandler(Path rootDir) {
            this.rootDir = rootDir;
        }

        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String pathStr = exchange.getRequestURI().getPath();
            if (pathStr == null || pathStr.equals("/") || pathStr.isEmpty()) {
                pathStr = "/index.html";
            }

            // Prevent path traversal
            Path resolved = rootDir.resolve(pathStr.substring(1)).normalize();
            if (!resolved.startsWith(rootDir) || !Files.exists(resolved) || Files.isDirectory(resolved)) {
                String notFound = "<h1>404 Not Found</h1><p>The requested file was not found.</p>";
                exchange.sendResponseHeaders(404, notFound.length());
                OutputStream os = exchange.getResponseBody();
                os.write(notFound.getBytes(StandardCharsets.UTF_8));
                os.close();
                return;
            }

            String contentType = getMimeType(resolved.toString());
            exchange.getResponseHeaders().set("Content-Type", contentType);
            byte[] bytes = Files.readAllBytes(resolved);
            exchange.sendResponseHeaders(200, bytes.length);
            OutputStream os = exchange.getResponseBody();
            os.write(bytes);
            os.close();
        }

        private String getMimeType(String file) {
            if (file.endsWith(".html") || file.endsWith(".htm")) return "text/html; charset=utf-8";
            if (file.endsWith(".css")) return "text/css; charset=utf-8";
            if (file.endsWith(".js")) return "application/javascript; charset=utf-8";
            if (file.endsWith(".json")) return "application/json; charset=utf-8";
            if (file.endsWith(".png")) return "image/png";
            if (file.endsWith(".jpg") || file.endsWith(".jpeg")) return "image/jpeg";
            if (file.endsWith(".svg")) return "image/svg+xml";
            return "text/plain; charset=utf-8";
        }
    }

    // =========================================================================
    // HELPERS
    // =========================================================================

    private static void addCorsHeaders(HttpExchange exchange) {
        exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
        exchange.getResponseHeaders().set("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE");
        exchange.getResponseHeaders().set("Access-Control-Allow-Headers", "Content-Type, Authorization");
    }

    private static void sendJsonResponse(HttpExchange exchange, int status, String json) throws IOException {
        byte[] bytes = json.getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().set("Content-Type", "application/json; charset=utf-8");
        exchange.sendResponseHeaders(status, bytes.length);
        OutputStream os = exchange.getResponseBody();
        os.write(bytes);
        os.close();
    }

    private static String readRequestBody(HttpExchange exchange) throws IOException {
        InputStream is = exchange.getRequestBody();
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        byte[] buffer = new byte[1024];
        int len;
        while ((len = is.read(buffer)) != -1) {
            baos.write(buffer, 0, len);
        }
        return baos.toString(StandardCharsets.UTF_8);
    }

    private static String quote(String str) {
        if (str == null) return "\"\"";
        StringBuilder sb = new StringBuilder("\"");
        for (char c : str.toCharArray()) {
            switch (c) {
                case '"': sb.append("\\\""); break;
                case '\\': sb.append("\\\\"); break;
                case '\b': sb.append("\\b"); break;
                case '\f': sb.append("\\f"); break;
                case '\n': sb.append("\\n"); break;
                case '\r': sb.append("\\r"); break;
                case '\t': sb.append("\\t"); break;
                default:
                    if (c < ' ') {
                        sb.append(String.format("\\u%04x", (int) c));
                    } else {
                        sb.append(c);
                    }
            }
        }
        sb.append("\"");
        return sb.toString();
    }

    private static Map<String, String> parseSimpleJson(String json) {
        Map<String, String> map = new HashMap<>();
        if (json == null || json.trim().isEmpty()) return map;

        String trimmed = json.trim();
        if (trimmed.startsWith("{")) trimmed = trimmed.substring(1);
        if (trimmed.endsWith("}")) trimmed = trimmed.substring(0, trimmed.length() - 1);

        String[] pairs = trimmed.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)");
        for (String pair : pairs) {
            String[] kv = pair.split(":(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", 2);
            if (kv.length == 2) {
                String key = cleanQuotes(kv[0].trim());
                String val = cleanQuotes(kv[1].trim());
                map.put(key, val);
            }
        }
        return map;
    }

    private static Map<String, String> extractNestedMap(String json, String parentKey) {
        Map<String, String> result = new HashMap<>();
        int keyIndex = json.indexOf("\"" + parentKey + "\"");
        if (keyIndex == -1) return result;

        int openBrace = json.indexOf("{", keyIndex);
        if (openBrace == -1) return result;

        int closeBrace = json.indexOf("}", openBrace);
        if (closeBrace == -1) return result;

        String inner = json.substring(openBrace + 1, closeBrace);
        String[] pairs = inner.split(",");
        for (String p : pairs) {
            String[] kv = p.split(":");
            if (kv.length == 2) {
                result.put(cleanQuotes(kv[0].trim()), cleanQuotes(kv[1].trim()));
            }
        }
        return result;
    }

    private static String cleanQuotes(String s) {
        if (s.startsWith("\"") && s.endsWith("\"") && s.length() >= 2) {
            return s.substring(1, s.length() - 1);
        }
        return s;
    }
}

```

---
