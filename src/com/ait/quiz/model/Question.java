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
