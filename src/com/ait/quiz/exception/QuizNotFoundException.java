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
