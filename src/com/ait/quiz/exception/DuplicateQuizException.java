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
