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
