package com.ait.quiz.exception;

/**
 * Base custom checked exception for all Quiz Management System domain errors.
 * Demonstrates inheritance within exception hierarchies (Unit IV).
 */
public class QuizException extends Exception {
    
    public QuizException(String message) {
        super(message);
    }

    public QuizException(String message, Throwable cause) {
        super(message, cause);
    }
}
