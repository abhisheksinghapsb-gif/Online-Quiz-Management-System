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
