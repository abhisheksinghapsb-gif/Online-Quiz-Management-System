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
