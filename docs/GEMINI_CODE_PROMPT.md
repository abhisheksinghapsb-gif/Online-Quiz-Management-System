# COMPLETE PROJECT MASTER CODE & STUDY PROMPT FOR GEMINI

Copy everything below this line and paste it into Google Gemini chat:

---

```markdown
Role: Act as an expert Java Professor and Senior Software Architect.
Task: Teach me every Java concept implemented in this "Online Quiz Management System" project in technical, clear, and comprehensive detail with code references so I can defend it in my University CIE-2 Oral Examination and Presentation.

Here is the complete architectural layout and full source code of the project:

================================================================================
MODULE 1: ABSTRACT CLASSES & SUBCLASSES (Unit III: OOP & Inheritance)
================================================================================

--- FILE 1.1: src/com/ait/quiz/model/Question.java (Abstract Base Class) ---
package com.ait.quiz.model;

import com.ait.quiz.exception.InvalidOptionException;
import com.ait.quiz.exception.InvalidQuestionException;

public abstract class Question {
    private final int id;
    private String questionText;
    private int marks;
    private String topic;
    private DifficultyLevel difficulty;

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

    public int getId() { return id; }
    public String getQuestionText() { return questionText; }
    public int getMarks() { return marks; }
    public String getTopic() { return topic; }
    public DifficultyLevel getDifficulty() { return difficulty; }

    public void displayHeader() {
        System.out.printf("[Q%d] [%s | %s | Marks: %d]%n", id, getQuestionType(), difficulty.getDisplayName(), marks);
        System.out.println("Topic: " + topic);
        System.out.println("Prompt: " + questionText);
    }

    // Abstract methods enforced on all question types
    public abstract void displayQuestion();
    public abstract boolean checkAnswer(String studentAnswer) throws InvalidOptionException;
    public abstract String getCorrectAnswerFormatted();
    public abstract String getQuestionType();
}

--- FILE 1.2: src/com/ait/quiz/model/MultipleChoiceQuestion.java (MCQ Subclass) ---
package com.ait.quiz.model;

import com.ait.quiz.exception.InvalidOptionException;
import com.ait.quiz.exception.InvalidQuestionException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MultipleChoiceQuestion extends Question {
    private final List<String> options;
    private final int correctOptionIndex;

    public MultipleChoiceQuestion(int id, String questionText, int marks, String topic,
                                  DifficultyLevel difficulty, List<String> options, int correctOptionIndex)
            throws InvalidQuestionException {
        super(id, questionText, marks, topic, difficulty); // Constructor chaining
        if (options == null || options.size() < 2) {
            throw new InvalidQuestionException("MCQ must have at least 2 options!");
        }
        if (correctOptionIndex < 0 || correctOptionIndex >= options.size()) {
            throw new InvalidQuestionException("Correct option index out of valid range!");
        }
        this.options = new ArrayList<>(options);
        this.correctOptionIndex = correctOptionIndex;
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
        return String.format("[%c] %s", (char) ('A' + correctOptionIndex), options.get(correctOptionIndex));
    }

    @Override
    public String getQuestionType() { return "Multiple Choice (MCQ)"; }
}

--- FILE 1.3: src/com/ait/quiz/model/TrueFalseQuestion.java (True/False Subclass) ---
package com.ait.quiz.model;

import com.ait.quiz.exception.InvalidOptionException;
import com.ait.quiz.exception.InvalidQuestionException;

public class TrueFalseQuestion extends Question {
    private final boolean correctAnswer;

    public TrueFalseQuestion(int id, String questionText, int marks, String topic,
                              DifficultyLevel difficulty, boolean correctAnswer)
            throws InvalidQuestionException {
        super(id, questionText, marks, topic, difficulty);
        this.correctAnswer = correctAnswer;
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
        boolean parsed;
        if (cleaned.equals("T") || cleaned.equals("TRUE")) parsed = true;
        else if (cleaned.equals("F") || cleaned.equals("FALSE")) parsed = false;
        else throw new InvalidOptionException(studentAnswer, "T, F, TRUE, or FALSE");
        return parsed == correctAnswer;
    }

    @Override
    public String getCorrectAnswerFormatted() { return correctAnswer ? "True" : "False"; }

    @Override
    public String getQuestionType() { return "True / False"; }
}

--- FILE 1.4: src/com/ait/quiz/model/NumericQuestion.java (Numeric & Exception Translation) ---
package com.ait.quiz.model;

import com.ait.quiz.exception.InvalidOptionException;
import com.ait.quiz.exception.InvalidQuestionException;

public class NumericQuestion extends Question {
    private final double correctAnswer;
    private final double tolerance;

    public NumericQuestion(int id, String questionText, int marks, String topic,
                           DifficultyLevel difficulty, double correctAnswer, double tolerance)
            throws InvalidQuestionException {
        super(id, questionText, marks, topic, difficulty);
        if (tolerance < 0) throw new InvalidQuestionException("Tolerance cannot be negative!");
        this.correctAnswer = correctAnswer;
        this.tolerance = tolerance;
    }

    @Override
    public void displayQuestion() {
        displayHeader();
        if (tolerance > 0) System.out.printf("   (Enter numeric answer with tolerance ±%.2f)%n", tolerance);
        else System.out.println("   (Enter exact numeric answer)");
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
            // EXCEPTION TRANSLATION: wrapping unchecked NumberFormatException into checked InvalidOptionException
            throw new InvalidOptionException(studentAnswer, "Valid numeric value (e.g., 4 or 3.14)");
        }
    }

    @Override
    public String getCorrectAnswerFormatted() { return String.valueOf(correctAnswer); }

    @Override
    public String getQuestionType() { return "Numeric / Direct Answer"; }
}

--- FILE 1.5: src/com/ait/quiz/model/User.java (Abstract Base User) ---
package com.ait.quiz.model;

public abstract class User {
    private final String userId;
    private String name;
    private String email;

    public User(String userId, String name, String email) {
        this.userId = userId;
        this.name = name;
        this.email = email;
    }

    public String getUserId() { return userId; }
    public String getName() { return name; }
    public String getEmail() { return email; }

    public abstract void displayDashboard();
    public abstract String getRole();
}

--- FILE 1.6: src/com/ait/quiz/model/Student.java (User Subclass) ---
package com.ait.quiz.model;

import java.util.ArrayList;
import java.util.List;

public class Student extends User {
    private final String rollNumber;
    private final String division;
    private final List<QuizAttempt> attempts;

    public Student(String userId, String name, String email, String rollNumber, String division) {
        super(userId, name, email);
        this.rollNumber = rollNumber;
        this.division = division;
        this.attempts = new ArrayList<>();
    }

    public String getRollNumber() { return rollNumber; }
    public void addAttempt(QuizAttempt attempt) { attempts.add(attempt); }

    @Override
    public void displayDashboard() {
        System.out.println("=== STUDENT PORTAL DASHBOARD ===");
        System.out.println("Name: " + getName() + " | Roll No: " + rollNumber + " | Div: " + division);
        System.out.println("Total Quizzes Attempted: " + attempts.size());
    }

    @Override
    public String getRole() { return "Student"; }
}


================================================================================
MODULE 2: INTERFACES & STRATEGY DESIGN PATTERN (Unit III)
================================================================================

--- FILE 2.1: src/com/ait/quiz/service/QuizEvaluator.java (Strategy Interface) ---
package com.ait.quiz.service;

import com.ait.quiz.model.QuizAttempt;

public interface QuizEvaluator {
    // Strategy evaluation contract
    double evaluateScore(QuizAttempt attempt);

    // Overloaded method demonstrating Compile-time Polymorphism (Method Overloading)
    double evaluateScore(double earnedMarks, int incorrectCount, double penaltyPerIncorrect);

    String generateGrade(double percentage);
    String getPolicyName();
    void printDetailedReport(QuizAttempt attempt);
}

--- FILE 2.2: src/com/ait/quiz/service/StandardGradingPolicy.java (Linear Academic Strategy) ---
package com.ait.quiz.service;

import com.ait.quiz.model.QuizAttempt;

public class StandardGradingPolicy implements QuizEvaluator {
    @Override
    public double evaluateScore(QuizAttempt attempt) {
        double total = 0.0;
        for (QuizAttempt.QuestionResult res : attempt.getQuestionResults()) {
            if (res.isCorrect()) total += res.getMarksAwarded();
        }
        return total;
    }

    @Override
    public double evaluateScore(double earnedMarks, int incorrectCount, double penaltyPerIncorrect) {
        return earnedMarks; // Zero penalty in standard linear grading
    }

    @Override
    public String generateGrade(double percentage) {
        if (percentage >= 80.0) return "Distinction";
        if (percentage >= 60.0) return "First Class";
        if (percentage >= 40.0) return "Pass";
        return "Fail";
    }

    @Override
    public String getPolicyName() { return "Standard Linear Evaluation (0% Penalty)"; }

    @Override
    public void printDetailedReport(QuizAttempt attempt) { /* prints report */ }
}

--- FILE 2.3: src/com/ait/quiz/service/NegativeMarkingGradingPolicy.java (Competitive Strategy) ---
package com.ait.quiz.service;

import com.ait.quiz.model.QuizAttempt;

public class NegativeMarkingGradingPolicy implements QuizEvaluator {
    private final double penaltyRate; // e.g. 0.25 (25% deduction)

    public NegativeMarkingGradingPolicy(double penaltyRate) {
        this.penaltyRate = penaltyRate;
    }

    @Override
    public double evaluateScore(QuizAttempt attempt) {
        double rawScore = 0.0;
        for (QuizAttempt.QuestionResult res : attempt.getQuestionResults()) {
            if (res.isCorrect()) {
                rawScore += res.getMarksAwarded();
            } else {
                rawScore -= (res.getMarksAwarded() * penaltyRate);
            }
        }
        return Math.max(0.0, rawScore);
    }

    @Override
    public double evaluateScore(double earnedMarks, int incorrectCount, double penaltyPerIncorrect) {
        return Math.max(0.0, earnedMarks - (incorrectCount * penaltyPerIncorrect));
    }

    @Override
    public String generateGrade(double percentage) {
        if (percentage >= 75.0) return "Rank 1 (Qualified with Distinction)";
        if (percentage >= 50.0) return "Qualified";
        return "Not Qualified (Below cutoff with penalties)";
    }

    @Override
    public String getPolicyName() {
        return String.format("Competitive Evaluation (%.0f%% Negative Penalty)", penaltyRate * 100);
    }

    @Override
    public void printDetailedReport(QuizAttempt attempt) { /* prints scorecard */ }
}

--- FILE 2.4: src/com/ait/quiz/service/QuizOperations.java (Operations Contract) ---
package com.ait.quiz.service;

import com.ait.quiz.exception.*;
import com.ait.quiz.model.*;
import java.util.List;

public interface QuizOperations {
    void createQuiz(Quiz quiz) throws DuplicateQuizException;
    void addQuestionToQuiz(String quizId, Question question) throws QuizNotFoundException, InvalidQuestionException;
    Quiz getQuiz(String quizId) throws QuizNotFoundException;
    List<Quiz> getAllQuizzes();
    // Method Overloading
    List<Quiz> searchQuiz(String topic);
    List<Quiz> searchQuiz(String topic, DifficultyLevel level);
    boolean deleteQuiz(String quizId) throws QuizNotFoundException;
    void recordAttempt(QuizAttempt attempt);
    List<QuizAttempt> getAllAttempts();
    List<QuizAttempt> getAttemptsByStudent(String rollNumber);
    int getQuizCount();
}

--- FILE 2.5: src/com/ait/quiz/service/QuizManager.java (Implementation with Overloading) ---
package com.ait.quiz.service;

import com.ait.quiz.exception.*;
import com.ait.quiz.model.*;
import java.util.*;

public class QuizManager implements QuizOperations {
    private final Map<String, Quiz> quizMap = new LinkedHashMap<>();
    private final List<QuizAttempt> attemptHistory = new ArrayList<>();

    @Override
    public void createQuiz(Quiz quiz) throws DuplicateQuizException {
        if (quizMap.containsKey(quiz.getQuizId())) {
            throw new DuplicateQuizException(quiz.getQuizId());
        }
        quizMap.put(quiz.getQuizId(), quiz);
    }

    @Override
    public Quiz getQuiz(String quizId) throws QuizNotFoundException {
        Quiz q = quizMap.get(quizId.trim().toUpperCase());
        if (q == null) throw new QuizNotFoundException(quizId);
        return q;
    }

    // Method Overloading 1: Search by topic
    @Override
    public List<Quiz> searchQuiz(String topic) {
        List<Quiz> matched = new ArrayList<>();
        for (Quiz q : quizMap.values()) {
            if (q.getTopic().toLowerCase().contains(topic.toLowerCase())) matched.add(q);
        }
        return matched;
    }

    // Method Overloading 2: Search by topic AND difficulty
    @Override
    public List<Quiz> searchQuiz(String topic, DifficultyLevel level) {
        List<Quiz> topicMatches = searchQuiz(topic);
        if (level == null) return topicMatches;
        List<Quiz> finalMatches = new ArrayList<>();
        for (Quiz q : topicMatches) {
            if (q.getDifficulty() == level) finalMatches.add(q);
        }
        return finalMatches;
    }

    // ... other methods ...
}


================================================================================
MODULE 3: CUSTOM CHECKED EXCEPTION HIERARCHY (Unit IV)
================================================================================

--- FILE 3.1: Root Exception: src/com/ait/quiz/exception/QuizException.java ---
package com.ait.quiz.exception;

public class QuizException extends Exception {
    public QuizException(String message) { super(message); }
    public QuizException(String message, Throwable cause) { super(message, cause); }
}

--- FILE 3.2: src/com/ait/quiz/exception/QuizNotFoundException.java ---
package com.ait.quiz.exception;

public class QuizNotFoundException extends QuizException {
    private final String quizId;
    public QuizNotFoundException(String quizId) {
        super("Quiz not found with ID: '" + quizId + "'. Please check the Quiz ID.");
        this.quizId = quizId;
    }
    public String getQuizId() { return quizId; }
}

--- FILE 3.3: src/com/ait/quiz/exception/DuplicateQuizException.java ---
package com.ait.quiz.exception;

public class DuplicateQuizException extends QuizException {
    private final String quizId;
    public DuplicateQuizException(String quizId) {
        super("A quiz with ID '" + quizId + "' already exists! Please use a unique identifier.");
        this.quizId = quizId;
    }
    public String getQuizId() { return quizId; }
}

--- FILE 3.4: src/com/ait/quiz/exception/EmptyQuizException.java ---
package com.ait.quiz.exception;

public class EmptyQuizException extends QuizException {
    private final String quizId;
    public EmptyQuizException(String quizId) {
        super("Quiz '" + quizId + "' contains no questions! Cannot launch empty quiz.");
        this.quizId = quizId;
    }
    public String getQuizId() { return quizId; }
}

--- FILE 3.5: src/com/ait/quiz/exception/InvalidQuestionException.java ---
package com.ait.quiz.exception;

public class InvalidQuestionException extends QuizException {
    public InvalidQuestionException(String message) { super(message); }
}

--- FILE 3.6: src/com/ait/quiz/exception/InvalidOptionException.java ---
package com.ait.quiz.exception;

public class InvalidOptionException extends QuizException {
    private final String chosenOption;
    private final String expectedFormat;

    public InvalidOptionException(String chosenOption, String expectedFormat) {
        super("Invalid option selected: '" + chosenOption + "'. Expected format: [" + expectedFormat + "]");
        this.chosenOption = chosenOption;
        this.expectedFormat = expectedFormat;
    }
    public String getChosenOption() { return chosenOption; }
    public String getExpectedFormat() { return expectedFormat; }
}


================================================================================
MODULE 4: INTEGRATED RUNTIME EXECUTION (Unit III & IV in Action)
================================================================================

--- Excerpt from src/com/ait/quiz/main/QuizApplication.java ---
// 1. Runtime Strategy Selection:
System.out.println("Select Grading Policy: 1. Standard Linear | 2. Competitive (-25% Negative Marking)");
int choice = scanner.nextInt();
QuizEvaluator evaluator = (choice == 1) 
        ? new StandardGradingPolicy() 
        : new NegativeMarkingGradingPolicy(0.25);

// 2. Launching Quiz with Exception Protection:
Quiz quiz;
try {
    quiz = quizManager.getQuiz(selectedQuizId);
    if (quiz.getQuestionCount() == 0) {
        throw new EmptyQuizException(selectedQuizId);
    }
} catch (QuizNotFoundException | EmptyQuizException e) {
    System.out.println("Quiz Launch Blocked: " + e.getMessage());
    return;
}

// 3. Runtime Polymorphism & Defensive Exception Handling Loop:
for (Question q : quiz.getQuestions()) {
    // Dynamic Method Dispatch: invokes the exact subclass implementation (MCQ, TrueFalse, or Numeric)
    q.displayQuestion();

    boolean answeredValidly = false;
    boolean isCorrect = false;

    // Graceful Recovery: loop ensures application NEVER terminates on invalid input
    while (!answeredValidly) {
        System.out.print(">> Your Answer: ");
        String studentAns = scanner.nextLine();
        try {
            // Polymorphic answer checking; throws InvalidOptionException on illegal format (e.g. 'Z')
            isCorrect = q.checkAnswer(studentAns);
            answeredValidly = true; // successfully processed
        } catch (InvalidOptionException ioe) {
            // Catches domain exception, presents error, and re-prompts the user
            System.out.println("[Input Error] " + ioe.getMessage());
            System.out.println("Please re-enter your response according to the specified format.");
        }
    }
}

// 4. Strategy Pattern Score Computation:
double finalScore = evaluator.evaluateScore(attempt);
String letterGrade = evaluator.generateGrade(attempt.getPercentage());
evaluator.printDetailedReport(attempt);
```

Please explain each concept above in depth, addressing:
1. Why this design was chosen over alternative approaches.
2. How the JVM executes dynamic method dispatch under the hood.
3. How the Strategy Pattern decouples algorithm from domain model.
4. How exception propagation and defensive programming protect application stability.
5. Anticipated oral viva questions with high-scoring technical answers.
```
---
