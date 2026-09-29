package com.ait.quiz.service;

import com.ait.quiz.model.QuizAttempt;

/**
 * Interface defining evaluation contracts and grading policies.
 * Demonstrates Unit III concept: Interfaces (defining common behaviour to be implemented).
 */
public interface QuizEvaluator {

    /**
     * Calculates the overall score for a completed quiz attempt.
     */
    double evaluateScore(QuizAttempt attempt);

    /**
     * Overloaded method demonstrating Compile-time Polymorphism (Method Overloading).
     * Calculates score based on raw marks and penalty deduction.
     */
    double evaluateScore(double earnedMarks, int incorrectCount, double penaltyPerIncorrect);

    /**
     * Determines letter grade based on percentage.
     */
    String generateGrade(double percentage);

    /**
     * Returns the title/description of the grading policy.
     */
    String getPolicyName();

    /**
     * Prints a comprehensive score breakdown and question-by-question review.
     */
    void printDetailedReport(QuizAttempt attempt);
}
