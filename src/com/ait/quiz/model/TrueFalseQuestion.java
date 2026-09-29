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
