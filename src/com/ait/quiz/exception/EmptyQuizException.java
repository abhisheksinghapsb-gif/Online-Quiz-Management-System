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
