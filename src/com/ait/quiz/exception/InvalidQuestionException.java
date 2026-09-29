package com.ait.quiz.exception;

/**
 * Thrown when question parameters fail domain validation constraints
 * (e.g., empty prompt, fewer than two options, or non-positive marks).
 */
public class InvalidQuestionException extends QuizException {

    public InvalidQuestionException(String message) {
        super(message);
    }
}
