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
